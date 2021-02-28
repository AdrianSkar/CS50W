from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    watchlist = []


class Category(models.Model):
    catName = models.CharField(
        max_length=64, null=True)

    def __str__(self):
        return f"{self.catName}"


class Listing(models.Model):
    status = models.BooleanField(default=True)
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=300)
    start_bid = models.DecimalField(max_digits=10, decimal_places=2)
    curr_bid = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    curr_bidder = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='curr_bidder', blank=True, null=True)
    image_url = models.URLField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name='category', null=True)
    lister = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='lister')

    def __str__(self):
        return f"{self.title}, {self.desc}"


class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bidder')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="list_bid", null=True)

    def __str__(self):
        return f"Bidder: {self.bidder}, amount: {self.amount}"


class Comment(models.Model):
    content = models.CharField(max_length=600)
    poster = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='poster')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="list_comment", null=True)

    def __str__(self):
        return f"Poster: {self.poster}, comment: {self.content}"
