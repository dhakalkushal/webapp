from django.shortcuts import render
from django.http import Http404
from .models import Album
from django.http import HttpResponse

def home(request):
    return render(request, 'users/base.html')

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums,}
    return render(request,'music/index.html', context)

def detail(request, album_id):
    try:
        album = Album.objects.get(pk = album_id)
        context = {'album': album}
    except Album.DoesNotExist:
        return render(request,'music/404.html')
    return render(request, 'music/details.html', context)
