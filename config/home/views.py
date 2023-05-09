from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,Category
from django.views import View


class Home(View):
    def get(self,request,*args,**kwargs):
        q=Product.objects.all().filter(
            is_access=True
        )
        contex={
            'q':q
        }
        return render(request,"home_app/index.html",contex)


class ProductDetail(View):
    def get(self,request,slug,*args,**kwargs):
        p=get_object_or_404(Product,slug=slug)
        contex={
            'q':p
        
        }
        return render(request,"home_app/product_detail.html",contex)
        
