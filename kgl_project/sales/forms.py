from django import forms
from .models import Sale
from BasicSystem.models import Product
from django.core.exceptions import ValidationError

class ProductSearchForm(forms.Form):
    name = forms.CharField(label='Enter Product Name or ID', max_length=100, required=False)

class AddToCartForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(label='Quantity', min_value=1)

class CheckoutForm(forms.Form):
    PAYMENT_CHOICES = Sale.PAYMENT_CHOICES
    payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES, label="Payment Method")
    amount_paid = forms.DecimalField(max_digits=10, decimal_places=2, label='Amount Paid')
    nin = forms.CharField(required=False, max_length=20, label='NIN')
    
    def clean(self):
        cleaned_data = super().clean()
        method = cleaned_data.get('payment_method')
        nin = cleaned_data.get('nin')
        if method == 'credit' and not nin:
            raise ValidationError('NIN is required for credit payment')
        
        return cleaned_data
