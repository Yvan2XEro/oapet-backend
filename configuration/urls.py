# WorkingDayListCreateAPIView
from .views import  *
from django.urls import path, include

urlpatterns = [
    path('', WorkingDayListCreateAPIView.as_view()),
    path('<int:pk>', WorkingDayUpdateDeleteAPIView.as_view())
]
