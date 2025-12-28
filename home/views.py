from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth import logout
from .models import Image_in_home


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


class CreateAccountView(View):
    def get(self, request):
        return render(request, 'account.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Paroll mas emas')
            return redirect('account')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Bu foydalanuvchi allaqochon mavjut')
            return redirect('account')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()

        messages.success(request, 'Accaunt yaralildi  ')
        return redirect('login')


def LogoutView(request):
    logout(request)
    return redirect('login')

def inage_in_home(request):
    image = Image_in_home.objects.first()
    return render(request,'index.html',{'image':image})
