from django.contrib.auth import get_user_model
from django.db import models
from catalog.models import Product

class WishList(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, name="wishlist_user")
    goods = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlist_goods')


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        cart_items = self.cart_items.all()
        total = sum([item.price for item in cart_items])
        return total

    @property
    def num_of_items(self):
        cart_items = self.cart_items.all()
        quantity = sum([item.quantity for item in cart_items])
        return quantity


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE, related_name="cart_items")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.title

    @property
    def price(self):
        return self.product.price * self.quantity
