from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from rebu.models import user, meal, cook, eater, plate, eater_rating, review
from django.forms.models import model_to_dict

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
            return HttpResponseBadRequest(str(e))
    elif request.method == 'POST':
        try:
            obj = user.objects.get(pk=id)
            if request.POST.get('first_name'):
                obj.first_name = request.POST.get('first_name')
            if request.POST.get('last_name'):
                obj.last_name = request.POST.get('last_name')
            if request.POST.get('street'):
                obj.street = request.POST.get('street')
            if request.POST.get('zip_code'):
                obj.zip_code = request.POST.get('zip_code')
            if request.POST.get('state'):
                obj.state = request.POST.get('state')
            if request.POST.get('country'):
                obj.country = request.POST.get('country')
            if request.POST.get('bio'):
                obj.bio = request.POST.get('bio')
            if request.POST.get('links'):
                obj.links = request.POST.get('links')
            if request.POST.get('language'):
                obj.language = request.POST.get('language')
            if request.POST.get('gender'):
                obj.gender = request.POST.get('gender')
            obj.save()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    elif request.method == 'DELETE':
        try:
            obj = user.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    else:
        return HttpResponseBadRequest('Bad request method')

def create_user(request):
    if request.method == 'POST':
        try:
            obj = user()
            if request.POST.get('first_name'):
                obj.first_name = request.POST.get('first_name')
            if request.POST.get('last_name'):
                obj.last_name = request.POST.get('last_name')
            if request.POST.get('street'):
                obj.street = request.POST.get('street')
            if request.POST.get('zip_code'):
                obj.zip_code = request.POST.get('zip_code')
            if request.POST.get('state'):
                obj.state = request.POST.get('state')
            if request.POST.get('country'):
                obj.country = request.POST.get('country')
            if request.POST.get('bio'):
                obj.bio = request.POST.get('bio')
            if request.POST.get('links'):
                obj.links = request.POST.get('links')
            if request.POST.get('language'):
                obj.language = request.POST.get('language')
            if request.POST.get('gender'):
                obj.gender = request.POST.get('gender')
            obj.save()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    else:
        return HttpResponseBadRequest('Bad request method')


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
            return HttpResponseBadRequest(str(e))
    elif request.method == 'POST':
        try:
            obj = cook.objects.get(pk=id)
            if request.POST.get('signature_dish'):
                obj.signature_dish = request.POST.get('signature_dish')
            if request.POST.get('user_id'):
                obj.user_id = user.objects.get(id=request.POST.get('user_id'))
            obj.save()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    elif request.method == 'DELETE':
        try:
            obj = cook.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    else:
        return HttpResponseBadRequest('Bad request method')

def create_cook(request):
    if request.method == 'POST':
        try:
            obj = cook()
            if request.POST.get('signature_dish'):
                obj.signature_dish = request.POST.get('signature_dish')
            if request.POST.get('user_id'):
                obj.user_id = user.objects.get(id=request.POST.get('user_id'))
            obj.save()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    else:
        return HttpResponseBadRequest('Bad request method')

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
            return HttpResponseBadRequest(str(e))
    elif request.method == 'POST':
        try:
            obj = eater.objects.get(pk=id)
            if request.POST.get('user_id'):
                obj.user_id = user.objects.get(id=request.POST.get('user_id'))
            obj.save()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    elif request.method == 'DELETE':
        try:
            obj = eater.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    else:
        return HttpResponseBadRequest('Bad request method')

def create_eater(request):
    if request.method == 'POST':
        try:
            obj = eater()
            if request.POST.get('user_id'):
                obj.user_id = user.objects.get(id=request.POST.get('user_id'))
            obj.save()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    else:
        return HttpResponseBadRequest('Bad request method')

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
            return HttpResponseBadRequest(str(e))
    elif request.method == 'POST':
        try:
            obj = meal.objects.get(pk=id)
            if request.POST.get('calories'):
                obj.calories = request.POST.get('calories')
            if request.POST.get('description'):
                obj.description = request.POST.get('description')
            if request.POST.get('spice'):
                obj.spice = request.POST.get('spice')
            if request.POST.get('price'):
                obj.price = request.POST.get('price')
            if request.POST.get('tags'):
                obj.tags = request.POST.get('tags')
            if request.POST.get('takeout_available'):
                obj.takeout_available = request.POST.get('takeout_available')
            if request.POST.get('num_plates'):
                obj.num_plates = request.POST.get('num_plates')
            if request.POST.get('start'):
                obj.start = request.POST.get('start')
            if request.POST.get('end'):
                obj.end = request.POST.get('end')
            if request.POST.get('cook_id'):
                obj.cook_id = cook.objects.get(id=request.POST.get('cook_id'))
            obj.save()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    elif request.method == 'DELETE':
        try:
            obj = meal.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    else:
        return HttpResponseBadRequest('Bad request method')

