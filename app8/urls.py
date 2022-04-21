from django.urls import path,include

from app8 import models
from. import views


urlpatterns = [
        path('helooii',views.helooiifun,name='helooii'),
        path('adminlogin',views.adminloginfun,name='adminlogin'),
        # path('adminreg',views.adminregfun,name='adminreg'),

        path('adminhomebasepage',views.adminhomebasepagefun,name='adminhomebasepage'),
        # path('admincharitycount',views.admincharityCount),
        path('adminhome',views.adminhomefun,name='adminhome'),
        path('food_accept',views.foodAccept,name='food_accept'),
        path('clothing_accept',views.clothingAccept,name='clothing_accept'),
        path('medicine_accept',views.medicineAccept,name='medicine_accept'),
        path('studyMaterial_accept',views.studyMaterialAccept,name='studyMaterial_accept'),
        path('other_accept',views.otherAccept,name='other_accept'),

        path('adminhomeviewprofile',views.adminhomeviewprofilefun,name='adminhomeviewprofile'),

        path('adminhomecharityorg',views.adminhomecharityorgfun,name='adminhomecharityorg'),
        path('adminhomecharitydelete/<int:id>',views.AdminHomeCharityDelete,name="adminhomecharitydelete"),

        path('searchcharityprofile',views.SerachCharityOrg,name="searchcharityprofile"),
        path('search_charity_profile/<int:id>',views.SearchCharityProfile,name="search_charity_profile"),

        # path('search_charity',views.adminhomecharityorgfun,name="search_charity"),


        path('adminhometotaluser',views.adminhometotaluserfun,name='adminhometotaluser'),
        path('adminsearchuserprofile',views.AdminSearchUser,name="adminsearchuserprofile"),
        path('admin_search_user_profile/<int:id>',views.SearchUserProfile,name="admin_search_user_profile"),

        path('adminhomeuserdelete/<int:id>',views.adminhomeuserdelete,name='adminhomeuserdelete'),
        path('adminhometotaldonationreq',views.adminhometotaldonationreqfun,name='adminhometotaldonationreq'),
        path('adminhometotaldonation',views.adminhometotaldonationfun,name='adminhometotaldonation'),


        path('adminhomefooddonation',views.adminhomefooddonationfun,name='adminhomefooddonation'),
        path('adminhomeclothingdonation',views.adminhomeclothingdonationfun,name='adminhomeclothingdonation'),
        path('adminhomemedicinedonation',views. adminhomemedicinedonationfun,name='adminhomemedicinedonation'),
        path('adminhomestudymaterialdonation',views.adminhomestudymaterialdonationfun,name='adminhomestudymaterialdonation'),
        path('adminhomeotherdonation',views.adminhomeotherdonationfun,name='adminhomeotherdonation'),

        path('adminhomeevents',views.adminhomeeventsfun,name='adminhomeevents'),

        path('adminhomeregisterdevent',views.adminhomeregisterdeventfun,name='adminhomeregisterdevent'),

        path('adminhomeviewfeedback',views.adminhomeviewuserfeedbackfun,name='adminhomeviewfeedback'),
        path('adminhomeviewcharityfeedback',views.adminhomeviewcharityfeedbackfun,name='adminhomeviewcharityfeedback'),

        path('adminhomelogout',views.adminhomelogoutfun,name='adminhomelogout'),



]
