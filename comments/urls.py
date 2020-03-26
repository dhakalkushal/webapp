from django.urls import path, include
from . import views

urlpatterns = [
    path('<pk>/delete/',views.CommentDelete.as_view(),name = 'comment-delete'),
    path('<pk>/edit/',views.CommentUpdate.as_view(),name = 'comment-update'),
]
