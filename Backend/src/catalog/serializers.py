from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from catalog.models import Category, Product


class CategorySerializer(ModelSerializer):
    products = SerializerMethodField()

    def get_products(self, obj):
        return f"http://127.0.0.1:8000/api/v1/category/{obj.id}/products/"

    class Meta:
        model = Category
        fields = ["id", "title", "characteristics", "products"]


class ProductSerializer(ModelSerializer):
    count = serializers.DecimalField(max_digits=10, decimal_places=2)
    category_name = serializers.CharField(source='category.characteristics')

    class Meta:
        model = Product
        fields = ["title", "description", "category", "count", "image", "price", "is_active", "category_name"]
