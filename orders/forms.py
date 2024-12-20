from django import forms
from .models import Customer, Order, Cupcake

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'delivery_type', 'fulfillment_date', 'fulfillment_time', 'notes']

class CupcakeForm(forms.ModelForm):
    class Meta:
        model = Cupcake
        fields = '__all__'
    