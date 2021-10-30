from django.urls import path
from .views import *

app_name = 'shop'
urlpatterns = [
    # shop/ will render the shopping cart details for us
    path('detail/', detail, name='detail'),
    path('add/<int:product_id>', add_cart, name='add_cart'),

]