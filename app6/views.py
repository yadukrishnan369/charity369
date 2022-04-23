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
from traceback import format_exc
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



def testfun(request):
    return HttpResponse('heloo  app6 testing')






def charity_login(request):


    if 'session_name' in request.session:
        return redirect('charityorghomepage')

    if request.method=='POST':
        email=request.POST['email'] 
        password=request.POST['password']
        try:
            charityorgvalidate=charitysignup.objects.get(email=email)

            if charityorgvalidate.email==email and charityorgvalidate.password==password:
                request.session['session_name']=charityorgvalidate.id
                return redirect('charityorghomepage')
            else:
                return render(request,'charityorglogin.html',{'message':'Login Failed','message2':'Incorrect Password'})
                
        except:
            return render(request,'charityorglogin.html',{'message':'Login Failed','message2':'Incorrect Email address'})
    return render(request,'charityorglogin.html')





def charity_org_login_forgot(request):
    return render(request,'charityorgloginforgot.html') 




def charity_org_signup(request):
    
    if request.method=='POST':
        charityname=request.POST['charityname']
        username=request.POST['username']
        address=request.POST['address']
        typeofcharity=request.POST['typeofcharity']
        email=request.POST['email'] 
        phonenumber=request.POST['phonenumber']
        password=request.POST['password']
        print(charityname)
        data=charitysignup(charityName=charityname,userName=username,address=address,typeofCharity=typeofcharity,email=email,phoneNumber=phonenumber,password=password)
        data.save()
        return redirect('charityorglogin')
    return render(request,'charityorgsignup.html')     

def check_username(request):
    uname=request.POST['username']
    try:
        charitysignup.objects.get(userName=uname)
        return JsonResponse({'message':True})

    except:
        return JsonResponse({'message':False})   

def check_userEmail(request):
    uEmail=request.POST['useremail']
    try:
        charitysignup.objects.get(email=uEmail)
        return JsonResponse({'message':True})
        
    except:
        return JsonResponse({'message':False})    

def check_user_Phone(request):
    uPhone=request.POST['phonenumber']
    try:
        charitysignup.objects.get(phoneNumber=uPhone)
        return JsonResponse({'message':True})
        
    except:
        return JsonResponse({'message':False})        




def charity_profile_edit(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'charityorghomeprofileedit.html',{'charity':charity})

def charity_org_profile_edit(request):
    if request.method=='POST':
        about=request.POST['charityorgabout']
        whatsapp=request.POST['charityorgwhatsapp']
        services=request.POST['charityorgservices']
        charityorg=request.session['session_name']
        print(charityorg)
        details=charitysignup.objects.filter(id=charityorg).update(aboutme=about,whatsapp=whatsapp,services=services)
        return render(request,'charityorghomeprofileedit.html')  
    return render(request,'charityorghomeprofileedit.html')




def search_User(request):   # searching user 
    if request.method=='POST':
        searchUser=request.POST['searchUser']
        if  usersignup.objects.filter(username__icontains=searchUser):
            userobj=usersignup.objects.filter(username__icontains=searchUser)
            return render(request,'search_user.html',{'user':userobj})
        else:
            return render(request,'user_not_found.html',{'message':'We Cannot Find the User You Are Searching For Maybe A Little Spelling Mistake ?'})   
    return render(request,'charityorghomepage.html')


def search_user_Profile(request,id):

    regEvent=EventsRegistrations.objects.filter(user_id=id)
    user=usersignup.objects.filter(id=id)
    food=FoodDonation.objects.filter(user_id=id)
    clothing=clothingDonation.objects.filter(user_id=id)
    medicine=medicineDonation.objects.filter(user_id=id)
    studymaterial=studyMaterialDonation.objects.filter(user_id=id)
    other=otherDonation.objects.filter(user_id=id)

    return render(request,'search_user_profile.html',{'event':regEvent,'sUser':user,'food':food,'clothing':clothing,'medicine':medicine,'studymaterial':studymaterial,'other':other})





def charity_org_change_password(request):
    return render(request,'charitychangepassword.html') 





