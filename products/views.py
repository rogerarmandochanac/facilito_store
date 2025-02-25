from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

class ProductView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-create_att')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product.html'

