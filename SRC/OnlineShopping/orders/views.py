from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from shop.shop import Shop
from suds.client import Client
from django.http import HttpResponse
from django.contrib import messages

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


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
description = 'صفحه پرداخت Emart'
# email and mobile of customer included in the receipt
# both are optional
mobile = '09121231200'
CallbackURL = 'http://localhost:8000/orders/verify/'


@login_required
def payment(request, order_id, price):
    # first version
    # make amount global so it can be accessible in verify view
    global amount, o_id
    amount = price
    o_id = order_id
    result = client.service.PaymentRequest(MERCHANT, amount, description, request.user.email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))


@login_required
# after payment gateway we come here to verify the payment
def verify(request):
    # first version
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            # set the paid variable True
            order = Order.objects.get(id=o_id)
            order.paid = True
            order.save()
            messages.success('Transaction was successful', 'success')
            return redirect('cart:home')
        elif result.Status == 101:
            return HttpResponse('Transaction Submitted Before')
        else:
            return HttpResponse('Error code')
    else:
        return HttpResponse('Transaction failed or canceled by user')
