from django.contrib import admin
from apps.user.models import TeamUser, UserProfileInfo

class TeamUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']
    filter_horizontal = ['user_permissions']
    

class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ["user", "email_address", "phone", "dob", "gender", "created_at"]

    
admin.site.register(TeamUser, TeamUserAdmin)
admin.site.register(UserProfileInfo, UserProfileInfoAdmin)
