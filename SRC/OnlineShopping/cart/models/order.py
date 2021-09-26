from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'
        ordering = ('start_date',)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    # moment that the order created
    start_date = models.DateTimeField(auto_now_add=True)
    # use ordered flag shows that the order is completed or not
    ordered = models.BooleanField(default=False)
    # date of order completion
    ordered_date = models.DateTimeField()
    address = models.ForeignKey('accounts.Address', on_delete=models.CASCADE, related_name="orders_to_this_address")
    coupon = models.ForeignKey('cart.Coupon', on_delete=models.CASCADE, related_name="orders_with_this_coupon", null=True,
                               blank=True)

    # calculate final price of cart with coupon and item discounts
    @property
    def final_price(self):
        cart_price = sum(item.final_price for item in self.items.all())
        try:
            if self.coupon is not None and self.coupon.is_active:
                discount_amount = ((self.coupon.percentage * cart_price) // 100)
                if discount_amount > self.coupon.max_amount:
                    discount_amount = self.coupon.max_amount
            else:
                raise ValidationError('Discount code is not valid')
        except:
            discount_amount = 0
        return cart_price - discount_amount

    # calculate total price of cart without coupon and item discounts
    @property
    def original_price(self):
        return sum(item.original_price for item in self.items.all())

    # calculate discount amount on cart
    @property
    def discount_amount(self):
        return (self.coupon.percentage * self.original_price) // 100

    def __str__(self):
        return "{}-{}".format(self.user.fullname, self.start_date)

class OrderItem(models.Model):
    class Meta:
        verbose_name = 'سفارش-محصول'
        verbose_name_plural = 'سفارش-محصول ها'
        ordering = ('ordered_date',)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField()

    # calculate item.final_price * amount
    @property
    def final_price(self):
        return self.item.final_price * self.amount

    # calculate the original price * amount
    @property
    def original_price(self):
        return self.item.unit_price * self.amount

    # return item original price  ( for just 1 item )
    @property
    def original_price_item(self):
        return self.item.unit_price

    # return item final price ( for just 1 item )
    @property
    def final_price_item(self):
        return self.item.final_price
