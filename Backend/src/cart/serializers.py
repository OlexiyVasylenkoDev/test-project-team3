from rest_framework.serializers import ModelSerializer, ReadOnlyField

from cart.models import Cart, CartItem, WishList


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartItemSerializer(ModelSerializer):
    price = ReadOnlyField()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'cart', 'quantity', 'price']


class WishlistSerializer(ModelSerializer):
    class Meta:
        model = WishList
        fields = ["goods", ]
