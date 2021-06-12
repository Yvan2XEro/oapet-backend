from django.db import models


class Pause(models.Model):
    begin_at = models.IntegerField(null=False)
    end_at = models.IntegerField(null=True)

    def __str__(self):
        return str(self.begin_at)


class Config(models.Model):
    DEFAULT_PERIOD_DURATION = 1
    DEFAULT_PAUSE_DURATION = 1
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

    def get_flags_days(self):
        return [self.Monday, self.Tuesday, self.Wednesday, self.Thursday, self.Friday, self.Saturday, self.Sunday]

    def get_working_days_count(self):
        oping_days = self.get_flags_days()
        i = 0
        for flag in oping_days:
            if flag:
                i += 1
        return i
