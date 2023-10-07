import datetime
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

from ratings.models import Rating

RATING_CALC_TIME = 1

class Products(models.Model):
    brand = models.CharField(max_length=120)
    resolution = models.TextField()
    size = models.CharField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    ratings = GenericRelation(Rating)
    rating_last_updated = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    rating_count = models.IntegerField(blank=True, null=True)
    rating_avg = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)

    def rating_avg_display(self):
        now = timezone.now()
        if not self.rating_last_updated:
            return self.calculate_rating()
        if self.rating_last_updated > now - datetime.timedelta(minutes=RATING_CALC_TIME):
            return self.rating_avg
        return self.calculate_rating()

    def calculate_ratings_count(self):
        return self.ratings.all().count()

    def calculate_ratings_avg(self):
        return self.ratings.all().avg()

    def calculate_rating(self, save=True):
        rating_avg = self.calculate_ratings_avg()
        rating_count = self.calculate_ratings_count()
        self.rating_count = rating_count
        self.rating_avg = rating_avg
        self.rating_last_updated = timezone.now()
        if save:
            self.save()
        return self.rating_avg

    