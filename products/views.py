from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def products_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, "products/products.html", {
        "products": products,
        "categories": categories,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.exclude(id=product.id)[:4]

    return render(request, "products/product-detail.html", {
        "product": product,
        "related_products": related_products,
    })


def categories_view(request):
    return render(request, 'products/categories.html')

def wishlist_view(request):
    return render(request, 'products/wishlist.html')
