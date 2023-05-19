from django.db import models
from catalog.models import Product
from phonenumber_field.modelfields import PhoneNumberField


class OrderItem(models.Model):
    goods = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_item_goods')
    quantity = models.IntegerField(default=1)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = PhoneNumberField(("phone"))
    address = models.TextField()
    ordered_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True)
    order_items = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='order_items')
