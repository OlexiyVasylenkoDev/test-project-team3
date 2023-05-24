from rest_framework import serializers
from .models import User, SellerProfile


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["email", "phone", "type", "password"]

    def create(self, validated_data):
        try:
            User.objects.get(email=validated_data["email"])
            raise serializers.ValidationError({f"User with email - {validated_data['email']} - is already registered"})
        except User.DoesNotExist:
            user = User.objects.create_user(email=validated_data["email"],
                                            password=validated_data["password"],
                                            phone=validated_data["phone"],
                                            type=validated_data["type"])
            user.set_password(validated_data["password"])
            user.is_active = True
            user.save()
            return user


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = "__all__"
