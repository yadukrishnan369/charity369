from django.urls import path,include
from. import views

urlpatterns = [
        path('helooi',views.testfun,name='helooi'),
        path('charityorgbasepage',views.charityorgbasepagefun,name='charityorgbasepage'),
        path('charityorg',views.charityorgfun,name='charityorg'),
        path('charityorgabout',views.charityorgaboutfun,name='charityorgabout'),
        path('charityorgcontact',views.charityorgcontactfun,name='charityorgcontact'),
        path('charityorglogin',views.charityorgloginfun,name='charityorglogin'),
        path('charityorgloginforgot',views.charityorgloginforgotfun,name='charityorgloginforgot'),
        path('charityorgsignup',views.charityorgsignupfun,name='charityorgsignup'),
        path('checkUserName',views.checkUserNamefun),
        path('checkUserEmail',views.checkUserEmailfun),
        path('checkUserPhonenumber',views.checkUserPhoneNumberfun),

        path('charityorghomebasepage',views.charityorghomebasepagefun,name='charityorghomebasepage'),
        path('charityorghomepage',views.charityorghomepagefun,name='charityorghomepage'),
        path('charityorghomeaboutus',views.charityorghomeaboutusfun,name='charityorghomeaboutus'),
        path('charityorghomemyevents',views.charityorghomemyeventsfun,name='charityorghomemyevents'),
        path('charityorghomeaddnewevents',views.charityorghomeaddneweventsfun,name='charityorghomeaddnewevents'),
        path('charityorghomeprofile',views.charityorghomeprofilefun,name='charityorghomeprofile'),
        path('charityorghomeprofileedit',views.charityorghomeprofileeditfun,name='charityorghomeprofileedit'),
        path('charityorghomechangepassword',views.charityorghomechangepasswordfun,name='charityorghomechangepassword'),
        path('renamecharitypassword',views.rename_charitypassword),

        path('changecharityname/',views.changecharitynamefun,name='changecharityname'),
        path('renamecharityname',views.rename_charityname),
        path('changetypeofcharity/',views.changetypeofcharityfun,name='changetypeofcharity'),
        path('renametypeofcharity',views.rename_typeofcharity),
        path('changecharityemail/',views.changecharityemailfun,name='changecharityemail'),
        path('renamecharityemail',views.rename_charityemail),
        path('changecharityphone/',views.changecharityphonefun,name='changecharityphone'),
        path('renamecharityphone',views.rename_charityphone),
        path('changecharitywhatsapp/',views.changecharitywhatsappfun,name='changecharitywhatsapp'),
        path('renamecharitywhatsapp',views.rename_charitywhatsapp),
        path('changecharityusername/',views.changecharityusernamefun,name='changecharityusername'),
        path('renamecharityusername',views.rename_charityusername),
        path('changecharityaddress/',views.changecharityaddressfun,name='changecharityaddress'),
        path('renamecharityaddress',views.rename_charityaddress),
        path('changecharityabout/',views.changecharityaboutfun,name='changecharityabout'),
        path('renamecharityabout',views.rename_charityabout),
        path('changecharityservices/',views.changecharityservicesfun,name='changecharityservices'),
        path('renamecharityServices',views.rename_charityservices),
        path('changecharityprofile/',views.changecharityprofilefun,name='changecharityprofile'),
        path('renamecharityprofile',views.rename_charityprofile),


        path('charityorgprofilelogout',views.charityorgprofilelogoutfun,name='charityorgprofilelogout'),

        path('charityorghomesendreq',views.charityorghomesendreqfun,name='charityorghomesendreq'),
        path('foodsendreq',views.foodsendreqfun,name='foodsendreq'),
        path('clothingsendreq',views.clothingsendreqfun,name='clothingsendreq'),
        path('medicinesendreq',views.medicinesendreqfun,name='medicinesendreq'),
        path('studymeterialsendreq',views.studymeterialsendreqfun,name='studymeterialsendreq'),
        path('othersendreq',views.othersendreqfun,name='othersendreq'),
        path('charityorg_mydonationrequest',views.mydonationrequestfun,name='charityorg_mydonationrequest'),



        path('charityorghomeviewdonations',views.charityorghomesviewdonationsfun,name='charityorghomeviewdonations'),
        path('charityorgaccepteddon',views.charityorgaccepteddonfun,name='charityorgaccepteddon'),

        path('charityorghomenotifications',views.charityorghomesnotificationsfun,name='charityorghomenotifications'),
        path('charityorghomeviewfeedback',views.charityorghomesviewfeedbackfun,name='charityorghomeviewfeedback'),
        path('charityorghomesendfeedback',views.charityorghomessendfeedbackfun,name='charityorghomesendfeedback'),


]
