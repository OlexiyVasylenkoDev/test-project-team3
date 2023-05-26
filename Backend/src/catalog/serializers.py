from django.db.models import Sum, When, Case
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from order.models import OrderItem
from catalog.models import Category, Product, CategoryAttribute, ProductAttribute


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


class ProductSerializer(serializers.ModelSerializer):
    count = serializers.DecimalField(max_digits=10, decimal_places=2)
    promo_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'category', 'count', 'image', 'base_price', 'promo_price', 'is_active']

    def get_promo_price(self, obj):
        return obj.price

    def get_top_sales(self, limit):
        # Отримуємо сумарну кількість продуктів замовлених по кожному товару
        top_sales = OrderItem.objects.values('goods').annotate(total_quantity=Sum('quantity')).order_by(
            '-total_quantity')[:limit]

        # Отримуємо ідентифікатори товарів з топ продажів
        top_product_ids = [sale['goods'] for sale in top_sales]

        # Отримуємо товари з бази даних, використовуючи ідентифікатори
        top_products = Product.objects.filter(id__in=top_product_ids).order_by(
            Case(*[When(id=id, then=pos) for pos, id in enumerate(top_product_ids)]))

        return top_products


class CategorySerializer(ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ["title", "product"]


class CategoryAttributeSerializer(ModelSerializer):
    class Meta:
        model = CategoryAttribute
        fields = "__all__"
