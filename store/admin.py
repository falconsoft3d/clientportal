from django.contrib import admin
from .models import Product, ProductGallery
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name', ) }
    inlines = [ProductGalleryInline]
    
    
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
    

