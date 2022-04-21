from unicodedata import name
from django.urls import path,include
from. import views

urlpatterns = [
        path('helooi',views.testfun,name='helooi'),
        path('charityorglogin',views.charity_login,name='charityorglogin'),
        path('charityorgloginforgot',views.charity_org_login_forgot,name='charityorgloginforgot'),
        path('charityorgsignup',views.charity_org_signup,name='charityorgsignup'),
        path('charityusernameAjax',views.check_username,name='charityusernameAjax'),
        path('charityuserEmailajax',views.check_userEmail,name='charityuserEmailajax'),
        path('charityuserPhoneajax',views.check_user_Phone,name="charityuserPhoneajax"),
        path('charityprofileedit',views.charity_profile_edit,name='charityprofileedit'),
        path('charityorghomeprofileedit',views.charity_org_profile_edit,name='charityorghomeprofileedit'),
        path('searchuser',views.search_User,name='searchuser'),
        path('searchuserprofile/<int:id>',views.search_user_Profile,name='searchuserprofile'),
        path('charityorghomechangepassword',views.charity_org_change_password,name='charityorghomechangepassword'),
        path('renamecharitypassword',views.rename_charity_password),

        path('charityorghomebasepage',views.charity_org_Home_Basepage,name='charityorghomebasepage'),
        path('charityorghomepage',views.charity_org_homepage,name='charityorghomepage'),
        path('charityorghomeaboutus',views.charity_org_home_aboutus,name='charityorghomeaboutus'),
        path('charityorghomemyevents',views.charity_org_home_myevents,name='charityorghomemyevents'),
        path('charityorghomeeventdelete/<int:id>',views.charity_org_home_event_delete,name='charityorghomeeventdelete'),

        path('charityorghomeusereventsreg',views.charity_org_home_userevents_reg,name='charityorghomeusereventsregfun'),

        path('charityorghomeaddnewevents',views.charity_org_home_add_newevents,name='charityorghomeaddnewevents'),
        path('charityorghomeprofile',views.charity_org_home_profile,name='charityorghomeprofile'),

        path('changecharityname/',views.change_charity_name,name='changecharityname'),
        path('renamecharityname',views.rename_charity_name),
        path('changetypeofcharity/',views.change_typeof_charity,name='changetypeofcharity'),
        path('renametypeofcharity',views.rename_typeof_charity),
        path('changecharityemail/',views.change_charity_email,name='changecharityemail'),
        path('renamecharityemail',views.rename_charity_email),
        path('changecharityphone/',views.change_charity_phone,name='changecharityphone'),
        path('renamecharityphone',views.rename_charity_phone),
        path('changecharitywhatsapp/',views.change_charity_whatsapp,name='changecharitywhatsapp'),
        path('renamecharitywhatsapp',views.rename_charity_whatsapp),
        path('changecharityusername/',views.change_charity_username,name='changecharityusername'),
        path('renamecharityusername',views.rename_charity_username),
        path('changecharityaddress/',views.change_charity_address,name='changecharityaddress'),
        path('renamecharityaddress',views.rename_charity_address),
        path('changecharityabout/',views.change_charity_about,name='changecharityabout'),
        path('renamecharityabout',views.rename_charity_about),
        path('changecharityservices/',views.change_charity_services,name='changecharityservices'),
        path('renamecharityServices',views.rename_charity_services),
        path('changecharityprofile/',views.change_charity_profile_picture,name='changecharityprofile'),
        path('renamecharityprofile',views.rename_charity_profile_picture,name='renamecharityprofile'),


        path('charityorgprofilelogout',views.charity_org_profile_logout,name='charityorgprofilelogout'),

        path('charityorghomesendreq',views.charity_org_home_send_req,name='charityorghomesendreq'),

        path('foodsendreq',views.food_send_req,name='foodsendreq'),
        path('charityorgfoodreqdelete/<int:id>',views.charity_org_food_req_delete,name='charityorgfoodreqdelete'),

        path('clothingsendreq',views.clothing_send_req,name='clothingsendreq'),
        path('charityorgclothingreqdelete/<int:id>',views.charity_org_clothing_req_delete,name='charityorgclothingreqdelete'),

        path('medicinesendreq',views.medicine_send_req,name='medicinesendreq'),
        path('charityorgmedicinereqdelete/<int:id>',views.charity_org_medicine_req_delete,name='charityorgmedicinereqdelete'),

        path('studymeterialsendreq',views.studymeterial_send_req,name='studymeterialsendreq'),
        path('charityorgstudymeterialreqdelete/<int:id>',views.charity_org_studymeterial_req_delete,name='charityorgstudymeterialreqdelete'),

        path('othersendreq',views.other_send_req,name='othersendreq'),
        path('charityorgotherreqdelete/<int:id>',views.charity_org_other_req_delete,name='charityorgotherreqdelete'),

        path('charityorg_mydonationrequest',views.mydonation_request,name='charityorg_mydonationrequest'),



        path('charityorghomeviewdonations',views.charity_org_home_view_donations,name='charityorghomeviewdonations'),


        
        path('charityorgaccepteddon/<int:id>',views.charity_org_accepted_don,name='charityorgaccepteddon'),


        path('foodacceptedcancel/<int:id>',views.food_accept_cancel,name='foodacceptedcancel'),
        path('clothingacceptedcancel/<int:id>',views.clothing_accept_cancel,name='clothingacceptedcancel'),
        path('medicineacceptedcancel/<int:id>',views.medicine_accept_cancel,name='medicineacceptedcancel'),
        path('studymaterialacceptedcancel/<int:id>',views.studyMaterial_accept_cancel,name='studymaterialacceptedcancel'),
        path('otheracceptedcancel/<int:id>',views.other_accept_cancel,name='otheracceptedcancel'),

        path('viewacceptdonation',views.view_accepted_dontaion,name='viewacceptdonation'),

       
        path('donationcollected/<int:id>',views.donation_collect,name='donationcollected'),

        path('viewcollecteddonations',views.view_collected_donations,name='viewcollecteddonations'),

        path('viewcollectedfood',views.view_collected_food,name='viewcollectedfood'),
        path('viewcollectedclothing',views.view_collected_clothing,name='viewcollectedclothing'),
        path('viewcollectedmedicine',views.view_collected_medicine,name='viewcollectedmedicine'),
        path('viewcollectedstudymaterial',views.view_collected_studymaterial,name='viewcollectedstudymaterial'),
        path('viewcollectedother',views.view_collected_other,name='viewcollectedother'),
        path('nocollecteddonations',views.no_collected_donations,name='nocollecteddonations'),


        path('charityorghomenotifications',views.charity_org_home_notifications,name='charityorghomenotifications'),
        path('charityorghomesendfeedback',views.charity_org_home_send_feedback,name='charityorghomesendfeedback'),
        path('charityorghomeviewfeedback',views.charity_org_home_view_feedback,name='charityorghomeviewfeedback'),
        path('deletecharityfeedback/<int:id>',views.delete_charity_feedback),

        path('charitynotevents',views.charity_not_event,name='charitynotevents'),
        path('usernotfound',views.user_not_found,name='usernotfound'),
        path('charitynotfeedback',views.charity_not_feedback,name='charitynotfeedback'),

]
