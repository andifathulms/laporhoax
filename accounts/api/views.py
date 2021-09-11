from rest_framework import parsers, renderers, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from django_rest_passwordreset.signals import reset_password_token_created

from django.http import HttpResponse, JsonResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text

from django.core.mail import EmailMessage, send_mail
from django.dispatch import receiver
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.template.loader import render_to_string

from accounts.models import User
from .serializers import RegistrationSerializer, CustomTokenSerializer, isActiveSerializer
from .tokens import account_activation_token


@api_view(['POST', ])
def registrationView(request):
	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			user = serializer.save()
			data['response'] = "Confirmation Pending"
			data['email'] = user.email
			data['name'] = user.name
			data['nohp'] = str(user.nohp)
			data['is_active'] = user.is_active
			data['is_staff'] = user.is_staff
			data['is_admin'] = user.is_admin
			token = Token.objects.create(user=user).key
			data['token'] = token
			try:
				emailSender(user)
			except:
				return Response({'email':"Can't send to this email"})

		else:
			data = serializer.errors
		return Response(data)

@csrf_exempt
def isActive(request):
	data = JSONParser().parse(request)
	try:
		snippet = [Token.objects.get(key=data["key"])]
		email = snippet[0].user
		user = [User.objects.get(email=email)]
	except Token.DoesNotExist:
		return HttpResponse(status=404)
	if request.method == 'GET':
		serializer = isActiveSerializer(user, many=True)
		#print(serializer)
		return JsonResponse(serializer.data, safe=False)

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "http://127.0.0.1:8000/{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        "Password Reset for {title}".format(title="Lapor Hoax"),
        email_plaintext_message,
        "noreply@somehost.local",
        [reset_password_token.user.email]
    )

def emailSender(user):
	mail_subject = "Aktifasi akun anda"
	message = render_to_string('acc_active_email.html',{
		'user' : user,
		'domain' : "http://127.0.0.1:8000",
		'uid': urlsafe_base64_encode(force_bytes(user.pk)),
		'token' : account_activation_token.make_token(user),
	})
	
	to_email = user.email
	email = EmailMessage(mail_subject, message, to=[to_email])
	email.send()

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		print(uid)
		userObj = User.objects.get(pk=uid)
		print(userObj)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		userObj = None
	if userObj is not None and account_activation_token.check_token(userObj, token):
		userObj.is_active = True
		userObj.save()
		login(request, userObj, backend='django.contrib.auth.backends.ModelBackend')
		#return redirect('home')
		return HttpResponse('Thank you for your email confirmation. Now you can login your account') 
	else:
		return HttpResponse('Activation link is invalid') #Change endpoint later
