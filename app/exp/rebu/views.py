from django.shortcuts import render
from django.http import JsonResponse
import urllib.request
import urllib.parse
import json

# Helpers
def get_response(url, post_data=None):
    if post_data:
        data = urllib.parse.urlencode(post_data).encode('utf-8')
        req = urllib.request.Request(url, data=data)
    else:
        req = urllib.request.Request(url)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    return json.loads(resp_json)

def check_if_logged_in(authenticator):
    if authenticator == "":
        return False
    context = get_response('http://models-api:8000/api/v1/authenticate/', post_data={'authenticator':authenticator})
    return context['ok']

def get_auth_id(authenticator):
    if authenticator == "":
        return False
    context = get_response('http://models-api:8000/api/v1/authenticate/', post_data={'authenticator':authenticator})
    if context['ok']:
        return context['user_id']
    else:
        return -1

# Create your views here.
def homepage_info(request):
    authenticator = request.POST['authenticator']
    context = get_response('http://models-api:8000/api/v1/meals/newest')
    for i in range(len(context['result']['newest_meals'])):
        context['result']['newest_meals'][i]['tags'] = context['result']['newest_meals'][i]['tags'].split(" ")
    context['logged_in'] = check_if_logged_in(authenticator)
    return JsonResponse(context)


def meal_info(request, meal_id):
    authenticator = request.POST['authenticator']
    context = get_response('http://models-api:8000/api/v1/meals/' + str(meal_id))
    context['logged_in'] = check_if_logged_in(authenticator)
    return JsonResponse(context)


def search_info(request):
    authenticator = request.POST['authenticator']
    context = get_response('http://models-api:8000/api/v1/meals/all')
    for i in range(len(context['result']['all_meals'])):
        context['result']['all_meals'][i]['tags'] = context['result']['all_meals'][i]['tags'].split(" ")
    context['logged_in'] = check_if_logged_in(authenticator)
    return JsonResponse(context)

def login(request):
#     authenticator = request.POST['authenticator']
#     if check_if_logged_in(authenticator):
#         context = {"ok":False, "message":"Already logged in"}
#         return JsonResponse(context)
    context = get_response('http://models-api:8000/api/v1/login/', post_data=request.POST)
    context['logged_in'] = False
    return JsonResponse(context)

def register(request):
    # authenticator = request.POST['authenticator']
    # if check_if_logged_in(authenticator):
        # return JsonResponse(context)
    context = get_response('http://models-api:8000/api/v1/users/create/', post_data=request.POST)
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
        context = get_response('http://models-api:8000/api/v1/meals/create/', post_data=post_copy)
        context['logged_in'] = True
        return JsonResponse(context)
    else:
        return JsonResponse({"ok":False, "error":"UNKNOWN_AUTH"})