import datetime
import pytz
import os
import hmac
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import make_password, check_password
from rebu.models import user, meal, cook, eater, plate, eater_rating, review, authenticator, recommendation
from .forms import userForm, mealForm, cookForm, eaterForm, plateForm, eaterRatingForm, reviewForm, authenticatorForm

# Create your views here.
def users(request, id=None):
    if request.method == 'GET':
        try:
            obj = user.objects.get(pk=id)
            response = {
                "ok":True,
                "result": model_to_dict(obj)
            }
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    elif request.method == 'POST':
        try:
            obj = user.objects.get(pk=id)
            user_form = userForm(data=request.POST)
            for i in user_form.data:
                if i == 'password':
                    obj.__setattr__(i, make_password(user_form.data[i]))
                else:
                    obj.__setattr__(i, user_form.data[i])
            obj.save()

#			if user_form.is_valid():
#				user_form.save()
#				obj = form.save()
#				obj.save()
#			else:
#			return JsonResponse({"ok":False, "message":obj})
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    elif request.method == 'DELETE':
        try:
            obj = user.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})

def create_user(request):
    if request.method == 'POST':
        try:
            obj = user()
            form = userForm(request.POST)
            if form.is_valid():
                obj.first_name = form.cleaned_data['first_name']
                obj.last_name = form.cleaned_data['last_name']
                obj.street = form.cleaned_data['street']
                obj.zip_code = form.cleaned_data['zip_code']
                obj.state = form.cleaned_data['state']
                obj.country = form.cleaned_data['country']
                obj.bio = form.cleaned_data['bio']
                obj.links = form.cleaned_data['links']
                obj.language = form.cleaned_data['language']
                obj.gender = form.cleaned_data['gender']
                obj.username = form.cleaned_data['username']
                obj.password = make_password(form.cleaned_data['password'])
                obj.save()
            else:
                return JsonResponse({"ok":False, "message":"Bad Form"})
            success, authenticator = get_authenticator(obj)
            if success:
                return JsonResponse({"ok":True, "authenticator":authenticator})
            else:
                return JsonResponse({"ok":False, "message":authenticator})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})


def cooks(request, id=None):
    if request.method == 'GET':
        try:
            obj = cook.objects.get(pk=id)
            response = {
                "ok":True,
                "result": model_to_dict(obj)
            }
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    elif request.method == 'POST':
        try:
            obj = cook.objects.get(pk=id)
            form = userForm(data=request.POST)
            for i in form.data:
                obj.__setattr__(i, form.data[i])
            obj.save()

#			obj = cook.objects.get(pk=id)
#			form = cookForm(request.POST or None, instance=obj)
#			if form.is_valid():
#				obj = form.save()
#				obj.save()
#			else:
#				return JsonResponse({"ok":False, "message":"Bad Form"})
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    elif request.method == 'DELETE':
        try:
            obj = cook.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})

def create_cook(request):
    if request.method == 'POST':
        try:
            obj = cook()
            form = cookForm(request.POST)
            if form.is_valid():
                obj.signature_dish = form.cleaned_data['signature_dish']
                obj.user = form.cleaned_data['user']
                obj.save()
            else:
                return JsonResponse({"ok":False, "message":"Bad Form"})

            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})

def eaters(request, id=None):
    if request.method == 'GET':
        try:
            obj = eater.objects.get(pk=id)
            response = {
                "ok":True,
                "result": model_to_dict(obj)
            }
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    elif request.method == 'POST':
        try:
            obj = eater.objects.get(pk=id)
            form = userForm(data=request.POST)
            for i in form.data:
                obj.__setattr__(i, form.data[i])
            obj.save()

#			obj = eater.objects.get(pk=id)
#			form = eaterForm(request.POST or None, instance=obj)
#			if form.is_valid():
#				obj = form.save()
#				obj.save()
#			else:
#				return JsonResponse({"ok":False, "message":"Bad Form"})
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    elif request.method == 'DELETE':
        try:
            obj = eater.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})

def create_eater(request):
    if request.method == 'POST':
        try:
            obj = eater()
            form = eaterForm(request.POST)
            if form.is_valid():
                obj.user =form.cleaned_data['user']
                obj.save()
            else:
                return JsonResponse({"ok":False, "message":"Bad Form"})
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})



