from security.models import User
from django.db import models

# Create your models here.


class Class(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    teaching_class = models.ForeignKey(to=Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(to=User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
