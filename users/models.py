from django.db import models
from django.contrib.auth.models import User
from home.models import Product
from django.shortcuts import render


# Create your models here.
class CustomUser(User):
    phone = models.CharField(max_length=13,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.first_name


class Cart(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(default=0)

    def save(self,*args,**kwargs):
        price = self.product.discount_price or self.product.price
        total_price = price * self.quantity
        self.total_price = total_price
        super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.user.username}-{self.product.name}'

class Order(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,blank=True,null=True,related_name='order')
    total_price = models.PositiveIntegerField(default=0)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.order.user.username


