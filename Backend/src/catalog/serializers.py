from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from catalog.models import Category, Product, CategoryAttribute, ProductAttribute


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryAttributeSerializer(ModelSerializer):
    class Meta:
        model = CategoryAttribute
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    count = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Product
        fields = ["title", "description", "category", "count", "image", "price", "is_active", "attributes"]


class ProductAttributeSerializer(ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = "__all__"

    def validate(self, data):
        attribute = data["attribute"]
        product = data["product"]
        if product.category in attribute.category.all():
            return data
        raise serializers.ValidationError("The product doesn`t have such an attribute!")

