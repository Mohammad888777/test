from django.contrib.auth.models import BaseUserManager

class UserManger(BaseUserManager):

    def create_user(self,email,phone_number,password=None):
        if not email:
            raise ValueError("email is required")
        if not phone_number:
            raise ValueError("phone is required")
        user=self.model(email=self.normalize_email(email),phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,phone_number,password):
        user=self.create_user(email=email,password=password,phone_number=phone_number)
        user.is_admin=True
        # user.is_staff=True
        user.is_superuser=True
        user.is_active=True
        user.save(using=self._db)
        return user
