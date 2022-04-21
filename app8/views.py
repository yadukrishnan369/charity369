from http.client import REQUEST_ENTITY_TOO_LARGE
from itertools import count
from operator import truediv
from django.shortcuts import render,redirect

from django.http import HttpResponse

from app8.models import adminlogin

from app8.models import adminreg


from .models import *

from app4.models import *
from app6.models import *



# Create your views here.

def helooiifun(request):
    return HttpResponse('heloo  app8 testing')

# def adminregfun(request):
#     if request.method=='POST':

#         adminname=request.POST['adminname'] 
#         adminpassword=request.POST['adminpassword']
#         confpassword=request.POST['confpassword']
#         print(adminname)
#         print(adminpassword)
#         print(confpassword)
#         data=adminreg(adminname=adminname,password=adminpassword,confpassword=confpassword)
#         data.save()
#     return render(request,'adminreg.html')

def adminloginfun(request):
    if(request.method=='POST'):
        adminname=request.POST['adminname']
        adminpassword=request.POST['adminpassword']
        adminvalidate=adminreg.objects.get(adminname=adminname)
        if adminvalidate.adminname==adminname and adminvalidate.password==adminpassword:
            return redirect('adminhome')
        else:
            return redirect('adminlogin')
    return render(request,'adminlogin.html')
    


