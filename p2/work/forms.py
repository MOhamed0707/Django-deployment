from django.contrib.auth.models import User
from work.models import UserInfo
from django import forms

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=("username","email","password")

class UserInfoForm(forms.ModelForm):
    class Meta():
        model=UserInfo
        fields=("user_site","user_profile_pic")
