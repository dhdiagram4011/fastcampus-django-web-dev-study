from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import *

def product_in_category(request, category_slug=None):
    pass

def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)

    return render(request, 'shop/product_detail.html', {'object':product})



