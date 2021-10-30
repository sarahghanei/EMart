from django.urls import path, re_path
from .views import *

app_name = 'cart'
urlpatterns = [
    path('home/', home, name='home'),
    # just for english slugs
    # path('products/<slug:slug>/', product_detail, name='product_detail'),
    re_path(r'^products/(?P<slug>[-\w]+)/', product_detail, name='product_detail'),
    # just for english slugs
    # path('category/<slug:slug>/', category_filter, name='category_filter'),
    re_path(r'^category/(?P<slug>[-\w]+)/', home, name='category_filter'),

]
# r'^(?P<slug>[^/]+)/$