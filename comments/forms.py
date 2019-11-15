from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):

    content = forms.CharField(label="",widget=forms.Textarea(attrs={"class":"form-control",'placeholder':'ask a question...','rows': '2','cols':'50'}))

    class Meta:
        model = Comment
        fields = ['content',]