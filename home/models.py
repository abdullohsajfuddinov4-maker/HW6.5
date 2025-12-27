from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    discount_price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='image/',blank=True,null=True)
    desc = models.TextField()
    quantity = models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='image/',blank=True,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')

    def __str__(self):
        return self.product.name


class ProductExtraInfo(models.Model):
    size = models.PositiveIntegerField(blank=True,null=True)
    color = models.CharField(max_length=100)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='extra_info')

    def __str__(self):
        return self.product.name

