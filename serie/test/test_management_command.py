from django.test import TestCase
from django.core.management import call_command
from serie.models import Series
from django.core import mail

class SeriesRatingTest(TestCase):
    def setUp(self):
        Series.objects.create(title='The Walking Dead', rating=9.0, summary='A group of survivors travel through a post-apocalyptic world, holding on to the hope of humanity by banding together to fight against the zombies that threaten their lives.', has_won_awards=1, seasons=10, country='US', spoken_in_language='EN')
        Series.objects.create(title='Breaking Bad', rating=9.5, summary='A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his familys future.', has_won_awards='1', seasons='5', country='US', spoken_in_language='EN')
        Series.objects.create(title='Game of Thrones', rating=9.3, summary='Nine noble families fight for control over the mythical lands of Westeros, while a forgotten', has_won_awards='1', seasons='8', country='US', spoken_in_language='EN')
        Series.objects.create(title='The Big Bang Theory', rating=5.7, summary='Test', has_won_awards='1', seasons='8', country='US', spoken_in_language='EN')
        Series.objects.create(title='The Simpsons', rating=8.7, summary='Test', has_won_awards='1', seasons='8', country='US', spoken_in_language='EN')
        Series.objects.create(title='The Office', rating=9.9, summary='Test', has_won_awards='1', seasons='8', country='US', spoken_in_language='EN')

    def test_rating(self):
        serie = Series.objects.get(title='The Walking Dead')
        self.assertEqual(serie.rating, 9.0)
        serie = Series.objects.get(title='Breaking Bad')
        self.assertEqual(serie.rating, 9.5)

    def test_email_has_been_sent(self):
        call_command('series_rating')
        self.assertEqual(len(mail.outbox), 1)

    def test_email_subject(self):
        call_command('series_rating')
        self.assertEqual(mail.outbox[0].subject, 'Top 3 series')

    def test_email_body(self):
        call_command('series_rating')
        for email in mail.outbox:
            self.assertEqual(email.body.count('This is the top 3 of the series based on the rating:'), 1)
        
    def test_top_three_series(self):
        call_command('series_rating')
        for email in mail.outbox:
            self.assertEqual(email.body.count('The Office'), 1)
            self.assertEqual(email.body.count('Breaking Bad'), 1)
            self.assertEqual(email.body.count('Game of Thrones'), 1)
        
    