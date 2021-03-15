from django.contrib import admin
from .models import *


class ListingAdmin(admin.ModelAdmin):
		list_display = ('title', 'status',  'desc', 'price', 'image_url', 'category', 'lister')

class ListingBid(admin.ModelAdmin):
	list_display= ('amount', 'bidder', 'listing')

class ListingComment(admin.ModelAdmin):
	list_display = ('poster', 'listing')

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Bid, ListingBid)
admin.site.register(Comment, ListingComment)
admin.site.register(Listing, ListingAdmin)
