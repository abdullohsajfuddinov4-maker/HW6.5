from idlelib.rpc import request_queue

from django.contrib.auth.decorators import login_required
from home.models import Product
from .models import Cart , CustomUser
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate ,login,logout
# Create your views here.

def login_view(request):
    if request.method ==  'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':' Invalid username or password '})
    return render(request, 'login.html')


@login_required
def add_to_cart(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        quantity = int(request.POST.get('quantity', 1))

        cart_item = Cart.objects.filter(
            user=request.user,
            product=product
        ).first()

        if cart_item:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            Cart.objects.create(
                user=request.user,
                product=product,
                quantity=quantity
            )

        return redirect('home')



