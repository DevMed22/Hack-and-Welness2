from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    energy = models.DecimalField(decimal_places=3, max_digits=6)
    protien = models.DecimalField(decimal_places=3, max_digits=6)
    fat = models.DecimalField(decimal_places=3, max_digits=6)
    carbo = models.DecimalField(decimal_places=3, max_digits=6)
    cl = models.DecimalField(decimal_places=3, max_digits=6)
    iron = models.DecimalField(decimal_places=3, max_digits=6)
    sodium = models.DecimalField(decimal_places=3, max_digits=6)
    vA = models.DecimalField(decimal_places=3, max_digits=6)
    
    vB1 = models.DecimalField(decimal_places=3, max_digits=6)
    vB2 = models.DecimalField(decimal_places=3, max_digits=6)
    vC = models.DecimalField(decimal_places=3, max_digits=6)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self): 
        return reverse('ing', kwargs={'pk': self.pk})