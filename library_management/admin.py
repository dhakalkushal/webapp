from django.contrib import admin
from .models import Book,Student,Borrower, Language, Genre

admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Borrower)
admin.site.register(Language)
admin.site.register(Genre)