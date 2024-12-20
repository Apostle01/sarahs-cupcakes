from django.contrib import admin
from .models import Customer, Order, Cupcake

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'delivery_type', 'fulfillment_date', 'fulfillment_time')

@admin.register(Cupcake)
class CupcakeAdmin(admin.ModelAdmin):
    list_display = ('order', 'flavor', 'icing_flavor', 'cupcake_color', 'icing_color', 'decorations')
