from django.http import response
from weekschedule.serializers import PeriodSerializer
from weekschedule.models import Period
from .models import *
from .serializers import *
from rest_framework import generics, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


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


class TeacherDashBoard(viewsets.ViewSet):
    def get(self, request, pk):
        teacher = get_object_or_404(User, pk=pk)
        courses = Course.objects.all().filter(teacher=pk)
        response = []
        for c in courses:
            course_serializer = CourseSerializer(c)
            periods = Period.objects.all().filter(occupied_by=c.pk)
            period_serializer = PeriodSerializer(periods, many=True)
            response.append({
                "cours": course_serializer.data,
                "periods": period_serializer.data
            })
        return Response(response)


class DeleteViewTest(viewsets.ViewSet):
    def delete(self, request, pk):
        c = get_object_or_404(Course, pk=pk)
        c.delete()
        return Response({"message": "success"})
