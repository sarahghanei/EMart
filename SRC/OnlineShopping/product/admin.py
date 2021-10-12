from django.contrib import admin
from .models import Category, Brand, Product
# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
# admin.site.register(Comment)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'label', 'available')
    list_filter = ('name', 'category', 'brand', '')



