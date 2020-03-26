from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):

    content = forms.CharField(label="",widget=forms.Textarea(attrs={"class":"form-control",'placeholder':'ask/answer...','rows': '2','cols':'50'}))

    class Meta:
        model = Comment
        fields = ['content',]