from django.urls import path,include
from. import views

urlpatterns = [
    path('heloo',views.testfun,name='heloo'),
    path('login',views.loginfun,name='login')
]