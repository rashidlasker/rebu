from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import urllib.request
import urllib.parse
import json
from .forms import LoginForm

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
    req = urllib.request.Request('http://exp-api:8000/search')
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    return render(request, 'pages/search.html', context)

def login(request):
    context = {}
    if request.method == 'GET':
        # display the login form page
        next = request.GET.get('next') or reverse('index')
        form = LoginForm()
        context['form'] = form
        return render(request, 'pages/login.html', context)

    f = LoginForm(request.POST)
    if not f.is_valid():
        # Form was bad -- send them back to login page and show them an error
        context['form'] = f
        return render(request, 'pages/login.html', context)

    username = f.cleaned_data['username']
    password = f.cleaned_data['password']

    # # Get next page
    next = f.cleaned_data.get('next') or reverse('index')

    # # Send validated information to our experience layer
    # resp = login_exp_api(username, password)

    # # Check if the experience layer said they gave us incorrect information
    # if not resp or not resp['ok']:
    #   # Couldn't log them in, send them back to login page with error
    #   return render('login.html', ...)

    """ If we made it here, we can log them in. """
    # Set their login cookie and redirect to back to wherever they came from
    # authenticator = resp['resp']['authenticator']
    authenticator = 1234567890

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
