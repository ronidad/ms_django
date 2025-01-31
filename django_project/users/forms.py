from django import forms
import django
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import EmailField
from .models import profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model=User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model=User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
   
    class Meta:
        model=profile
        fields = ['image']