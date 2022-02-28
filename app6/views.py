from dataclasses import dataclass
from os import system
from pyexpat import model
from tkinter.tix import Form
from random import random
from django.core.files.storage import FileSystemStorage

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
# from app6.forms import charitysignupform
from .models import *
from app4.models import *
# Create your views here.

def testfun(request):
    return HttpResponse('heloo  app6 testing')

def charityorgbasepagefun(request):
    return render(request,'charityorgbasepage.html') 

def charityorgfun(request):
    return render(request,'charityorg.html')     

def charityorgaboutfun(request):
    return render(request,'charityorgabout.html')         

def charityorgcontactfun(request):
    return render(request,'charityorgcontact.html')     

def charityorgloginfun(request):
    if request.method=='POST':
        email=request.POST['email'] 
        password=request.POST['password']
        try:
            charityorgvalidate=charitysignup.objects.get(email=email)
            if charityorgvalidate.email==email and charityorgvalidate.password==password:
                request.session['session_name']=charityorgvalidate.id
                return redirect('charityorghomepage')
            else:
                return redirect('charityorglogin')
        except charitysignup.DoesNotExist:
            return render(request,'charityorglogin.html',{'message':'Login Failed'})
    return render(request,'charityorglogin.html')

def charityorgloginforgotfun(request):
    return render(request,'charityorgloginforgot.html') 




def charityorgsignupfun(request):
    # form=charitysignupform()
    if request.method=='POST':
        # form=charitysignupform(request.POST)
        # if form.is_valid():
        #     CharityName=form.cleaned_data['charityname']
        #     UserName=form.cleaned_data['username']
        #     Address=form.cleaned_data['address']
        #     TypeOfCharity=form.cleaned_data['typeofcharity']
        #     Email=form.cleaned_data['email']
        #     PhoneNumber=form.cleaned_data['phonenumber']
        #     Password=form.cleaned_data['password']
        #     ConfPassword=form.cleaned_data['confpassword']


        #     data=charitysignup(charityname=CharityName,username=UserName,address=Address,typeofcharity=TypeOfCharity,Email=Email,phonenumber=PhoneNumber,password=Password,confpassword=ConfPassword)
        #     data.save()
        # else:
        #     print(form.errors)    
            

        charityname=request.POST['charityname']
        username=request.POST['username']
        address=request.POST['address']
        typeofcharity=request.POST['typeofcharity']
        email=request.POST['email'] 
        phonenumber=request.POST['phonenumber']
        password=request.POST['password']
        confpassword=request.POST['confpassword']

        print(charityname)
        data=charitysignup(charityname=charityname,username=username,address=address,typeofcharity=typeofcharity,email=email,phonenumber=phonenumber,password=password,confpassword=confpassword)
        data.save()
    return render(request,'charityorgsignup.html')     


def charityorghomeprofileeditfun(request):
    if request.method=='POST':
        about=request.POST['charityorgabout']
        whatsapp=request.POST['charityorgwhatsapp']
        services=request.POST['charityorgservices']
        picture=request.FILES['charitypicture']
        filename=str(random())+picture.name
        print(filename)
        Fileobj=FileSystemStorage()
        Fileobj.save(filename,picture)
        charityorg=request.session['session_name']
        print(charityorg)
        details=charitysignup.objects.filter(id=charityorg).update(aboutme=about,whatsapp=whatsapp,services=services,picture=filename)
        return render(request,'charityorghomeprofileedit.html')  
    return render(request,'charityorghomeprofileedit.html')

def charityorghomechangepasswordfun(request):
    
    return render(request,'charitychangepassword.html') 

def rename_charitypassword(request):
    if request.method=='POST':
        oldpassword=request.POST['oldpassword']
        print(oldpassword)
        newpassword=request.POST['newpassword']
        print(newpassword)
        confpassword=request.POST['confirmPassword']
        print(confpassword)
        user_id=request.session['session_name']
        print(user_id)
        charity_password=charitysignup.objects.get(id=user_id)
        if(charity_password.password==oldpassword):
            charity_password.password=newpassword
            charity_password.save()
        else:
            return render(request,'changepassword.html',{'message':'Incorrect Your Old Password'})

                
    return redirect('charityorghomeprofile')    

