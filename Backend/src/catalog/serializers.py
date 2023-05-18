from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from catalog.models import Category, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "description", "category", "count", "image", "price", "is_active"]


