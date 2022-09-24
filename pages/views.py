from django.views.generic import TemplateView



class AboutPageView(TemplateView):
    template_name='pages/about.html'


class HomePageView(TemplateView):
    template_name='pages/home.html'    