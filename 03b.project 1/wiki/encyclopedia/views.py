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
                				# "form": form
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
		if util.get_entry(query):
			# Convert MD to HTML and mark it as safe to output
			output = mark_safe(markdown2.markdown(util.get_entry(query)))
			return render(request, "encyclopedia/entries.html", {
                            "entry": output,
                        })
		elif util.subs(query):  # check if substring like in tests.py
			print('test')

	return render(request, "encyclopedia/results.html", {
            "query": "No query found named "+query
        })
