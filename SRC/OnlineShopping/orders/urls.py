from django.urls import path
from .views import *

app_name = 'orders'
urlpatterns = [
    path('create/', create_order, name='create'),
    path('<int:order_id>/', order_detail, name='detail'),
]