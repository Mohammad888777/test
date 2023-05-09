from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser,BaseUserManager
from .managers import UserManger
from django.utils import timezone
from .utils import findTimeDiffrence



class User(AbstractBaseUser):
    email=models.EmailField(unique=True,max_length=200)
    phone_number=models.CharField(max_length=11,unique=True)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)

    objects=UserManger()

    USERNAME_FIELD="phone_number"
    REQUIRED_FIELDS=["email"]

    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin
    


class OtpCode(models.Model):
    phone_number=models.CharField(max_length=100)
    code=models.IntegerField()
    created=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.phone_number)+str(self.code)
    

    def expire(self):
      
        b=findTimeDiffrence(time_1=timezone.now(),time_2=self.created)
        print(b)

        if  timezone.now().year - self.created.year ==0:

            if timezone.now().month - self.created.month==0:
       
                if timezone.now().day-self.created.day ==0:

                    if 0<=findTimeDiffrence(timezone.now(),self.created).total_seconds()/3600<1:
                            if 0<=findTimeDiffrence(timezone.now(),self.created).total_seconds()/60 <=1:
                                return True
                            return False
                    return False
                return False
            return False
        return False
    
                                

