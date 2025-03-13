from django.contrib import admin
from apps.user.models import CustomUser, UserProfileGeneralInfo

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'created_at']
    

class UserProfileGeneralInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'alternative_email', 'phone', 'dob', 'gender']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfileGeneralInfo, UserProfileGeneralInfoAdmin)
