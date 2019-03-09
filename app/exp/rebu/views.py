from django.shortcuts import render
from django.http import JsonResponse
import urllib.request
import urllib.parse
import json

# Helpers
def check_if_logged_in(authenticator):
    if authenticator == "":
        return False
    data = urllib.parse.urlencode({'authenticator':authenticator}).encode('utf-8')
    req = urllib.request.Request('http://models-api:8000/api/v1/authenticate/', data=data)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    return context['ok']

def get_auth_id(authenticator):
    if authenticator == "":
        return False
    data = urllib.parse.urlencode({'authenticator':authenticator}).encode('utf-8')
    req = urllib.request.Request('http://models-api:8000/api/v1/authenticate/', data=data)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    if context['ok']:
        return context['user_id']
    else:
        return -1

# Create your views here.
def homepage_info(request):
    authenticator = request.POST['authenticator']
    req = urllib.request.Request('http://models-api:8000/api/v1/meals/newest')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    for i in range(len(context['result']['newest_meals'])):
        context['result']['newest_meals'][i]['tags'] = context['result']['newest_meals'][i]['tags'].split(" ")
    context['logged_in'] = check_if_logged_in(authenticator)
    return JsonResponse(context)


def meal_info(request, meal_id):
    authenticator = request.POST['authenticator']
    req = urllib.request.Request('http://models-api:8000/api/v1/meals/' + str(meal_id))
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    context['logged_in'] = check_if_logged_in(authenticator)
    return JsonResponse(context)


def search_info(request):
    authenticator = request.POST['authenticator']
    req = urllib.request.Request('http://models-api:8000/api/v1/meals/all')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    for i in range(len(context['result']['all_meals'])):
        context['result']['all_meals'][i]['tags'] = context['result']['all_meals'][i]['tags'].split(" ")
    context['logged_in'] = check_if_logged_in(authenticator)
    return JsonResponse(context)

def login(request):
    data = urllib.parse.urlencode(request.POST).encode('utf-8')
    req = urllib.request.Request('http://models-api:8000/api/v1/login/', data=data)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    context['logged_in'] = False
    return JsonResponse(context)

def register(request):
    data = urllib.parse.urlencode(request.POST).encode('utf-8')
    req = urllib.request.Request('http://models-api:8000/api/v1/users/create/', data=data)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    context['logged_in'] = False
    return JsonResponse(context)

def create_meal(request):
    authenticator = request.POST['authenticator']
    logged_in = check_if_logged_in(authenticator)
    if logged_in:
        post_copy = request.POST.copy()
        post_copy.pop('authenticator')
        cook_id = get_auth_id(authenticator)
        post_copy['cook'] = cook_id
        data = urllib.parse.urlencode(post_copy).encode('utf-8')
        req = urllib.request.Request('http://models-api:8000/api/v1/meals/create/', data=data)
        resp_json = urllib.request.urlopen(req).read().decode('utf-8')
        context = json.loads(resp_json)
        return JsonResponse(context)
    else:
        return JsonResponse({"ok":False, "error":"UNKNOWN_AUTH"})