# Generated by Django 3.1.7 on 2021-03-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210311_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watch', to='auctions.Listing'),
        ),
    ]