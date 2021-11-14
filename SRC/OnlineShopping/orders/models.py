from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    discount = models.IntegerField(blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'
        ordering = ('created',)

    @property
    def get_total_cost(self):
        total = sum(item.get_cost() for item in self.items.all())
        if self.discount:
            discount_price = (self.discount / 100) * total
            return int(total - discount_price)
        else:
            return total

    def __str__(self):
        return f'{self.user}-{str(self.id)}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='order_items')
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.IntegerField()
    quantity = models.PositiveSmallIntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return f'{str(self.id)}'


class Coupon(models.Model):
    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کدهای تخفیف'

    code = models.CharField(unique=True, max_length=30)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    # discount percent between 0 to 100
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.code
