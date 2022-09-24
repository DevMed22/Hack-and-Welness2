from django.views.generic import TemplateView, ListView
from accounts.models import Hero


class AboutPageView(TemplateView):
    template_name='pages/about.html'


class HomePageView(ListView):
    model = Hero
    context_object_name = 'heros_list'
    template_name='pages/home.html'   
    def get_queryset(self):
        heros_list = Hero.objects.all().order_by('-points')
        return heros_list