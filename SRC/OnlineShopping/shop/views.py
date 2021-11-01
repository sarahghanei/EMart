from django.shortcuts import render, get_object_or_404, redirect
from .shop import Shop
from product.models import Product
from .forms import AddForm
from django.views.decorators.http import require_POST


# Create your views here.
# display the shopping cart detail
def detail(request):
    shop = Shop(request)
    return render(request, 'shop/detail.html', {'shop': shop})


# adding items to cart
# user must access this view by post method
@require_POST
def add_cart(request, product_id):
    shop = Shop(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        shop.add(product, cd['quantity'])
    return redirect('shop:detail')


# remove item from shopping cart
def remove_cart(request, product_id):
    shop = Shop(request)
    product = get_object_or_404(Product, id=product_id)
    shop.remove(product)
    return redirect('shop:detail')
