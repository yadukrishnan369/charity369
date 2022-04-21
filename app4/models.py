from email.policy import default
from enum import unique
from pyexpat import model
from django.db import models

from app6.models import FoodRequest
from app6.models import *
# import app6.models


# Create your models here.

class userlogin(models.Model):

    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class usersignup(models.Model):
    username=models.CharField(max_length=50)
    useremail=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    address=models.SlugField(max_length=100, default="")
    website=models.CharField(max_length=100, default="")
    bio=models.CharField(max_length=100, default="")
    phone=models.CharField(max_length=50, default="")
    whatsapp=models.CharField(max_length=50, default="")
    aboutme=models.SlugField(max_length=1000, default="")
    picture=models.ImageField(default="")

   


    
#-------------------------------- User Food doantion -------------------------------#

class FoodDonation(models.Model):
    foodType=models.CharField(max_length=200)
    foodQuantity=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    address=models.SlugField(max_length=500)
    buildingNumber=models.CharField(max_length=1000)
    tradeMark=models.SlugField(max_length=500)
    user=models.ForeignKey(usersignup, on_delete=models.CASCADE)
    FoodRequest=models.ForeignKey(FoodRequest, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    isCollected = models.BooleanField(default=False)

    
class clothingDonation(models.Model):
    clothingType=models.CharField(max_length=200)
    clothingQuantity=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    address=models.SlugField(max_length=500)
    buildingNumber=models.CharField(max_length=1000)
    tradeMark=models.SlugField(max_length=500)
    user=models.ForeignKey(usersignup, on_delete=models.CASCADE, default="")
    clothingRequest=models.ForeignKey(ClothingRequest, on_delete=models.CASCADE, default="")
    status = models.BooleanField(default=False)
    isCollected = models.BooleanField(default=False)


class medicineDonation(models.Model):
    medicineType=models.CharField(max_length=200)
    medicineQuantity=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    address=models.SlugField(max_length=500)
    buildingNumber=models.CharField(max_length=1000)
    tradeMark=models.SlugField(max_length=500)
    user=models.ForeignKey(usersignup, on_delete=models.CASCADE, default="")
    medicineRequest=models.ForeignKey(MedicineRequest, on_delete=models.CASCADE, default="")
    status = models.BooleanField(default=False)
    isCollected = models.BooleanField(default=False)


class studyMaterialDonation(models.Model):
    studyMaterialType=models.CharField(max_length=200)
    studyMaterialQuantity=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    address=models.SlugField(max_length=500)
    buildingNumber=models.CharField(max_length=1000)
    tradeMark=models.SlugField(max_length=500)
    user=models.ForeignKey(usersignup, on_delete=models.CASCADE, default="")
    studyMaterialRequest=models.ForeignKey(StudyMaterialRequest, on_delete=models.CASCADE, default="")
    status = models.BooleanField(default=False)
    isCollected = models.BooleanField(default=False)


class otherDonation(models.Model):
    otherType=models.CharField(max_length=200)
    otherQuantity=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    address=models.SlugField(max_length=500)
    buildingNumber=models.CharField(max_length=1000)
    tradeMark=models.SlugField(max_length=500)
    user=models.ForeignKey(usersignup, on_delete=models.CASCADE, default="")
    otherRequest=models.ForeignKey(OtherRequest, on_delete=models.CASCADE, default="")
    status = models.BooleanField(default=False)
    isCollected = models.BooleanField(default=False)
 
#-------------------------------- User Food doantion End -------------------------------#

           




class EventsRegistrations(models.Model):
    
    class Meta:
        unique_together = ('user','event')

    user=models.ForeignKey(usersignup, on_delete=models.CASCADE)
    event=models.ForeignKey(addevents, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)


class UserFeedback(models.Model):
    message=models.CharField(max_length=1000)
    user=models.ForeignKey(usersignup, on_delete=models.CASCADE)    





