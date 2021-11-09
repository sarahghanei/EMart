from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from shop.shop import Shop


# Create your views here.
@login_required
def create_order(request):
    # retrieve all things in the shop session related to this request
    shop = Shop(request)
    order = Order.objects.create(user=request.user)
    for item in shop:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
    # making shopping cart empty
    shop.clear()
    return redirect('orders:detail', order.id)


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})
