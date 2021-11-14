from django.urls import path
from .views import *

app_name = 'orders'
urlpatterns = [
    path('create/', create_order, name='create'),
    path('<int:order_id>/', order_detail, name='detail'),
    path('payment/<int:order_id>/<price>', payment, name='payment'),
    path('verify/', verify, name='verify'),
    path('apply/<int:order_id>/', coupon_apply, name='coupon_apply'),
]