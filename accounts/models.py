from django.db import models
from django.contrib.auth.models import AbstractUser

class Hero(AbstractUser):
    name = models.CharField(max_length=200)
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    bmi = models.PositiveIntegerField()
    points = models.PositiveIntegerField()