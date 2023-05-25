from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from catalog.models import Product
from core.validators import validate_product_price

class Order(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In progress'),
        ('delivering', 'Delivering'),
        ('canceled', 'Canceled'),
        ('closed', 'Closed')
    ]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = PhoneNumberField(("phone"))
    address = models.TextField()
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES)
    closed_at = models.DateTimeField(null=True)
    total_sum = models.DecimalField(max_digits=14, decimal_places=2, validators=[validate_product_price, ])

    def __str__(self):
        return "Order#" + str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.order} - {self.product.title}"

    @property
    def price(self):
        return self.product.price * self.quantity
