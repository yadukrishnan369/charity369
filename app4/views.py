from __future__ import print_function
from cgi import print_directory
from dataclasses import dataclass
from operator import truediv
from os import system
import queue
import re
from ssl import AlertDescription
from tkinter.messagebox import RETRY
from tkinter.tix import Form
from traceback import format_exc
from xml.etree.ElementTree import QName
from  django.core.files.storage import FileSystemStorage
from random import random
from contextlib import redirect_stderr
import email    
from random import random
from app4.models import usersignup


from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

from app4.forms import SignupForm
from .models import *
from app6.models import *
from django.views.decorators.csrf import csrf_exempt
from traceback import format_exc


# Create your views here.


def charityWelcomepage(request):
    userfeedback=UserFeedback.objects.all()
    charityfeedback=CharityFeedback.objects.all()
    return render(request,'charityWelcomepage.html',{'userfeedback':userfeedback,'charityfeedback':charityfeedback}) 



 #------------------- user login ----------------------#

def userloginfun(request):
    
    if 'usersession_name' in request.session:
        return redirect('userhomepage')
       
    if(request.method=='POST'):
        useremail=request.POST['email']
        userpassword=request.POST['password']
        try:   
            uservalidate=usersignup.objects.get(useremail=useremail)
            if uservalidate.useremail==useremail and uservalidate.password==userpassword:
                request.session['usersession_name']=uservalidate.id
                return redirect('userhomepage')
            else:
                return render(request,'userlogin.html',{'message':'Login Failed','message2':'Incorrect Your Password'})
        except:
            return render(request,'userlogin.html',{'message':'Login Failed','message2':'Incorrect Your Email Address'})
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
        data=usersignup(username=name,useremail=email,password=password)
        data.save()    
        return redirect('userlogin')
    return render(request,'usersignup.html')

def usernameAjax(request):
    uname=request.POST['username']
    try:
        usersignup.objects.get(username=uname)
        return JsonResponse({'message':True})

    except:
        return JsonResponse({'message':False})        


def userEmailAjax(request):
    uEmail=request.POST['useremail']
    try:
        usersignup.objects.get(useremail=uEmail)
        return JsonResponse({'message':True})
        
    except:
        return JsonResponse({'message':False})    
    


#--------------------- user signup end -----------------------#















#-------------------user event section-----------------------#



def usereventsfun(request):  #user view Events

    if 'usersession_name'not in request.session:
            return redirect("userlogin")

    
   
    if addevents.objects.select_related("charity"):
        events=addevents.objects.select_related("charity")
        return render(request,'userevents.html',{'charityevents':events}) 
    else:

        return render(request,'user_no_event.html',{'message':'You Have no Upcoming Events.'}) 



@csrf_exempt
def usereventsregfun(request):  #User Event Registration  

    user_id=usersignup.objects.get(id=request.session['usersession_name'])
    if request.method=='POST':
        event_id=addevents.objects.get(id=request.POST['event_id'])
        
        eventReg=EventsRegistrations(event=event_id,user=user_id)
        eventReg.save()
        return JsonResponse({"message":True})  

    else:
        return JsonResponse({'message':False})


def userRegisterdEvents(request):   #  User View Registerd Events

    currentUser=request.session['usersession_name']
    if EventsRegistrations.objects.filter(user_id=currentUser):
    
        events=EventsRegistrations.objects.filter(user_id=currentUser) 
        for i in events:
            print(i.event.charity.charityName)
        return render(request,'userRegisterdEvents.html',{'events':events})              
    else:
        return render(request,'user_no_event.html',{'message':'You Are Not Registerd For Events'})              



def userHomeEventCancel(request,id):
    EventsRegistrations.objects.filter(id=id).delete()
    return redirect('userregisterdevents')              

#-------------------user event section end-----------------------#






#-------------------------------------- user profile ------------------------------------#



def userprofilefun(request):    #  User Profile
    try:
        active_session=request.session['usersession_name']
        userDetailes=usersignup.objects.get(id=active_session)
        return render(request,'userprofile.html',{"userdata":userDetailes})
    except Exception:
        error=format_exc()
        print(error)
        return redirect('userlogin')





