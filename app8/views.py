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
    return render(request,'adminhomebasepage.html' ) 

def adminhomefun(request):
    return render(request,'adminhome.html')  

def adminhomeviewprofilefun(request):
    return render(request,'adminhomeviewprofile.html')           

def adminhomecharityorgfun(request):
    charityorgreg=charitysignup.objects.all()
    return render(request,'adminhomecharityorg.html',{'charityorgreg':charityorgreg})  

def adminhometotaluserfun(request):
    userreg=usersignup.objects.all()
    return render(request,'adminhometotaluser.html',{'userreg':userreg})  

def adminhometotaldonationreqfun(request):
    foodRequest=FoodRequest.objects.all()
    clothingRequest=ClothingRequest.objects.all()
    medicineRequest=MedicineRequest.objects.all()
    studymaterialRequest=StudyMaterialRequest.objects.all()
    otherRequest=OtherRequest.objects.all()

    return render(request,'adminhometotaldonationreq.html',{'food':foodRequest,'clothing':clothingRequest,'medicine':medicineRequest,'studymaterial':studymaterialRequest,'other':otherRequest})             

def adminhometotaldonationfun(request):
    return render(request,'adminhometotaldonation.html')  

def adminhomecharityorgaddfun(request):
    charityorgreg=charitysignup.objects.all()

    return render(request,'adminhomecharityorgadd.html',{'charityorgreg':charityorgreg})       

def adminhomedonationreqfun(request):
   

    return render(request,'adminhomedonationreq.html')  

def adminhomeuserdonationfun(request):
       
      
    return render(request,'adminhomeuserdonation.html')        


def adminhomeeventsfun(request):
    userEvents=addevents.objects.all()
    return render(request,'adminhomeevents.html',{'events':userEvents})   

def adminhomeaddservicesfun(request):
    return render(request,'adminhomeaddservices.html')        

def adminhomeeditprofilefun(request):
    return render(request,'adminhomeeditprofile.html')  

def adminhomeviewfeedbackfun(request):
    return render(request,'adminhomeviewfeedback.html')     

def adminhomelogoutfun(request):
    try:
        request.session.flush()
        return redirect('adminlogin')
    except adminreg.DoesNotExit:
    
        return render(request,'adminlogin.html')               



