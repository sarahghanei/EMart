# naming sessions related to the shopping cart
SHOP_SESSION_ID = 'shop'


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

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.shop:
            self.shop[product_id] = {'quantity': 1, 'price': str(product.unit_price)}
        else:
            self.shop[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # saving session's changes manually.
        self.session.modified = True
