from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

greeting = 'Hi'


def index(request):
	return render(request, "secondApp/index.html")


def adrian(request):
	return HttpResponse(f'{greeting} Adrian')


def brian(request):
    return HttpResponse("<h1 style=\"color: blue;\">Hello, Brian!</h1>")


def number(request, number):
	return HttpResponse(f"Hello, the number you chose was {number}")


def greet(request, name):
	# return HttpResponse(f"Hello, the string you chose was {name.capitalize()}")
	return render(request, 'secondApp/greet.html', {
		"name": name.capitalize()
	})
