from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Brand, Category


# Create your views here.
# views for Product
class ProductList(ListView):
    model = Product
    paginate_by = 100
    context_object_name = 'products'
    template_name = 'product_list.html'

    def get_queryset(self):
        qs = super(ProductList, self).get_queryset().filter(inventory__gt=0).order_by('name')
        return qs


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'


# views for Brand
class BrandList(ListView):
    model = Brand
    paginate_by = 100
    context_object_name = 'brands'
    template_name = 'brand_list.html'

    def get_queryset(self):
        qs = super(BrandList, self).get_queryset().order_by('name')
        return qs


class BrandDetail(DetailView):
    model = Brand
    context_object_name = 'brand'


# views for Category
class CategoryList(ListView):
    model = Category
    paginate_by = 100
    context_object_name = 'categories'
    template_name = 'category_list.html'

    def get_queryset(self):
        qs = super(CategoryList, self).get_queryset().order_by('name')
        return qs


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'
