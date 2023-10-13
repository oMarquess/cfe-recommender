from django.shortcuts import render
from django.views import generic
from .models import Products

# Create your views here.


class ProductListView(generic.ListView):
    template_name = 'products/list.html'
    paginate_by = 20
    queryset = Products.objects.all().order_by('-rating_avg')

product_list_view = ProductListView.as_view()

class ProductDetailView(generic.DetailView):
    template_name = 'products/detail.html'
    queryset = Products.objects.all()

product_detail_view = ProductDetailView.as_view()
