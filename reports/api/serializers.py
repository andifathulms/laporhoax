from django.db import transaction

from rest_framework import serializers

from reports.models import Report, Category
from accounts.models import User

class ReportSerializer(serializers.ModelSerializer):
	user = serializers.SlugRelatedField(read_only=True,slug_field="email")
	category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())
	class Meta:
		model = Report
		#fields = ['email','url','img','category']
		fields = '__all__' 

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__' 