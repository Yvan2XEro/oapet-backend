# WorkingDayListCreateAPIView
from .views import  *
from django.urls import path, include

urlpatterns = [
    path('configurations/', ConfigListCreateAPIView.as_view()),
    path('configurations/<int:pk>', ConfigUpdateDeleteAPIView.as_view()),
    path('working-days', WorkingDayListCreateAPIView.as_view()),
    path('working-days/<pk>', WorkingDayUpdateDeleteAPIView.as_view()),
]
