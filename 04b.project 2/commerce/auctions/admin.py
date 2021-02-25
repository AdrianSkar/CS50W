from django.contrib import admin
from .models import *


class ListingAdmin(admin.ModelAdmin):
	list_display = ('title', 'desc', 'start_bid', 'image_url', 'category')


# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Listing, ListingAdmin)
