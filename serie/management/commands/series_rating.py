from django.core.management.base import BaseCommand, CommandError
from serie.models import Series
from django.core.mail import send_mail

class Command(BaseCommand):
    help = "Automatically check each week for the top 3 based on the rating of the series"

    def handle(self, *args, **options):
        series = Series.objects.all().order_by('-rating')[:3]

        send_mail(
            'Top 3 series',
            'The top 3 series are: ' + series[0].title + ', ' + series[1].title + ', ' + series[2].title,
            'erhan@test.nl',
            ['erhan.citil@maykinmedia.nl'],
        )
