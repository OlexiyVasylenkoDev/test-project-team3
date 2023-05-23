from rest_framework import serializers

from core.models import BuyerProfile
from order.models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    ordered_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    closed_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

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
    ordered_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    closed_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'address', 'ordered_at', 'closed_at', 'order_items']
