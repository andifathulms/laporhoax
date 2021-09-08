from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from reports.models import Category, Report
from reports.api.serializers import CategorySerializer, ReportSerializer

@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(["POST"])
def post_report(request):
	if request.method == "POST":
		data = JSONParser().parse(request)
		serializer = ReportSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def report_list(request):
    data = JSONParser().parse(request)
    print(data)
    try:
        snippet = Report.objects.filter(email=data["email"])
    except Report.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ReportSerializer(snippet, many=True)
        return JsonResponse(serializer.data, safe=False)
