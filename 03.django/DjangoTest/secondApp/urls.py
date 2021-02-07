from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("adrian", views.adrian, name="adrian"),
	path("brian", views.brian, name="brian"),
	path("<int:number>", views.number, name="number"),
	path("<str:name>", views.greet, name="greet")
]
