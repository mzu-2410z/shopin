from django.shortcuts import render

def user_dashboard(request):
    return render(request, 'dashboard/user-dashboard.html')

def profile_view(request):
    return render(request, 'dashboard/profile.html')

def orders_view(request):
    return render(request, 'dashboard/orders.html')
