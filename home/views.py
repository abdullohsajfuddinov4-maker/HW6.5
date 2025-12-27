from django.shortcuts import redirect

from .models import Product
from users.models import Cart
from django.shortcuts import get_object_or_404, render
# Create your views here.
def home(request):
    product = Product.objects.all().order_by('-id')
    context = {'product':product}
    return render(request,'index.html',context)

def cart_detail(request):
    user = request.user
    items = Cart.objects.filter(user=user)
    context = {'items':items}
    return render(request,'shop-cart.html',context)


def cart_delete(request, pk):
    item = get_object_or_404(Cart,pk=pk,user=request.user)
    item.delete()
    return redirect('cart_detail')


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