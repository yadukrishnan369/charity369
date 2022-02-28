from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.

class adminreg(models.Model):
    adminname=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    confpassword=models.CharField(max_length=50)

class adminlogin(models.Model):

    name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)