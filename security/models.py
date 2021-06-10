from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    phone = models.CharField(max_length=20, null=True)

    email = models.CharField(max_length=255, unique=True, verbose_name='email')

    REQUIRED_FIELDS = ['phone', 'username', 'first_name', 'last_name']

    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


class Teacher(User):

    teacher_matricule = models.CharField(max_length=255, primary_key=True)


# Create your models here.
