from .models import Book, Student, Borrower
from django import forms
from pagedown.widgets import PagedownWidget

class ListForms(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['isbn','title','author','summary','genre','language','total_copies','available_copies',]

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['id', 'name','contact','email']