def create_meal(request):
    if request.method == 'POST':
        try:
            obj = meal()
            if request.POST.get('calories'):
                obj.calories = request.POST.get('calories')
            if request.POST.get('description'):
                obj.description = request.POST.get('description')
            if request.POST.get('spice'):
                obj.spice = request.POST.get('spice')
            if request.POST.get('price'):
                obj.price = request.POST.get('price')
            if request.POST.get('tags'):
                obj.tags = request.POST.get('tags')
            if request.POST.get('takeout_available'):
                obj.takeout_available = request.POST.get('takeout_available')
            if request.POST.get('num_plates'):
                obj.num_plates = request.POST.get('num_plates')
            if request.POST.get('start'):
                obj.start = request.POST.get('start')
            if request.POST.get('end'):
                obj.end = request.POST.get('end')
            if request.POST.get('cook_id'):
                obj.cook_id = cook.objects.get(id=request.POST.get('cook_id'))
            obj.save()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    else:
        return HttpResponseBadRequest('Bad request method')


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
            return HttpResponseBadRequest(str(e))
    elif request.method == 'POST':
        try:
            obj = plate.objects.get(pk=id)
            if request.POST.get('meal_id'):
                obj.meal_id = meal.objects.get(id=request.POST.get('meal_id'))
            if request.POST.get('eater_id'):
                obj.eater_id = eater.objects.get(id=request.POST.get('eater_id'))
            obj.save()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    elif request.method == 'DELETE':
        try:
            obj = plate.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    else:
        return HttpResponseBadRequest('Bad request method')

def create_plate(request):
    if request.method == 'POST':
        try:
            obj = plate()
            if request.POST.get('meal_id'):
                obj.meal_id = meal.objects.get(id=request.POST.get('meal_id'))
            if request.POST.get('eater_id'):
                obj.eater_id = eater.objects.get(id=request.POST.get('eater_id'))
            obj.save()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    else:
        return HttpResponseBadRequest('Bad request method')


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
            return HttpResponseBadRequest(str(e))
    elif request.method == 'POST':
        try:
            obj = eater_rating.objects.get(pk=id)
            if request.POST.get('rating'):
                obj.rating = request.POST.get('rating')
            if request.POST.get('description'):
                obj.description = request.POST.get('description')
            if request.POST.get('cook_id'):
                obj.cook_id = cook.objects.get(id=request.POST.get('cook_id'))
            if request.POST.get('eater_id'):
                obj.eater_id = eater.objects.get(id=request.POST.get('eater_id'))
            obj.save()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    elif request.method == 'DELETE':
        try:
            obj = eater_rating.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    else:
        return HttpResponseBadRequest('Bad request method')

def create_eater_rating(request):
    if request.method == 'POST':
        try:
            obj = eater_rating()
            if request.POST.get('rating'):
                obj.rating = request.POST.get('rating')
            if request.POST.get('description'):
                obj.description = request.POST.get('description')
            if request.POST.get('cook_id'):
                obj.cook_id = cook.objects.get(id=request.POST.get('cook_id'))
            if request.POST.get('eater_id'):
                obj.eater_id = eater.objects.get(id=request.POST.get('eater_id'))
            obj.save()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    else:
        return HttpResponseBadRequest('Bad request method')

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
            return HttpResponseBadRequest(str(e))
    elif request.method == 'POST':
        try:
            obj = review.objects.get(pk=id)
            if request.POST.get('rating'):
                obj.rating = request.POST.get('rating')
            if request.POST.get('description'):
                obj.description = request.POST.get('description')
            if request.POST.get('eater_id'):
                obj.eater_id = eater.objects.get(id=request.POST.get('eater_id'))
            if request.POST.get('cook_id'):
                obj.cook_id = cook.objects.get(id=request.POST.get('cook_id'))
            if request.POST.get('meal_id'):
                obj.meal_id = meal.objects.get(id=request.POST.get('meal_id'))
            obj.save()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    elif request.method == 'DELETE':
        try:
            obj = review.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    else:
        return HttpResponseBadRequest('Bad request method')

def create_review(request):
    if request.method == 'POST':
        try:
            obj = review()
            if request.POST.get('rating'):
                obj.rating = request.POST.get('rating')
            if request.POST.get('description'):
                obj.description = request.POST.get('description')
            if request.POST.get('eater_id'):
                obj.eater_id = eater.objects.get(id=request.POST.get('eater_id'))
            if request.POST.get('cook_id'):
                obj.cook_id = cook.objects.get(id=request.POST.get('cook_id'))
            if request.POST.get('meal_id'):
                obj.meal_id = meal.objects.get(id=request.POST.get('meal_id'))
            obj.save()
            return JsonResponse({"ok":True})
        except Exception as e:
            return HttpResponseBadRequest(str(e))
    else:
        return HttpResponseBadRequest('Bad request method')