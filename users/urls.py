from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('register/', views.UserFormView.as_view(), name='register'),
    path('profile/', views.profile, name = 'profile'),

]