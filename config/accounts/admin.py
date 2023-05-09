from django.contrib import admin
from  .models import User,OtpCode
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreation,ChangeForm
from django.contrib.auth.models import Group

class UserAdmin(BaseUserAdmin):
    
    form=ChangeForm
    add_form=UserCreation

    list_display=["email","phone_number","is_admin",]
    list_filter=("is_admin",)

    fieldsets=(
        (None,{"fields":("email","phone_number","password")}),
        ("Permissions",{"fields":("is_active","is_admin","last_login")})
    )

    add_fieldsets=(
        (None,{"fields":("phone_number","email","password",'password_confirm')}),
    )

    search_fields=("email",)
    ordering=["email"]
    filter_horizontal=[

    ]


class OtpAdmin(admin.ModelAdmin):
    list_display=["phone_number","code"]

admin.site.register(OtpCode,OtpAdmin)







admin.site.unregister(Group)

admin.site.register(User,UserAdmin)
