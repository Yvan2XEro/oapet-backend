from django.db import models


class Config(models.Model):
    period_duration = models.IntegerField(default=60)
    pause_duration = models.IntegerField(default=30)
    Monday = models.BooleanField(default=True)
    Tuesday = models.BooleanField(default=True)
    Wdnesday = models.BooleanField(default=True)
    Thursday = models.BooleanField(default=True)
    Friday = models.BooleanField(default=True)
    Saturday = models.BooleanField(default=True)
    Sunday = models.BooleanField(default=True)
