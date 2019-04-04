from django.shortcuts import render
from django.http import JsonResponse
from elasticsearch import Elasticsearch
from kafka import KafkaProducer
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
def auth_check(request):
    authenticator = request.POST.get('authenticator', "")
    return JsonResponse({'ok':check_if_logged_in(authenticator)})

def homepage_info(request):
    authenticator = request.POST.get('authenticator', "")
    context = get_response('http://models-api:8000/api/v1/meals/newest')
    for i in range(len(context['result']['newest_meals'])):
        context['result']['newest_meals'][i]['tags'] = context['result']['newest_meals'][i]['tags'].split(" ")
    context['logged_in'] = check_if_logged_in(authenticator)
    return JsonResponse(context)


def meal_info(request, meal_id):
    authenticator = request.POST.get('authenticator', "")
    context = get_response('http://models-api:8000/api/v1/meals/' + str(meal_id))
    context['logged_in'] = check_if_logged_in(authenticator)
    return JsonResponse(context)


def search_info(request):
    authenticator = request.POST.get('authenticator', "")
    query = request.GET.get('query', "")
    count = request.GET.get('count', 100)
    es = Elasticsearch(['es'])
    context = {}
    if len(query) > 0:
        search_result = es.search(index='meals_index', body={'query': {'query_string': {'query': query}}, 'size': count})
    else:
        search_result = es.search(index='meals_index', body={'query': {'query': {'match_all': {}}}, 'size': count})

    meals = [o['_source'] for o in search_result['hits']['hits']]
    for i in range(len(meals)):
        meals[i]['tags'] = meals[i]['tags'].split(" ")
    context['result'] = meals
    context['query'] = query
    context['logged_in'] = check_if_logged_in(authenticator)
    return JsonResponse(context)

def login(request):
    authenticator = request.POST.get('authenticator', "")
    if check_if_logged_in(authenticator):
        context = {"ok":False, "message":"Logged in"}
        return JsonResponse(context)
    context = get_response('http://models-api:8000/api/v1/login/', post_data=request.POST)
    context['logged_in'] = False
    return JsonResponse(context)

def register(request):
    authenticator = request.POST.get('authenticator', "")
    if check_if_logged_in(authenticator):
        context = {"ok":False, "message":"Logged in"}
        return JsonResponse(context)
    context = get_response('http://models-api:8000/api/v1/users/create/', post_data=request.POST)
    context['logged_in'] = False
    return JsonResponse(context)

def create_meal(request):
    authenticator = request.POST.get('authenticator', "")
    logged_in = check_if_logged_in(authenticator)
    if logged_in:
        post_copy = request.POST.copy()
        post_copy.pop('authenticator')
        cook_id = get_auth_id(authenticator)
        post_copy['cook'] = cook_id
        # add kafka producer here
        context = get_response('http://models-api:8000/api/v1/meals/create/', post_data=post_copy)
        context['logged_in'] = True
        if 'ok' in context and context['ok']:
            producer = KafkaProducer(bootstrap_servers='kafka:9092')
            post_copy['id'] = context['id']
            producer.send('new-meals-topic', json.dumps(post_copy).encode('utf-8'))
        return JsonResponse(context)
    else:
        return JsonResponse({"ok":False, "error":"UNKNOWN_AUTH"})