from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='covid_19'),
    path('yesterday/', views.yesterday, name = 'yesterday'),
    path('compare/', views.compare, name = 'compare'),
    path('<str:country>/', views.country_detail, name = 'country_detail'),

]
