from .views import *
from django.urls import path

urlpatterns = [
    path('courses/<int:pk>/delete',
         DeleteViewTest.as_view({'delete': 'delete'})),
    path('courses/<int:pk>', CourseUpdateDeleteAPIView.as_view()),
    path('classes/', ClassListCreateAPIView.as_view()),
    path('classes/<int:pk>', ClassUpdateDeleteAPIView.as_view()),
    path('classes/<int:pk>/courses',
         CourseByClassviewset.as_view({'get': 'getCoursesByClass'})),
    path('teachers/<int:pk>/get-dashboard',
         TeacherDashBoard.as_view({'get': 'get'})),

]
