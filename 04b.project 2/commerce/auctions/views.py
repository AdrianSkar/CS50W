from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


def index(request):
	listings = Listing.objects.all()
	return render(request, "auctions/index.html", {
		"listings": listings
	})

def categories_view(request):
	categories = Category.objects.all()
	return render(request, "auctions/categories.html", {
		"categories": categories
	})
def spec_category_view(request, category_name):
	cat = Category.objects.get(catName=category_name)
	listings = Listing.objects.filter(category=cat)
	return render(request, "auctions/spec_category.html", {
		"listings": listings,
		"cat": cat
	})


@login_required(login_url = 'login')
def watchlist_view(request):
	user = User.objects.get(id=request.user.id)
	watched_items = user.watchlist.all()

	return render(request, "auctions/watchlist.html",{
		"watched_listings": watched_items
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
			if request.POST.get('next'):
				next_url = request.POST.get('next')
				return redirect(next_url)
			else:
				return redirect('index')
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

@login_required(login_url = 'login')
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
	bids = Bid.objects.filter(listing=listing)

	# Check for previous bids/bidders
	last_bid = float(listing.list_bid.last().amount) if listing.list_bid.last() else ''
	last_bidder = listing.list_bid.last().bidder.username if listing.list_bid.last() else ''

	# Current bid + initial value display to make new bid
	curr_bid = float(listing.price)
	test = {
		"amount": '{:.2f}'.format(curr_bid + 0.01)
	}

	# Define common params for returned view context
	context = {
		"listing": listing,
		"form": BidForm(None, initial=test),
		"comment_form": CommentForm(),
		"comments": Comment.objects.filter(listing=listing),
		"last_bid": last_bid,
		"last_bidder": last_bidder,
		"num_bids": bids.count() or 0,
		"bids": bids.all()
	}

	if request.user.is_authenticated:
		user = User.objects.get(id=request.user.id)
		listing.watched = listing in user.watchlist.all()
	
	# Differentiate between forms
	if request.method == 'POST':

		## Watchlist form
		if 'watchlist' in request.POST:
			print('WATCHLIST form')
			ret_to_listing = HttpResponseRedirect(reverse('listing', args=(listing.id,)))
			if listing.watched:
				user.watchlist.remove(listing)
				user.save()
				print(f"removed {listing}")
				return ret_to_listing
			else:
				user.watchlist.add(listing)
				user.save()
				print(f"appended {listing}")
				return ret_to_listing

		## Comment form
		elif 'comment' in request.POST:
			print('COMMENT form')
			comment_form = CommentForm(request.POST)
			if comment_form.is_valid():
				try:
					obj = comment_form.save(commit=False)
					obj.poster = request.user
					obj.listing = listing
					obj.save()
				except IntegrityError as error:
						context['message']=error
						return render(request, "auctions/listing.html", context)
				# Success comment
				return HttpResponseRedirect(reverse('listing', args=(listing.id,)))

		## Bid form
		else:
			print('BID form')
			bid_form = BidForm(request.POST)
			if bid_form.is_valid():
				if float(bid_form.cleaned_data['amount']) > curr_bid:
					# Make bid
					try:
						# Save new amounts and bidder to objects before proccessing them
						obj = bid_form.save(commit=False)
						obj.bidder = request.user
						listing.price = obj.amount
						listing.save()
						obj.listing = listing
						obj.save()

					except IntegrityError as error:
						context['message']=error
						return render(request, "auctions/listing.html", context)
					# Success feedback and render
					context['message'] = 'Thank you for your bid!'
					context['alert_type'] = 'alert-success'
					return render(request, "auctions/listing.html", context)
				# Not enough amount feedback and render
				else:
					context['message']= 'Your bid must be higher than the current one.'
					context['alert_type']= 'alert-warning'
					return render(request, "auctions/listing.html", context)

	return render(request, "auctions/listing.html", context)