def changecharitynamefun(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changecharityname.html',{'charity':charity})

def rename_charityname(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        charityName=request.POST['changecharityname']
        print(charityName)
        renameCharityname=charitysignup.objects.filter(id=charity_session).update(charityName=charityName)
    return redirect('charityorghomeprofile') 


def changetypeofcharityfun(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changetypeofcharity.html',{'charity':charity})    

def rename_typeofcharity(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        typeofCharity=request.POST['changetypeofcharity']
        print(typeofCharity)
        renameTypeofCharity=charitysignup.objects.filter(id=charity_session).update(typeofCharity=typeofCharity)
    return redirect('charityorghomeprofile') 

def changecharityemailfun(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changecharityemail.html',{'charity':charity})

def rename_charityemail(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        charityEmail=request.POST['changecharityemail']
        print(charityEmail)
        renameCharityEmail=charitysignup.objects.filter(id=charity_session).update(email=charityEmail)
    return redirect('charityorghomeprofile')            

def changecharityphonefun(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changecharityphone.html',{'charity':charity})

def rename_charityphone(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        charityPhone=request.POST['changecharityphone']
        print(charityPhone)
        renameCharityPhone=charitysignup.objects.filter(id=charity_session).update(phoneNumber=charityPhone)
    return redirect('charityorghomeprofile')            

def changecharitywhatsappfun(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changecharitywhatsapp.html',{'charity':charity})

def rename_charitywhatsapp(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        charitywhatsapp=request.POST['changecharitywhatsapp']
        print(charitywhatsapp)
        renameCharityWhatsapp=charitysignup.objects.filter(id=charity_session).update(whatsapp=charitywhatsapp)
    return redirect('charityorghomeprofile')            

def changecharityusernamefun(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changecharityusername.html',{'charity':charity})

def rename_charityusername(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        charityuserName=request.POST['changecharityusername']
        print(charityuserName)
        renameCharityusername=charitysignup.objects.filter(id=charity_session).update(userName=charityuserName)
    return redirect('charityorghomeprofile') 

def changecharityaddressfun(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changecharityaddress.html',{'charity':charity})

def rename_charityaddress(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        charityAddress=request.POST['changecharityaddress']
        print(charityAddress)
        renameCharityusername=charitysignup.objects.filter(id=charity_session).update(address=charityAddress)
    return redirect('charityorghomeprofile') 

def changecharityaboutfun(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changecharityabout.html',{'charity':charity})

def rename_charityabout(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        charityAbout=request.POST['changecharityabout']
        print(charityAbout)
        charityAbout=charitysignup.objects.filter(id=charity_session).update(aboutme=charityAbout)
    return redirect('charityorghomeprofile') 

def changecharityservicesfun(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changecharityservices.html',{'charity':charity})

def rename_charityservices(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        charityServices=request.POST['changecharityservices']
        print(charityServices)
        charityServices=charitysignup.objects.filter(id=charity_session).update(services=charityServices)
    return redirect('charityorghomeprofile')     


def changecharityprofilefun(request):
  
    return render(request,'changecharityprofile.html')

def rename_charityprofile(request):
    charity_session=request.session['session_name']
    print(charity_session)
    if request.method=='POST':
        profile=request.FILES['changecharityprofile']
        filename=str(random())+profile.name
        Fileobj=FileSystemStorage()
        Fileobj.save(filename,profile)
        changeprofile=charitysignup.objects.get(id=request.session['session_name'])
        changeprofile.picture=profile
        changeprofile.save()

    return redirect('charityorghomeprofile')


def checkUserNamefun(request):
    user_name=request.GET['user_name']
    print(user_name)
    isNameExist=charitysignup.objects.filter(username=user_name).exists()
    print(isNameExist)
    return JsonResponse({'isExist':isNameExist})


def checkUserEmailfun(request):
    user_email=request.GET['email']
    print(user_email)
    isEmailExist=charitysignup.objects.filter(email=user_email).exists()
    print(isEmailExist)
    return JsonResponse({'isExist':isEmailExist})



def checkUserPhoneNumberfun(request):
    user_phone=request.GET['phone_number']
    print(user_phone)
    isEmailExist=charitysignup.objects.filter(phonenumber=user_phone).exists()
    print(isEmailExist)
    return JsonResponse({'isExist':isEmailExist})





def charityorghomebasepagefun(request):
    return render(request,'charityorghomebasepage.html')     

def charityorghomepagefun(request):
    return render(request,'charityorghomepage.html')   

def charityorghomeaboutusfun(request):
    return render(request,'charityorghomeaboutus.html')

def charityorghomemyeventsfun(request):
    charityEvents=addevents.objects.all()
    return render(request,'charityorghomemyevents.html',{'events':charityEvents}) 

def charityorghomeaddneweventsfun(request):
    if request.method=='POST':
        eventname=request.POST['eventname']
        eventstarttime=request.POST['starttime']
        eventendtime=request.POST['endtime']
        date=request.POST['date']
        location=request.POST['location']
        discription=request.POST['discription']
        image=request.FILES['image']
        filename=str(random())+image.name
        charityId=request.session['session_name']
        print(filename)
        Fileobj=FileSystemStorage()
        Fileobj.save(filename,image)
        events=addevents(eventname=eventname,starttime=eventstarttime,endtime=eventendtime,date=date,location=location,discription=discription,image=filename,charity_id=charityId)
        events.save()
    return render(request,'charityorghomeaddnewevents.html') 


def charityorghomeprofilefun(request):
    active_session=request.session['session_name']
    active_user=charitysignup.objects.get(id=active_session)
    return render(request,'charityorghomeprofile.html',{'charity':active_user})                     



def charityorgprofilelogoutfun(request):
    try:
        request.session.flush()
        return redirect('charityorglogin')
    except charitysignup.DoesNotExit:
        return render(request,'charityorglogin.html')






  #  charity send donation request  

def charityorghomesendreqfun(request):  
    return render(request,'charityorghomesendreq.html') 


def foodsendreqfun(request):  
    if request.method=='POST':
        quantity=request.POST['foodquantity'] 
        expectedItem=request.POST['foodexpecteditem'] 
        discription=request.POST['fooddiscription']
        charityId=request.session['session_name']
        print(quantity)
        data=FoodRequest(foodQuantity=quantity,foodExpectedItem=expectedItem,foodDiscription=discription,charity_id=charityId)
        data.save()
    return render(request,'foodsendreq.html')   


def clothingsendreqfun(request):
    if request.method=='POST':
        quantity=request.POST['clothingquantity'] 
        expectedItem=request.POST['clothingexpecteditem'] 
        discription=request.POST['clothingdiscription']
        charityId=request.session['session_name']
        print(quantity)
        data=ClothingRequest(clothingQuantity=quantity,clothingExpectedItem=expectedItem,clothingDiscription=discription,charity_id=charityId)
        data.save()  
    return render(request,'clothingsendreq.html')


def medicinesendreqfun(request):
    if request.method=='POST':
        quantity=request.POST['medicinequantity'] 
        expectedItem=request.POST['medicineexpecteditem'] 
        discription=request.POST['medicinediscription']
        charityId=request.session['session_name']
        print(quantity)
        data=MedicineRequest(medicineQuantity=quantity,medicineExpectedItem=expectedItem,medicineDiscription=discription,charity_id=charityId)
        data.save()    
    return render(request,'medicinesendreq.html')                     


def studymeterialsendreqfun(request):

    if request.method=='POST':
        quantity=request.POST['studymaterialquantity'] 
        expectedItem=request.POST['studymaterialexpecteditem'] 
        discription=request.POST['studymaterialdiscription']
        charityId=request.session['session_name']
        print(quantity)
        data=StudyMaterialRequest(studymaterialQuantity=quantity,studymaterialExpectedItem=expectedItem,studymaterialDiscription=discription,charity_id=charityId)
        data.save()    
    return render(request,'studymeterialsendreq.html')



def othersendreqfun(request):
    if request.method=='POST':
        quantity=request.POST['otherquantity'] 
        expectedItem=request.POST['otherexpecteditem'] 
        discription=request.POST['otherdiscription']
        charityId=request.session['session_name']
        print(quantity)
        data=OtherRequest(otherQuantity=quantity,otherExpectedItem=expectedItem,otherDiscription=discription,charity_id=charityId)
        data.save()   
    return render(request,'othersendreq.html')  


def mydonationrequestfun(request):

    fooddonationRequests=FoodRequest.objects.all()
    clothingRequests=ClothingRequest.objects.all()
    medicineRequests=MedicineRequest.objects.all()
    studyMaterialRequest=StudyMaterialRequest.objects.all()
    otherRequest=OtherRequest.objects.all()



    return render(request,'charityorg_mydonationrequest.html',{'foodrequest':fooddonationRequests,'clothingrequest':clothingRequests,'medicinerequest':medicineRequests,'studymaterialrequest':studyMaterialRequest,'otherrequest':otherRequest})


  #  charity send donation request  








def charityorghomesviewdonationsfun(request):
    return render(request,'charityorghomeviewdonations.html')

def charityorgaccepteddonfun(request):
    return render(request,'charityorgaccepteddon.html')                                      

def charityorghomesnotificationsfun(request):
    return render(request,'charityorghomenotifications.html')

def charityorghomesviewfeedbackfun(request):
    return render(request,'charityorghomeviewfeedback.html')

def charityorghomessendfeedbackfun(request):
    return render(request,'charityorghomesendfeedback.html')    