def meals(request, id=None):
    if request.method == 'GET':
        try:
            obj = meal.objects.get(pk=id)
            response = {
                "ok":True,
                "result": model_to_dict(obj)
            }
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    elif request.method == 'POST':
        try:
            obj = meal.objects.get(pk=id)
            form = userForm(data=request.POST)
            for i in form.data:
                obj.__setattr__(i, form.data[i])
            obj.save()

#			obj = meal.objects.get(pk=id)
#			form = mealForm(request.POST or None, instance=obj)
#			if form.is_valid():
#				obj = form.save()
#				obj.save()
#			else:
#				return JsonResponse({"ok":False, "message":"Bad Form"})
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    elif request.method == 'DELETE':
        try:
            obj = meal.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})


def create_meal(request):
    if request.method == 'POST':
        try:
            obj = meal()
            form = mealForm(request.POST)
            if form.is_valid():
                obj.name = form.cleaned_data['name']
                obj.calories = form.cleaned_data['calories']
                obj.description = form.cleaned_data['description']
                obj.spice = form.cleaned_data['spice']
                obj.price = form.cleaned_data['price']
                obj.tags = form.cleaned_data['tags']
                obj.takeout_available = form.cleaned_data['takeout_available']
                obj.num_plates = form.cleaned_data['num_plates']
                obj.start = form.cleaned_data['start']
                obj.end = form.cleaned_data['end']
                obj.cook = form.cleaned_data['cook']#cook.objects.get(pk=form.cleaned_data['cook'])
                obj.save()
            else:
                return JsonResponse({"ok":False, "message": str(request.POST)})

            return JsonResponse({"ok":True, "id":obj.pk})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})


def plates(request, id=None):
    if request.method == 'GET':
        try:
            obj = plate.objects.get(pk=id)
            response = {
                "ok":True,
                "result": model_to_dict(obj)
            }
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    elif request.method == 'POST':
        try:
            obj = plate.objects.get(pk=id)
            form = userForm(data=request.POST)
            for i in form.data:
                obj.__setattr__(i, form.data[i])
            obj.save()

#			obj = plate.objects.get(pk=id)
#			form = plateForm(request.POST or None, instance=obj)
#			if form.is_valid():
#				obj = form.save()
#				obj.save()
#			else:
#				return JsonResponse({"ok":False, "message":"Bad Form"})
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    elif request.method == 'DELETE':
        try:
            obj = plate.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})

def create_plate(request):
    if request.method == 'POST':
        try:
            obj = plate()
            form = plateForm(request.POST)
            if form.is_valid():
                obj.meal = form.cleaned_data['meal']
                obj.eater = form.cleaned_data['eater']
                obj.save()
            else:
                return JsonResponse({"ok":False, "message":"Bad Form"})

            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})


def eater_ratings(request, id=None):
    if request.method == 'GET':
        try:
            obj = eater_rating.objects.get(pk=id)
            response = {
                "ok":True,
                "result": model_to_dict(obj)
            }
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    elif request.method == 'POST':
        try:
            obj = eater_rating.objects.get(pk=id)
            form = userForm(data=request.POST)
            for i in form.data:
                obj.__setattr__(i, form.data[i])
            obj.save()

#			obj = eater_rating.objects.get(pk=id)
#			form = eaterRatingForm(request.POST or None, instance=obj)
#			if form.is_valid():
#				obj = form.save()
#				obj.save()
#			else:
#				return JsonResponse({"ok":False, "message":"Bad Form"})

            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    elif request.method == 'DELETE':
        try:
            obj = eater_rating.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})

def create_eater_rating(request):
    if request.method == 'POST':
        try:
            obj = eater_rating()
            form = eaterRatingForm(request.POST)
            if form.is_valid():
                obj.rating = form.cleaned_data['rating']
                obj.description = form.cleaned_data['description']
                obj.cook = form.cleaned_data['cook']
                obj.eater = form.cleaned_data['eater']
                obj.save()
            else:
                return JsonResponse({"ok":False, "message":"Bad Form"})
            obj.save()
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})

def reviews(request, id=None):
    if request.method == 'GET':
        try:
            obj = review.objects.get(pk=id)
            response = {
                "ok":True,
                "result": model_to_dict(obj)
            }
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    elif request.method == 'POST':
        try:
            obj = review.objects.get(pk=id)
            form = userForm(data=request.POST)
            for i in form.data:
                obj.__setattr__(i, form.data[i])
            obj.save()

