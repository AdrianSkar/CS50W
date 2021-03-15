from django import forms

from .models import *


# class WatchForm(forms.Form):
# 	status = forms.BooleanField()

class BidForm(forms.ModelForm):
	amount = forms.DecimalField(
			label ="Bid amount", 
			widget=forms.NumberInput(attrs={
				'class': 'form-control my-2 bid_field'
			})
		)
	class Meta:
		model = Bid
		fields = [
			'amount'
		]
class CommentForm(forms.ModelForm):
	content = forms.CharField(
			label = '',
			widget=forms.Textarea(
				attrs = {
					'rows': 6, 
					'placeholder':'Your comment',
					'class': 'form-control mb-2'
					}
			)
		)
	class Meta:
		model = Comment
		fields = [
			'content'
		]

class CreateListingForm(forms.ModelForm):
	#  https://stackoverflow.com/a/29717314
	def __init__(self, *args, **kwargs):
		super(CreateListingForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			# print(visible.field.widget)
			# add 'form-select' to category
			if hasattr(visible.field.widget, 'choices'):
				visible.field.widget.attrs['class'] = 'form-control form-select mb-3'
			# Otherwise add regular form classes
			else:
				visible.field.widget.attrs['class'] = 'form-control mb-3'

	desc = forms.CharField(
		widget=forms.Textarea(attrs={
			'rows': 6,
		})
	)

	class Meta:
		model = Listing
		fields = [
			'title',
			'desc',
			'price', 
			'image_url',
			'category'
		]