from .models import *
from .serializers import *
from rest_framework import generics


class WorkingDayListCreateAPIView(generics.ListCreateAPIView):
    queryset = WorkingDay.objects.all()
    serializer_class = WorkingDaySerializer


class WorkingDayUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkingDay.objects.all()
    serializer_class = WorkingDaySerializer
