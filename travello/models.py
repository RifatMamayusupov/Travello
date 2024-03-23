from django.db import models

# Create your models here.
class Destinations(models.Model):
    
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

class CustomUser(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=False)

    created_at = models.DateTimeField(auto_now_add=True)

class Trip(models.Model):

    city = models.CharField(max_length=50)
    departure = models.DateField(blank=True)
    arrival = models.DateField(blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)