from django.urls import path,include
from. import views

urlpatterns = [


    path('charityWelcomepage',views.charityWelcomepage,name='charityWelcomepage'),

    path('userlogin',views.userloginfun,name='userlogin'),
    path('userloginforgot',views.userloginforgotfun,name='userloginforgot'),
    path('usersignup',views.usersignupfun,name='usersignup'),
    path('usernameAjax',views.usernameAjax,name='usernameAjax'),
    path('userEmailajax',views.userEmailAjax,name='userEmailAjax'),
    

    path('useraboutus',views.useraboutusfun,name='useraboutus'),
    path('userevents',views.usereventsfun,name='userevents'),
    path('usereventsreg',views.usereventsregfun,name='usereventsreg'),
    path('userregisterdevents',views.userRegisterdEvents,name='userregisterdevents'),
    path('userhomeeventcancel/<int:id>',views.userHomeEventCancel,name='userhomeeventcancel'),

    path('userprofile',views.userprofilefun,name='userprofile'),




    path('userprofileedit',views.userprofileedit,name='userprofileedit'),

    
    path('userprofileeditform',views.userprofileeditfun,name='userprofileeditform'),




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
    path('renameuserprofile',views.rename_profile,name='renameuserprofile'),






    path('userprofilelogout',views.userprofilelogoutfun,name='userprofilelogout'),


    path('userhomepage',views.userhomepagefun,name='userhomepage'),


    path('usercharityorg',views.usercharityorgfun,name='usercharityorg'),

    path('searchcharity',views.searchCharity,name='searchcharity'),
    path('searchcharityprofile/<int:id>',views.searchcharityProfile,name='searchcharityprofile'),


    path('userdonationsreq',views.userdonationsreqfun,name='userdonationsreq'),



    

    path('userfoodacceptreq/<int:id>',views.userfoodacceptreqfun,name='userfoodacceptreq'),
    path('userclothingacceptreq/<int:id>',views.userclothingacceptreqfun,name='userclothingacceptreq'),
    path('usermedicineacceptreq/<int:id>',views.usermedicineacceptreqfun,name='usermedicineacceptreq'),
    path('userstudymaterialacceptreq/<int:id>',views.userstudymaterialacceptreqfun,name='userstudymaterialacceptreq'),
    path('userotheracceptreq/<int:id>',views.userotheracceptreqfun,name='userotheracceptreq'),





    path('userfoodreq',views.show_food_request,name='userfoodreq'),
    path('userclothingreq',views.show_clothing_request,name='userclothingreq'),
    path('usermedicinesreq',views.show_medicine_request,name='usermedicinesreq'),
    path('userstudymeterialsreq',views.show_studymaterial_request,name='userstudymeterialsreq'),
    path('userotherreq',views.show_other_request,name='userotherreq'),




    path('usernotifications',views.usernotificationsfun,name='usernotifications'),


    path('usermydonations',views.usermydonationsfun,name='usermydonations'),
    path('cancelfooddonation/<int:id>',views.CancelFoodDonation),
    path('cancelclothingdonation/<int:id>',views.CancelClothingDonation),
    path('cancelmedicinedonation/<int:id>',views.CancelMedicineDonation),
    path('cancelstudymaterialdonation/<int:id>',views.CancelStudyMaterialDonation),
    path('cancelotherdonation/<int:id>',views.CancelOtherDonation),
    path('usersendcompfeedback',views.usersendcompfeedbackfun,name='usersendcompfeedback'),
    path('userviewfeedback',views.userviewfeedbackfun,name='userviewfeedback'),
    path('deletefeedback/<int:id>',views.DeleteFeedBack),

    path('userhomebasepage',views.userhomebasepagefun,name='userhomebasepage'),
    path('user_user',views.UserUser,name='user_user'),
    path('user_no_events',views.UserNoevent,name='user_no_events'),
    path('charitynotfound',views.CharityNotFound,name='charitynotfound'),
    path('nofeedback',views.NoFeedback,name='nofeedback'),



   




    






 
  
    

]