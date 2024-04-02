from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Package(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.CharField(max_length=100, blank=False)

    def __str__(self):
       return f"{self.name} - {self.price}"


class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank= True)
    name = models.CharField(max_length=100, blank=False)
    date = models.DateField(blank=False)
    package_choices = [(package.name, f"{package.name} - {package.price}") for package in Package.objects.all()]
    package = models.CharField(max_length=100, choices = package_choices)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length = 10, blank=False)


    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank = False)


    def __str__(self):
       return self.name
    


class Enquiry(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length = 10, blank=False)
    message = models.TextField(blank = False)


    def __str__(self):
       return self.name
    
