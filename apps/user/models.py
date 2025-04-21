from django.db import models
from django.contrib.auth.models import AbstractUser     
from apps.user.managers import CustomUserManager
from apps.user.choices import GenderChoice, UserRole
from apps.base.models import BaseModel


class TeamUser(AbstractUser):
    
    email = models.EmailField(unique=True, verbose_name='Your Email')
    user_role =models.CharField(
        choices=UserRole.choices(), verbose_name='Role in Company'
        )
    gender = models.CharField(choices=GenderChoice.choices())
    
    created_by= models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, 
        related_name="created_users"
        )
    updated_by= models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        related_name="updated_user"
        )
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = "teamtracker_user"
        verbose_name = "TeamTracker User"
        verbose_name_plural = "TamTracker Users"



class UserProfileInfo(BaseModel):
    
    user = models.OneToOneField(
        TeamUser ,on_delete=models.CASCADE, related_name="profile"
        )
    user_profile = models.ImageField(
        upload_to="media/userprofile",blank=True, null=True
        )
    email_address = models.EmailField(blank=True , null=True)
    alternative_address = models.EmailField(blank=True , null=True)
    phone = models.CharField(blank=True , null=True)
    alternative_phone = models.EmailField(blank=True , null=True)
    dob = models.DateField(blank=True , null=True)
    skype = models.URLField(max_length=200 , blank=True , null=True)
    ssn = models.BigIntegerField(blank=True , null=True)
    gender = models.CharField(
        max_length=10, choices=GenderChoice.choices(), blank=True, null=True
        )

    def __str__(self):
        return self.user.email
    
    class Meta:
        db_table = "profile_general_info"
        verbose_name = "General Profile"
        verbose_name_plural = "General Profiles"
        ordering = ['-created_at']
