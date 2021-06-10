from rest_framework import serializers
from .models import *


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'
