from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.user.views import  (
    CustomUserRegisterAPIView, UserLoginViewSet,ProfileGeneralInfoView,
)
user_router = DefaultRouter()
user_router.register(
    r'register', CustomUserRegisterAPIView, basename='register'
    )
user_router.register(
    r'auth', UserLoginViewSet, basename='auth'
    )
user_router.register(
    r'userprofile', ProfileGeneralInfoView, basename='userprofile'
    )

urlpatterns = [
    path('', include(user_router.urls)),
]
from apps.user.views import (
    profile_view, login_view
)
urlpatterns += [
    path('profile/',profile_view, name='profile'),
    path('login/', login_view, name='login'),
]