# Generated by Django 3.1.1 on 2020-12-19 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_remove_listings_time_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='time_created',
            field=models.DateTimeField(default=None),
        ),
    ]
