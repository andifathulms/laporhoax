from django.db import models

# Create your models here.

class Feed(models.Model):
	#id = models.CharField(max_length = 10, primary_key=True)
	id = models.BigAutoField(primary_key=True)
	title = models.CharField(max_length = 200)
	content = models.TextField()
	thumbnail = models.TextField(blank=True, null=True)
	author = models.CharField(max_length = 100)
	date = models.DateTimeField(auto_now_add=True)
	view = models.IntegerField(default=0)