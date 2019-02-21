from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def homepage_info(request):
    context = {
        "newest_meals": [
            {
                "name": "Pizza",
                "description": "its food!",
                "calories": 600,
                "tags": ["yum", "yummy", "yum"],
                "pk": 1,
            },
            {
                "name": "Pizza2",
                "description": "its food2!",
                "calories": 700,
                "tags": ["yum2", "yummy", "yum"],
                "pk": 2,
            },
            {
                "name": "Pizza3",
                "description": "its food3!",
                "calories": 800,
                "tags": ["yum3", "yummy", "yum"],
                "pk": 3,
            },
        ]
    }
    return JsonResponse(context)

def meal_info(request, meal_id):
    context = {
        "meal": {
            "name": "Pizza",
            "description": "its food!",
            "calories": 600,
            "tags": ["yum", "yummy", "yum"],
            "pk": meal_id,
        }
    }
    return JsonResponse(context)