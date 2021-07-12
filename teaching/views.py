from .models import *
from .serializers import *
from rest_framework import generics, viewsets
from rest_framework.response import Response


class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ClassListCreateAPIView(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class CourseByClassviewset(viewsets.ViewSet):
    def getCoursesByClass(Self, request, pk):
        querySet = Course.objects.all().filter(level_class=pk)
        serializer = CourseSerializer(querySet, many=True)
        return Response(serializer.data)
