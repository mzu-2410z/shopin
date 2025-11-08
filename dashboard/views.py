from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def user_dashboard(request):
    return render(request, 'dashboard/user-dashboard.html')


@login_required
def profile_view(request):
    return render(request, 'dashboard/profile.html')


@login_required
def wishlist(request):
    return render(request, 'dashboard/wishlist.html')


@login_required
def orders_view(request):
    return render(request, 'dashboard/orders.html')
