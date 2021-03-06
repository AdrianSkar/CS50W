from django.urls import path, re_path

from . import views

urlpatterns = [
	path("listings/<int:listing_id>", views.listing_view, name="listing"),
	path("login", views.login_view, name="login"),
	path("logout", views.logout_view, name="logout"),
	path("register", views.register_view, name="register"),
	path("create", views.create_listing_view, name="create"),
	path("watchlist", views.watchlist_view, name="watchlist"),
	path("categories", views.categories_view, name="categories"),
	path("categories/<str:category_name>", views.spec_category_view, name="spec_category"),
	re_path(r'^$|listings', views.index, name="index"),
]

