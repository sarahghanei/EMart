from django.shortcuts import render, get_object_or_404
from product.models import Product, Category, Brand
from shop.forms import AddForm


def home(request, slug=None):
    categories = Category.objects.filter(is_sub=False)
    products = Product.objects.filter(available=True)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    return render(request, 'cart/home.html', {'products': products,
                                              'categories': categories,
                                              })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form = AddForm()
    return render(request, 'cart/product_detail.html', {'product': product, 'form': form})
