from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from rebu.models import user
from django.forms.models import model_to_dict

# Create your views here.
def users(request, id=-1):
    if request.method == 'GET':
        try:
            obj = user.objects.get(pk=id)
            return JsonResponse(model_to_dict(obj))
        except:
            return HttpResponseBadRequest()
    elif request.method == 'POST':
        return JsonResponse({'foo':id})
    elif request.method == 'DELETE':
        return JsonResponse({'foo':id})

def create_user(request):
    return JsonResponse({'foo':'bar'})