from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField
from datetime import date
from django.core.exceptions import ValidationError
from ..managers import ProductManager

# Create your models here.
LABEL = (
    ('B', 'پرفروش'),  # blue tag primary color
    ('N', 'جدید'),  # purple tag secondary color
    ('Un', 'ناموجود'),  # red tag danger color
    ('O', 'اصالت کالا'),
)


class Product(models.Model):
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ('created_at',)

    name = models.CharField(max_length=50)
    category = models.ForeignKey('product.Category', on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey('product.Brand', on_delete=models.CASCADE, related_name='products')
    # labels such as bestseller, new, not available, etc ...
    label = models.CharField(choices=LABEL, max_length=2)
    image = models.ImageField(upload_to='product/static/product/images/', null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    is_original = models.BooleanField()
    inventory = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    number_sold = models.PositiveIntegerField(default=0, null=True, blank=True)
    # discount code for this book
    cash_code = models.ForeignKey('cart.CashDiscount', null=True, on_delete=models.CASCADE, blank=True,
                                  related_name='related_products')
    percentage_code = models.ForeignKey('cart.PercentageDiscount', null=True, on_delete=models.CASCADE,
                                        related_name='related_products', blank=True)
    # for food and health products:
    expiration_date = models.DateField(null=True, blank=True)
    # slug = AutoSlugField(populate_from=['name', 'brand'], allow_unicode=True, unique=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, editable=False)
    objects = ProductManager()

    # another way of defining price field, as an example: 999,999.99
    # price = models.DecimalField('قیمت', max_digits=8, decimal_places=2)

    # def slug(self):
    #     return slugify(self.name, self.brand)

    @property
    def final_price(self):
        if self.get_sale() is not None:
            return self.get_sale()
        else:
            return self.unit_price

    def get_sale(self):
        if self.cash_code is not None:
            return self.unit_price - self.cash_code.amount
        elif self.percentage_code is not None:
            return self.unit_price - ((self.percentage_code.percentage * self.unit_price) // 100)
        else:
            return None

    def save(self, *args, **kwargs):
        # if not self.slug:
        self.slug = slugify(self.name, allow_unicode=True) + '-' + slugify(self.brand.name, allow_unicode=True)
        print(self.slug)
        if self.cash_code:
            self.percentage_code = None
        elif self.percentage_code:
            self.cash_code = None
        else:
            self.percentage_code = None
            self.cash_code = None
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse("product_detail", kwargs={"id": self.id})
        return reverse("product_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.brand, self.category)
