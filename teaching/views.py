from .models import *
from .serializers import *
from rest_framework import generics


class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursSerializer


class CourseUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursSerializer


class ClassListCreateAPIView(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
