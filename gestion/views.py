from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Product
# Create your views here.

def index(request):
    page_number = request.GET.get('page')

    productos_page = Paginator(Product.objects.all(), 5)
    try:
        productos = productos_page.get_page(page_number)
    except PageNotAnInteger:
        productos = productos_page.get_page(1)
    except EmptyPage:
        productos = productos_page.get_page(1)
    
    data  = {'poductos': productos}


    return render(request, 'index.html',data)


def show(request, pk):
    product = get_list_or_404(Product, id=pk)[0]

    data  = {'product': product}
    return render(request, 'details.html', data)