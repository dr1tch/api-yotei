from re import search
from rest_framework import serializers
from .models import Service
from users.models import User
from appointments.models import Appointment
from users.serializers import UserSerializer
from appointments.serializers import AppointmentSerializer
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class ServiceSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    clientBlacklisted = serializers.SerializerMethodField('getBlacklisted')
    serviceAppointments = serializers.SerializerMethodField('getAppointments')

    def getBlacklisted(self, obj):
        return UserSerializer(User.objects.filter(client_blacklist__service=obj.id), many=True).data

    def getAppointments(self, obj):
        return AppointmentSerializer(Appointment.objects.filter(service=obj.id), many=True).data

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
            'serviceAppointments',
        )
        read_only_fields = ('is_validated', 'id',)
