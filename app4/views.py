from __future__ import print_function
from cgi import print_directory
from dataclasses import dataclass
from os import system
from ssl import AlertDescription
from tkinter.messagebox import RETRY
from tkinter.tix import Form
from django.core.files.storage import FileSystemStorage
from random import random
from contextlib import redirect_stderr
import email    
from random import random

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

from app4.forms import SignupForm
from .models import *
from app6.models import *

# Create your views here.


def userbasepagefun(request):
    return render(request,'userbasepage.html') 

def charityhomefun(request):
    return render(request,'charityhome.html')

def aboutusfun(request):   
    return render(request,'aboutus.html')  

 #------------------- user login ----------------------#

def userloginfun(request):
    if(request.method=='POST'):
        username=request.POST['email']
        userpassword=request.POST['password']
        uservalidate=usersignup.objects.get(useremail=username)
        if uservalidate.useremail==username and uservalidate.password==userpassword:
            request.session['session_name']=uservalidate.id
            return redirect('userhomepage')
        return redirect('userlogin')
    return render(request,'userlogin.html')

    #------------------- user login end ----------------------#


 

def userloginforgotfun(request):
     return render(request,'userloginforgot.html')   




#--------------------- user signup -----------------------#

def usersignupfun(request):
    if request.method=='POST':
        name=request.POST['username'] 
        email=request.POST['useremail'] 
        password=request.POST['password']
        confpassword=request.POST['confpassword']
        data=usersignup(username=name,useremail=email,password=password,confpassword=confpassword)
        data.save()    
    return render(request,'usersignup.html')

#--------------------- user signup end -----------------------#


def CheckUserNamefun(request):
    user_name =request.GET['user_name']
    print(user_name)
    isNameExist=usersignup.objects.filter(username=user_name).exists()
    print(isNameExist)
    return JsonResponse({'isExist':isNameExist})


def CheckUserEmailfun(request):
    user_email=request.GET['user_email']
    print(user_email)
    isEmailExist=usersignup.objects.filter(useremail=user_email).exists()
    print(isEmailExist)
    return JsonResponse({'isEmailExist':isEmailExist})




def forgotpasswordfun(request):
    return render(request,'forgotpassword.html')  



def userhomefun(request):
    return render(request,'userhome.html')

#-------------------user event section-----------------------#

def usereventsfun(request):
    events=addevents.objects.select_related("charity")
    return render(request,'userevents.html',{'charityevents':events})    


def usereventsregfun(request):
    user_id=request.session['session_name']
    # userEvents=
    # eventdata.save()
    return render(request,'usereventsreg.html')    


#-------------------user event section end-----------------------#






#-------------------------------------- user profile ------------------------------------#

def userprofilefun(request):
    active_session=request.session['session_name']
    userDetailes=usersignup.objects.get(id=active_session)
    return render(request,'userprofile.html',{"userdata":userDetailes}) 

def userprofileeditfun(request):        
    if request.method=='POST':
        address=request.POST['address']
        website=request.POST['website']
        bio=request.POST['bio']
        phone=request.POST['phone']
        whatsapp=request.POST['whatsapp']
        about=request.POST['about']
        picture=request.FILES['picture']
        filename=str(random())+picture.name
        print(filename)
        Fileobj=FileSystemStorage()
        Fileobj.save(filename,picture)
        user=request.session['session_name']
        print(user)
        details=usersignup.objects.filter(id=user).update(address=address,website=website,bio=bio,phone=phone,whatsapp=whatsapp,aboutme=about,picture=filename)
        # active_session=request.session['session_editprofile']
        # active_user=usereditprofile.objects.get(id=active_session)
    return render(request,'userprofileedit.html')  

def changepasswordfun(request):
    return render(request,'changepassword.html') 

def rename_userpassword(request):
    if request.method=='POST':
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        confpassword=request.POST['confirmPassword']
        user_id=request.session['session_name']
        user_password=usersignup.objects.get(id=user_id)
        if(user_password.password==oldpassword):
            user_password.password=newpassword
            user_password.save()
        else:
            return render(request,'changepassword.html',{'message':'Incorrect Your Old Password'})

                
    return redirect('userprofile')

