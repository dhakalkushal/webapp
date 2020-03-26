from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField

class UserForm(UserCreationForm):
    captcha = CaptchaField()
    email = forms.EmailField(max_length=50)
    class Meta:
        model = User
        fields = ['username','email','password1','password2', 'captcha']

class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']