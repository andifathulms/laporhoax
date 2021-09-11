from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class UserSocialForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('name','email',)

