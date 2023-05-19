from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from catalog.models import Category, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    count = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Product
        fields = ["title", "description", "category", "count", "image", "price", "is_active"]
