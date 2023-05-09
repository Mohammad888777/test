from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .forms import UserRegisterForm,VerifyCodeForm

import random
from .utils import send_otp
from .models import OtpCode,User
from django.contrib import messages



class Register(View):

    form_class=UserRegisterForm

    def get(self,request,*args,**kwargs):

        form=self.form_class
        contex={
            'form':form
        }
        
        return render(request,"accounts/register.html",contex)

    def post(self,request,*args,**kwargs):
        form=self.form_class(self.request.POST)
        if form.is_valid():
            code=random.randrange(1000,9999)
            send_otp(phone_number=form.cleaned_data.get("phone_number"),code=code)
            ot=OtpCode(
                phone_number=form.cleaned_data.get("phone_number"),
                code=code,

            )
            ot.save()

            self.request.session["user_info"]={
                "phone_number":form.cleaned_data.get("phone_number"),
                "email":form.cleaned_data.get("email"),
                "password":form.cleaned_data.get("password")
            }

            messages.success(request,"we sent you code",'success')
            return redirect("verify")
        messages.error(request,"not valid form")
        return render(request,"accounts/register.html",{"form":form})
    


class UserRegisterVerifyCode(View):

    form_class=VerifyCodeForm

    def get(self,request):

        # print(self.user_info)
        form=self.form_class()

        contex={
            'form':form
        }
        return render(request,"accounts/verify.html",contex)
    

    def post(self,request):

        user_info:dict=self.request.session.get("user_info")

        otp=OtpCode.objects.filter(phone_number=user_info.get("phone_number")).last()
        form=self.form_class(self.request.POST)
        if form.is_valid():
            print(form)
            if  otp.code == form.cleaned_data.get("code"):
                if otp.expire():
                    user=User(
                        password=user_info.get("password"),
                        email=user_info.get("email"),
                        phone_number=user_info.get("phone_number"),
                    )
                    user.save()
                    otp.delete()
                    messages.success(request,"you were registred")
                    return redirect("home")
                messages.error(request,"otp expired")
                return redirect(self.request.META.get("HTTP_REFERER"))
            messages.error(request,"not correct code")
            return redirect(self.request.META.get("HTTP_REFERER"))
        messages.error(request,"not vaild form")
        return redirect("home")
    
