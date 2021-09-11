from rest_framework import serializers

from feeds.models import Feed

class FeedSerializer(serializers.ModelSerializer):
	class Meta:
		model = Feed
		fields = '__all__'

class FeedHeaderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Feed
		fields = ['id','title','thumbnail']

class FeedSerializer(serializers.ModelSerializer):
	class Meta:
		model = Feed
		fields = '__all__'