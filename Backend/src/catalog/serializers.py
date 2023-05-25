from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from decimal import Decimal

from catalog.models import Category, Product
from promotions.models import Promotion, ProductsOnPromotions


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    promo_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'category', 'count', 'image', 'price', 'promo_price', 'is_active']


    def get_promo_price(self, obj):
        try:
            promo_product = Promotion.products_on_promotion.through.objects.get(
                Q(promotion_id__is_active=True) & Q(product_id=obj.id)
            )
            return str(promo_product.promo_price)
        except ObjectDoesNotExist:
            return None
