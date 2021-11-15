from django.db.models.signals import post_save
from product.models import Product
from .models import Order, OrderItem
from django.dispatch import receiver
import logging

# __name__ is the name of a python module that contains the logger
logger = logging.getLogger(__name__)


# update inventory of items in the order
@receiver(signal=post_save, sender=OrderItem)
def update_inventory(sender, instance, **kwargs):
    instance.product.inventory -= instance.quantity
    print("Inventory updated!")
    logger.info('Product: {} Inventory:{} '.format(instance.product.name, instance.product.inventory))
    if instance.product.inventory == 0:
        instance.product.available = False
        logger.warning('Product {} unavailable.'.format(instance.product.name))
    instance.product.save()
