from django import forms
from .models import TrustedCustomer

class TrustedCustomerForm(forms.ModelForm):
    class Meta:
        model = TrustedCustomer
        fields = ['name', 'contact', 'nin', 'location']

