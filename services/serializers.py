from re import search
from rest_framework import serializers
from .models import Service
from users.models import User
from appointments.models import Appointment
from users.serializers import UserSerializer
# from appointments.serializers import AppointmentSerializer
from feedbacks.models import Feedback
from feedbacks.serializers import FeedbackSerializer
from categories.models import Category
from categories.serializers import CategorySerializer
from blacklists.serializers import BlacklistSerializer
from blacklists.models import Blacklist
from wilayas.serializers import WilayaSerializer
from wilayas.models import Wilaya

from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class ServiceSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    clientBlacklisted = serializers.SerializerMethodField('getBlacklisted')
    appointments = serializers.SerializerMethodField('getAppointments')
    feedbacks = serializers.SerializerMethodField('getFeedbacks')
    service_category = serializers.SerializerMethodField('getCategory')
    service_wilaya = serializers.SerializerMethodField('getWilaya')

    def getBlacklisted(self, obj):
        return UserSerializer(User.objects.filter(client_blacklist__service=obj.id), many=True).data

    def getAppointments(self, obj):
        return AppointmentSerializer(Appointment.objects.filter(service=obj.id), many=True).data

    def getWilaya(self, obj):
        return WilayaSerializer(Wilaya.objects.filter(wilaya_service=obj.id)).data

    def getFeedbacks(self, obj):
        return FeedbackSerializer(Feedback.objects.filter(service=obj.id), many=True).data

    def getCategory(self, obj):
        return CategorySerializer(Category.objects.filter(category_services=obj.id), many=True).data

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
            'address',
            'longtitude',
            'latitude',
            'logo',
            'phone_number',
            'clientBlacklisted',
            'appointments',
            'feedbacks',
            'service_category',
            'service_wilaya',
            'created_date'
        )
        read_only_fields = ('is_validated', 'id',)


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
# TODO: return list of services where the current user is not blacklisted
