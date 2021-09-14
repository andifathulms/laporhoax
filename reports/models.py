from django.db import models

from accounts.models import User

class Category(models.Model):
	id = models.CharField(max_length = 10, primary_key=True)
	header = models.CharField(max_length = 50)
	content = models.CharField(max_length = 100)

class Report(models.Model):
	id = models.BigAutoField(primary_key=True)
	email = models.EmailField()
	url = models.CharField(max_length = 200,blank=True,null=True)
	img = models.TextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	report = models.CharField(default="Saved", max_length = 20)
	isAnonym = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=True)
	description = models.CharField(max_length = 150)