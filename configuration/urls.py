# WorkingDayListCreateAPIView
from .views import  *
from django.urls import path

urlpatterns = [
    path('configurations/', ConfigListCreateAPIView.as_view()),
    path('configurations/<int:pk>', ConfigUpdateDeleteAPIView.as_view()),
    path('configurations/defined-pauses', PauseListCreateAPIView.as_view()),
    path('configurations/defined-pause/<int:pk>', PauseUpdateDeleteAPIView.as_view()),
]
