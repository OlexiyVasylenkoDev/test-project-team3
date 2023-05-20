from rest_framework import serializers

from core.models import BuyerProfile
from order.models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(required=False)
    ordered_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'address', 'ordered_at', 'order_items']

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
                validated_data['first_name'] = profile.name
                validated_data['last_name'] = profile.surname
                validated_data['email'] = self.context['request'].user.email
                validated_data['phone'] = self.context['request'].user.phone
        return super().create(validated_data)