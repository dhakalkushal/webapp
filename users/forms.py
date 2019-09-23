from django.contrib.auth.models import User
from django import forms

from captcha.fields import CaptchaField

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True, min_length=8)
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ['username','email','password', 'captcha']
