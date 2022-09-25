from django.db import models
from django.urls import reverse


class Meal(models.Model):
    name = models.CharField(max_length=150)
    MEALS = (
        ('Breakfast','BF'),
        ('Lunch','L'),
        ('Dinner', 'D')
    )
    category = models.CharField(max_length=100, choices=MEALS)
    thumb = models.ImageField(blank=True, null=True)
    plate = models.TextField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('meal', kwargs={'pk':self.pk})
