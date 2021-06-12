from .views import *
from django.urls import path

urlpatterns = [
    path('periods/', PeriodListCreateAPIView.as_view()),
    path('periods/<int:pk>', PeriodUpdateDeleteAPIView.as_view()),
    path('days/', DayListCreateAPIView.as_view()),
    path('days/<int:pk>', DayUpdateDeleteAPIView.as_view()),
    path('weeks/', WeekListCreateAPIView.as_view()),
    path('weeks/<int:pk>/generate-schedule', ScheduleGenratorView.as_view()),
    path('weeks/<int:pk>/', WeekUpdateDeleteAPIView.as_view()),
]
