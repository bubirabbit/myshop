from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def product_list(request):
    products=Product.objects.all()#取得所有商品
    return render(request,'products/index.html',{'products':products})

def about_page(request):
    return render(request, 'products/about.html')

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def privacy_policy(request):
    return render(request, 'products/privacy.html')