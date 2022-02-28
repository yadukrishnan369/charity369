from django.urls import path,include
from. import views

urlpatterns = [
    path('userbasepage',views.userbasepagefun,name='userbasepage'),
    path('charityhome',views.charityhomefun,name='charityhome'),
    path('aboutus',views.aboutusfun,name='aboutus'),
    path('userlogin',views.userloginfun,name='userlogin'),
    path('userloginforgot',views.userloginforgotfun,name='userloginforgot'),
    path('usersignup',views.usersignupfun,name='usersignup'),
    path('CheckUserName',views.CheckUserNamefun),
    path('CheckUserEmail',views.CheckUserEmailfun),

    path('forgotpassword',views.forgotpasswordfun,name='forgotpassword'),
    path('userhome',views.userhomefun,name='userhome'),
    path('useraboutus',views.useraboutusfun,name='useraboutus'),
    path('userevents',views.usereventsfun,name='userevents'),
    path('usereventsreg',views.usereventsregfun,name='usereventsreg'),

    path('userprofile',views.userprofilefun,name='userprofile'),
    path('userprofileedit',views.userprofileeditfun,name='userprofileedit'),
    path('changepassword/',views.changepasswordfun,name='changepassword'),
    path('renameuserpassword',views.rename_userpassword),

    path('changeusername/',views.changeusernamefun,name='changeusername'),
    path('renameusername',views.rename_username),
    path('changewebsite/',views.changewebsitefun,name='changewebsite'),
    path('renameuserwebsite',views.rename_website),
    path('changeemail/',views.changeemailfun,name='changeemail'),
    path('renameuseremail',views.rename_email),
    path('changebio/',views.changebiofun,name='changebio'),
    path('renameuserbio',views.rename_bio),
    path('changeaddress/',views.changeaddressfun,name='changeaddress'),
    path('renameuseraddress',views.rename_address),
    path('changeabout/',views.changeaboutfun,name='changeabout'),
    path('renameuserabout',views.rename_about),
    path('changephone/',views.changephonefun,name='changephone'),
    path('renameuserphone',views.rename_phone),
    path('changewhatsapp/',views.changewhatsappfun,name='changewhatsapp'),
    path('renameuserwhatsapp',views.rename_whatsapp),
    path('changeprofile',views.changeprofilefun,name='changeprofile'),
    path('renameuserprofile',views.rename_profile),






    path('userprofilelogout',views.userprofilelogoutfun,name='userprofilelogout'),


    path('userhomepage',views.userhomepagefun,name='userhomepage'),
    path('servicesviewmore',views.servicesviewmorefun,name='servicesviewmore'),
    path('usercharityorg',views.usercharityorgfun,name='usercharityorg'),
    path('userdonationsreq',views.userdonationsreqfun,name='userdonationsreq'),
    path('userfoodreq',views.show_food_request,name='userfoodreq'),
    path('userclothingreq',views.show_clothing_request,name='userclothingreq'),
    path('usermedicinesreq',views.show_medicine_request,name='usermedicinesreq'),
    path('userstudymeterialsreq',views.show_studymaterial_request,name='userstudymeterialsreq'),
    path('userotherreq',views.show_other_request,name='userotherreq'),
    path('useracceptreq',views.useracceptreqfun,name='useracceptreq'),


    path('usernotifications',views.usernotificationsfun,name='usernotifications'),
    path('usermydonations',views.usermydonationsfun,name='usermydonations'),
    path('usersendcompfeedback',views.usersendcompfeedbackfun,name='usersendcompfeedback'),
    path('userviewfeedback',views.userviewfeedbackfun,name='userviewfeedback'),


    path('userhomebasepage',views.userhomebasepagefun,name='userhomebasepage'),


    path('reg',views.regfun,name='reg'),

    path('checkUserName',views.checkUserNamefun),
    path('checkUserEmail',views.checkUserEmailfun),


    path('sampleajax',views.sampleajaxfun),

    path('sampletable',views.sampletablefun),

    


    
  
    

]