from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meals/<int:meal_id>/', views.meal_detail, name='meal_detail'),
    path('search/', views.search, name='search'),
]