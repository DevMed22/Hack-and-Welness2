from django.db import models
from django.contrib.auth.models import AbstractUser

class Hero(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    height = models.DecimalField(decimal_places=2, max_digits=5,null=True, blank=True)
    weight = models.DecimalField(decimal_places=2, max_digits=5,null=True, blank=True)
    bmi = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    points = models.PositiveIntegerField(null=True, blank=True)
    Breakfast = models.BooleanField(null=True, blank=True)
    Dinner = models.BooleanField(null=True, blank=True)
    Lunch = models.BooleanField(null=True, blank=True)
    Workouthome = models.BooleanField(null=True, blank=True)
    Run = models.BooleanField(null=True, blank=True)
    SleepEarly = models.BooleanField(null=True, blank=True)
    WakeEarly = models.BooleanField(null=True, blank=True)
    Gym = models.BooleanField(null=True, blank=True)