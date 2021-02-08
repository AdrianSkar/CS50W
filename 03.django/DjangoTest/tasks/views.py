from django.shortcuts import render

# Create your views here.

tasks = ['foo', 'fooly', 'foolong']


def index(request):
	return render(request, 'tasks/index.html', {
		"tasks": tasks	})

# Add new task:


def add(request):
	return render(request, "tasks/add.html")
