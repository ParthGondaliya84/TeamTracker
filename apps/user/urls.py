from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.user.views import  (
    CustomUserRegisterAPIView,
    UserLoginViewSet,
    CustomUserView
)
user_router = DefaultRouter()
user_router.register(r'register', CustomUserRegisterAPIView, basename='register')
user_router.register(r'auth', UserLoginViewSet, basename='auth')
user_router.register(r'profile', CustomUserView, basename='profile')

urlpatterns = [
    path('', include(user_router.urls)),
]
