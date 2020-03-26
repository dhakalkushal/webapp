from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class List(models.Model):
    tasks = models.CharField(max_length=1000)
    completed = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.tasks + "-" + str(self.completed)
