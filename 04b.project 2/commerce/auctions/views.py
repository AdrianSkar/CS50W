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


def register(request):
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
	form = CreateListingForm(request.POST or None)

	if form.is_valid():
		try:
			obj = form.save(commit=False)
			obj.lister = request.user
			obj.save()
			form = CreateListingForm()
			return render(request, "auctions/listing.html", {
				"listing": Listing.objects.last(),
				"message": 'Thank you for your listing!'
			})
		except IntegrityError as error:
			return render(request, "auctions/listing.html",{
				"message": "Invalid listing, try again.",
				# "details": (listing, error)
			})
	return render(request, 'auctions/create.html', {
		'form': form
	})


def listing_view(request, listing_id):
	listing = Listing.objects.get(id=listing_id)
	poster = listing.lister
	if listing.list_bid.last():
		last_bid = listing.list_bid.last().amount
		last_bidder = listing.list_bid.last().bidder.username
	else:
		last_bid = ''
		last_bidder = ''

	context = {
		"listing": listing,
		"lister": poster,
		"last_bid": last_bid,
		"last_bidder": last_bidder,
	}
	return render(request, "auctions/listing.html", context)


def bid(request):
	if request.method == 'POST':
		bid = float(request.POST['curr_bid'])
		bidder = User.objects.get(id=int(request.POST['user_id']))
		listing_id = int(request.POST['listing_id'])
		listing = Listing.objects.get(id=listing_id)

		test = listing.list_bid.last().amount or 0
		if bid > test and bid > listing.start_bid:
			# Make bid
			try:
				bid = Bid(amount=bid, bidder=bidder, listing= listing)
				bid.save()

			except IntegrityError as error:
				return render(request, "auctions/listing.html", {"listing": listing_id, "message": error})
		else:
		 return render(request, "auctions/listing.html", {"listing": listing, "message": 'Your bid must be higher than the current one.'})
	return render(request, "auctions/listing.html", {"listing": listing, "message": 'Thank you for your bid.'})

# def bid_form_view(request):
# 	form = BidForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = BidForm()
# 	return render(request, 'auctions.listing.html', {
# 		'form': form
# 	})