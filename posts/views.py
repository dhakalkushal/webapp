from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Post

# Create your views here.
class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content']