def rename_charity_password(request):
    if request.method=='POST':
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        confpassword=request.POST['confirmPassword']
        user_id=request.session['session_name']
        charity_password=charitysignup.objects.get(id=user_id)
        if(charity_password.password==oldpassword):
            charity_password.password=newpassword
            charity_password.save()
        else:
            return render(request,'changepassword.html',{'message':'Incorrect Your Old Password'})
    return redirect('charityorghomeprofile')    





def change_charity_name(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changecharityname.html',{'charity':charity})




def rename_charity_name(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        charityName=request.POST['changecharityname']
        print(charityName)
        renameCharityname=charitysignup.objects.filter(id=charity_session).update(charityName=charityName)
    return redirect('charityorghomeprofile') 





def change_typeof_charity(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changetypeofcharity.html',{'charity':charity})    




def rename_typeof_charity(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        typeofCharity=request.POST['changetypeofcharity']
        print(typeofCharity)
        renameTypeofCharity=charitysignup.objects.filter(id=charity_session).update(typeofCharity=typeofCharity)
    return redirect('charityorghomeprofile') 




def change_charity_email(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changecharityemail.html',{'charity':charity})




def rename_charity_email(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        charityEmail=request.POST['changecharityemail']
        print(charityEmail)
        renameCharityEmail=charitysignup.objects.filter(id=charity_session).update(email=charityEmail)
    return redirect('charityorghomeprofile')            




def change_charity_phone(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changecharityphone.html',{'charity':charity})




def rename_charity_phone(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        charityPhone=request.POST['changecharityphone']
        print(charityPhone)
        renameCharityPhone=charitysignup.objects.filter(id=charity_session).update(phoneNumber=charityPhone)
    return redirect('charityorghomeprofile')            




def change_charity_whatsapp(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changecharitywhatsapp.html',{'charity':charity})




def rename_charity_whatsapp(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        charitywhatsapp=request.POST['changecharitywhatsapp']
        print(charitywhatsapp)
        renameCharityWhatsapp=charitysignup.objects.filter(id=charity_session).update(whatsapp=charitywhatsapp)
    return redirect('charityorghomeprofile')            




def change_charity_username(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changecharityusername.html',{'charity':charity})




def rename_charity_username(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        charityuserName=request.POST['changecharityusername']
        print(charityuserName)
        renameCharityusername=charitysignup.objects.filter(id=charity_session).update(userName=charityuserName)
    return redirect('charityorghomeprofile') 




def change_charity_address(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changecharityaddress.html',{'charity':charity})




def rename_charity_address(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        charityAddress=request.POST['changecharityaddress']
        print(charityAddress)
        renameCharityusername=charitysignup.objects.filter(id=charity_session).update(address=charityAddress)
    return redirect('charityorghomeprofile') 




def change_charity_about(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changecharityabout.html',{'charity':charity})




def rename_charity_about(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        charityAbout=request.POST['changecharityabout']
        print(charityAbout)
        charityAbout=charitysignup.objects.filter(id=charity_session).update(aboutme=charityAbout)
    return redirect('charityorghomeprofile') 




def change_charity_services(request):
    charity_session=request.session['session_name']
    charity=charitysignup.objects.get(id=charity_session)
    return render(request,'changecharityservices.html',{'charity':charity})




def rename_charity_services(request):
    charity_session=request.session['session_name']
    if request.method=='POST':
        charityServices=request.POST['changecharityservices']
        print(charityServices)
        charityServices=charitysignup.objects.filter(id=charity_session).update(services=charityServices)
    return redirect('charityorghomeprofile')     





def change_charity_profile_picture(request):
    return render(request,'changecharityprofile.html')




def rename_charity_profile_picture(request):
    charity_session=request.session['session_name']
    print(charity_session)
    if request.method=='POST':
        profile=request.FILES['changecharityprofile']
        filename=str(random())+profile.name
        Fileobj=FileSystemStorage()
        Fileobj.save(filename,profile)
        changeprofile=charitysignup.objects.get(id=request.session['session_name'])
        changeprofile.picture=filename
        changeprofile.save()
    return redirect('charityorghomeprofile')










def charity_org_Home_Basepage(request):
    return render(request,'charityorghomebasepage.html')     




def charity_org_homepage(request):
    
    if 'charityId' in request.session:
        return redirect('charityorghomepage')

    charityId=request.session['session_name']
    charity=charitysignup.objects.filter(id=charityId)
    return render(request,'charityorghomepage.html',{'currentUser':charity})   




def charity_org_home_aboutus(request):
    return render(request,'charityorghomeaboutus.html')




#------------------------- event section --------------------------#







def charity_org_home_myevents(request):
    currentUser=request.session['session_name']
    if addevents.objects.filter(charity_id=currentUser):
        charityEvents=addevents.objects.filter(charity_id=currentUser)
        return render(request,'charityorghomemyevents.html',{'events':charityEvents})    
    else:
        return render(request,'charity_no_events.html',{'message':'You Have not Added Events.'})    





def charity_org_home_event_delete(request,id):
    active_user=request.session['session_name']
    addevents.objects.filter(id=id).delete()
    return redirect('charityorghomemyevents')


 








def charity_org_home_userevents_reg(request):
    currentUser=request.session['session_name']
    if EventsRegistrations.objects.filter(event__charity_id=currentUser):
        userEventReg=EventsRegistrations.objects.filter(event__charity_id=currentUser) 
        return render(request,'charityorghomeusereventreg.html',{'userreg':userEventReg})    
    else:
        return render(request,'user_not_register_events.html',{'message':'Users Are Not Register In Events'})    


#------------------------- event section end --------------------------#



def charity_org_home_add_newevents(request):
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
        return redirect('charityorghomemyevents')
    return render(request,'charityorghomeaddnewevents.html') 









def charity_org_home_profile(request):
    try:
        active_session=request.session['session_name']
        active_user=charitysignup.objects.get(id=active_session)
        return render(request,'charityorghomeprofile.html',{"charity":active_user})
    except Exception:
        error=format_exc()
        print(error)
        return redirect('charityorglogin')





def charity_org_profile_logout(request):
    try:
        request.session.flush()
        return redirect('charityorglogin')
    except charitysignup.DoesNotExit:
        return render(request,'charityorglogin.html')






  #  ------------------------------charity send donation request ---------------------------------- 

def charity_org_home_send_req(request):  
    return render(request,'charityorghomesendreq.html') 




def food_send_req(request):   #   request form
    if request.method=='POST':
        quantity=request.POST['foodquantity'] 
        expectedItem=request.POST['foodexpecteditem'] 
        discription=request.POST['fooddiscription']
        charityId=request.session['session_name']
        print(quantity)
        data=FoodRequest(foodQuantity=quantity,foodExpectedItem=expectedItem,foodDiscription=discription,charity_id=charityId)
        data.save()
        return redirect('charityorg_mydonationrequest')
    return render(request,'foodsendreq.html') 




def charity_org_food_req_delete(request,id):   #  Cancel food donation request
    FoodRequest.objects.filter(id=id).delete()
    return redirect('charityorg_mydonationrequest')      





def clothing_send_req(request):  #   request form
    if request.method=='POST':
        quantity=request.POST['clothingquantity'] 
        expectedItem=request.POST['clothingexpecteditem'] 
        discription=request.POST['clothingdiscription']
        charityId=request.session['session_name']
        print(quantity)
        data=ClothingRequest(clothingQuantity=quantity,clothingExpectedItem=expectedItem,clothingDiscription=discription,charity_id=charityId)
        data.save()  
        return redirect('charityorg_mydonationrequest')

    return render(request,'clothingsendreq.html') 





def charity_org_clothing_req_delete(request,id):        #  Cancel clothing donation request
    ClothingRequest.objects.filter(id=id).delete()
    return redirect('charityorg_mydonationrequest')       




def medicine_send_req(request):  #   request form
    if request.method=='POST':
        quantity=request.POST['medicinequantity'] 
        expectedItem=request.POST['medicineexpecteditem'] 
        discription=request.POST['medicinediscription']
        charityId=request.session['session_name']
        print(quantity)
        data=MedicineRequest(medicineQuantity=quantity,medicineExpectedItem=expectedItem,medicineDiscription=discription,charity_id=charityId)
        data.save()
        return redirect('charityorg_mydonationrequest')
    
    return render(request,'medicinesendreq.html') 




def charity_org_medicine_req_delete(request,id):       #  Cancel medicine donation request
    MedicineRequest.objects.filter(id=id).delete()
    return redirect('charityorg_mydonationrequest')      





def studymeterial_send_req(request):     #   request form
    if request.method=='POST':
        quantity=request.POST['studymaterialquantity'] 
        expectedItem=request.POST['studymaterialexpecteditem'] 
        discription=request.POST['studymaterialdiscription']
        charityId=request.session['session_name']
        print(quantity)
        data=StudyMaterialRequest(studymaterialQuantity=quantity,studymaterialExpectedItem=expectedItem,studymaterialDiscription=discription,charity_id=charityId)
        data.save()
        return redirect('charityorg_mydonationrequest')
    
    return render(request,'studymeterialsendreq.html') 





def charity_org_studymeterial_req_delete(request,id):      #  Cancel studymaterial donation request
    StudyMaterialRequest.objects.filter(id=id).delete()
    return redirect('charityorg_mydonationrequest') 




def other_send_req(request):    #   request form
    if request.method=='POST':
        quantity=request.POST['otherquantity'] 
        expectedItem=request.POST['otherexpecteditem'] 
        discription=request.POST['otherdiscription']
        charityId=request.session['session_name']
        print(quantity)
        data=OtherRequest(otherQuantity=quantity,otherExpectedItem=expectedItem,otherDiscription=discription,charity_id=charityId)
        data.save()
        return redirect('charityorg_mydonationrequest')
   
    return render(request,'othersendreq.html') 




def charity_org_other_req_delete(request,id):         #  Cancel other donation request
    OtherRequest.objects.filter(id=id).delete()
    return redirect('charityorg_mydonationrequest') 




def mydonation_request(request):
    currentUser=request.session['session_name']
    fooddonationRequests=FoodRequest.objects.filter(charity_id=currentUser)
    clothingRequests=ClothingRequest.objects.filter(charity_id=currentUser)
    medicineRequests=MedicineRequest.objects.filter(charity_id=currentUser)
    studyMaterialRequest=StudyMaterialRequest.objects.filter(charity_id=currentUser)
    otherRequest=OtherRequest.objects.filter(charity_id=currentUser)
    return render(request,'charityorg_mydonationrequest.html',{'foodrequest':fooddonationRequests,'clothingrequest':clothingRequests,'medicinerequest':medicineRequests,'studymaterialrequest':studyMaterialRequest,'otherrequest':otherRequest})




  # -------------=----------------End charity send donation request  -----------------------------








def charity_org_home_view_donations(request):
    currentUser=request.session['session_name']
    Food=FoodDonation.objects.filter(FoodRequest__charity_id=currentUser)
    clothing=clothingDonation.objects.filter(clothingRequest__charity_id=currentUser)
    medicine=medicineDonation.objects.filter(medicineRequest__charity_id=currentUser)
    studymaterial=studyMaterialDonation.objects.filter(studyMaterialRequest__charity_id=currentUser)
    other=otherDonation.objects.filter(otherRequest__charity_id=currentUser)
    return render(request,'charityorghomeviewdonations.html',{'fooddonation':Food,'clothingdonation':clothing,'medicinedonation':medicine,'studymaterialdonation':studymaterial,'otherdonation':other})



def charity_org_accepted_don(request,id):
    print(id)
    FoodDonation.objects.filter(id=id).update(status=True)
    clothingDonation.objects.filter(id=id).update(status=True)
    medicineDonation.objects.filter(id=id).update(status=True)
    studyMaterialDonation.objects.filter(id=id).update(status=True)
    otherDonation.objects.filter(id=id).update(status=True)
    return redirect("viewacceptdonation")
    


    #---------------------- Cancel Accepted Donation---------------------


def food_accept_cancel(request,id):
    FoodDonation.objects.filter(id=id).update(status=False)
    return redirect('viewacceptdonation')    


def clothing_accept_cancel(request,id):
    clothingDonation.objects.filter(id=id).update(status=False)
    return redirect('viewacceptdonation')

def medicine_accept_cancel(request,id):
    medicineDonation.objects.filter(id=id).update(status=False)
    return redirect('viewacceptdonation')

def studyMaterial_accept_cancel(request,id):
    studyMaterialDonation.objects.filter(id=id).update(status=False)
    return redirect('viewacceptdonation')

def other_accept_cancel(request,id):
    otherDonation.objects.filter(id=id).update(status=False)
    return redirect('viewacceptdonation')


     #----------------------End  Cancel Accepted Donation---------------------




def view_accepted_dontaion(request):
    foodacceptdonation=FoodDonation.objects.filter(status=True)
    clothingacceptdonation=clothingDonation.objects.filter(status=True)
    medicineacceptdonation=medicineDonation.objects.filter(status=True)
    studymaterialacceptdonation=studyMaterialDonation.objects.filter(status=True)
    otheracceptdonation=otherDonation.objects.filter(status=True)
    return render(request,'charityorgaccepteddon.html',{'foodaccept':foodacceptdonation,'clothingaccept':clothingacceptdonation,'medicineaccept':medicineacceptdonation,'studymaterialaccept':studymaterialacceptdonation,'otheraccept':otheracceptdonation})



def donation_collect(request,id):
    FoodDonation.objects.filter(id=id).update(isCollected=True)
    clothingDonation.objects.filter(id=id).update(isCollected=True)
    medicineDonation.objects.filter(id=id).update(isCollected=True)
    studyMaterialDonation.objects.filter(id=id).update(isCollected=True)
    otherDonation.objects.filter(id=id).update(isCollected=True)

    return redirect('viewcollecteddonations')



def view_collected_donations(request):
   
    foodcollect=FoodDonation.objects.filter(isCollected=True)
    clothtingcollect=clothingDonation.objects.filter(isCollected=True)
    medicinecollect=medicineDonation.objects.filter(isCollected=True)
    studyMaterialcollect=studyMaterialDonation.objects.filter(isCollected=True)
    othercollect=otherDonation.objects.filter(isCollected=True)
    return render(request,'charity_org_collected_donation.html',{'foodcollect':foodcollect,'clothingcollect':clothtingcollect,'medicinecollect':medicinecollect,'studyMaterialcollect':studyMaterialcollect,'othercollect':othercollect})



def view_collected_food_details(request,id):
    foodcollect=FoodDonation.objects.filter(id=id)
    return render(request,'view_collected_food_detailes.html',{'foodcollect':foodcollect})    

def view_collected_clothing_details(request,id):
    clothingcollect=clothingDonation.objects.filter(id=id)
    return render(request,'view_collected_clothing_detailes.html',{'clothingcollect':clothingcollect})    

def view_collected_medicine_details(request,id):
    medicinecollect=medicineDonation.objects.filter(id=id)
    return render(request,'view_collected_medicine_detailes.html',{'medicinecollect':medicinecollect})    

def view_collected_studymaterial_details(request,id):
    studyMaterialcollect=studyMaterialDonation.objects.filter(id=id)
    return render(request,'view_collected_studymaterial_detailes.html',{'studyMaterialcollect':studyMaterialcollect})    

def view_collected_other_details(request,id):
    othercollect=otherDonation.objects.filter(id=id)
    return render(request,'view_collected_other_detailes.html',{'othercollect':othercollect})    

def view_collected_food(request):
    if FoodDonation.objects.filter(isCollected=True):
        foodcollect=FoodDonation.objects.filter(isCollected=True)
        return render(request,'collected_food.html',{'foodcollect':foodcollect})
    else:
        return render(request,'no_collected_donations.html',{'message':'You Have No Collected Food Donations'})

    

def view_collected_clothing(request):
    if clothingDonation.objects.filter(isCollected=True):
        clothtingcollect=clothingDonation.objects.filter(isCollected=True)
        return render(request,'collected_clothing.html',{'clothtingcollect':clothtingcollect})
    else:
        return render(request,'no_collected_donations.html',{'message':'You Have No Collected Clothing Donations'})


def view_collected_medicine(request):
    if medicineDonation.objects.filter(isCollected=True):
        medicinecollect=medicineDonation.objects.filter(isCollected=True)
        return render(request,'collected_medicine.html',{'medicinecollect':medicinecollect})
    else:
        return render(request,'no_collected_donations.html',{'message':'You Have No Collected Medicines Donations'})


def view_collected_studymaterial(request):
    if studyMaterialDonation.objects.filter(isCollected=True):
        studyMaterialcollect=studyMaterialDonation.objects.filter(isCollected=True)
        return render(request,'collected_studymaterial.html',{'studyMaterialcollect':studyMaterialcollect})
    else:
        return render(request,'no_collected_donations.html',{'message':'You Have No Collected Study Materials Donations'})


def view_collected_other(request):
    if otherDonation.objects.filter(isCollected=True):
        othercollect=otherDonation.objects.filter(isCollected=True)
        return render(request,'collected_other.html',{'othercollect':othercollect})
    else:
        return render(request,'no_collected_donations.html',{'message':'You Have No Collected Other Donations'})


def no_collected_donations(request):
    return render(request,'no_collected_donations.html')

def charity_org_home_notifications(request):
    currentUser=request.session['session_name']
    print(currentUser)
    eventnotification=EventsRegistrations.objects.filter(event__charity_id=currentUser)
    foodDonationNotification=FoodDonation.objects.filter(FoodRequest__charity_id=currentUser)
    clothingDonationNotification=clothingDonation.objects.filter(clothingRequest__charity_id=currentUser)
    medicineDonationNotification=medicineDonation.objects.filter(medicineRequest__charity_id=currentUser)
    studymaterialdonationNotification=studyMaterialDonation.objects.filter(studyMaterialRequest__charity_id=currentUser)
    otherDonationNotification=otherDonation.objects.filter(otherRequest__charity_id=currentUser)

    for i in eventnotification:

        print(i.event.eventname)
        print(i.user.username)
        print(i.event.charity.charityName)

    return render(request,'charityorghomenotifications.html',{'eventreg':eventnotification,'fooddonationnotification':foodDonationNotification,'clothingdonationnotification':clothingDonationNotification,'medicinedonationnotification':medicineDonationNotification,'studymaterialdonationnotification':studymaterialdonationNotification,'otherdonationnotification':otherDonationNotification})





def charity_org_home_send_feedback(request):
    if request.method=='POST':
        charityMessage=request.POST['charityfeedback']
        charityId=request.session['session_name']
        charityfeedback=CharityFeedback(message=charityMessage,charity_id=charityId)
        charityfeedback.save()
        return redirect('charityorghomeviewfeedback')
    return render(request,'charityorghomesendfeedback.html') 




def charity_org_home_view_feedback(request):
    currentUser=request.session['session_name']
    if CharityFeedback.objects.filter(charity_id=currentUser):
        viewMyFeedback=CharityFeedback.objects.filter(charity_id=currentUser)
        return render(request,'charityorghomeviewfeedback.html',{'viewMyFeedback':viewMyFeedback})
    else:
        return render(request,'charity_not_feedback.html',{'message':'Feedback You Have no Feedback. Lets Send Feedback.'})


def delete_charity_feedback(request,id):
    active_user=request.session['session_name']
    CharityFeedback.objects.filter(id=id).delete()
    return redirect('charityorghomeviewfeedback')

def charity_not_event(request):
    return render(request,'charity_no_events.html')

def user_not_found(request):
    return render(request,'user_not_found.html')

def charity_not_feedback(request):
    return render(request,'charity_not_feedback.html')

def user_not_register_events(request):
    return render(request,'user_not_register_events.html') 
   