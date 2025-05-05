from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from BasicSystem.models import Product
from django.utils import timezone
from django.db.models import Sum
from .models import Sale, SaleItem
from .forms import ProductSearchForm, CheckoutForm
from home.models import TrustedCustomer
from datetime import timedelta

# @login_required
def pos_view(request):
    cart = request.session.get('cart', {})  # {product_id: quantity}
    products_in_cart = []
    grand_total = 0

    # Build cart item list and compute total
    for pid, qty in cart.items():
        try:
            product = Product.objects.get(product_id=int(pid))
            subtotal = product.price * qty
            grand_total += subtotal
            products_in_cart.append({
                'product_id': product.product_id,
                'name': product.name,
                'quantity': qty,
                'price': product.price,
                'subtotal': subtotal,
            })
        except Product.DoesNotExist:
            continue

    search_form = ProductSearchForm()
    checkout_form = CheckoutForm()
    context = {
        'search_form': search_form,
        'checkout_form': checkout_form,
        'cart': products_in_cart,
        'grand_total': grand_total,
    }

    if request.method == 'POST':
        if 'search' in request.POST:
            search_form = ProductSearchForm(request.POST)
            if search_form.is_valid():
                name = search_form.cleaned_data['name']
                try:
                    product = Product.objects.get(name=name)
                    context['product'] = product
                except Product.DoesNotExist:
                    search_form.add_error('name', 'Product not found.')
            return render(request, 'sales.html', context)

        elif request.POST.get('action') == 'add_to_cart':
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity'))
            try:
                product = Product.objects.get(product_id=product_id)
                cart = request.session.get('cart', {})
                pid_str = str(product_id)
                cart[pid_str] = cart.get(pid_str, 0) + quantity
                request.session['cart'] = cart
                request.session.modified = True
                messages.success(request, f"{product.name} added to cart.")
                return redirect('sales:pos')
            except Product.DoesNotExist:
                messages.error(request, "Product not found.")
                return redirect('sales:pos')

        elif 'checkout' in request.POST:
            checkout_form = CheckoutForm(request.POST)
            if checkout_form.is_valid():
                payment_method = checkout_form.cleaned_data['payment_method']
                amount_paid=checkout_form.cleaned_data['amount_paid']
                nin = checkout_form.cleaned_data['nin']
                if payment_method!= 'cash':
                    amount_paid=grand_total

                if payment_method== 'credit':
                    try:
                        customer = TrustedCustomer.objects.get(nin=nin)
                    except TrustedCustomer.DoesNotExist:
                        messages.error(request, "Customer not found.")
                        return redirect('sales:pos')
                    amount_paid= grand_total
                    change=0
                    due_date = timezone.now() + timedelta(days=30)
                else:
                  if amount_paid < grand_total:
                    messages.error(request, "Amount paid is less than grand total.")
                    return redirect('sales:pos')
                  change = amount_paid - grand_total
                  due_date = None
                  customer = None
                for pid, qty in cart.items():
                    product = Product.objects.get(product_id=pid)
                    if product.quantity < qty:
                        sale.delete()
                        messages.error(request, f"Not enough stock for {product.name}")
                        return redirect('sales:pos')
                
                sale = Sale.objects.create(
                    
                    # user=request.user,
                    # branch=request.user.branch,
                    date=timezone.now(),
                    payment_method=payment_method,
                    grand_total=grand_total,
                    amount_paid=amount_paid,
                    change=change,
                    due_date=due_date,
                    customer=customer,
                    
                )
               
                SaleItem.objects.create(
                        sale=sale,
                        product=product,
                        quantity=qty,
                        price=product.price,
                        subtotal=product.price * qty,
                    )
                product.quantity -= qty
                product.save()

                request.session['cart'] = {}
                is_credit = payment_method == 'credit'
                return render(request, 'receipt.html', {
                    'sale': sale,
                    'items': sale.items.all(),
                    'is_credit': is_credit,
                })

        elif request.POST.get('action') == 'remove_from_cart':
            product_id = request.POST.get('product_id')
            try:
                product = Product.objects.get(product_id=product_id)
                cart = request.session.get('cart', {})
                pid_str = str(product_id)
                if pid_str in cart:
                    del cart[pid_str]
                    request.session['cart'] = cart
                    request.session.modified = True
                    messages.success(request, f"{product.name} removed from cart.")
                else:
                    messages.error(request, f"{product.name} not in cart.")
                return redirect('sales:pos')
            except Product.DoesNotExist:
                messages.error(request, "Product not found.")
                return redirect('sales:pos')

    return render(request, 'sales.html', context)

def home_view(request):
    return render(request, 'home.html')


def receipt_pdf_view(request, sale_id):
    sale= get_object_or_404(Sale, id=sale_id)
    items=sale.items.all()
    return render(request, 'receiptpdf.html', {'sale': sale, 'items': items})
    

def sales_report_view(request):
    sales = Sale.objects.all().select_related('user', 'branch').order_by('-date')
   
    # Optional filters
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    branch = request.GET.get('branch')

    if start_date:
        sales = sales.filter(date__gte=start_date)
    if end_date:
        sales = sales.filter(date__lte=end_date)
    if branch:
        sales = sales.filter(branch__name=branch)

    total = sales.aggregate(total=Sum('grand_total'))['total'] or 0

    return render(request, 'report.html', {
        'sales': sales,
        'total': total,
    })

def branch_totals_view(request):
    from_date = request.GET.get('from')
    to_date = request.GET.get('to')

    filters = {}
    if from_date:
        filters['date__gte'] = from_date
    if to_date:
        filters['date__lte'] = to_date

    summary = Sale.objects.filter(**filters).values('branch__name').annotate(
        total_sales=Sum('grand_total')
    ).order_by('branch__name')

    return render(request, 'branch_summary.html', {
        'summary': summary,
        'from_date': from_date,
        'to_date': to_date,
    })
def mark_sale_as_paid(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)

    if sale.payment_method == 'credit' and not sale.is_paid:
        sale.is_paid = True
        sale.save()
        messages.success(request, f"Sale #{sale.id} marked as paid.")
    else:
        messages.warning(request, "Sale already paid or not a credit sale.")

    return redirect('sales:credit_sales_list')  # or wherever you want to go after

def credit_sales_list(request):
    credit_sales = Sale.objects.filter(payment_method='credit', is_paid=False)
    return render(request, 'credit_sales_list.html', {'credit_sales': credit_sales})