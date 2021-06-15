from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import BaseUserManager

from .models import User



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'name',
            'description',
            'role',
            'wilaya',
            'address',
            'phone_number',
            'logo',
            'created_date',
        )
        depth = 1

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password',
            'name',
            'description',
            'wilaya',
            'role',
            'address',
            'phone_number',
            'logo',
        )

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError("Email already exists!")
        return BaseUserManager.normalize_email(value)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user

class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError(
                'Current password does not match')
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value

# class ReturnUserSerializer(serializers.Serializer):
#     key = serializers.CharField()
#     def get(self, data):
#         user_id = Token.objects.get(key=data).user_id
#         user = User.objects.get(id=user_id)
#         return user