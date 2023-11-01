from django.test import TestCase
from ..models import *
from ..views import *
from django.urls import reverse
from django.contrib.auth.models import User

class SerieViewTestCase(TestCase):
    def setUp(self):
        self.series1 = Series.objects.create(title='The Walking Dead', rating=9.0, summary='A group of survivors travel through a post-apocalyptic world, holding on to the hope of humanity by banding together to fight against the zombies that threaten their lives.', has_won_awards=1, seasons=10, country='US', spoken_in_language='EN')
        self.series2 = Series.objects.create(title='Breaking Bad', rating=9.5, summary='A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his familys future.', has_won_awards='1', seasons='5', country='US', spoken_in_language='EN')
        self.series3 = Series.objects.create(title='Game of Thrones', rating=9.3, summary='Nine noble families fight for control over the mythical lands of Westeros, while a forgotten', has_won_awards='1', seasons='8', country='US', spoken_in_language='EN')
        self.user = User.objects.create_user(username='root', password='test')
        self.client.login(username='root', password='test')

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        url = reverse('detailserie', kwargs={'pk': self.series1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_update(self):
        url = reverse('updateserie', kwargs={'pk': self.series1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_create(self):
        response = self.client.get('/createserie/')
        self.assertEqual(response.status_code, 200)

class SerieViewTestContent(TestCase):
    def setUp(self):
        self.series1 = Series.objects.create(title='The Walking Dead', rating=9.0, summary='A group of survivors travel through a post-apocalyptic world, holding on to the hope of humanity by banding together to fight against the zombies that threaten their lives.', has_won_awards=1, seasons=10, country='US', spoken_in_language='EN')
        self.series2 = Series.objects.create(title='Breaking Bad', rating=9.5, summary='A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his familys future.', has_won_awards='1', seasons='5', country='US', spoken_in_language='EN')
        self.series3 = Series.objects.create(title='Game of Thrones', rating=9.3, summary='Nine noble families fight for control over the mythical lands of Westeros, while a forgotten', has_won_awards='1', seasons='8', country='US', spoken_in_language='EN')
        self.user = User.objects.create_user(username='root', password='test')
        self.client.login(username='root', password='test')
    def test_index(self):
        response = self.client.get('/')
        self.assertContains(response, 'The Walking Dead')
        self.assertContains(response, 'Breaking Bad')
        self.assertContains(response, 'Game of Thrones')
    
    def test_detail(self):
        url = reverse('detailserie', kwargs={'pk': self.series1.pk})
        response = self.client.get(url)
        self.assertContains(response, self.series1.title)
        self.assertContains(response, self.series1.rating)
        self.assertContains(response, self.series1.summary)
        self.assertContains(response, self.series1.has_won_awards)
        self.assertContains(response, self.series1.seasons)
        self.assertContains(response, self.series1.country)
        self.assertContains(response, self.series1.spoken_in_language)
    
    def test_update(self):
        url = reverse('updateserie', kwargs={'pk': self.series1.pk})
        response = self.client.get(url)
        self.assertContains(response, self.series1.title)
        self.assertContains(response, self.series1.rating)
        self.assertContains(response, self.series1.summary)
        self.assertContains(response, self.series1.has_won_awards)
        self.assertContains(response, self.series1.seasons)
        self.assertContains(response, self.series1.country)
        self.assertContains(response, self.series1.spoken_in_language)