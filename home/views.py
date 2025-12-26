from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404, render
# Create your views here.
def home(request):
    product = Product.objects.all().order_by('-id')
    context = {'product':product}
    return render(request,'index.html',context)

def product_detail(request,pk):
    product = get_object_or_404(Product, pk=pk)
    images = product.images.all()
    contex ={'product':product,'images': images}
    return render(request,'shop-single-product-2.html',contex)


def contact(request):
    return render(request,'contact.html')

def products(request):
    product = Product.objects.all().order_by('-id')
    context = {'product': product}
    return render(request,'shop-list.html',context)