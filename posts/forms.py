from .models import Post
from django import forms

class ListForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']
