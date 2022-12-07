from django.test import TestCase
from .models import *
from .views import *
from django.urls import reverse
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
    def setUp(self):
        self.movie1 = Movies.objects.create(title="Test Movie", length_in_minutes=100, released_at="2020-01-01", country_of_origin="NL", summary="Test summary", youtube_trailer_id="123456789")
        self.movie2 = Movies.objects.create(title="Test Movie2", length_in_minutes=100, released_at="2020-01-01", country_of_origin="NL", summary="Test summary", youtube_trailer_id="123456789")
        self.movie3 = Movies.objects.create(title="Test Movie3", length_in_minutes=100, released_at="2020-01-01", country_of_origin="NL", summary="Test summary", youtube_trailer_id="123456789")
        self.movie4 = Movies.objects.create(title="Test Movie4", length_in_minutes=100, released_at="2020-01-01", country_of_origin="NL", summary="Test summary", youtube_trailer_id="123456789")

    def test_index(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_detailmovie(self):
        url = reverse('detailmovie', kwargs={'pk': self.movie1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_updatemovie(self):
        url = reverse('updatemovie', kwargs={'pk': self.movie1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class MovieViewsTestContent(TestCase):
    def setUp(self):
        self.movie1 = Movies.objects.create(title="Test Movie", length_in_minutes=100, released_at="2020-01-01", country_of_origin="NL", summary="Test summary", youtube_trailer_id="123456789")
        self.movie2 = Movies.objects.create(title="Test Movie2", length_in_minutes=100, released_at="2020-01-01", country_of_origin="NL", summary="Test summary", youtube_trailer_id="123456789")
        self.movie3 = Movies.objects.create(title="Test Movie3", length_in_minutes=100, released_at="2020-01-01", country_of_origin="NL", summary="Test summary", youtube_trailer_id="123456789")
        self.movie4 = Movies.objects.create(title="Test Movie4", length_in_minutes=100, released_at="2020-01-01", country_of_origin="NL", summary="Test summary", youtube_trailer_id="123456789")
    
    def test_index(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertContains(response, self.movie1.title)
        self.assertContains(response, self.movie2.title)
        self.assertContains(response, self.movie3.title)
        self.assertContains(response, self.movie4.title)

    def test_detailmovie(self):
        url = reverse('detailmovie', kwargs={'pk': self.movie1.pk})
        response = self.client.get(url)
        self.assertContains(response, self.movie1.title)
        self.assertContains(response, self.movie1.length_in_minutes)
        self.assertContains(response, self.movie1.country_of_origin)
        self.assertContains(response, self.movie1.summary)

    def test_updatemovie(self):
        url = reverse('updatemovie', kwargs={'pk': self.movie1.pk})
        response = self.client.get(url)
        self.assertContains(response, self.movie1.title)
        self.assertContains(response, self.movie1.length_in_minutes)
        self.assertContains(response, self.movie1.released_at)
        self.assertContains(response, self.movie1.country_of_origin)
        self.assertContains(response, self.movie1.summary)
        self.assertContains(response, self.movie1.youtube_trailer_id)