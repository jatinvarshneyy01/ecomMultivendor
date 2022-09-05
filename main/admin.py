from django.contrib import admin
from .models import Vendor, Product, ProductCategory

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id','user','address')

admin.site.register(Vendor, VendorAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','detail','price')

admin.site.register(Product, ProductAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title','detail')

admin.site.register(ProductCategory, ProductCategoryAdmin)