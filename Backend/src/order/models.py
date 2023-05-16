from django.db import models


class Order(models.Model):
    id = models.AutoField(primary_key=True, default=1000000)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    address = models.TextField()
    ordered_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(blank=True)


class OrderItem(models.Model):
    #goods
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
