from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostCreate.as_view(), name = 'create-post')

]