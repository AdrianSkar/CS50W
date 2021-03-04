from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *
from .forms import *


def create_listing(request):
	if request.method == 'POST':
		title = request.POST["title"]
		description = request.POST["description"]
		start_bid = float(request.POST["start_bid"])
		image_url = request.POST["image_url"] or "https://images.pexels.com/photos/4439444/pexels-photo-4439444.jpeg"

		category = Category.objects.get(id=int(request.POST["category"]))
		lister = User.objects.get(id=int(request.POST["user_id"]))

		# Create listing
		try:
			listing = Listing(title=title, desc=description,
                            start_bid=start_bid, image_url=image_url, category=category, lister=lister)
			listing.save()
			return render(request, "auctions/listing.html", {
				"listing": Listing.objects.last(),
				"message": 'Thank you for your listing!'
			})
		except IntegrityError as error:
			return render(request, "auctions/create.html", {
				"message": "Invalid listing, try again.",
				# "details": (listing, error)
			})
	categories = Category.objects.all()
	return render(request, "auctions/create.html", {
		"categories": categories
	})