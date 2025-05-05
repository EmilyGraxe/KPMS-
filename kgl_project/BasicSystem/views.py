# from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q # For complex lookups
from django.http import JsonResponse
from .models import StockUpdate
from .forms import StockUpdateForm
from datetime import datetime
from django.contrib.auth.decorators import user_passes_test


# Create your views here.
from .forms import ProductForm
from .models import Product

# CRUD = Create, Read, Update, Delete
# home view
def home_view(request):
    return render(request, 'invApp/home.html')
# Create view
def Product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form': form})

# Read view
def Product_list_view(request):
    query = request.GET.get('q')  
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(product_id__icontains=query))
    else:
        products = Product.objects.all()
    return render(request, 'invApp/product_list.html', {'products': products})

def category_list_view(request):
   categories = Product.objects.values_list('category', flat = True).distinct()
   selected_category = request.GET.get('category')
   if selected_category:
       products = Product.objects.filter(category=selected_category)  
   else: products = [] 

   return render(request, 'invApp/category_list.html', {'categories': categories, 'selected_category': selected_category, 'products': products})

def Product_delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'invApp/product_confirm_delete.html', {'product': product})


def Product_update_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = StockUpdateForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            price = form.cleaned_data['price']
            supplier = form.cleaned_data['supplier']
            reason = form.cleaned_data['reason']
            supply_price = form.cleaned_data['supply_price']
            if quantity < 0 and not reason:
               form.add_error('reason', 'Reason for negative adjustment is required.')
               return render(request, 'invApp/stock_update.html', {'form': form, 'product': product})
            # Update the stock for the product
            product.quantity += quantity
            product.price = price
            product.supplier = supplier
            product.supply_price = supply_price
            product.save()
            #record stock update
            StockUpdate.objects.create(
                product=product, quantity=quantity,
                price=price, supplier=supplier,
                supply_price=supply_price, reason=reason,
            )

            return redirect('product_list')
    else:
        #prefill price with current price
        form = StockUpdateForm(initial={'price': product.price, 'supplier': product.supplier, 'supply_price': product.supply_price})

    return render(request, 'invApp/stock_update.html', {'form': form, 'product': product})

# inventory reporting
def inventory_report(request):
    products = Product.objects.all()
    stock_updates = StockUpdate.objects.select_related('product').all()

    query = request.GET.get('query')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    if query:
        stock_updates = stock_updates.filter(Q(product__name__icontains=query) | Q(product__product_id__icontains=query))
        if from_date:
            from_date_obj = datetime.strptime(from_date, '%Y-%m-%d')
            stock_updates = stock_updates.filter(updated_at__gte=from_date_obj)
        if to_date:
            to_date_obj = datetime.strptime(to_date, '%Y-%m-%d')
            stock_updates = stock_updates.filter(updated_at__lte=to_date_obj)
    context = {
            'products': products,
            'stock_updates': stock_updates,
        }
    return render(request, 'invApp/inventory_report.html', context)