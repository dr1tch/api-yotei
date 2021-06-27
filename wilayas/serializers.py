from rest_framework import serializers
from .models import Wilaya

class WilayaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wilaya
        fields = ('id', 'name')
        read_only_fields = ('id', 'name')