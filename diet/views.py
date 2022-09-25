from django.views.generic import ListView, DetailView

from .models import Ingredient


class IngList(ListView):
    model = Ingredient
    context_object_name = 'ing_list'
    template_name = 'diet/list.html'


class IngDetail(DetailView):
    model = Ingredient
    template_name = 'diet/charts.html'
