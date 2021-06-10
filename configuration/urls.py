# WorkingDayListCreateAPIView
from .views import  *
from django.urls import path

urlpatterns = [
    path('configurations/', ConfigListCreateAPIView.as_view()),
    path('configurations/<int:pk>', ConfigUpdateDeleteAPIView.as_view()),
]
