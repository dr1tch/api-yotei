from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'username', 'name',)
    # list_filter = ('id', 'logo', 'email', 'username', 'name',
    #                'phone_number', 'is_active', 'is_staff', 'type')
    ordering = ('-created_date',)
    list_display = ('id', 'email', 'username', 'name', 
                    'phone_number', 'is_active', 'is_staff', 'wilaya','role')


admin.site.register(User, UserAdminConfig)