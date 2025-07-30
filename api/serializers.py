from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    class Meta:
        model = User
        fields = ['username', 'password']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already taken.")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['user']

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("User does not exist")

        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect password")

        if not user.is_active:
            raise serializers.ValidationError("User account is inactive")

        return super().validate(attrs)
