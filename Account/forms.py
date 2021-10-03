from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, fields
from django.contrib.auth.models import User
from django.utils.regex_helper import Choice
from .utils import (Profile_Gender , profile_files_path)
from django.contrib import messages


class ProfileForm(ModelForm) :
    age = forms.IntegerField(label="سن", required=False)
    n_code = forms.CharField(label="کدملی", max_length=10, required=False)
    phone = forms.CharField(label="تلفن همراه", max_length=11, required=False)
    gender = forms.CharField(label="جنسیت", required=False)
    cv = forms.FileField(label=" فایل رزومه", required=False)
    bio = forms.CharField(label="درباره ی من", required=False, widget=(forms.Textarea)) 
    gender = forms.CharField(label="جنسیت", required=False )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'username', 'age', 'n_code', 'phone', 'cv', 'bio', 'gender']


class SignupForm(UserCreationForm) :
    age = forms.IntegerField(label="سن")
    n_code = forms.CharField(label="کدملی", max_length=10, required=True)
    phone = forms.CharField(label="تلفن همراه", max_length=11, required=True)
    gender = forms.CharField(label="جنسیت")
    cv = forms.FileField(label=" فایل رزومه")
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'age', 'n_code', 'phone', 'gender', 'cv', 'password1','password2']

