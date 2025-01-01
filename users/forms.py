from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#To add additional email field to the existing user creation form
class UserRegisterForm(UserCreationForm):
  email=forms.EmailField()

  class Meta:
    model = User
    fields = ['username','email','password1','password2']