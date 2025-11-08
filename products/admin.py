from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "stock", "is_featured", "created_at")
    list_filter = ("category", "is_featured")
    search_fields = ("title", "category__name")
    prepopulated_fields = {"slug": ("title",)}
