from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager

class User(AbstractBaseUser):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	nohp = PhoneNumberField()
	dateJoin = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = UserManager()

	def __str__(self):
		return self.email
	def get_full_name(self):
		return self.name
	def get_short_name(self):
		return self.name
	def has_perm(self, perm, obj=None):
		return True
	def has_module_perms(self, app_label):
		return True

