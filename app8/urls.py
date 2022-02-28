from django.urls import path,include

from app8 import models
from. import views


urlpatterns = [
        path('helooii',views.helooiifun,name='helooii'),
        path('adminlogin',views.adminloginfun,name='adminlogin'),
        # path('adminreg',views.adminregfun,name='adminreg'),

        path('adminhomebasepage',views.adminhomebasepagefun,name='adminhomebasepage'),
        path('adminhome',views.adminhomefun,name='adminhome'),
        path('adminhomeviewprofile',views.adminhomeviewprofilefun,name='adminhomeviewprofile'),

        path('adminhomecharityorg',views.adminhomecharityorgfun,name='adminhomecharityorg'),
        path('adminhometotaluser',views.adminhometotaluserfun,name='adminhometotaluser'),
        path('adminhometotaldonationreq',views.adminhometotaldonationreqfun,name='adminhometotaldonationreq'),
        path('adminhometotaldonation',views.adminhometotaldonationfun,name='adminhometotaldonation'),
        path('adminhomecharityorgadd',views.adminhomecharityorgaddfun,name='adminhomecharityorgadd'),
        path('adminhomedonationreq',views.adminhomedonationreqfun,name='adminhomedonationreq'),
        path('adminhomeuserdonation',views. adminhomeuserdonationfun,name='adminhomeuserdonation'),
        path('adminhomeevents',views.adminhomeeventsfun,name='adminhomeevents'),
        path('adminhomeaddservices',views. adminhomeaddservicesfun,name='adminhomeaddservices'),
        path('adminhomeeditprofile',views.adminhomeeditprofilefun,name='adminhomeeditprofile'),
        path('adminhomeviewfeedback',views.adminhomeviewfeedbackfun,name='adminhomeviewfeedback'),
        path('adminhomelogout',views.adminhomelogoutfun,name='adminhomelogout'),



]
