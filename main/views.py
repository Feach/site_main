from django.db.models import Prefetch
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Product, Category


class HomeView(ListView):
    model = Product
    template_name = "main/home.html"


class MenuView(ListView):
    model = Category, Product
    template_name = "main/menu.html"

    def get_queryset(self):
        return Category.objects.prefetch_related(Prefetch("product", Product.objects.all()))


class ProductListView(ListView):
    model = Product
    template_name = "main/category.html"

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    slug_url_kwarg = 'product_slug'






