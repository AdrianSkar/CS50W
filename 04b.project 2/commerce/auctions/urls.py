from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("login", views.login_view, name="login"),
	path("logout", views.logout_view, name="logout"),
	path("register", views.register_view, name="register"),
	path("create", views.create_listing_view, name="create"),
	path("listings/<int:listing_id>", views.listing_view, name="listing"),
]

