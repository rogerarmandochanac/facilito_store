from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **k):
        context = super().get_context_data(**k)
        context['title'] = "Listado de productos"
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product.html'

class ProductSearchListView(ListView):
    template_name = 'product/search.html'

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.query())
    
    def query(self):
        return self.request.GET.get('q')
    
    def get_context_data(self, **k):
        context = super().get_context_data(**k)
        context['query'] = self.query()
        context['count'] = context['object_list'].count()
        return context