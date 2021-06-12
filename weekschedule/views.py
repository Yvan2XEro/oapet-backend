from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

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
        first_day = week.first_day
        n = config.get_working_days_count()
        dates = [first_day + datetime.timedelta(days=x) for x in range(n)]
        for date in dates:
            weekday = date.weekday()
            if flags_days[weekday]:
                d = Day()
                d.date = datetime.date(int(date.year), int(date.month), int(date.day))
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
        # serializer = WeekSerializer(week)
        k = datetime.date(int(dates[0].year), int(dates[0].month), int(dates[0].day))
        return Response({
            "test": str(k)
        })

