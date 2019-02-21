from django.shortcuts import render
from django.http import JsonResponse
from rebu.models import user, meal, cook, eater, plate, eater_rating, review
from django.forms.models import model_to_dict
from django import forms

class userForm(forms.ModelForm):
	first_name = forms.CharField(label="First name", max_length=20)
	last_name = forms.CharField(label="Last name", max_length=20)
	street = forms.CharField(label="Street", max_length=100)
	zip_code = forms.CharField(label="Zip Code", max_length=5)
	state = forms.CharField(label="State", max_length=20)
	country = forms.CharField(label="Country", max_length=40)
	bio = forms.CharField(label="Bio", max_length=150)
	links = forms.CharField(label="Social Media Links", max_length=120)
	language = forms.CharField(label="Language", max_length=20)
	gender = forms.CharField(label="Gender", max_length=15)
	class Meta:
		model = user
		fields = ['first_name', 'last_name', 'street','zip_code','state','country','bio','links','language','gender']


class cookForm(forms.ModelForm):
	signature_dish = forms.CharField(label="Signature Dish")
	user = forms.ModelChoiceField(label="userid", queryset=user.objects.all())
	class Meta:
		model = cook
		fields = ['signature_dish', 'user']

class eaterForm(forms.ModelForm):
	user = forms.ModelChoiceField(label="userid", queryset=user.objects.all())
	class Meta:
		model = eater
		fields = ['user']

class mealForm(forms.ModelForm):
	calories = forms.CharField(label='Calories')
	description = forms.CharField(label='Description')
	spice = forms.CharField(label='Spice')
	price = forms.CharField(label='Price')
	tags = forms.CharField(label='Tags', max_length=150)
	takeout_available = forms.CharField(label='Takeout Available')
	num_plates = forms.CharField(label='Number of Plates', max_length=3)
	start = forms.CharField(label='Start Time/Date', max_length=50)
	end = forms.CharField(label='End Time/Date', max_length=50)
	cook = forms.ModelChoiceField(label='cookid', queryset=cook.objects.all())
	class Meta:
		model = meal
		fields = ['calories','description','spice','price','tags','takeout_available','num_plates','start','end','cook']

class plateForm(forms.ModelForm):
	meal = forms.ModelChoiceField(label='mealid', queryset=meal.objects.all())
	eater = forms.ModelChoiceField(label='eaterid', queryset=eater.objects.all())
	class Meta:
		model = plate
		fields = ['meal','eater']

class eaterRatingForm(forms.ModelForm):
	rating = forms.IntegerField(label='Rating')
	description = forms.CharField(label='Description', max_length=150)
	cook = forms.ModelChoiceField(label='cookid', queryset=cook.objects.all())
	eater = forms.ModelChoiceField(label='eaterid', queryset=eater.objects.all())
	class Meta:
		model = eater_rating
		fields = ['rating','description','cook','eater']

class reviewForm(forms.ModelForm):
	rating = forms.IntegerField(label='Rating')
	description = forms.CharField(label='Description', max_length=150)
	eater = forms.ModelChoiceField(label='eaterid', queryset=eater.objects.all())
	cook = forms.ModelChoiceField(label='cookid', queryset=cook.objects.all())
	meal = forms.ModelChoiceField(label='mealid', queryset=meal.objects.all())
	class Meta:
		model = eater_rating
		fields = ['rating','description','eater','cook','meal']
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
			form = userForm(request.POST or None, instance=obj)
			if form.is_valid():
				obj = form.save()
				obj.save()
			else:
				return JsonResponse({"ok":False, "message":"Bad Form"})
			return JsonResponse({"ok1":True})
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
				obj.save()
			else:
				return JsonResponse({"ok":False, "message":"Bad Form"})

			return JsonResponse({"ok":True})
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
			form = cookForm(request.POST or None, instance=obj)
			if form.is_valid():
				obj = form.save()
				obj.save()
			else:
				return JsonResponse({"ok":False, "message":"Bad Form"})	
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
			form = eaterForm(request.POST or None, instance=obj)
			if form.is_valid():
				obj = form.save()
				obj.save()
			else:
				return JsonResponse({"ok":False, "message":"Bad Form"})
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
			form = mealForm(request.POST or None, instance=obj)
			if form.is_valid():
				obj = form.save()
				obj.save()
			else:
				return JsonResponse({"ok":False, "message":"Bad Form"})
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
				return JsonResponse({"ok":False, "message": form.data["cook"]})

			return JsonResponse({"ok":True})
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
			form = plateForm(request.POST or None, instance=obj)
			if form.is_valid():
				obj = form.save()
				obj.save()
			else:
				return JsonResponse({"ok":False, "message":"Bad Form"})
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
			form = eaterRatingForm(request.POST or None, instance=obj)
			if form.is_valid():
				obj = form.save()
				obj.save()
			else:
				return JsonResponse({"ok":False, "message":"Bad Form"})

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
			if form.is_valid():
				obj = form.save()
				obj.save()
			else:
				return JsonResponse({"ok":False, "message":"Bad Form"})	
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
