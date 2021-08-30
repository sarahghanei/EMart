from django.conf import settings
from django.db import models

# class OrderItem(models.Model):
#     item = models.ForeignKey('product.Product', on_delete=models.CASCADE)
#
#
# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEl, on_delete=models.CASCADE, related_name="orders")
#     items = models.ManyToManyField(OrderItem)
#     # moment that the order created
#     start_date = models.DateTimeField(auto_now_add=True)
#     # use ordered flag shows that the order is completed or not
#     ordered = models.BooleanField(default=False)
#     ordered_date = models.DateTimeField()
#     address = models.ForeignKey(on_delete=models.CASCADE, related_name="orders_to_this_address")
#     coupon = models.ForeignKey(on_delete=models.CASCADE, related_name="orders_with_this_coupon", null=True, blank=True)
