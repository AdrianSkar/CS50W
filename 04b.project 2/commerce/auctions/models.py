from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    catName = models.CharField(
        max_length=64, null=True)

    def __str__(self):
        return f"{self.catName}"


class Bid(models.Model):
    pass


class Comment(models.Model):
    pass


class Listing(models.Model):
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=300)
    start_bid = models.DecimalField(max_digits=5, decimal_places=2)
    # curr_bid = models.IntegerField(blank=True)
    image_url = models.URLField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name='category', null=True)

    def __str__(self):
        return f"{self.title}, {self.desc}"
