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

class test_netland(models.Model):
    title = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    summary = models.TextField()
    has_won_awards = models.IntegerField()
    seasons = models.IntegerField()
    country = models.CharField(max_length=2)
    spoken_in_language = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'test_netland'