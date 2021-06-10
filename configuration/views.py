from .models import Config
from .serializers import *
from rest_framework import generics


class ConfigListCreateAPIView(generics.ListCreateAPIView):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer


class ConfigUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer
