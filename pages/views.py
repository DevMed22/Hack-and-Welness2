from django.views.generic import TemplateView, ListView, FormView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from accounts.models import Hero
from .forms import CheckForm


class AboutPageView(TemplateView):
    template_name='pages/about.html'


class HomePageView(ListView):
    model = Hero
    context_object_name = 'heros_list'
    template_name='pages/home.html'   
    def get_queryset(self):
        heros_list = Hero.objects.all().order_by('-points')
        return heros_list


class CheckList(DetailView, FormView):
    model = Hero
    form_class = CheckForm
    template_name = 'pages/check_list.html'
    success_url = reverse_lazy("home")
    def form_valid(self,form):
        if form.instance.Breakfast:
            k = Hero.objects.get(id=self.request.user.id)
            q = k.points
            q += 10
            Hero.objects.filter(id=self.request.user.id).update(points= q)
        if form.instance.Dinner:
            k = Hero.objects.get(id=self.request.user.id)
            q = k.points
            q += 10
            Hero.objects.filter(id=self.request.user.id).update(points= q)
        if form.instance.Lunch:
            k = Hero.objects.get(id=self.request.user.id)
            q = k.points
            q += 10
            Hero.objects.filter(id=self.request.user.id).update(points= q)
        if form.instance.Run:
            k = Hero.objects.get(id=self.request.user.id)
            q = k.points
            q += 10
            Hero.objects.filter(id=self.request.user.id).update(points= q)
        if form.instance.WakeEarly:
            k = Hero.objects.get(id=self.request.user.id)
            q = k.points
            q += 10
            Hero.objects.filter(id=self.request.user.id).update(points= q)
        if form.instance.SleepEarly:
            k = Hero.objects.get(id=self.request.user.id)
            q = k.points
            q += 10
            Hero.objects.filter(id=self.request.user.id).update(points= q)
        if form.instance.Workouthome:
            k = Hero.objects.get(id=self.request.user.id)
            q = k.points
            q += 10
            Hero.objects.filter(id=self.request.user.id).update(points= q)
        if form.instance.Gym:
            k = Hero.objects.get(id=self.request.user.id)
            q = k.points
            q += 10
            Hero.objects.filter(id=self.request.user.id).update(points= q)
        
        return redirect("home")