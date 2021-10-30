from django.contrib import admin
from .models import Category, Brand, Product


# admin.site.register(Comment)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name',)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'brand', 'available', 'inventory', 'unit_price')
    list_filter = ('name', 'category', 'brand', 'available', 'created_at')
    list_editable = ('unit_price', 'inventory', 'available')
    search_fields = ('name', 'brand', 'category')
    actions = ['make_available']

    @admin.action(description='make selected objects available')
    def make_available(self, request, queryset):
        updated = queryset.update(available=True)
        self.message_user(request, 'Successfully made {} object(s) available.'.format(updated))


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
