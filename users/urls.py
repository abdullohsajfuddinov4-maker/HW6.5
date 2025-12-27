from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('add_to_cart/<int:pk>',views.add_to_cart,name='add_to_cart'),
]