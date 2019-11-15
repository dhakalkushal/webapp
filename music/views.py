from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.shortcuts import render

def home(request):
    return render(request, 'music/home.html')
