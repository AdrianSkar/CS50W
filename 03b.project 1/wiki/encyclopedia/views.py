from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

from . import util


# md to html
import markdown2

# test marksafe
from django.utils.safestring import mark_safe


def index(request):
	return render(request, "encyclopedia/index.html", {
		"entries": util.list_entries()
	})


def entries(request, entry):

	if util.get_entry(entry):
		# Convert MD to HTML and mark it as safe to output
		output = mark_safe(markdown2.markdown(util.get_entry(entry)))
		title = ''
	else:
		output = False
		title = 'Oops'

	return render(request, "encyclopedia/entries.html", {
		"entry": output,
		"title": title,
		"name": entry
	})


# def search(request):
# 	# if request.method == "POST":
# 	# 	form = NewSearchForm(request.POST)
# 	# 	if form.is_valid():
# 	# 		# Isolate the task from the 'cleaned' version of form data
# 	# 		search = form.cleaned_data["query"]

# 	# 		#Redirect user to tasks list
# 	# 		# return HttpResponseRedirect(reverse("tasks:index"))
# 	# 		return render(request, "entries.html", search)

# 	# 	else:
# 	# 		return render(request, "entries.html", 'css')

# 	return render(request, "encyclopedia/index.html", {
# 		"entries": util.list_entries()
# 	})


# # search class
# class NewSearchForm(forms.Form):
# 	query = forms.CharField(label='search', help_text='Search here')
