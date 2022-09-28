# Generated by Django 4.1 on 2022-09-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('length_in_minutes', models.IntegerField()),
                ('released_at', models.DateField(blank=True, null=True)),
                ('country_of_origin', models.CharField(blank=True, max_length=2, null=True)),
                ('summary', models.TextField()),
                ('youtube_trailer_id', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'movies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('summary', models.TextField()),
                ('has_won_awards', models.IntegerField()),
                ('seasons', models.IntegerField()),
                ('country', models.CharField(max_length=2)),
                ('spoken_in_language', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'series',
                'managed': False,
            },
        ),
    ]