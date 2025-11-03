from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard:user_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')


def register_view(request):
    if request.method == 'POST':
        # You’ll replace this with a real registration form later
        pass
    return render(request, 'accounts/register.html')


def logout_view(request):
    logout(request)
    return redirect('core:home')


def password_reset_view(request):
    return render(request, 'accounts/password-reset.html')
