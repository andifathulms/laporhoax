from django.shortcuts import render

# Create your views here.
def testGoogleAuth(request):
	return render(request, "googleauth.html", {})