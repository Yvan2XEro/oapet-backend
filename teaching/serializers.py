from rest_framework import serializers
from .models import *


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
