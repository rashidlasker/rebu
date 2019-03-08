from django.shortcuts import render
from django.http import JsonResponse
from rebu.models import user, meal, cook, eater, plate, eater_rating, review, authenticator
from django.forms.models import model_to_dict
from django import forms

class authenticatorForm(forms.ModelForm):
	user_id = forms.CharField(label='User_ID')
	authenticator = forms.CharField(label='Authenticator')
	date_created = forms.DateTimeField(label='Date_Created')

	class Meta:
		model = authenticator
		fields = ['user_id', 'authenticator', 'date_created']

class userForm(forms.ModelForm):
	first_name = forms.CharField(label='First Name')
	last_name = forms.CharField(label='Last Name')
	street = forms.CharField(label='Street')
	zip_code = forms.CharField(label='Zip Code')
	state = forms.CharField(label='State')
	country = forms.CharField(label='Country')
	bio = forms.CharField(label='Bio')
	links = forms.CharField(label='Links')
	language = forms.CharField(label='Language')
	gender = forms.CharField(label='Gender')
	password = forms.CharField(label='Password')

	class Meta:
		model = user
		fields = ['first_name', 'last_name', 'street','zip_code','state','country','bio','links','language','gender', 'password']

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
			user_form = userForm(data=request.POST)
			for i in user_form.data:
				obj.__setattr__(i, user_form.data[i])
			obj.save()

#			if user_form.is_valid():
#				user_form.save()
#				obj = form.save()
#				obj.save()
#			else:
#			return JsonResponse({"okx":False, "message":obj})
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
				obj.password = form.cleaned_data['password']
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

