from django.contrib import admin
from .models import Order, OrderItem, Coupon


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'updated', 'paid')
    list_filter = ('paid', 'user')
    inlines = (OrderItemInline,)


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'valid_from', 'valid_to', 'active')
    list_filter = ('active', 'valid_from', 'valid_to')
    search_fields = ('code',)