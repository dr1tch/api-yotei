from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import BaseUserManager
from services.models import Service
# from services.serializers import ServiceSerializer
# from appointments.serializers import AppointmentSerializer
from appointments.models import Appointment
from feedbacks.models import Feedback
from categories.models import Category
from wilayas.models import Wilaya

from feedbacks.serializers import FeedbackSerializer
from categories.serializers import CategorySerializer
from wilayas.serializers import WilayaSerializer

from .models import User
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class UserSerializer(serializers.ModelSerializer):
    services = serializers.SerializerMethodField('getServices')
    feedbacks = serializers.SerializerMethodField('getFeedbacks')
    wilaya = serializers.SerializerMethodField('getWilaya')

    def getServices(self, obj):
        return ServiceSerializer(Service.objects.filter(owner=obj.id), many=True).data

    def getFeedbacks(self, obj):
        return FeedbackSerializer(Feedback.objects.filter(client=obj.id), many=True).data

    def getWilaya(self, obj):
        return WilayaSerializer(Wilaya.objects.filter(wilaya_user=obj.id), many=True).data

    class Meta:
        model = User
        # fields = '__all__'
        fields = (
            'id',
            'email',
            'username',
            'name',
            'description',
            'role',
            'wilaya',
            'address',
            'services',
            'feedbacks',
            'phone_number',
            'logo',
            'created_date',
        )


class ServiceSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    clientBlacklisted = serializers.SerializerMethodField('getBlacklisted')
    appointments = serializers.SerializerMethodField('getAppointments')
    feedbacks = serializers.SerializerMethodField('getFeedbacks')
    category = serializers.SerializerMethodField('getCategory')
    wilaya = serializers.SerializerMethodField('getWilaya')

    def getBlacklisted(self, obj):
        return UserSerializer(User.objects.filter(client_blacklist__service=obj.id), many=True).data

    def getAppointments(self, obj):
        return AppointmentSerializer(Appointment.objects.filter(service=obj.id), many=True).data

    def getCategory(self, obj):
        return CategorySerializer(Category.objects.filter(category_services=obj.id), many=True).data

    def getWilaya(self, obj):
        return WilayaSerializer(Wilaya.objects.filter(wilaya_service=obj.id), many=True).data

    def getFeedbacks(self, obj):
        return FeedbackSerializer(Feedback.objects.filter(service=obj.id), many=True).data

    class Meta:
        model = Service
        fields = (
            'id',
            'owner',
            'name',
            'description',
            'category',
            'is_validated',
            'tags',
            'wilaya',
            'visibility',
            'longtitude',
            'latitude',
            'address',
            'logo',
            'created_date',
            'phone_number',
            'clientBlacklisted',
            'appointments',
            'feedbacks',
        )
        read_only_fields = ('is_validated', 'id',)


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


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    client = serializers.SerializerMethodField('getUser')

    def getUser(self, obj):
        return UserSerializer(User.objects.filter(client_appointment=obj.id).first()).data

    class Meta:
        model = Appointment

        fields = (
            'id',
            'client',
            'service',
            'day',
            'start',
            'end',
            'status',
            'created_date'
        )
