from django.db import models


class Pause(models.Model):
    begin_at = models.IntegerField(null=False)
    end_at = models.IntegerField(null=True)

    def __str__(self):
        return str(self.begin_at)


class Config(models.Model):
    DEFAULT_PERIOD_DURATION = 60
    DEFAULT_PAUSE_DURATION = 30
    DEFAULT_HOUR_BEGINING_DAY = 8
    DEFAULT_HOUR_ENDING_DAY = 18
    # duree d'une periode et pause
    period_duration = models.IntegerField(default=DEFAULT_PERIOD_DURATION)
    pause_duration = models.IntegerField(default=DEFAULT_PAUSE_DURATION)
    # Heure de debut et de fin d'une journee
    begin_at = models.IntegerField(default=DEFAULT_HOUR_BEGINING_DAY)
    end_at = models.IntegerField(default=DEFAULT_HOUR_ENDING_DAY)

    # Les jours ouvrables
    Monday = models.BooleanField(default=True)
    Tuesday = models.BooleanField(default=True)
    Wednesday = models.BooleanField(default=True)
    Thursday = models.BooleanField(default=True)
    Friday = models.BooleanField(default=True)
    Saturday = models.BooleanField(default=True)
    Sunday = models.BooleanField(default=False)

    pauses = models.ManyToManyField(Pause)
