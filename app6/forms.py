from dataclasses import fields
from cProfile import label
from email.headerregistry import Address
from pyexpat import model
from django import forms
from app6.models import charitysignup


from app6.models import charitysignup

# class charitysignupform(forms.ModelForm):
#     CharityName=forms.CharField(label="Charity Organization Name",  widget=forms.TextInput(attrs={'placeholder':'Enter Your Charity Name'}))
#     UserName=forms.CharField(label="User Name",widget=forms.TextInput(attrs={'placeholder':'Enter Your Name'}))
#     Address=forms.CharField(label="Address",widget=forms.TextInput(attrs={'placeholder':'Enter Your Address'}))
#     TypeOfCharity=forms.CharField(label="Type Of Charity",widget=forms.TextInput(attrs={'placeholder':'Type Of Charity'}))
#     Email=forms.CharField(label="Email",widget=forms.TextInput(attrs={'placeholder':'Enter Your Email'}))
#     PhoneNumber=forms.CharField(label="Phone Number",widget=forms.NumberInput(attrs={'placeholder':'enter your Phone Number'}))
#     password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'placeholder':'enter password'}))
#     confpassword=forms.CharField(label="confirm password",widget=forms.PasswordInput(attrs={'placeholder':'confirm password'}))


# class meta:

#     model=charitysignup
#     fields="__all__"


# def clean_password(self):
       
        
#         pswd=self.cleaned_data['password']
        
#         if len(pswd)<8:
#             # print('******************************')
#             raise forms.ValidationError("minimum 8 characters required")
          
#         return pswd    


