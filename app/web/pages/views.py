from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
import urllib.request
import urllib.parse
import json
from .forms import LoginForm, RegisterForm, MealForm

# Create your views here.
def index(request):
    if 'auth' in request.COOKIES:
        authenticator = request.COOKIES['auth']
    else:
        authenticator = ""
    data = urllib.parse.urlencode({'authenticator':authenticator}).encode('utf-8')
    req = urllib.request.Request('http://exp-api:8000/homepage/', data=data)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    return render(request, 'pages/index.html', context)

def meal_detail(request, meal_id):
    if 'auth' in request.COOKIES:
        authenticator = request.COOKIES['auth']
    else:
        authenticator = ""
    data = urllib.parse.urlencode({'authenticator':authenticator}).encode('utf-8')
    req = urllib.request.Request('http://exp-api:8000/meal/' + str(meal_id) + "/", data=data)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    context = json.loads(resp_json)
    return render(request, 'pages/meal_detail.html', context)

def search(request):
    if 'auth' in request.COOKIES:
        authenticator = request.COOKIES['auth']
    else:
        authenticator = ""
    data = urllib.parse.urlencode({'authenticator':authenticator}).encode('utf-8')
    req = urllib.request.Request('http://exp-api:8000/search/', data=data)
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

    # Get next page
    next = f.cleaned_data.get('next') or reverse('index')

    # Send validated information to experience layer
    data = urllib.parse.urlencode(f.cleaned_data).encode('utf-8')
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
    response.delete_cookie("user_id")
    return response

def register(request):
    context = {}
    if request.method == 'GET':
        next = request.GET.get('next') or reverse('index')
        form = RegisterForm()
        context['form'] = form
        return render(request, 'pages/register.html', context)
    
    f = RegisterForm(request.POST)

    # Return form with errors if invalid
    if not f.is_valid():
        context['form'] = f
        return render(request, 'pages/register.html', context)

    # Get next page
    next = f.cleaned_data.get('next') or reverse('index')

    # Send validated information to experience layer
    data = urllib.parse.urlencode(f.cleaned_data).encode('utf-8')
    req = urllib.request.Request('http://exp-api:8000/register/', data=data)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    # Check if experience layer returned an error
    if not resp or not resp['ok']:
        form = RegisterForm()
        context['form'] = form
        context['auth_error'] = resp['message']
        return render(request, 'pages/register.html', context)

    """ If we made it here, we can log them in. """
    # Set login cookie and redirect 
    authenticator = resp['authenticator']
    response = HttpResponseRedirect(next)
    response.set_cookie("auth", authenticator)
    return response

def create_meal(request):
    context = {}
    # Try to get the authenticator cookie
    auth = request.COOKIES.get('auth')

    # If the authenticator cookie wasn't set...
    if not auth:
        # Handle user not logged in while trying to create a listing
        return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_meal"))

    context['logged_in'] = True
    
    # If we received a GET request instead of a POST request...
    if request.method == 'GET':
        # Return to form page
        form = MealForm()
        context['form'] = form
        return render(request, 'pages/create_meal.html', context)

    # Otherwise, create a new form instance with our POST data
    f = MealForm(request.POST)
    if not f.is_valid():
        context['form'] = f
        return render(request, 'pages/create_meal.html', context)

    # Send validated information to our experience layer
    req_data = f.cleaned_data
    req_data['authenticator'] = auth
    data = urllib.parse.urlencode(req_data).encode('utf-8')
    req = urllib.request.Request('http://exp-api:8000/create_meal/', data=data)
    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    # Check if the experience layer said they gave us incorrect information
    if resp and not resp['ok']:
        if 'error' in resp and resp['error'] == "UNKNOWN_AUTH":
            return HttpResponseRedirect(reverse("login") + "?next=" + reverse("create_meal"))
        else:
            context['form'] = f
            context['auth_error'] = resp['message']
            return render(request, 'pages/create_meal.html', context)

    return render(request, 'pages/create_meal_success.html', context)