from .models import *
from django.db import models


class BrandManager(models.Manager):
    def products_of_brands(self):
        return self.products.all()


class CategoryManager(models.Manager):
    def products_of_category(self):
        return self.products.all()


class ProductManager(models.Manager):
    # newly added products
    def new_products(self):
        return self.objects.filter(label='N')

    # unavailable products
    def unavailable_products(self):
        return self.objects.filter(label='Un')

    # bestseller products
    def bestseller_products(self):
        return self.objects.filter(label='B')

    # products with 20% discount
    def product_percent_discount(self, percent):
        return self.objects.filter(discount_code__percentage=percent)

    # products with 20 T discount
    def product_cash_discount(self, cash):
        return self.objects.filter(cash_code__amount=cash)
