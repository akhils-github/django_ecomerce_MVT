from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','username','last_login','date_joined','is_active','phone_number')
    
    
    filter_horizontal=()
    list_filter=()
    fieldsets=()
admin.site.register(Account,AccountAdmin)


