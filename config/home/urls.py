from django.urls import path
from . import views

urlpatterns=[

    path("",views.Home.as_view(),name="home"),
    path("<slug:slug>/",views.ProductDetail.as_view(),name="product-detail"),
    
]