def adminhomebasepagefun(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon
    return render(request,'adminhomebasepage.html',{'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation}) 


# def admincharityCount(request):
#     charity=charitysignup.objects.all().count()
#     print(charity)
#     return redirect('adminhomebasepage',{'count':charity})

def adminhomefun(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon
    return render(request,'adminhome.html',{'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})  


def foodAccept(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    if FoodDonation.objects.filter(status=True):
        foodacceptdonation=FoodDonation.objects.filter(status=True)
        return render(request,'food_accept.html',{'donation':foodacceptdonation,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})
    else:
        return render(request,'food_accept.html',{'message':'No Accepted Food Donation !'})

def clothingAccept(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    if clothingDonation.objects.filter(status=True):
        clothingacceptdonation=clothingDonation.objects.filter(status=True)
        return render(request,'clothing_accept.html',{'donation':clothingacceptdonation,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})    
    else:
        return render(request,'clothing_accept.html',{'message':'No Accepted Clothing Donation !'})    

def medicineAccept(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    if medicineDonation.objects.filter(status=True):
        medicineacceptdonation=medicineDonation.objects.filter(status=True)
        return render(request,'medicine_accept.html',{'donation':medicineacceptdonation,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})        
    else:
        return render(request,'medicine_accept.html',{'message':'No Accepted Medicine Donaton !'})



def studyMaterialAccept(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    if studyMaterialDonation.objects.filter(status=True):
        studyMaterialacceptdonation=studyMaterialDonation.objects.filter(status=True)
        return render(request,'studyMaterial_accept.html',{'donation':studyMaterialacceptdonation,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})            
    else:
        return render(request,'studyMaterial_accept.html',{'message':'No Accepted Study Material Donation'})            

def otherAccept(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    if otherDonation.objects.filter(status=True):
        otheracceptdonation=otherDonation.objects.filter(status=True)
        return render(request,'other_accept.html',{'donation':otheracceptdonation,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})        
    else:
        return render(request,'other_accept.html',{'message':'No Accepted Other Donation !'})        



def adminhomeviewprofilefun(request):

    return render(request,'adminhomeviewprofile.html')           

def adminhomecharityorgfun(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

   
    charityorgreg=charitysignup.objects.all()                                                                                                                                               
    return render(request,'adminhomecharityorg.html',{'charityorgreg':charityorgreg,'count':charity,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})  

def AdminHomeCharityDelete(request,id):
    charity=charitysignup.objects.filter(id=id).delete()
    return render(request,'adminhomecharityorg.html')

def SerachCharityOrg(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    if request.method=='POST':
        search_charity=request.POST['searchCharity']
        charity_obj=charitysignup.objects.filter(charityName__icontains=search_charity)
        return render(request,'adminsearch_charity.html',{'charity':charity_obj,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})  
    return redirect('adminhomecharityorg')    

def SearchCharityProfile(request,id):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    Charity=charitysignup.objects.filter(id=id)
    events=addevents.objects.filter(charity__id=id)
    fooddon=FoodRequest.objects.filter(charity_id=id)
    clothingdon=ClothingRequest.objects.filter(charity_id=id)
    medicinedon=MedicineRequest.objects.filter(charity_id=id)
    studymaterialdon=StudyMaterialRequest.objects.filter(charity_id=id)
    otherdon=OtherRequest.objects.filter(charity_id=id)
    return render (request,'admin_search_charity_profile.html',{'charityProfile':Charity,'events':events,'fooddon':fooddon,'clothingdon':clothingdon,'medicinedon':medicinedon,'studymaterialdon':studymaterialdon,'otherdon':otherdon,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})



def adminhometotaluserfun(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    userreg=usersignup.objects.all()
    return render(request,'adminhometotaluser.html',{'userreg':userreg,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})  

def AdminSearchUser(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    if request.method=="POST":
        searchuser=request.POST['adminsearchUser']
        userobj=usersignup.objects.filter(username__icontains=searchuser)
        return render(request,'admin_search_user.html',{'user':userobj,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})
    return redirect('adminhometotaluser')

def SearchUserProfile(request,id):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    
    searchuser=usersignup.objects.filter(id=id)
    regevent=EventsRegistrations.objects.filter(user_id=id)
    fooddonation=FoodDonation.objects.filter(user_id=id)
    clothingdonation=clothingDonation.objects.filter(user_id=id)
    medicinedonation=medicineDonation.objects.filter(user_id=id)
    studymaterialdonation=studyMaterialDonation.objects.filter(user_id=id)
    otherdonation=otherDonation.objects.filter(user_id=id)

    return render(request,'admin_search_user_profile.html',{'searchuser':searchuser,'regevent':regevent,'fdonation':fooddonation,'clothingdonation':clothingdonation,'medicinedonation':medicinedonation,'studymaterialdonation':studymaterialdonation,'otherdonation':otherdonation,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})

def adminhomeuserdelete(request,id):
    user=usersignup.objects.filter(id=id).delete()
    return render(request,'adminhometotaluser.html')  

def adminhometotaldonationreqfun(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon


    userfooddonation=FoodDonation.objects.all()
    foodRequest=FoodRequest.objects.all()
    clothingRequest=ClothingRequest.objects.all()
    medicineRequest=MedicineRequest.objects.all()
    studymaterialRequest=StudyMaterialRequest.objects.all()
    otherRequest=OtherRequest.objects.all()

    return render(request,'adminhometotaldonationreq.html',{'food':foodRequest,'clothing':clothingRequest,'medicine':medicineRequest,'studymaterial':studymaterialRequest,'other':otherRequest,'fooddonation':userfooddonation,'count':charity,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})             

def adminhometotaldonationfun(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    fooddonation=FoodDonation.objects.all()
    clothingdonation=clothingDonation.objects.all()
    medicinedonation=medicineDonation.objects.all()
    studymaterialdonation=studyMaterialDonation.objects.all()
    otherdonation=otherDonation.objects.all()
    return render(request,'adminhometotaldonation.html',{'food':fooddonation,'clothing':clothingdonation,'medicine':medicinedonation,'studymaterial':studymaterialdonation,'other':otherdonation,'fooddonation':fooddon,'count':charity,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})  

def adminhomefooddonationfun(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    userfooddonation=FoodDonation.objects.all()

    return render(request,'adminhomefooddonation.html',{'fooddonation':userfooddonation,'count':charity,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})       

def adminhomeclothingdonationfun(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    userclothingdonation=clothingDonation.objects.all()

    return render(request,'adminhomeclothingdonation.html',{'clothingdonation':userclothingdonation,'count':charity,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})  

def adminhomemedicinedonationfun(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon
    usermedicinedonation=medicineDonation.objects.all()
    return render(request,'adminhomemedicinedonation.html',{'medicinedonation':usermedicinedonation,'count':charity,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})        


def adminhomestudymaterialdonationfun(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    userstudymaterialdonation=studyMaterialDonation.objects.all()

    return render(request,'adminhomestudymaterialdonation.html',{'studymaterialdonation':userstudymaterialdonation,'count':charity,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})

def adminhomeotherdonationfun(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    userotherdonation=otherDonation.objects.all()

    return render(request,'adminhomeotherdonation.html',{'otherdonation':userotherdonation,'count':charity,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})


def adminhomeeventsfun(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    userEvents=addevents.objects.all()

    return render(request,'adminhomeevents.html',{'events':userEvents,'count':charity,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})    

def adminhomeregisterdeventfun(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    userregEvents=EventsRegistrations.objects.all()

    return render(request,'adminhomeregisterdevent.html',{'regevents':userregEvents,'count':charity,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})       



def adminhomeviewuserfeedbackfun(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon
    
    userFeedback=UserFeedback.objects.all()

    return render(request,'adminhomeviewfeedback.html',{'userfeedback':userFeedback,'count':charity,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})     

def adminhomeviewcharityfeedbackfun(request):
    adminname=adminreg.objects.all()
    charity=charitysignup.objects.all().count()
    user=usersignup.objects.all().count()
    Foodreq=FoodRequest.objects.all().count()
    clothingreq=ClothingRequest.objects.all().count()
    medicinereq=MedicineRequest.objects.all().count()
    studymaterialreq=StudyMaterialRequest.objects.all().count()
    othereq=OtherRequest.objects.all().count()
    totalRequest=Foodreq+clothingreq+medicinereq+studymaterialreq+othereq
    fooddon=FoodDonation.objects.all().count()
    clothingdon=clothingDonation.objects.all().count()
    medicinedon=medicineDonation.objects.all().count()
    studymaterialdon=studyMaterialDonation.objects.all().count()
    otherdon=otherDonation.objects.all().count()
    totalDonation=fooddon+clothingdon+medicinedon+studymaterialdon+otherdon

    charityFeedback=CharityFeedback.objects.all()

    return render(request,'adminhomeviewcharityfeedback.html',{'charityfeedback':charityFeedback,'count':charity,'adminname':adminname,'charitycount':charity,'usercount':user,'donationrequestcount':totalRequest,'donationcount':totalDonation})     


def adminhomelogoutfun(request):
    try:
        request.session.flush()
        return redirect('adminlogin')
    except adminreg.DoesNotExit:
    
        return render(request,'adminlogin.html')               



