from django.db import models
from django.conf import settings
from django.utils import timezone
from BasicSystem.models import Product
from home.models import TrustedCustomer
import uuid

class Sale(models.Model):
    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('credit', 'Credit'),
        ('visa', 'Visa'),
        ('mobile_money', 'Mobile Money'),
    ]
    # Sale_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(TrustedCustomer, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    branch = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)
    change = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.date} - Sale ID: {self.id} by {self.payment_method}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.price
        super().save(*args, **kwargs)

