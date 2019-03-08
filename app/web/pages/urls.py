from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('meals/create', views.create_meal, name='create_meal'),
    path('meals/<int:meal_id>/', views.meal_detail, name='meal_detail'),
]