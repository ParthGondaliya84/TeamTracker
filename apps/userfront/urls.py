from django.urls import path
from apps.userfront.views import login_view, profile_view

urlpatterns = [
    path('profile/',profile_view, name='profile'),
    path('login/', login_view, name='login'),
]
