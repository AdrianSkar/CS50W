from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

from . import util


# md to html
import markdown2

# test marksafe
from django.utils.safestring import mark_safe


def index(request):
	# form = NewSearchForm()
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
		substr = util.subs(query)

		if util.get_entry(query):  # If we have such an entry
			# Convert MD to HTML and mark it as safe to output
			output = mark_safe(markdown2.markdown(util.get_entry(query)))
			return render(request, "encyclopedia/entries.html", {
														"entry": output,
														"name": query.capitalize()
												})
		elif substr:  # If query is substring of existing entries
			# new_entries = list(filter(lambda k: query in k, util.list_entries()))
			return render(request, 'encyclopedia/results.html', {
				"entries": substr,
				"query": query
			})

	# If no complete or partial match is found
	return render(request, "encyclopedia/results.html", {
            "no_match": query
				})
