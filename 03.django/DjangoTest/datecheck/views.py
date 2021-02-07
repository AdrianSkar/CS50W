from django.shortcuts import render
import datetime

# Create your views here.


def index(request):
	now = datetime.datetime.now()
	return render(request, 'datecheck/index.html', {
		'target': now.day == 7 and now.year == 2021,
		'targetDay': "now.day == 7 and now.year == 2021"
	})
