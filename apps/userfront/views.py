from django.shortcuts import render

def login_view(request):
    return render(request, 'user/login.html')


def profile_view(request):
    return render(request, 'user/profile.html')