from django.contrib import admin
from .models import StockUpdate
from .models import Product


# Register your models here.
admin.site.register(StockUpdate)
admin.site.register(Product)

