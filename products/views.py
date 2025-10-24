from django.shortcuts import render

def products_list(request):
    return render(request, 'products/products.html')

def product_detail(request, product_id):
    return render(request, 'products/product-detail.html', {'product_id': product_id})

def categories_view(request):
    return render(request, 'products/categories.html')

def wishlist_view(request):
    return render(request, 'products/wishlist.html')
