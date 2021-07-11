from .views import *
from django.urls import path

urlpatterns = [
    path('courses/', CourseListCreateAPIView.as_view()),
    path('courses/<int:pk>', CourseUpdateDeleteAPIView.as_view()),
    path('classes/', ClassListCreateAPIView.as_view()),
    path('classes/<int:pk>', ClassUpdateDeleteAPIView.as_view()),
]
