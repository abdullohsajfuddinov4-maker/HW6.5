from django.urls import path
from . import views
from .views import CreateAccountView , LogoutView

urlpatterns = [
    path('',views.home,name='home'),
    path('cart_detail/',views.cart_detail,name='cart_detail'),
    path('cart/delete/<int:pk>/', views.cart_delete, name='cart_delete'),
    path('contact/',views.contact,name='contact'),
    path('products/', views.products, name='products'),
    path('products_detail/<int:pk>', views.product_detail, name='product_detail'),
    path('account/', CreateAccountView.as_view(), name='account'),
    path('logout/', LogoutView, name='logout'),
]