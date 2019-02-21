"""microservices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rebu import views as rebu_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/<int:id>/', rebu_views.users, name='user'),
    path('api/v1/users/create/', rebu_views.create_user, name='user_create'),
    path('api/v1/cooks/<int:id>/', rebu_views.cooks, name='cook'),
    path('api/v1/cooks/create/', rebu_views.create_cook, name='cook_create'),
    path('api/v1/eaters/<int:id>/', rebu_views.eaters, name='eater'),
    path('api/v1/eaters/create/', rebu_views.create_eater, name='eater_create'),
    path('api/v1/meals/<int:id>/', rebu_views.meals, name='meal'),
    path('api/v1/meals/create/', rebu_views.create_meal, name='meal_create'),
    path('api/v1/plates/<int:id>/', rebu_views.plates, name='plate'),
    path('api/v1/plates/create/', rebu_views.create_plate, name='plate_create'),
    path('api/v1/eater_ratings/<int:id>/', rebu_views.eater_ratings, name='eater_rating'),
    path('api/v1/eater_ratings/create/', rebu_views.create_eater_rating, name='eater_rating_create'),
    path('api/v1/reviews/<int:id>/', rebu_views.reviews, name='review'),
    path('api/v1/reviews/create/', rebu_views.create_review, name='review_create'),
    path('api/v1/meals/all/', rebu_views.all_meals, name='all'),
    path('api/v1/meals/newest/', rebu_views.newest_meals, name='newest'),
]
