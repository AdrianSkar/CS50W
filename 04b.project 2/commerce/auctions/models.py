from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    watchlist = models.ManyToManyField("Listing", blank=True, related_name = 'watch')


class Category(models.Model):
    catName = models.CharField(
        max_length=64, null=True)
    cat_img = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.catName}"


class Listing(models.Model):
    status = models.BooleanField(default=True)
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=600)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name='category', blank=True, null=True)
    lister = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='lister')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Title: {self.title}, status: {self.status}, category: {self.category}, price: {self.price}"


class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bidder')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="list_bid", null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bidder: {self.bidder}, amount: {self.amount}, listing: {self.listing}"


class Comment(models.Model):
    content = models.CharField(max_length=600)
    poster = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='poster')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="list_comment")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Poster: {self.poster}, comment: {self.content}, listing: {self.listing.title}"
