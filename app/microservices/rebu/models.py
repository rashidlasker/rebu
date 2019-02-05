from django.db import models

# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    bio = models.TextField()
    links = models.TextField()
    language = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    #cook_id = 
    #eater_id = 

class eater(models.Model):
    rating = models.IntegerField()
    #user_id = 

class cook(models.Model):
    signature_dish = models.TextField()
    #user_id = 

class review(models.Model):
    rating = models.IntegerField()
    description = models.TextField()
    #eater_id = 
    #cook_id = 
    #meal_id = 

class meal(models.Model):
    calories = models.IntegerField()
    description = models.TextField()
    spice = models.IntegerField()
    price = models.FloatField()
    tags = models.TextField()
    takeout_available = models.BooleanField()
    num_plates = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    cook_id = models.ForeignKey(cook, on_delete=models.CASCADE)

class plate(models.Model):
    meal_id = models.ForeignKey(meal, on_delete=models.CASCADE)

class eater_rating(models.Model):
    rating = models.IntegerField()
    description = models.TextField()
    #cook_id = 
    #ater_id = 
