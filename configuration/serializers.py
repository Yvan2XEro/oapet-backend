from rest_framework import serializers
from .models import *


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'


class PauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pause
        fields = '__all__'
