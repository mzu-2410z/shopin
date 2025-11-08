from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from .forms import EmailAuthenticationForm


def login_view(request):
    # ✅ If already logged in, send to dashboard
    if request.user.is_authenticated:
        return redirect('dashboard:user_dashboard')

    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully!")

            # ✅ Redirect to next (if user tried to access a protected page)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)

            # ✅ Default redirect (change if needed)
            return redirect('core:home')

        else:
            messages.error(request, "Invalid email or password.")
    else:
        form = EmailAuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def register_view(request):

    if request.user.is_authenticated:
        return redirect('dashboard:user_dashboard')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created. Please login.')
            return redirect('accounts:login')  # ensure you have a login route
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('core:home')


def password_reset_view(request):
    return render(request, 'accounts/password-reset.html')