def changeusernamefun(request):
    user_session=request.session['session_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'changeusername.html',{'user':user})

def rename_username(request):
    user_session=request.session['session_name']
    if request.method=='POST':
        username=request.POST['changeusername']
        print(username)
        renameUsername=usersignup.objects.filter(id=user_session).update(username=username)
    return redirect('userprofile')

def changewebsitefun(request):
    user_session=request.session['session_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'changewebsite.html',{'user':user})

def rename_website(request):
    user_session=request.session['session_name']
    if request.method=='POST':
        website=request.POST['changewebsite']
        renameWebsite=usersignup.objects.filter(id=user_session).update(website=website)
    return redirect('userprofile')

def changeemailfun(request):
    user_session=request.session['session_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'changeemail.html',{'user':user})

def rename_email(request):
    user_session=request.session['session_name']
    if request.method=='POST':
        email=request.POST['changeuseremail']
        renameeamil=usersignup.objects.filter(id=user_session).update(useremail=email)
    return redirect('userprofile')

def changebiofun(request):
    user_session=request.session['session_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'changebio.html',{'user':user})

def rename_bio(request):
    user_session=request.session['session_name']
    if request.method=='POST':
        bio=request.POST['changeuserbio']
        renamebio=usersignup.objects.filter(id=user_session).update(bio=bio)
    return redirect('userprofile')

def changeaddressfun(request):
    user_session=request.session['session_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'changeaddress.html',{'user':user})

def rename_address(request):
    user_session=request.session['session_name']
    if request.method=='POST':
        address=request.POST['changeuseraddress']
        renameaddress=usersignup.objects.filter(id=user_session).update(address=address)
    return redirect('userprofile')


def changeaboutfun(request):
    user_session=request.session['session_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'changeabout.html',{'user':user})

def rename_about(request):
    user_session=request.session['session_name']
    if request.method=='POST':
        about=request.POST['changeuserabout']
        renameabout=usersignup.objects.filter(id=user_session).update(aboutme=about)
    return redirect('userprofile')

def changephonefun(request):
    user_session=request.session['session_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'changephone.html',{'user':user})

def rename_phone(request):
    user_session=request.session['session_name']
    if request.method=='POST':
        phone=request.POST['changeuserphone']
        renamephone=usersignup.objects.filter(id=user_session).update(phone=phone)
    return redirect('userprofile')

def changewhatsappfun(request):
    user_session=request.session['session_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'changewhatsapp.html',{'user':user})

def rename_whatsapp(request):
    user_session=request.session['session_name']
    if request.method=='POST':
        whatsapp=request.POST['changeuserwhatsapp']
        renamewhatsapp=usersignup.objects.filter(id=user_session).update(whatsapp=whatsapp)
    return redirect('userprofile')

def changeprofilefun(request):
    return render(request,'changecharityprofile.html')

def rename_profile(request):
    user_session=request.session['session_name']
    print(user_session)
    if request.method=='POST':
        profile=request.FILES['changeuserprofile']
        filename=str(random())+profile.name
        Fileobj=FileSystemStorage()
        Fileobj.save(filename,profile)
        changeprofile=usersignup.objects.get(id=request.session['session_name'])
        changeprofile.picture=profile
        changeprofile.save()

    return redirect('charityprofile')

def userprofilelogoutfun(request):
    try:
        request.session.flush()
        return redirect('userlogin')
    except usersignup.DoesNotExit:
        return render(request,'userlogin.html')  


   #------------------------------------- user profile end ----------------------------------#



def userhomepagefun(request):
    return render(request,'userhomepage.html')

def servicesviewmorefun(request):
    return render(request,'servicesviewmore.html')

def useraboutusfun(request):
    return render(request,'useraboutus.html')    

def usercharityorgfun(request):
    charity=charitysignup.objects.all()
    return render(request,'usercharityorg.html',{'charity':charity})



#---------------------------------- user donation request -----------------------------------#


def userdonationsreqfun(request):
    return render(request,'userdonationsreq.html')  

def show_food_request(request):
    foodRequests=FoodRequest.objects.select_related("charity")
    return render(request,'userfoodreq.html',{'data':foodRequests}) 

def show_clothing_request(request):
    clothingRequests=ClothingRequest.objects.select_related("charity")
    return render(request,'userclothingreq.html',{'data':clothingRequests})  

def show_medicine_request(request):
    medicinesRequests=MedicineRequest.objects.select_related("charity")
    return render(request,'usermedicinesreq.html',{'data':medicinesRequests}) 

def show_studymaterial_request(request):
    studyMaterialRequests=StudyMaterialRequest.objects.select_related("charity")
    return render(request,'userstudymeterialsreq.html',{'data':studyMaterialRequests})  

def show_other_request(request):
    otherRequests=OtherRequest.objects.select_related("charity")
    return render(request,'userotherreq.html',{'data':otherRequests})  

def useracceptreqfun(request):
    return render(request,'useracceptreq.html')  

#---------------------------------- user donation request end -----------------------------------#



def usernotificationsfun(request):
    return render(request,'usernotifications.html')   

def usermydonationsfun(request):
    return render(request,'usermydonations.html')  

def usersendcompfeedbackfun(request):
    return render(request,'usersendcompfeedback.html')    

def userviewfeedbackfun(request):
    return render(request,'userviewfeedback.html')    




def userhomebasepagefun(request):
    user=usersignup.objects.all()
    return render(request,'userhomebasepage.html',{'username':user})  


def regfun(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        username=request.POST['user_name']
        password=request.POST['passwd']
        data=UserReg(name=name,email=email,age=age,user_name=username,password=password)
        data.save()
      
    userdetailes=UserReg.objects.all()
    return render(request,'reg.html',{'user':userdetailes})    


def checkUserNamefun(request):
    user_name=request.GET['user_name']
    print(user_name)
    isNameExist=UserReg.objects.filter(user_name=user_name).exists()
    print(isNameExist)
    return JsonResponse({'isExist':isNameExist})


def checkUserEmailfun(request):
    user_email=request.GET['user_email']
    print(user_email)
    isEmailExist=UserReg.objects.filter(email=user_email).exists()
    print(isEmailExist)
    return JsonResponse({'isEmailExist':isEmailExist})


def sampleajaxfun(request):

    return render(request,'sampleajax.html')    

def sampletablefun(request):

    return render(request,'sampletable.html')    