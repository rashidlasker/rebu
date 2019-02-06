from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from rebu.models import user
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
        except:
            return HttpResponseBadRequest()
    elif request.method == 'POST':
        try:
            obj = user.objects.get(pk=id)
            #print(request.body)
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
        except:
            return HttpResponseBadRequest()
    elif request.method == 'DELETE':
        try:
            obj = user.objects.get(pk=id)
            obj.delete()
            return JsonResponse({"ok":True})
        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()

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
        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()
