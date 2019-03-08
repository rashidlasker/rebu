from django.shortcuts import render
from django.http import JsonResponse
import urllib.request
import urllib.parse
import json

# Create your views here.
def homepage_info(request):
    req = urllib.request.Request('http://models-api:8000/api/v1/meals/newest')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    for i in range(len(context['result']['newest_meals'])):
        context['result']['newest_meals'][i]['tags'] = context['result']['newest_meals'][i]['tags'].split(" ")
    return JsonResponse(context)

def meal_info(request, meal_id):
    req = urllib.request.Request('http://models-api:8000/api/v1/meals/' + str(meal_id))
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    return JsonResponse(context)

def search_info(request):
    req = urllib.request.Request('http://models-api:8000/api/v1/meals/all')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    for i in range(len(context['result']['all_meals'])):
        context['result']['all_meals'][i]['tags'] = context['result']['all_meals'][i]['tags'].split(" ")
    return JsonResponse(context)

def login(request):
    data = urllib.parse.urlencode(request.POST).encode('utf-8')
    req = urllib.request.Request('http://models-api:8000/api/v1/authenticate/', data=data)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    return JsonResponse(context)

def register(request):
    data = urllib.parse.urlencode(request.POST).encode('utf-8')
    req = urllib.request.Request('http://models-api:8000/api/v1/users/create/', data=data)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    return JsonResponse(context)