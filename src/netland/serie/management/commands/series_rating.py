from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError
from django.utils.html import strip_tags

from serie.models import Series


class Command(BaseCommand):
    help = (
        "Automatically check each week for the top 3 based on the rating of the series"
    )

    def handle(self, *args, **options):
        series = Series.objects.all().order_by("-rating")[:3]

        body = """
        <h1> Hello! </h1>
        <p> This is the top 3 of the series based on the rating: </p>
        <ul>
            <li> {0}, {1} </li>
            <li> {2}, {3} </li>
            <li> {4}, {5} </li>
        </ul>

               
 \ \        / / | | |     | |                  | |
  \ \  /\  / /__| | |   __| | ___  _ __   ___  | |
   \ \/  \/ / _ \ | |  / _` |/ _ \| '_ \ / _ \ | |
    \  /\  /  __/ | | | (_| | (_) | | | |  __/ |_|
     \/  \/ \___|_|_|  \__,_|\___/|_| |_|\___| (_)
        """.format(
            series[0].title,
            series[0].rating,
            series[1].title,
            series[1].rating,
            series[2].title,
            series[2].rating,
        )

        send_mail(
            "Top 3 series",
            strip_tags(body),
            "test@gmail.nl",
            ["erhan.citil@maykinmedia.nl"],
        )
