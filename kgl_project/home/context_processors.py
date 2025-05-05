from BasicSystem.models import Product
from datetime import date
from sales.models import Sale
from django.shortcuts import render

def stock_alerts(request):
    out_of_stock = Product.objects.filter(quantity__lte=0)
    return {'out_of_stock':out_of_stock}
def credit_overdue(request):
    overdue_sales= Sale.objects.filter(payment_method = 'credit', due_date__lt=date.today(), is_paid= False)
    return {
        'overdue_sales': overdue_sales,
    }

