from django.views import generic
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.shortcuts import redirect, render_to_response, get_object_or_404, render
import requests
from .models import Movie, Rating
from comments.models import Comment
from .forms import ListForms
from django.urls import reverse
from comments.forms import CommentForm
from django.db.models import Q

def home(request):

    return render(request, 'music/404.html')

class MovieCreate(CreateView):
    model = Movie
    form_class = ListForms

    def form_valid(self, form):
        url = "http://www.omdbapi.com/?i={}&apikey=bf90de3b"
        r = requests.get(url.format(form.instance.id)).json()

        if r['Response'] == 'True':
            return super().form_valid(form)
        return super().form_invalid(form)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False

    def get_success_url(self):
        return reverse('index')

class SearchResultView(generic.ListView):
    template_name = 'music/search-index.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Movie.objects.filter(Q(title__icontains=query))
        print(object_list)
        return object_list

def index(request):
    url = "http://www.omdbapi.com/?i={}&apikey=bf90de3b"

    movies = Movie.objects.all()

    object_list = []

    for movie_id in movies:

        r = requests.get(url.format(movie_id.id)).json()

        movie_datas ={
            'Trending': movie_id.trending,
            'imdbID': movie_id.id,
            'Title':r['Title'],
            'Released':r['Released'],
            'Genre':r['Genre'],
            'Poster':r['Poster'],
        }

        object_list.append(movie_datas)

    context = {
        'object_list' : object_list
    }
    return render(request, 'music/index.html', context)

def view_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    comments = Comment.objects.filter(movie_id=movie, reply=None)
    form = CommentForm(request.POST or None)

    url = "http://www.omdbapi.com/?i={}&apikey=bf90de3b"

    r = requests.get(url.format(pk)).json()

    #no_of_rating = Movie.no_of_ratings(movie)

    #avg_rating = Movie.avg_rating(movie)

    movie_data = {
        'Title': r['Title'],
        'Released': r['Released'],
        'Genre': r['Genre'],
        'Poster': r['Poster'],
        'Actor': r['Actors'],
        'Director': r['Director'],
        'Plot': r['Plot'],
    }

    if request.method == 'POST':
        obj = Rating.objects.filter(movie=movie)
        if not obj:
            obj.movie = movie
            obj.save()
        else:
            obj.update()

    else:
        obj = Rating.objects.filter(movie=movie)
        print(obj)
        if not obj:
            obj = Rating()
            obj.movie = movie
            obj.save()
            obj = Rating.objects.filter(movie=movie)
        print(obj)

    context = {
        'obj':obj,
        #'avg_rating' : avg_rating,
        #'no_of_rating':no_of_rating,
        'comments':comments,
        'form':form,
        'movie':movie,
        'movie_data':movie_data,
    }

    if form.is_valid():
        comment = form.save(commit=False)
        comment.movie_id = movie
        comment.author = request.user
        reply_id = request.POST.get('comment_id')
        comment_qs = None
        if reply_id:
            comment_qs = Comment.objects.get(id=reply_id)
        comment.reply = comment_qs
        comment.save()
        return redirect(request.path)

    return render(request, 'music/home.html', context)
