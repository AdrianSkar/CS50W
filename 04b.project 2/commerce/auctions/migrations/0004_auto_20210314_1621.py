# Generated by Django 3.1.7 on 2021-03-14 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listing_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='auctions.category'),
        ),
    ]
