from django import forms
from .models import List

class ListForm(forms.ModelForm):

    due_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = List
        fields = ['tasks', 'completed',]

