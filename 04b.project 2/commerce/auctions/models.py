from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	pass


class Category(models.Model):
	catName = models.CharField(max_length=64)


class Bid(models.Model):
	pass


class Comment(models.Model):
	pass


class Listing(models.Model):
	title = models.CharField(max_length=64)
	desc = models.CharField(max_length=300)
	# start_bid = models.IntegerField(default="0")
	# curr_bid = models.IntegerField(blank=True)
	# image_url = models.CharField(max_length=200)
	# category = models.ForeignKey(
	# 	Category, on_delete=models.CASCADE, related_name='category')

	def __str__(self):
		return f"{self.title}, {self.desc}"
