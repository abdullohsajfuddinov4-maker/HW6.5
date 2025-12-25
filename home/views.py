from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def products(request):
    return render(request,'shop-list.html')