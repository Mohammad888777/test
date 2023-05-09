from typing import Any, Dict
from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreation(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput())
    password_confirm=forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model=User
        fields=[
            "email","phone_number",
            "password",'password_confirm'
        ]
    
    def clean(self,*args,**kwargs):
        pas1=self.cleaned_data.get("password")
        pas2=self.cleaned_data.get("password_confirm")
        if pas1!=pas2:
            raise forms.ValidationError("not match passowrd")
        return super().clean(*args,**kwargs)
    
    def save(self,*args,**kwargs):
        user=super().save(*args,**kwargs)
        user.set_password(self.cleaned_data.get("password"))
        user.save()
        return user
    


class ChangeForm(forms.ModelForm):

    password=ReadOnlyPasswordHashField(
        help_text="change here <a href=\"../password\" > here</a>"
    )

    class Meta:
        model=User
        fields=[
            "email",
            "phone_number",
            "password",
            "last_login"
        ]



class UserRegisterForm(forms.Form):
    
    email=forms.EmailField(max_length=38)
    phone_number=forms.CharField(max_length=11)
    password=forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
        email=self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("email already taken")
        return email
    
    def clean_phone_number(self):
        phone_number=self.cleaned_data.get("phone_number")
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("phone_number already taken")
        return phone_number



class VerifyCodeForm(forms.Form):
    code=forms.IntegerField()