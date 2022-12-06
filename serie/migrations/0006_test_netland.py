# Generated by Django 4.1.1 on 2022-12-06 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serie', '0005_delete_test_netland'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_netland',
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
                'db_table': 'test_netland',
                'managed': False,
            },
        ),
    ]
