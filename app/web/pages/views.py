from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	context = {
		"newest_meals": [
			{
				"name": "Pizza",
				"description": "its food!",
				"calories": 600,
				"tags": ["yum", "yummy", "yum"]
			},
			{
				"name": "Pizza2",
				"description": "its food2!",
				"calories": 700,
				"tags": ["yum2", "yummy", "yum"]
			},
			{
				"name": "Pizza3",
				"description": "its food3!",
				"calories": 800,
				"tags": ["yum3", "yummy", "yum"]
			},
		]
	}
	return render(request, 'pages/index.html', context)

def meal_detail(request, meal_id):
    return HttpResponse("You're looking at meal %s." % meal_id)

def search(request):
    return HttpResponse("Search Page")