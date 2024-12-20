from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Customer, Order, Cupcake
from .forms import CustomerForm, OrderForm, CupcakeForm

def home(request):
    return render(request, 'orders/home.html')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'orders/customer_list.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers_list')
    else:
        form = CustomerForm()
    return render(request, 'orders/add_customer.html', {'form': form})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

def daily_orders(request):
    orders = Order.objects.all()  # Filter orders based on specific criteria if needed
    return render(request, 'orders/daily_orders.html', {'orders': orders})

def daily_orders_report(request):
    # Get filter parameters from the request
    fulfillment_date = request.GET.get('fulfillment_date')
    delivery_type = request.GET.get('delivery_type')
    customer_name = request.GET.get('customer_name')
    
    # Query the database
    orders = Order.objects.all()
    if fulfillment_date:
        orders = orders.filter(fulfillment_date=fulfillment_date)
    if delivery_type:
        orders = orders.filter(delivery_type=delivery_type)
    if customer_name:
        orders = orders.filter(
            Q(customer__first_name__icontains=customer_name) | 
            Q(customer__last_name__icontains=customer_name)
        )
    
    # Render the filtered results
    return render(request, 'reports/daily_orders.html', {'orders': orders})

