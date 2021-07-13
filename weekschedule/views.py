from teaching.serializers import CourseSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from security.models import User
from security.serializers import UserCreateSerializer

import datetime


class PeriodListCreateAPIView(generics.ListCreateAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer


class PeriodUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer


class DayListCreateAPIView(generics.ListCreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class DayUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class WeekListCreateAPIView(generics.ListCreateAPIView):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer


class WeekUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer


class ScheduleGenratorView(APIView):

    def get(self, request, pk, Format=None):
        week = get_object_or_404(Week, pk=pk)
        serializer = WeekSerializer(week)
        return Response(serializer.data)

    def post(self, request, pk, Format=None):
        week = get_object_or_404(Week, pk=pk)
        config = week.configurations
        begin_day_at = config.begin_at
        end_day_at = config.end_at
        period_duration = config.period_duration
        pause_duration = config.pause_duration
        pauses = config.pauses.all()

        flags_days = config.get_flags_days()
        delta = week.last_day - week.first_day
        dates = [week.first_day +
                 datetime.timedelta(days=x) for x in range(delta.days)]
        if week.is_generated == False:
            for date in dates:
                weekday = date.weekday()
                if flags_days[weekday]:
                    d = Day()
                    d.date = datetime.date(
                        int(date.year), int(date.month), int(date.day))
                    d.week = week
                    d.save()

                    next_period_begin = begin_day_at
                    while next_period_begin < end_day_at:
                        period = Period()
                        period.hour_begin = next_period_begin
                        if next_period_begin not in [p.begin_at for p in pauses]:
                            next_period_begin += period_duration
                        else:
                            next_period_begin += pause_duration
                            period.is_pause = True
                        period.hour_end = next_period_begin
                        period.day = d
                        period.save()
            week.is_generated = True
            week.save()

        serializer = WeekSerializer(week)
        return Response(serializer.data)


class DaysByWeekViewSet(viewsets.ViewSet):
    def getDaysByWeekId(self, request, pk):
        queryset = Day.objects.all().filter(week=pk)
        serializer = DaySerializer(queryset, many=True)
        return Response(serializer.data)


class PeriodByDayViewSet(viewsets.ViewSet):
    def getPeriodsByDayId(self, request, pk):
        queryset = Period.objects.all().filter(day=pk)
        serializer = PeriodSerializer(queryset, many=True)
        return Response(serializer.data)


class DaysAndPeriodsViewSet(viewsets.ViewSet):
    def getDaysAndPeriodsByWeekId(self, request, pk):
        days = Day.objects.all().filter(week=pk)
        days_ad_periods = []
        for day in days:
            day_serializer = DaySerializer(day)
            period_serializer = PeriodSerializer(
                Period.objects.all().filter(day=day.id), many=True)
            days_ad_periods.append({
                "day": day_serializer.data,
                "periods":  period_serializer.data
            })
        return Response(days_ad_periods)

    def getCourseAndTeacherByPeriod(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        teacher = get_object_or_404(User, pk=course.teacher.id)
        course_serializer = CourseSerializer(course)
        teacher_serializer = UserCreateSerializer(teacher)
        return Response({
            "course": course_serializer.data,
            "teacher": teacher_serializer.data
        })
