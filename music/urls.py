from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    #path('physics/', views.physics, name = 'physics')
    #path('', views.IndexView.as_view(), name='index'),
    #path('<pk>/', views.DetailView.as_view(), name='detail'),
]

