from django.db import models
from accounts.models import User
from django.urls import reverse


class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering=["name"]
    
    def __str__(self) -> str:
        return self.name






class Product(models.Model):
    
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)
    image=models.ImageField(upload_to="Products",null=True,blank=True)
    description=models.TextField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
    is_access=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)



    class Meta:
        ordering=["name"]
        # verbose_name="category"
        # verbose_name_plural="categorie"
    
    def __str__(self) -> str:
        return self.name



    def get_absolute_url(self):
        return reverse("product-detail",args=(self.slug,))