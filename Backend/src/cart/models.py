from django.db import models
from catalog.models import Product


class Cart(models.Model):
    goods = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_goods')


class WishList(models.Model):
    № user = models.ForeignKey
    goods = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlist_goods')
