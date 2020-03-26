from django.urls import path, include
from . import views
#from comments.views import CommentCreate

urlpatterns = [
    path('',views.PostIndex.as_view(), name = 'post-index'),
    path('add/', views.PostCreate.as_view(), name = 'create-post'),
    path('search/',views.SearchResultView.as_view(),name = 'search-result'),
    path('<slug:slug>/', views.view_post, name ='detail-post'),
    path('<slug:slug>/edit/',views.PostUpdate.as_view(),name = 'update-post'),
]

