from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('product-list/', view=ProductList.as_view(), name='product_list'),
    re_path(r'product-detail/(?P<slug>[-\w]+)/', view=ProductDetail.as_view(), name='product_detail'),
    path('brand-list/', view=BrandList.as_view(), name='brand_list'),
    re_path(r'brand-detail/(?P<slug>[-\w]+)/', view=BrandDetail.as_view(), name='brand_detail'),
    path('category-list/', view=CategoryList.as_view(), name='category_list'),
    re_path(r'category-detail/(?P<slug>[-\w]+)/', view=CategoryDetail.as_view(), name='category_detail'),
]
