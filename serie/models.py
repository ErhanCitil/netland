from django.db import models

# Create your models here.

class Series(models.Model):
    title = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    summary = models.TextField()
    has_won_awards = models.IntegerField()
    seasons = models.IntegerField()
    country = models.CharField(max_length=2)
    spoken_in_language = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'series'

class Movies(models.Model):
    title = models.CharField(max_length=100)
    length_in_minutes = models.IntegerField()
    released_at = models.DateField(blank=True, null=True)
    country_of_origin = models.CharField(max_length=2, blank=True, null=True)
    summary = models.TextField()
    youtube_trailer_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'