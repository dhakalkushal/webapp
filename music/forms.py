from .models import Movie
from django import forms

class ListForms(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['id','title']
