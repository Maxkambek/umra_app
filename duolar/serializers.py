from rest_framework import serializers
from .models import UmraDuo


class UmraDuoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UmraDuo
        fields = ['id', 'name', 'audio', 'description']