def userprofileedit(request):   #  User Profile Edit

    user_session=request.session['usersession_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'userprofileedit.html',{'user':user})




def userprofileeditfun(request):      # User Profile Edit form

    user=request.session['usersession_name']
    if request.method=='POST':
        address=request.POST['address']
        website=request.POST['website']
        bio=request.POST['bio']
        phone=request.POST['phone']
        whatsapp=request.POST['whatsapp']
        about=request.POST['about']
       
        usersignup.objects.filter(id=user).update(address=address,website=website,bio=bio,phone=phone,whatsapp=whatsapp,aboutme=about,picture=filename)
    return redirect('userprofile')  




def changepasswordfun(request):
    return render(request,'changepassword.html') 




def rename_userpassword(request):    #  User Change Password

    if request.method=='POST':
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        confpassword=request.POST['confirmPassword']
        user_id=request.session['usersession_name']
        user_password=usersignup.objects.get(id=user_id)
        if(user_password.password==oldpassword):
            user_password.password=newpassword
            user_password.save()
        else:
            return render(request,'changepassword.html',{'message':'Incorrect Your Old Password'})
    return redirect('userprofile')




def changeusernamefun(request):
    user_session=request.session['usersession_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'changeusername.html',{'user':user})




def rename_username(request):
    user_session=request.session['usersession_name']
    if request.method=='POST':
        username=request.POST['changeusername']
        print(username)
        renameUsername=usersignup.objects.filter(id=user_session).update(username=username)
    return redirect('userprofile')




def changewebsitefun(request):
    user_session=request.session['usersession_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'changewebsite.html',{'user':user})




def rename_website(request):
    user_session=request.session['usersession_name']
    if request.method=='POST':
        website=request.POST['changewebsite']
        renameWebsite=usersignup.objects.filter(id=user_session).update(website=website)
    return redirect('userprofile')




def changeemailfun(request):
    user_session=request.session['usersession_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'changeemail.html',{'user':user})




def rename_email(request):
    user_session=request.session['usersession_name']
    if request.method=='POST':
        email=request.POST['changeuseremail']
        renameeamil=usersignup.objects.filter(id=user_session).update(useremail=email)
    return redirect('userprofile')




def changebiofun(request):
    user_session=request.session['usersession_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'changebio.html',{'user':user})




def rename_bio(request):
    user_session=request.session['usersession_name']
    if request.method=='POST':
        bio=request.POST['changeuserbio']
        renamebio=usersignup.objects.filter(id=user_session).update(bio=bio)
    return redirect('userprofile')




def changeaddressfun(request):
    user_session=request.session['usersession_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'changeaddress.html',{'user':user})




def rename_address(request):
    user_session=request.session['usersession_name']
    if request.method=='POST':
        address=request.POST['changeuseraddress']
        renameaddress=usersignup.objects.filter(id=user_session).update(address=address)
    return redirect('userprofile')





def changeaboutfun(request):
    user_session=request.session['usersession_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'changeabout.html',{'user':user})




def rename_about(request):
    user_session=request.session['usersession_name']
    if request.method=='POST':
        about=request.POST['changeuserabout']
        renameabout=usersignup.objects.filter(id=user_session).update(aboutme=about)
    return redirect('userprofile')




def changephonefun(request):
    user_session=request.session['usersession_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'changephone.html',{'user':user})




def rename_phone(request):
    user_session=request.session['usersession_name']
    if request.method=='POST':
        phone=request.POST['changeuserphone']
        renamephone=usersignup.objects.filter(id=user_session).update(phone=phone)
    return redirect('userprofile')




def changewhatsappfun(request):
    user_session=request.session['usersession_name']
    user=usersignup.objects.get(id=user_session)
    return render(request,'changewhatsapp.html',{'user':user})





def rename_whatsapp(request):
    user_session=request.session['usersession_name']
    if request.method=='POST':
        whatsapp=request.POST['changeuserwhatsapp']
        renamewhatsapp=usersignup.objects.filter(id=user_session).update(whatsapp=whatsapp)
    return redirect('userprofile')





def changeprofilefun(request):
    return render(request,'changeprofile.html')





def rename_profile(request):
    user_session=request.session['usersession_name']
    print(user_session)
    if request.method=='POST':
        profile=request.FILES['changeuserprofile']
        filename=str(random())+profile.name
        Fileobj=FileSystemStorage()
        print(filename)
        Fileobj.save(filename,profile)
        print(filename)
        changeprofile=usersignup.objects.get(id=request.session['usersession_name'])
        changeprofile.picture=filename
        changeprofile.save()
    return redirect('userprofile')




def userprofilelogoutfun(request):
    try:
        request.session.flush()
        return redirect('userlogin')
    except usersignup.DoesNotExit:
        return render(request,'userlogin.html')  


   #------------------------------------- user profile end ----------------------------------#








def userhomepagefun(request):
    
    if 'currentUser' in request.session:
        return render(request,'userhomepage.html')

    currentUser=request.session['usersession_name']
    activeUser=usersignup.objects.filter(id=currentUser)
    return render(request,'userhomepage.html',{'user':activeUser})
 



def useraboutusfun(request):
    return render(request,'userhomeaboutus.html')    




def usercharityorgfun(request):
    charity=charitysignup.objects.all()
    return render(request,'usercharityorg.html',{'charity':charity})


def searchCharity(request):    # searching charity organization
        if request.method=='POST':
            searchcharity=request.POST['searchCharity']
        if charitysignup.objects.filter(charityName__icontains=searchcharity):    
            charityObj=charitysignup.objects.filter(charityName__icontains=searchcharity)
            return render(request,'search_charity.html',{'charity':charityObj})
        else:
            return render(request,'charity_not_found.html',{'message':'We Cannot Find the Charity Organization You Are Searching For Maybe A Little Spelling Mistake ?'})
        # return redirect('usercharityorg')


def searchcharityProfile(request,id):
        events=addevents.objects.filter(charity_id=id)

        charity=charitysignup.objects.filter(id=id)
        fooddon=FoodRequest.objects.filter(charity_id=id)
        clothingdon=ClothingRequest.objects.filter(charity_id=id)
        medicinedon=MedicineRequest.objects.filter(charity_id=id)
        studymaterialdon=StudyMaterialRequest.objects.filter(charity_id=id)
        otherdon=OtherRequest.objects.filter(charity_id=id)
        return render(request,'search_charity_profile.html',{'event':events,'charity':charity,'fooddon':fooddon,'clothingdon':clothingdon,'medicinedon':medicinedon,'studymaterialdon':studymaterialdon,'otherdon':otherdon})
    



#---------------------------------- user donation request -----------------------------------#




def userdonationsreqfun(request):      #All Donations function

    foodRequests=FoodRequest.objects.select_related("charity")
    clothingRequests=ClothingRequest.objects.select_related("charity")
    medicinesRequests=MedicineRequest.objects.select_related("charity")
    studyMaterialRequests=StudyMaterialRequest.objects.select_related("charity")
    otherRequests=OtherRequest.objects.select_related("charity")
    return render(request,'userdonationsreq.html',{'food':foodRequests,'clothing':clothingRequests,'medicine':medicinesRequests,'studymaterial':studyMaterialRequests,'other':otherRequests})  




def show_food_request(request):  #User View Food Donation Request
    if FoodRequest.objects.select_related("charity"):
        foodRequests=FoodRequest.objects.select_related("charity")
        return render(request,'userfoodreq.html',{'data':foodRequests}) 
    else:
        return render(request,'user_user.html',{'message':'You Have no Food Donations. Lets Change Donation Request.'}) 




def show_clothing_request(request):  #User View Clothing Donation Request
    if ClothingRequest.objects.select_related("charity"):
        clothingRequests=ClothingRequest.objects.select_related("charity")
        return render(request,'userclothingreq.html',{'data':clothingRequests})  
    else:
        return render(request,'user_user.html',{'message':'You Have no Clothing Donations. Lets Change Donation Request.'}) 




def show_medicine_request(request):   #User View Medicine Donation Request
    if MedicineRequest.objects.select_related("charity"):
        medicinesRequests=MedicineRequest.objects.select_related("charity")
        return render(request,'usermedicinesreq.html',{'data':medicinesRequests}) 
    else:
        return render(request,'user_user.html',{'message':'You Have no Medicine Donations. Lets Change Donation Request.'}) 




def show_studymaterial_request(request):   #User View study Material Donation Request
    if StudyMaterialRequest.objects.select_related("charity"):
        studyMaterialRequests=StudyMaterialRequest.objects.select_related("charity")
        return render(request,'userstudymeterialsreq.html',{'data':studyMaterialRequests})  
    else:
        return render(request,'user_user.html',{'message':'You Have no Study Material Donations. Lets Change Donation Request.'}) 




def show_other_request(request):   #User View Other Donation Request

    if OtherRequest.objects.select_related("charity"):

        otherRequests=OtherRequest.objects.select_related("charity")
        return render(request,'userotherreq.html',{'data':otherRequests})  
    else:
         return render(request,'user_user.html',{'message':'You Have no Other Donations. Lets Change Donation Request.'}) 





#---------------------------------- user donation request end -----------------------------------#






    

#-------------------------------- Doantion accept --------------------------------#



def userfoodacceptreqfun(request,id):  #Accepted Form
   
        food_id=id

        if request.method=='POST':
            foodType=request.POST['foodtype'] 
            foodQuantity=request.POST['foodquantity'] 
            date=request.POST['date']
            time=request.POST['time']
            address=request.POST['address']
            buildingNumber=request.POST['buildingnumber']
            tradeMark=request.POST['trademark']
            userId=request.session['usersession_name']
            print(foodType)
            foodDonation=FoodDonation(foodType=foodType,foodQuantity=foodQuantity,date=date,time=time,address=address,buildingNumber=buildingNumber,tradeMark=tradeMark,user_id=userId,FoodRequest_id=food_id)
            foodDonation.save()
            return redirect('usermydonations')
        return render(request,'userfoodacceptreq.html')  

   



def userclothingacceptreqfun(request,id): #Accepted Form
    print(id)
    clothing_id=id
    if request.method=='POST':
        clothingType=request.POST['clothingtype'] 
        clothingQuantity=request.POST['clothingquantity'] 
        date=request.POST['date']
        time=request.POST['time']
        address=request.POST['address']
        buildingNumber=request.POST['buildingnumber']
        tradeMark=request.POST['trademark']
        userId=request.session['usersession_name']
        print(clothingType)
        ClothingDonation=clothingDonation(clothingType=clothingType,clothingQuantity=clothingQuantity,date=date,time=time,address=address,buildingNumber=buildingNumber,tradeMark=tradeMark,user_id=userId,clothingRequest_id=clothing_id)
        ClothingDonation.save()
        return redirect('usermydonations')

    return render(request,'userclothingacceptreq.html')  





def usermedicineacceptreqfun(request,id): #Accepted Form
    print(id)
    medicine_id=id
    if request.method=='POST':
        medicineType=request.POST['medicinetype'] 
        medicineQuantity=request.POST['medicinequantity'] 
        date=request.POST['date']
        time=request.POST['time']
        address=request.POST['address']
        buildingNumber=request.POST['buildingnumber']
        tradeMark=request.POST['trademark']
        userId=request.session['usersession_name']
        print(medicineType)
        MedicineDonation=medicineDonation(medicineType=medicineType,medicineQuantity=medicineQuantity,date=date,time=time,address=address,buildingNumber=buildingNumber,tradeMark=tradeMark,user_id=userId,medicineRequest_id=medicine_id)
        MedicineDonation.save()
        return redirect('usermydonations')

    return render(request,'usermedicineacceptreq.html')  





def userstudymaterialacceptreqfun(request,id): #Accepted Form
    print(id)
    studymaterial_id=id
    if request.method=='POST':
        studyMaterialType=request.POST['studymaterialtype'] 
        studyMaterialQuantity=request.POST['studymaterialquantity'] 
        date=request.POST['date']
        time=request.POST['time']
        address=request.POST['address']
        buildingNumber=request.POST['buildingnumber']
        tradeMark=request.POST['trademark']
        userId=request.session['usersession_name']
        print(studyMaterialType)
        StudyMaterialDonation=studyMaterialDonation(studyMaterialType=studyMaterialType,studyMaterialQuantity=studyMaterialQuantity,date=date,time=time,address=address,buildingNumber=buildingNumber,tradeMark=tradeMark,user_id=userId,studyMaterialRequest_id=studymaterial_id)
        StudyMaterialDonation.save()
        return redirect('usermydonations')
 
    return render(request,'userstudymaterialacceptreq.html')






def userotheracceptreqfun(request,id):  #Accepted Form
    print(id)
    other_id=id
    if request.method=='POST':
        otherType=request.POST['othertype'] 
        otherQuantity=request.POST['otherquantity'] 
        date=request.POST['date']
        time=request.POST['time']
        address=request.POST['address']
        buildingNumber=request.POST['buildingnumber']
        tradeMark=request.POST['trademark']
        userId=request.session['usersession_name']
        print(otherType)
        OtherDonation=otherDonation(otherType=otherType,otherQuantity=otherQuantity,date=date,time=time,address=address,buildingNumber=buildingNumber,tradeMark=tradeMark,user_id=userId,otherRequest_id=other_id)
        OtherDonation.save()
        return redirect('usermydonations')

    return render(request,'userotheracceptreq.html')  

#--------------------------------- Doantion accept End --------------------------------#








def usernotificationsfun(request):  # User Notification
    foodacceptdonation=FoodDonation.objects.filter(status=True)
    clothingacceptdonation=clothingDonation.objects.filter(status=True)
    medicineacceptdonation=medicineDonation.objects.filter(status=True)
    studymaterialacceptdonation=studyMaterialDonation.objects.filter(status=True)
    otheracceptdonation=otherDonation.objects.filter(status=True)

    foodcollectdonation=FoodDonation.objects.filter(isCollected=True)
    clothingcollectdonation=clothingDonation.objects.filter(isCollected=True)
    medicinecollectdonation=medicineDonation.objects.filter(isCollected=True)
    studymaterialcollectdonation=studyMaterialDonation.objects.filter(isCollected=True)
    othercollectdonation=otherDonation.objects.filter(isCollected=True)


    return render(request,'usernotifications.html',{'foodacceptnotification':foodacceptdonation,'clothingacceptnotification':clothingacceptdonation,'medicineacceptnotificaton':medicineacceptdonation,'studymaterialacceptnotification':studymaterialacceptdonation,'otheracceptnotification':otheracceptdonation,'foodcollectdonation':foodcollectdonation,'clothingcollectdonation':clothingcollectdonation,'medicinecollectdonation':medicinecollectdonation,'studymaterialcollectdonation':studymaterialcollectdonation,'othercollectdonation':othercollectdonation})   








def usermydonationsfun(request):  # User Donated List
    currentUser=request.session['usersession_name']
    food=FoodDonation.objects.filter(user_id=currentUser)
    cloth=clothingDonation.objects.filter(user_id=currentUser)
    medicine=medicineDonation.objects.filter(user_id=currentUser)
    studymaterial=studyMaterialDonation.objects.filter(user_id=currentUser)
    other=otherDonation.objects.filter(user_id=currentUser)
    return render(request,'usermydonations.html',{'fooddon':food,'clothingdon':cloth,'medicinedon':medicine,'studymaterialdon':studymaterial,'otherdon':other})  


def CancelFoodDonation(request,id):
    FoodDonation.objects.filter(id=id).delete()
    return redirect('usermydonations')

def CancelClothingDonation(request,id):
    clothingDonation.objects.filter(id=id).delete()
    return redirect('usermydonations')

def CancelMedicineDonation(request,id):
    medicineDonation.objects.filter(id=id).delete()
    return redirect('usermydonations')

def CancelStudyMaterialDonation(request,id):
    studyMaterialDonation.objects.filter(id=id).delete()
    return redirect('usermydonation')

def CancelOtherDonation(request,id):
    otherDonation.objects.filter(id=id).delete()
    return redirect('usermydonation')    
    

def usersendcompfeedbackfun(request):  # user send Feedback Form

    if request.method=='POST':
        message=request.POST['message']
        userId=request.session['usersession_name']
        userFeedback=UserFeedback(message=message,user_id=userId)
        userFeedback.save()
        return redirect('userviewfeedback')
    return render(request,'usersendcompfeedback.html')    




def userviewfeedbackfun(request): # User Send feedback View
        currentUser=request.session['usersession_name']
        if UserFeedback.objects.filter(user_id=currentUser):
            UserMyFeedback=UserFeedback.objects.filter(user_id=currentUser)
            return render(request,'userviewfeedback.html',{'UserMyFeedback':UserMyFeedback})    
        else:   
            return render(request,'no_feedback.html',{'message':' Feedback You Have no Feedback. Lets Send Feedback.'})




def DeleteFeedBack(request,id):
    current_user=request.session['usersession_name']
    UserFeedback.objects.filter(id=id).delete()
    return redirect('userviewfeedback')



def userhomebasepagefun(request):
    userId=request.session['usersession_name']
    currentuser=usersignup.objects.filter(id=userId)
    return render(request,'userhomebasepage.html',{'name':currentuser})  


def UserUser(request):
    return render(request,'user_user.html')


def UserNoevent(request):
    return render(request,'user_no_event.html')


def CharityNotFound(request):
    return render(request,'charity_not_found.html')


def NoFeedback(request):
    return render(request,'no_feedback.html')










