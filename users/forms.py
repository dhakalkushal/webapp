from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True, min_length=8)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']