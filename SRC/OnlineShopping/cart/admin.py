from django.contrib import admin
from .models import Coupon, CashDiscount, PercentageDiscount
# from .models import OrderItem, Order

# Register your models here.
admin.site.register(Coupon)
admin.site.register(CashDiscount)
admin.site.register(PercentageDiscount)
# admin.site.register(Order)
# admin.site.register(OrderItem)
