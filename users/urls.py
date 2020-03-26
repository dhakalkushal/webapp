from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.UserFormView.as_view(), name='register'),
    path('profile/', views.profile, name = 'profile'),
    path('profile/edit/',views.UserProfileUpdate.as_view(), name = 'profile-edit'),
]
