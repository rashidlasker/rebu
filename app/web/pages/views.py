from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import urllib.request
import urllib.parse
import json
from .forms import LoginForm

# Create your views here.
def index(request):
    req = urllib.request.Request('http://exp-api:8000/homepage/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    return render(request, 'pages/index.html', context)

def meal_detail(request, meal_id):
    req = urllib.request.Request('http://exp-api:8000/meal/' + str(meal_id))
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    return render(request, 'pages/meal_detail.html', context)

def search(request):
    req = urllib.request.Request('http://exp-api:8000/search/')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    return render(request, 'pages/search.html', context)

def login(request):
    context = {}
    if request.method == 'GET':
        next = request.GET.get('next') or reverse('index')
        form = LoginForm()
        context['form'] = form
        return render(request, 'pages/login.html', context)

    f = LoginForm(request.POST)

    # Return form with errors if invalid
    if not f.is_valid():
        context['form'] = f
        return render(request, 'pages/login.html', context)

    username = f.cleaned_data['username']
    password = f.cleaned_data['password']

    # Get next page
    next = f.cleaned_data.get('next') or reverse('index')

    # Send validated information to experience layer
    data = urllib.parse.urlencode({'username':username,'password':password}).encode('utf-8')
    req = urllib.request.Request('http://exp-api:8000/login/', data=data)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    # Check if experience layer returned an error
    if not resp or not resp['ok']:
        form = LoginForm()
        context['form'] = form
        context['auth_error'] = resp['message']
        return render(request, 'pages/login.html', context)

    """ If we made it here, we can log them in. """
    # Set login cookie and redirect 
    authenticator = resp['authenticator']
    response = HttpResponseRedirect(next)
    response.set_cookie("auth", authenticator)
    return response

def logout(request):
    context = {}
    response = render(request, 'pages/logout.html', context)
    response.delete_cookie("auth")
    return response

def register(request):
    # req = urllib.request.Request('http://exp-api:8000/search')
    # resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    # context = json.loads(resp_json)
    context = {}
    return render(request, 'pages/register.html', context)

def create_meal(request):
    # req = urllib.request.Request('http://exp-api:8000/search')
    # resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    # context = json.loads(resp_json)
    context = {}
    return render(request, 'pages/create_meal.html', context)
