from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_date = models.DateField(default=timezone.now)
    end_date= models.DateField(blank=True, null=True)
    duration = models.PositiveIntegerField()


    def __str__(self):
        return self.title


class MovieReview(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rating = models.IntegerField(range(1, 5))
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.movie.title} by {self.user.username}"