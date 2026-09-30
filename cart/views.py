# cart/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from products.models import Product
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required

def _get_cart_for_request(request):
    """
    Return Cart object associated with authenticated user or session.
    Create one if it doesn't exist.
    """
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, _ = Cart.objects.get_or_create(session_key=session_key, user=None)
    return cart

def view_cart(request):
    cart = _get_cart_for_request(request)
    # ensure properties are available for template
    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart.html', context)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = _get_cart_for_request(request)

    # try to find existing item
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
    item.save()
    messages.success(request, f"Added {product.title} to cart.")
    return redirect(request.META.get('HTTP_REFERER', 'products:product_list'))

def update_cart(request, item_id):
    if request.method != 'POST':
        return redirect('cart:view_cart')
    item = get_object_or_404(CartItem, id=item_id)
    quantity = int(request.POST.get('quantity', 1))
    if quantity < 1:
        item.delete()
        messages.info(request, "Item removed from cart.")
    else:
        item.quantity = quantity
        item.save()
        messages.success(request, "Cart updated.")
    return redirect('cart:view_cart')

def remove_from_cart(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(CartItem, id=item_id)
        item.delete()
        messages.success(request, "Removed item from cart.")
    return redirect('cart:view_cart')
