# Generated by Django 3.1.1 on 2020-12-19 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listings_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
