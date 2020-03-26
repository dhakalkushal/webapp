from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings import get_star_ratings_rating_model_name

class Movie(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    trending = models.BooleanField(default=False)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    '''def no_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings)> 0:
            return sum / len(ratings)
        else:
            return 0'''
    
class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = GenericRelation(get_star_ratings_rating_model_name(), related_query_name='ratings')

    def __str__(self):
        return str(self.movie)