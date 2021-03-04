from django import forms

from .models import *

class BidForm(forms.ModelForm):


	class Meta:
		model = Bid
		fields = [
			'amount', 
			'bidder', 
			'listing'
		]

class CreateListingForm(forms.ModelForm):
	class Meta:
		model = Listing
		fields = [
			'title',
			'desc',
			'start_bid', 
			'image_url',
			'category'
		]