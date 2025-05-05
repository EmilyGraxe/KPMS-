

# Create your models here.
from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)  
    category = models.CharField(max_length=50, choices=(('Beans', 'Beans'), ('Maize', 'Maize'), ('Cowpeas', 'Cowpeas'), ('Gnuts', 'Gnuts'), ('Soyabeans', 'Soyabeans')))
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    supplier = models.CharField(max_length=100)
    supply_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null= True)
    @property
    def is_out_of_stock(self):
        return self.quantity <= 0

    def __str__(self):
        return self.name

class StockUpdate(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stock_updates')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()# Positive for increase, negative for decrease
    supplier = models.CharField(max_length=100, blank=True, null=True)
    reason = models.CharField(max_length=1000, blank=True, null=True)
    supply_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.product.name} update"