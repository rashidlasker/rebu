from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import urllib.parse
import json

# Create your views here.
def index(request):
    req = urllib.request.Request('http://exp-api:8000/homepage')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    return render(request, 'pages/index.html', context)

def meal_detail(request, meal_id):
    req = urllib.request.Request('http://exp-api:8000/meal/' + str(meal_id))
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    return render(request, 'pages/meal_detail.html', context)

def search(request):
    return HttpResponse("Search Page")
