from django.contrib import admin
from apps.user.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'created_at']
    

admin.site.register(CustomUser, CustomUserAdmin)
