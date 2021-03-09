from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *
from .forms import *


def index(request):
	listings = Listing.objects.all()
	return render(request, "auctions/index.html", {
		"listings": listings
	})


def login_view(request):
	if request.method == "POST":

		# Attempt to sign user in
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)

		# Check if authentication successful
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("index"))
		else:
			return render(request, "auctions/login.html", {
				"message": "Invalid username and/or password."
			})
	else:
		return render(request, "auctions/login.html")


def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse("index"))


def register_view(request):
	if request.method == "POST":
		username = request.POST["username"]
		email = request.POST["email"]

		# Ensure password matches confirmation
		password = request.POST["password"]
		confirmation = request.POST["confirmation"]
		if password != confirmation:
			return render(request, "auctions/register.html", {
				"message": "Passwords must match."
			})

		# Attempt to create new user
		try:
			user = User.objects.create_user(username, email, password)
			user.save()
		except IntegrityError:
			return render(request, "auctions/register.html", {
				"message": "Username already taken."
			})
		login(request, user)
		return HttpResponseRedirect(reverse("index"))
	else:
		return render(request, "auctions/register.html")

def create_listing_view(request):
	# This allows to render an empty form if there's no POST request
	form = CreateListingForm(request.POST or None)

	if form.is_valid():
		try:
			# Hold form and add who is listing it
			obj = form.save(commit=False)
			obj.lister = request.user
			# Add default image if none is provided
			if not obj.image_url:
				obj.image_url = "https://images.pexels.com/photos/4439444/pexels-photo-4439444.jpeg"
			# Save form and redirect to that listing
			obj.save()
			listing = Listing.objects.last()
			return HttpResponseRedirect(reverse('listing', args=(listing.id,)))

		except IntegrityError as error:
			return render(request, "auctions/create.html",{
				"message": "Invalid listing, try again.",
				# "details": (listing, error)
			})
	return render(request, 'auctions/create.html', {
		'form': form
	})


def listing_view(request, listing_id):
	listing = Listing.objects.get(id=listing_id)

	# Check for previous bids
	if listing.list_bid.last():
		last_bid = float(listing.list_bid.last().amount)
		last_bidder = listing.list_bid.last().bidder.username
	else:
		last_bid = ''
		last_bidder = ''

	# Process bid form or make default
	bid_form = BidForm(request.POST or None)
	if bid_form.is_valid():
		if float(bid_form.cleaned_data['amount']) > listing.start_bid:
			# print(bid_form.cleaned_data['amount'])
			# print(listing.start_bid)
			# Make bid
			try:
				obj = bid_form.save(commit=False)
				obj.bidder = request.user
				listing.start_bid = obj.amount
				obj.listing = listing
				obj.save()

			except IntegrityError as error:
				return render(request, "auctions/listing.html", {
					"listing": listing, 
					"message": error
					})
			return render(request, "auctions/listing.html", {
				"listing": listing, 
				"form": bid_form,
				"alert_type": "alert-success",
				"message": 'Thank you for your bid!'})

		else:
			return render(request, "auctions/listing.html", {
				"listing": listing, 
				"form": bid_form,
				"alert_type": "alert-warning",
				"message": 'Your bid must be higher than the current one.'
				})

	context = {
		"listing": listing,
		"last_bid": last_bid,
		"last_bidder": last_bidder,
		"form": bid_form
	}
	return render(request, "auctions/listing.html", context)

