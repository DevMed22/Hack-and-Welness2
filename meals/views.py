from django.views.generic import ListView, DetailView
from .models import Meal




class MealsList(ListView):
    model = Meal
    context_object_name = "meals"
    template_name = 'meals/meals.html'



class MealDetail(DetailView):
    model = Meal
    template_name = 'meals/meal_detail.html'