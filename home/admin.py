from django.contrib import admin
from .models import Product ,ProductImage ,ProductExtraInfo ,Category ,Image_in_home
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductExtraInfo)
admin.site.register(Image_in_home)

