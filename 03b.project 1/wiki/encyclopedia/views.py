from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util


# md to html
import markdown2

# test marksafe
from django.utils.safestring import mark_safe


def index(request):
		return render(request, "encyclopedia/index.html", {
                    "entries": util.list_entries(),
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


def search(request):
	if request.method == "GET":
		query = request.GET.get('query')
		substr = util.subs_filter(query)

		# If we have such an entry
		if util.get_entry(query):
			# Convert MD to HTML and mark it as safe to output
			# You can also use {{ var | safe }} on the target .html
			output = mark_safe(markdown2.markdown(util.get_entry(query)))
			return render(request, "encyclopedia/entries.html", {
														"entry": output,
														"name": query.capitalize()
												})

		# If query is a substring of existing entries
		elif substr:
			return render(request, 'encyclopedia/results.html', {
				"entries": substr,
				"query": query
			})

	# If no complete or partial match is found
	return render(request, "encyclopedia/results.html", {
					"no_match": query
				})


def new(request):
	if request.method == "POST":
		title = request.POST['title']
		content = request.POST['content']
		if util.get_entry(title):
			# prints the relative url only (YET)
			link = request.build_absolute_uri(reverse("entries", args=[title]))
			link = f"<a href='{link}'>{reverse('entries', args=[title])}</a>"

			return render(request, "encyclopedia/error.html", {
				"title": title,
				"error_message": mark_safe(f"Sorry, an article titled <i>'{title}'</i> already exists at {link}.")
			})
		return render(request, "encyclopedia/results.html", {
			"no_match": title + content
		})
	return render(request, "encyclopedia/new.html")