#			obj = review.objects.get(pk=id)
#			form = reviewForm(request.POST, instance=obj)
#			if form.is_valid():
#				obj = form.save()
#				obj.save()
#			else:
#				return JsonResponse({"ok":False, "message":"Bad Form"})
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    elif request.method == 'DELETE':
        try:
            obj = review.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})

def create_review(request):
    if request.method == 'POST':
        try:
            obj = review()
            form = reviewForm(request.POST)
            if form.is_valid():
                obj.rating = form.cleaned_data['rating']
                obj.description = form.cleaned_data['description']
                obj.eater = form.cleaned_data['eater']
                obj.cook = form.cleaned_data['cook']
                obj.meal = form.cleaned_data['meal']
                obj.save()
            else:
                return JsonResponse({"ok":False, "message":"Bad Form"})
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})

def all_meals(request):
    if request.method == 'GET':
        try:
            objs = list(meal.objects.all().values())
            response = {
                "ok":True,
                "result": {
                    "all_meals":objs
                }
            }
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})

def newest_meals(request):
    if request.method == 'GET':
        try:
            objs = list(meal.objects.all().order_by('-start').values()[:3])
            response = {
                "ok":True,
                "result": {
                    "newest_meals":objs
                }
            }
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})

# Authentication Helpers
def get_authenticator(userObj):
    try:
        auth = authenticator.objects.get(user_id=userObj.pk)
        if auth.date_created < pytz.UTC.localize(datetime.datetime.now() - datetime.timedelta(weeks=1)):
            auth.authenticator = hmac.new(
                    key = settings.SECRET_KEY.encode('utf-8'),
                    msg = os.urandom(32),
                    digestmod = 'sha256',
                ).hexdigest()
            auth.date_created = datetime.datetime.now()
            auth.save()
        return True, auth.authenticator
    except authenticator.DoesNotExist:
        auth = authenticator()
        auth.user_id = userObj.pk
        auth.authenticator = hmac.new(
                key = settings.SECRET_KEY.encode('utf-8'),
                msg = os.urandom(32),
                digestmod = 'sha256',
            ).hexdigest()
        auth.date_created = datetime.datetime.now()
        auth.save()
        return True, auth.authenticator
    except Exception as e:
        return False, str(e)

def check_authenticator(authenticatorString):
    try:
        auth = authenticator.objects.get(authenticator=authenticatorString)
        if auth.date_created < pytz.UTC.localize(datetime.datetime.now() - datetime.timedelta(weeks=1)):
            return False, "Auth token too old"
        return True, "Success!", user.objects.get(pk=auth.user_id)
    except Exception as e:
        return False, str(e)

def login(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            password = request.POST['password']
            userObj = user.objects.get(username=username)
            if check_password(password, userObj.password):
                success, authenticatorString = get_authenticator(userObj)
                if success:
                    return JsonResponse({"ok":True, "authenticator":authenticatorString})
                else:
                    return JsonResponse({"ok":False, "message":authenticatorString})
            else:
                return JsonResponse({"ok":False, "message":"Password did not match"})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})

def authenticate(request):
    try:
        if request.method == 'POST':
            authenticatorString = request.POST['authenticator']
            status, message, userObj = check_authenticator(authenticatorString)
            return JsonResponse({"ok":status, "message":message, "user_id":userObj.pk})
        else:
            return JsonResponse({"ok":False, "message":"Bad request method"})
    except Exception as e:
        return JsonResponse({"ok":False, "error":str(e)})

def recommendations(request, id=None):
    if request.method == 'GET':
        try:
            obj = recommendation.objects.get(pk=id)
            response = {
                "ok":True,
                "result": model_to_dict(obj)
            }
            return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    elif request.method == 'POST':
        try:
            obj = recommendation.objects.get(pk=id)
            form = userForm(data=request.POST)
            for i in form.data:
                obj.__setattr__(i, form.data[i])
            obj.save()
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    elif request.method == 'DELETE':
        try:
            obj = recommendation.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"ok":True})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})

def create_recommendation(request):
    if request.method == 'POST':
        try:
            obj = recommendation()
            form = recommendationForm(request.POST)
            if form.is_valid():
                obj.meal = form.cleaned_data['meal']
                obj.recommended_meals = form.cleaned_data['recommended_meals']
                obj.save()
            else:
                return JsonResponse({"ok":False, "message": str(request.POST)})

            return JsonResponse({"ok":True, "id":obj.pk})
        except Exception as e:
            return JsonResponse({"ok":False, "message":str(e)})
    else:
        return JsonResponse({"ok":False, "message":"Bad request method"})
