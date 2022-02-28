from datetime import date
import email
from tkinter.tix import Tree
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

from app4.models import usersignup

# Create your models here.
class charitysignup(models.Model):
    charityName=models.CharField(max_length=50)
    userName=models.CharField(max_length=50)
    address=models.SlugField(max_length=100)
    typeofCharity=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phoneNumber=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    aboutme=models.SlugField(max_length=1000, default="")
    whatsapp=models.CharField(max_length=50, default="")
    services=models.SlugField(max_length=1000, default="")
    picture=models.ImageField(default="")



#--------------------------- Event Section ----------------------------#

class addevents(models.Model):
    eventname=models.CharField(max_length=250)
    starttime=models.TimeField()
    endtime=models.TimeField()    
    date=models.DateField()
    location=models.CharField(max_length=255)
    discription=models.SlugField(max_length=2500)
    image=models.ImageField()
    charity=models.ForeignKey(charitysignup, on_delete=models.CASCADE)


class EventsRegistrations(models.Model):
    user=models.ForeignKey(usersignup, on_delete=models.CASCADE)
    event=models.ForeignKey(addevents, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)


#--------------------------- Event Section end ----------------------------#





#---------------------------- donations requests -------------------------------#


class FoodRequest(models.Model):
    foodQuantity=models.IntegerField()
    foodExpectedItem=models.CharField(max_length=500)
    foodDiscription=models.CharField(max_length=1000)
    charity=models.ForeignKey(charitysignup, on_delete=models.CASCADE)
    

    
class ClothingRequest(models.Model):
    clothingQuantity=models.IntegerField()
    clothingExpectedItem=models.CharField(max_length=500)
    clothingDiscription=models.CharField(max_length=1000)
    charity=models.ForeignKey(charitysignup, on_delete=models.CASCADE)

class MedicineRequest(models.Model):
    medicineQuantity=models.IntegerField()
    medicineExpectedItem=models.CharField(max_length=500)
    medicineDiscription=models.CharField(max_length=1000)
    charity=models.ForeignKey(charitysignup, on_delete=models.CASCADE)


class StudyMaterialRequest(models.Model):
    studymaterialQuantity=models.IntegerField()
    studymaterialExpectedItem=models.CharField(max_length=500)
    studymaterialDiscription=models.CharField(max_length=1000)
    charity=models.ForeignKey(charitysignup, on_delete=models.CASCADE)

class OtherRequest(models.Model):
    otherQuantity=models.IntegerField()
    otherExpectedItem=models.CharField(max_length=500)
    otherDiscription=models.CharField(max_length=1000)
    charity=models.ForeignKey(charitysignup, on_delete=models.CASCADE)




#---------------------------- donations requests end -------------------------------#

            

        

        

    


