from django import forms

from .models import *

class BidForm(forms.ModelForm):
	class Meta:
		model = Bid
		fields = [
			'amount'
		]

class CreateListingForm(forms.ModelForm):
	#  https://stackoverflow.com/a/29717314
	def __init__(self, *args, **kwargs):
		super(CreateListingForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Listing
		fields = [
			'title',
			'desc',
			'start_bid', 
			'image_url',
			'category'
		]