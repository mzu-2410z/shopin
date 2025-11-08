from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.user_dashboard, name='user_dashboard'),
    path('orders/', views.orders_view, name='orders'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('profile/', views.profile_view, name='profile'),
]




# from django.urls import path
# from django.contrib.auth.decorators import login_required
# from .views import dashboard_home, profile_view, orders_view
#
# app_name = 'dashboard'
#
# urlpatterns = [
#     path('', login_required(dashboard_home), name='home'),
#     path('profile/', login_required(profile_view), name='profile'),
#     path('orders/', login_required(orders_view), name='orders'),
# ]
