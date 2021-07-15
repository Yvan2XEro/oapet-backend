from .views import *
from django.urls import path

urlpatterns = [
    path('periods/', PeriodListCreateAPIView.as_view()),
    path('periods/<int:pk>', PeriodUpdateDeleteAPIView.as_view()),
    path('days/', DayListCreateAPIView.as_view()),
    path('days/<int:pk>', DayUpdateDeleteAPIView.as_view()),
    path('days/<int:pk>/periods',
         PeriodByDayViewSet.as_view({'get': 'getPeriodsByDayId'})),
    path('weeks/', WeekListCreateAPIView.as_view()),
    path('weeks/<int:pk>/generate-schedule', ScheduleGenratorView.as_view()),
    path('weeks/<int:pk>/', WeekUpdateDeleteAPIView.as_view()),
    path('weeks/<int:pk>/days',
         DaysByWeekViewSet.as_view({'get': 'getDaysByWeekId'})),
    path('weeks/<int:pk>/days-perriods',
         DaysAndPeriodsViewSet.as_view({'get': 'getDaysAndPeriodsByWeekId'})),
    path('periods/<int:pk>/course-and-teacher',
         DaysAndPeriodsViewSet.as_view({'get': 'getCourseAndTeacherByPeriod'})),
    path('classes/<int:pk>/weeks',
         WeekShedulesByClassId.as_view({'get': 'get'})),
]
