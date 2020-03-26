from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'home'),
    path('add/',views.TodoCreate.as_view(),name = 'todo-add'),
    path('<pk>/delete/', views.TodoDelete.as_view(), name = 'todo-delete'),
    path('<pk>/',views.TodoUpdate.as_view(), name = 'update'),
]
