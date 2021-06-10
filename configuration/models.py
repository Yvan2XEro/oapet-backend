from django.db import models


class WorkingDay(models.Model):
    name = models.CharField(max_length=255, primary_key=True, unique=True)

    def __str__(self):
        return self.name


class Config(models.Model):
    period_duration = models.IntegerField(default=60)
    pause_duration = models.IntegerField(default=30)
    workings_days = models.ManyToManyField(to=WorkingDay)
