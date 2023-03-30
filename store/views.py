from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
from shop.views import store


def home(request):
    products=Product.objects.all().filter(is_available=True)
    context={
        'products':products,
    }
    return render(request,'home.html',context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword) | Q(price__icontains=keyword))
            products_count=products.count()
        if keyword == '':
            products=0
            products_count=products
    
    context = {
        'products' : products,
        'products_count':products_count,

    }
    return render(request,'store/store.html',context)

def checkout(request):
    return HttpResponse('<h1> will be coming soon </h1>')
