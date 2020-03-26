from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('movies/',views.index, name = 'movies-index' ),
    path('movies/add/', views.MovieCreate.as_view(), name = 'movie-add'),
    path('movies/search/', views.SearchResultView.as_view(), name = 'movie-search'),
    path('movies/<str:pk>/',views.view_movie, name= 'movie-detail'),
    #path('physics/', views.physics, name = 'physics'),
    #path('', views.IndexView.as_view(), name='index'),
    #path('<pk>/', views.DetailView.as_view(), name='detail'),
]

