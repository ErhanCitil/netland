from django.test import TestCase
from .models import *
from .views import *
# Create your tests here.
class MovieTest(TestCase):
    def test_movie(self):
        movie = Movies.objects.create(title="Test Movie", length_in_minutes=100, released_at="2020-01-01", country_of_origin="NL", summary="Test summary", youtube_trailer_id="123456789")
        self.assertEqual(movie.title, "Test Movie")
        self.assertEqual(movie.length_in_minutes, 100)
        self.assertEqual(movie.released_at, "2020-01-01")
        self.assertEqual(movie.country_of_origin, "NL")
        self.assertEqual(movie.summary, "Test summary")
        self.assertEqual(movie.youtube_trailer_id, "123456789")
    
    def test_movie2(self):
        movie = Movies.objects.create(title="Test Movie2", length_in_minutes=100, released_at="2020-01-01", country_of_origin="NL", summary="Test summary", youtube_trailer_id="123456789")
        self.assertEqual(movie.title, "Test Movie2")
        self.assertEqual(movie.length_in_minutes, 100)
        self.assertEqual(movie.released_at, "2020-01-01")
        self.assertEqual(movie.country_of_origin, "NL")
        self.assertEqual(movie.summary, "Test summary")
        self.assertEqual(movie.youtube_trailer_id, "123456789")

class MovieViewsTest(TestCase):
    def test_detail(self):
        response = self.client.get('/movie/1/')
        self.assertEqual(response.status_code, 200)
    
    def test_update(self):
        response = self.client.patch('/updatemovie/1')
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.get('/createmovie/')
        self.assertEqual(response.status_code, 200)