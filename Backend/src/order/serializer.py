from rest_framework import serializers

from catalog.models import Product
from core.models import BuyerProfile
from order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

    def validate(self, data):
        product = data["goods"]
        attribute = data["quantity"]
        if product.count > int(attribute):
            return data
        raise serializers.ValidationError("Такої кількості товарів немає в наявності")


class OrderSerializer(serializers.ModelSerializer):
    ordered_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    closed_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    orderitem_set = OrderItemSerializer(read_only=True, many=True)
    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'address', 'ordered_at', 'closed_at', 'orderitem_set']

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method == 'POST' and request.user.is_authenticated:
            fields['first_name'].required = False
            fields['last_name'].required = False
            fields['email'].required = False
            fields['phone'].required = False
        if request and request.method == 'PUT':
            # Поле необов'язкове при оновленні
            fields['first_name'].required = False
            fields['last_name'].required = False
            fields['email'].required = False
            fields['phone'].required = False
            fields['address'].required = False
            fields['orderitem_set'].required = False
        return fields

    def validate(self, attrs):
        if not self.context['request'].user.is_authenticated:
            if not attrs.get('first_name'):
                raise serializers.ValidationError("First name is required.")
            if not attrs.get('last_name'):
                raise serializers.ValidationError("Last name is required.")
            if not attrs.get('email'):
                raise serializers.ValidationError("Email is required.")
            if not attrs.get('phone'):
                raise serializers.ValidationError("Phone is required.")
        return attrs

    def create(self, validated_data):
        if self.context['request'].user.is_authenticated:
            profile = BuyerProfile.objects.filter(user=self.context['request'].user).first()
            if profile:
                validated_data.setdefault('first_name', profile.name)
                validated_data.setdefault('last_name', profile.surname)
                validated_data.setdefault('email', self.context['request'].user.email)
                validated_data.setdefault('phone', self.context['request'].user.phone)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class OrderUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    order_items = OrderItemSerializer(many=True, read_only=True)
    ordered_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    closed_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'address', 'ordered_at', 'closed_at', 'order_items']

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method == 'POST' and request.user.is_authenticated:
            fields['first_name'].required = False
            fields['last_name'].required = False
            fields['email'].required = False
            fields['phone'].required = False
        if request and request.method == 'PUT':
            # Поле необов'язкове при оновленні
            fields['first_name'].required = False
            fields['last_name'].required = False
            fields['email'].required = False
            fields['phone'].required = False
            fields['address'].required = False
            fields['order_items'].required = False
        return fields

    def update(self, instance, validated_data):
        if validated_data["closed_at"]:
            for i in OrderItem.objects.filter(order=instance):
                order_item = OrderItem.objects.filter(pk=i.id).first()
                product = Product.objects.filter(pk=order_item.product.pk).first()

                product.count -= order_item.quantity
                product.save()

        return super().update(instance, validated_data)
