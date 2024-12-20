from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    street_address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Order(models.Model):
    DELIVERY_TYPE_CHOICES = [
        ('Pickup', 'Pickup'),
        ('Delivery', 'Delivery'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateField(auto_now_add=True)
    delivery_type = models.CharField(max_length=10, choices=DELIVERY_TYPE_CHOICES)
    fulfillment_date = models.DateField()
    fulfillment_time = models.TimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer}"
    
class Cupcake(models.Model):
    FLAVOR_CHOICES = [
        ('Vanilla', 'Vanilla'),
        ('Chocolate', 'Chocolate'),
        ('French Vanilla',	'French Vanilla'),
        ('White Chocolate',	'White Chocolate'),
        ('Double Chocolate', 'Double Chocolate'), 
        ('Strawberry', 'Strawberry'),
        ('Peanut Butter', 'Peanut Butter'),
        ('Pumpkin Spice', 'Pumpkin Spice'), 
        ('Blueberry Mint', 'Blueberry Mint'), 
        ('Apple Cinnamon', 'Cookies and Cream'),
        ('Cookies and Cream', 'Cookies and Cream'), 
        ('Champagne', 'champagne'), 
        ('Chocolate Chip', 'Chocolate Chip'),
        ('Mississippi Mud', 'Mississippi Mud'), 
        ('Red Velvet', 'Red Velvet'),
        ('Coconut', 'Coconut'), 
    ]

    ICING_CHOICES = [
        ('Vanilla', 'Vanilla'),
        ('Butter Cream', 'Butter Cream'),
        ('Lemon', 'Lemon'),
        ('Cream Cheese', 'Cream Cheese'),
        ('Strawberry', 'Strawberry'),
        ('Peanut Butter', 'Peanut Butter'),
        ('Oreo', 'Oreo'), 
		('Champagne', 'Champagne'), 
		('Chocolate', 'Chocolate'), 
		('German Chocolate', 'German Chocolate'), 
		('Espresso', 'Espresso'), 
		('Pink Lemonade', 'Pink Lemonade'), 
 		('Cheesecake Maple Bacon', 'Cheesecake Maple Bacon'), 
 		('Dark Chocolate', 'Dark Chocolate'), 
		('Milk Chocolate', 'Milk Chocolate'), 					
        ('Coconut Pecan', 'Coconut Pecan'), 
    ]

    COLORS = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Purple', 'Purple'),
        ('Green', 'Green'),
        ('Orange', 'Orange'),
        ('Yellow', 'Yellow'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='cupcakes')
    flavor = models.CharField(max_length=50, choices=FLAVOR_CHOICES)
    icing_flavor = models.CharField(max_length=50, choices=ICING_CHOICES)
    cupcake_color = models.CharField(max_length=20, choices=COLORS, blank=True, null=True)
    icing_color = models.CharField(max_length=20, choices=COLORS, blank=True, null=True)
    decorations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Cupcake #{self.id} for Order #{self.order.id}"

