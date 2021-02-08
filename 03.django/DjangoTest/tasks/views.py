from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

# Hardcoded task list (use sessions)
# tasks = ['foo', 'fooly', 'foolong']


def index(request):
	# return render(request, 'tasks/index.html', {
	# 	"tasks": tasks	})

	# Create an empty list if one doesn't exist
	if "tasks" not in request.session:
		request.session["tasks"] = []
	return render(request, "tasks/index.html", {
		"tasks": request.session["tasks"]
	})

# Add new task:


# def add(request):
# 	return render(request, "tasks/add.html")

def add(request):

	if request.method == "POST":
		form = NewTaskForm(request.POST)
		if form.is_valid():
			# Isolate the task from the 'cleaned' version of form data
			task = form.cleaned_data["task"]
			deleteField = form.cleaned_data["deleteField"]
			# tasks.append(task)
			request.session["tasks"] += [task]

			## Delete field if provided
			if deleteField:
				for test in request.session["tasks"]:
					if test == deleteField:
						request.session["tasks"].remove(test)
			##

			#Redirect user to tasks list
			return HttpResponseRedirect(reverse("tasks:index"))
		else:
			return render(request, "tasks/add.html", {
				"form": form,
			})

	return render(request, "tasks/add.html", {
		"form": NewTaskForm(),
		"test": 123,
		"renderData": request.session["tasks"]
	})


# Create form
class NewTaskForm(forms.Form):
	task = forms.CharField(label='New task')
	difField = forms.IntegerField(max_value=3, label='number below 4')
	deleteField = forms.CharField(label='delete this', required=False)
