from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# This kind of discount will be calculated on shopping cart and decrease some amount of total price.
class Coupon(models.Model):
    class Meta:
        verbose_name = 'کوپن'
        verbose_name_plural = 'کوپن ها'
        ordering = ('valid_from', 'valid_to')

    code = models.CharField(max_length=20, help_text="Just numbers and characters are allowed.")
    description = models.CharField(max_length=100, null=True, blank=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    is_active = models.BooleanField()
    percentage = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    max_amount = models.DecimalField(max_digits=8, decimal_places=2,
                                     validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    number_used = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])

    def save(self, *args, **kwargs):
        if self.valid_from > self.valid_to:
            raise ValidationError('Start date should be smaller than end date.')
        super(Coupon, self).save(*args, **kwargs)

    def __str__(self):
        return "{} : {}".format(self.description, self.max_amount)


class CashDiscount(models.Model):
    class Meta:
        verbose_name = 'تخفیف نقدی محصول'
        verbose_name_plural = 'تخفیف های نقدی'
        ordering = ('valid_from', 'valid_to')

    amount = models.DecimalField(max_digits=8, decimal_places=2,
                                 validators=[MinValueValidator(0), MaxValueValidator(100)])
    description = models.CharField(max_length=100, null=True, blank=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    is_active = models.BooleanField()

    def save(self, *args, **kwargs):
        if self.valid_from > self.valid_to:
            raise ValidationError('Start date should be smaller than end date.')
        super(CashDiscount, self).save(*args, **kwargs)

    def __str__(self):
        return "Maximum amount of discount : {}".format(self.amount)


class PercentageDiscount(models.Model):
    class Meta:
        verbose_name = 'تخفیف درصدی'
        verbose_name_plural = 'تخفیف های درصدی'
        ordering = ('valid_from', 'valid_to')

    max_amount = models.DecimalField(max_digits=8, decimal_places=2,
                                     validators=[MinValueValidator(0), MaxValueValidator(100)])
    percentage = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    description = models.CharField(max_length=100, null=True, blank=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    is_active = models.BooleanField()

    def save(self, *args, **kwargs):
        if self.valid_from > self.valid_to:
            raise ValidationError('Start date should be smaller than end date.')
        super(PercentageDiscount, self).save(*args, **kwargs)

    def __str__(self):
        return "{} : {}".format(self.description, self.max_amount)

# class ItemDiscount(models.Model):
#     TYPE = (
#         ('Cash', 'نقدی'),
#         ('Percentage', 'درصدی')
#     )
#     type = models.CharField(max_length=10, choices=TYPE)
#     is_valid = models.BooleanField()
#     valid_from = models.DateTimeField()
#     valid_to = models.DateTimeField()
#     amount = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20000)], null=True,
#                                          blank=True, default=0)
#     percent = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True,
#                                           blank=True, default=0)
#     products = models.ManyToManyField('product.Product', related_name='discounts')
