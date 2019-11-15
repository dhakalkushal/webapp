from .models import Post, Subject
from django import forms
from pagedown.widgets import PagedownWidget

class ListForms(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget())
    class Meta:
        model = Post
        fields = ['title','content','overview','subject','level',]

