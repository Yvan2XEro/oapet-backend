from django.db import models
import datetime
from configuration.models import Config


class Week(models.Model):
    first_day = models.DateField(null=False)
    last_day = models.DateField(null=True)
    is_ok = models.BooleanField(default=False)
    is_generated = models.BooleanField(default=False)
    configurations = models.ForeignKey(Config, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.first_day)


class Day(models.Model):
    date = models.DateField(null=False)
    begin_at = models.IntegerField(default=Config.DEFAULT_HOUR_BEGINING_DAY)
    end_at = models.IntegerField(default=Config.DEFAULT_HOUR_ENDING_DAY)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)


class Period(models.Model):
    hour_begin = models.IntegerField(null=False)
    hour_end = models.IntegerField(null=True)
    is_pause = models.BooleanField(default=False)
    is_occupied = models.BooleanField(default=False)
    was_occupied = models.BooleanField(default=False)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.hour_begin)+"-"+str(self.hour_end)
