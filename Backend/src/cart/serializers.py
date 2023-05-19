from rest_framework.serializers import ModelSerializer

from cart.models import Cart, WishList


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class WishlistSerializer(ModelSerializer):
    class Meta:
        model = WishList
        fields = ["goods", ]
