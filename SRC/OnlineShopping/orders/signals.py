from django.db.models.signals import post_save
from product.models import Product
from .models import Order, OrderItem
from django.dispatch import receiver


@receiver(signal=post_save, sender=OrderItem)
def update_inventory(sender, instance, **kwargs):
    instance.product.inventory -= instance.quantity
    print("Inventory updated!")
    if instance.product.inventory == 0:
        instance.product.available = False
    instance.product.save()
