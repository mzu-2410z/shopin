from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.user_dashboard, name='user_dashboard'),
    path('orders/', views.orders_view, name='orders'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('profile/', views.profile_view, name='profile'),
]
