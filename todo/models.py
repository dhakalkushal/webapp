from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class List(models.Model):
    tasks = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.tasks + "-" + str(self.completed)
