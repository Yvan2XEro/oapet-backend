from .models import *
from .serializers import *
from rest_framework import generics


class ConfigListCreateAPIView(generics.ListCreateAPIView):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer


class ConfigUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer


class WorkingDayListCreateAPIView(generics.ListCreateAPIView):
    queryset = WorkingDay.objects.all()
    serializer_class = WorkingDaySerializer


class WorkingDayUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkingDay.objects.all()
    serializer_class = WorkingDaySerializer
