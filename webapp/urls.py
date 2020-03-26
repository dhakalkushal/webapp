from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('secrete/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('', include('music.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('todo/',include('todo.urls')),
    path('captcha/', include('captcha.urls')),
    path('library/', include('library_management.urls')),
    path('post/', include('posts.urls')),
    path('comment/',include('comments.urls')),
    path('ratings/', include('star_ratings.urls',namespace ='ratings')),
    path('corona/', include('covid_19.urls')),

]
