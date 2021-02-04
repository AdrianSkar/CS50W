from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

greeting = 'Hi'


def index(request):
	return HttpResponse(f'{greeting} there!!')


def adrian(request):
	return HttpResponse(f'{greeting} Adrian')


def brian(request):
    return HttpResponse("Hello, Brian!")


def greet(request, name):
	return HttpResponse(f"Hello, {name.capitalize()}")
