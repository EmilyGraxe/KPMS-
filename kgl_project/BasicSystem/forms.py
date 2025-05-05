from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': "Product ID",
            'name': "Product Name",
            'category': "Product category",
            'price': "Product Price",
            'quantity': "Product Quantity",
            'supplier': "Product Supplier",
            'supply_price': "Product Supply Price",
        }
        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder':'e.g. 1','class':'form-control'}),
            'name': forms.TextInput(attrs={'placeholder':'e.g. hybrid_maize','class':'form-control'}),
            'category': forms.Select(attrs={'placeholder':'e.g. Beans','class':'form-select'}),
            'price': forms.NumberInput(attrs={'placeholder':'e.g. 100.00','class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder':'e.g. 10','class':'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder':'e.g. ABC','class':'form-control'}),
            'supply_price': forms.NumberInput(attrs={'placeholder':'e.g. 100.00','class':'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Product.objects.all()

class StockUpdateForm(forms.Form):
    quantity = forms.IntegerField(label='Quantity')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Price')
    supplier = forms.CharField(max_length=100, label='Supplier', required=False)
    reason = forms.CharField(max_length=100, label='Reason For Negative Adjustment', required=False)
    supply_price = forms.DecimalField(max_digits=10, decimal_places=2, label='Supply Price', required=False)

