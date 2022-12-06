from django.test import TestCase
from .models import *
# Create your tests here.

class SerieTestCase(TestCase):
    def setUp(self):
        Series.objects.create(title='The Walking Dead', rating=9.0, summary='A group of survivors travel through a post-apocalyptic world, holding on to the hope of humanity by banding together to fight against the zombies that threaten their lives.', has_won_awards=1, seasons=10, country='US', spoken_in_language='EN')
        Series.objects.create(title='Breaking Bad', rating='9.5', summary='A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his familys future.', has_won_awards='1', seasons='5', country='US', spoken_in_language='EN')
        Series.objects.create(title='Game of Thrones', rating='9.3', summary='Nine noble families fight for control over the mythical lands of Westeros, while a forgotten', has_won_awards='1', seasons='8', country='US', spoken_in_language='EN')

    def test_title(self):
        serie = Series.objects.get(title='The Walking Dead')
        self.assertEqual(serie.title, 'The Walking Dead')
    
    def test_rating(self):
        serie = Series.objects.get(rating=9.0)
        self.assertEqual(serie.rating, 9.0)
    
    def test_summary(self):
        serie = Series.objects.get(summary='A group of survivors travel through a post-apocalyptic world, holding on to the hope of humanity by banding together to fight against the zombies that threaten their lives.')
        self.assertEqual(serie.summary, 'A group of survivors travel through a post-apocalyptic world, holding on to the hope of humanity by banding together to fight against the zombies that threaten their lives.')
    
    def test_has_won_awards(self):
      for serie in Series.objects.all():
        self.assertEqual(serie.has_won_awards, 1)
    
    def test_seasons(self):
        serie = Series.objects.get(seasons=10)
        self.assertEqual(serie.seasons, 10)
    
    def test_country(self):
        for serie in Series.objects.all():
            self.assertEqual(serie.country, 'US')
    
    def test_spoken_in_language(self):
        for serie in Series.objects.all():
            self.assertEqual(serie.spoken_in_language, 'EN')