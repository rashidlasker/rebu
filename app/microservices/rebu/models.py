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

class eater(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE, parent_link=True, default=-1)

class cook(models.Model):
    signature_dish = models.TextField()
    user = models.OneToOneField(user, on_delete=models.CASCADE, parent_link=True, default=-1)

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
    cook = models.ForeignKey(cook, on_delete=models.CASCADE)

class plate(models.Model):
    meal = models.ForeignKey(meal, on_delete=models.CASCADE)
    eater = models.ForeignKey(eater, on_delete=models.CASCADE)

class eater_rating(models.Model):
    rating = models.IntegerField()
    description = models.TextField()
    cook = models.ForeignKey(cook, on_delete=models.CASCADE)
    eater = models.ForeignKey(eater, on_delete=models.CASCADE)

class review(models.Model):
    rating = models.IntegerField()
    description = models.TextField()
    eater = models.ForeignKey(eater, on_delete=models.CASCADE)
    cook = models.ForeignKey(cook, on_delete=models.CASCADE)
    meal = models.ForeignKey(meal, on_delete=models.CASCADE)
