from rest_framework import serializers
from .models import Service
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class ServiceSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

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
            'logo',
            'phone_number',
            # 'deleted',
            # 'created_date',
        )
        read_only_fields = ('is_validated', 'id',)