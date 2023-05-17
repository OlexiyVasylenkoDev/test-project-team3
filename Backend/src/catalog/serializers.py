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

    # def create(self, validated_data):
    #     print(validated_data)
    #     items_data = validated_data
    #
    #     # similar to Parent.objects.create(**validated_data)
    #     parent = super().create(**validated_data)
    #
    #     for item_data in items_data:
    #         Product.objects.create(parent=parent, created_by=self.request.user, **item_data)
    #     return parent


class UpdateProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "description", "category", "count", "image", "price", "is_active"]


class ProductsByCategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ["title", ]
