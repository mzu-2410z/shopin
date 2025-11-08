from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="products")

    # Main image
    image = models.ImageField(upload_to="products/main/")

    # Additional gallery images
    gallery1 = models.ImageField(upload_to="products/gallery/", blank=True, null=True)
    gallery2 = models.ImageField(upload_to="products/gallery/", blank=True, null=True)
    gallery3 = models.ImageField(upload_to="products/gallery/", blank=True, null=True)
    gallery4 = models.ImageField(upload_to="products/gallery/", blank=True, null=True)

    short_description = models.TextField(max_length=300)
    full_description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_percent = models.PositiveIntegerField(blank=True, null=True)

    stock = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    tag = models.CharField(max_length=20, blank=True, null=True)  # e.g., "New", "Sale"

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        # auto calculate discount percentage
        if self.old_price and self.price:
            try:
                self.discount_percent = int(((self.old_price - self.price) / self.old_price) * 100)
            except:
                pass
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("products:product_detail", kwargs={"slug": self.slug})
