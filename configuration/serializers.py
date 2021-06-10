from rest_framework import serializers
from .models import *


class WorkingDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingDay
        fields = '__all__'
