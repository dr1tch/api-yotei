from django.db import models
from rest_framework import serializers
from .models import Blacklist


class BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blacklist
        fields = '__all__'
