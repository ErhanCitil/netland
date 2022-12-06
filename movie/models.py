from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    length_in_minutes = models.IntegerField()
    released_at = models.DateField(blank=True, null=True)
    country_of_origin = models.CharField(max_length=2, blank=True, null=True)
    summary = models.TextField()
    youtube_trailer_id = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'movies'