from email.policy import default
from django.db import models

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




class UserReg(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    age=models.IntegerField()
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


       





