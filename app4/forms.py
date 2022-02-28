from cProfile import label
from dataclasses import fields
from pyexpat import model
from tkinter import Place
from django import forms

from app4.models import usersignup

class SignupForm(forms.ModelForm):
    username=forms.CharField(label="username", widget=forms.TextInput(attrs={'placeholder':'enter User name'}))
    useremail=forms.CharField(label="username", widget=forms.TextInput(attrs={'placeholder':'enter your email'}))

    password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'placeholder':'enter password'}))
    confpassword=forms.CharField(label="confirm password",widget=forms.PasswordInput(attrs={'placeholder':'confirm password'}))

    # useremail=forms.CharField(label="useremail",widget=forms.EmailInput)
    class Meta:

        model=usersignup
        fields="__all__"
        # fields=('username','useremail','password','confpassword')

    def clean_password(self):
       
        
        pswd=self.cleaned_data['password']
        
        if len(pswd)<8:
            raise forms.ValidationError("minimum 8 characters required")
          
        return pswd    




