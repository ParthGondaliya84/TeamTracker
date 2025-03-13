from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.user.managers import CustomUserManager
from django.conf import settings
from apps.user.choices import GENDER_CHOICE


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_%(class)s_set"
        )
    updated_by= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_%(class)s_set"
        )
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)


    class Meta:
        abstract = True

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True,blank=True,)
    updated_at = models.DateTimeField(null=True,blank=True,)
    created_by= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_%(class)s_set"
        )
    updated_by= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="updated_%(class)s_set"
        )
    
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


class UserProfileGeneralInfo(BaseModel):

    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE ,related_name="profile")
    user_profile = models.ImageField(upload_to="userprofile/" , blank=True, null=True)
    alternative_email = models.EmailField(blank=True , null=True)
    phone = models.CharField(blank=True , null=True)
    alternative_phone = models.EmailField(blank=True , null=True)
    dob = models.DateField(blank=True , null=True)
    skype = models.URLField(max_length=200 , blank=True , null=True)
    ssn = models.BigIntegerField(blank=True , null=True)
    gender = models.CharField(max_length=10 , choices=GENDER_CHOICE , blank=True , null=True)

    def __str__(self):
        return self.user.first_name
