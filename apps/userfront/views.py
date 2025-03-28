from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.userfront.decorators import token_required
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/team-user/profile/')
        else:
            return render(request, 'user/login.html', {'error': 'Invalid credentials'})
    return render(request, 'user/login.html')

@login_required(login_url='/team-user/login/')
def profile_view(request):
    print("User authenticated:", request.user.is_authenticated)
    print("User:", request.user)
    return render(request, 'user/profile.html')