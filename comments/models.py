from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from music.models import Movie

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, null = True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='replies', null = True)

    def __str__(self):
        return self.content


