from product.models import Product
from decimal import Decimal

# naming sessions related to the shopping cart
SHOP_SESSION_ID = 'shop'


# structure of shopping cart
# {
#     'shop': {
#         '2': {
#             'name': 'asus gl 702',
#             'price': '720',
#             'quantity': 1
#         },
#         '5': {
#             'name': 'lg k10',
#             'price': '120',
#             'quantity': 2
#         }
#     }
# }


# handling session
class Shop:
    def __init__(self, request):
        self.session = request.session
        # having all sessions related to the shopping cart
        shop = self.session.get(SHOP_SESSION_ID)
        if not shop:
            # create an empty cart
            shop = self.session[SHOP_SESSION_ID] = {}
        self.shop = shop

    def __iter__(self):
        # getting id of products in the shopping cart
        product_ids = self.shop.keys()
        # retrieve those products
        products = Product.objects.filter(id__in=product_ids)
        # copy of shopping cart
        shop = self.shop.copy()
        # adding fields of product info and total price for each item in the basket
        for product in products:
            shop[str(product.id)]['product'] = product
        for item in shop.values():
            # item is the dict for each product
            # price in shop is in the string format, so for calculating we cast it to decimal
            item['total_price'] = Decimal(item['price']) * item['quantity']
            yield item

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.shop:
            self.shop[product_id] = {'quantity': quantity, 'price': str(product.unit_price)}
        else:
            self.shop[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.shop:
            del self.shop[product_id]
            self.save()

    def save(self):
        # saving session's changes manually.
        self.session.modified = True
