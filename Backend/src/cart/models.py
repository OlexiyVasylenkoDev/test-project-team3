from django.contrib.auth import get_user_model
from django.db import models
from catalog.models import Product


class Cart(models.Model):
    goods = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_goods')


class WishList(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, name="wishlist_user")
    goods = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlist_goods')
