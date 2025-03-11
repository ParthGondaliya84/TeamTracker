from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView 
from apps.user.views import  CustomUserRegisterAPIView, UserLoginViewSet
user_router = DefaultRouter()
user_router.register(r'register', CustomUserRegisterAPIView, basename='register')
user_router.register(r'auth', UserLoginViewSet, basename='auth')

urlpatterns = [
    path('refresh/' , TokenRefreshView.as_view() , name="Token_refresh"),
    path('', include(user_router.urls)),
]
