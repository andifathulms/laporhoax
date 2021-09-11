from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from feeds.api.serializers import FeedSerializer,FeedHeaderSerializer,FeedSerializer
from feeds.models import Feed

@api_view(["POST"])
def post_feed(request):
	if request.method == "POST":
		data = JSONParser().parse(request)
		serializer = FeedSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def getHeaderFeed(request):
	if request.method == 'GET':
		category = Feed.objects.all().order_by('date')[:3]
		serializer = FeedHeaderSerializer(category, many=True)
		return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def getFeed(request, pk):
	if request.method == 'GET':
		category = Feed.objects.get(id=pk)
		category.view = F('view')+1
		category.save()
		feed = Feed.objects.filter(id=pk)
		serializer = FeedSerializer(feed, many=True)
		return JsonResponse(serializer.data, safe=False)