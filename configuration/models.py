from django.db import models


class Pause(models.Model):
    begin_at = models.IntegerField(null=False)
    end_at = models.IntegerField(null=True)

    def __str__(self):
        return str(self.begin_at)


class Config(models.Model):
    # duree d'une periode et pause
    period_duration = models.IntegerField(default=60)
    pause_duration = models.IntegerField(default=30)
    # Heure de debut et de fin d'une journee
    begin_at = models.IntegerField(default=8)
    end_at = models.IntegerField(default=18)

    # Les jours ouvrables
    Monday = models.BooleanField(default=True)
    Tuesday = models.BooleanField(default=True)
    Wednesday = models.BooleanField(default=True)
    Thursday = models.BooleanField(default=True)
    Friday = models.BooleanField(default=True)
    Saturday = models.BooleanField(default=True)
    Sunday = models.BooleanField(default=False)

    pauses = models.ManyToManyField(Pause)
