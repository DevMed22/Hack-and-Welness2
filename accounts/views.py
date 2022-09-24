from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm



class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("home")
    def form_valid(self, form):
        form.instance.bmi = form.instance.weight / ((form.instance.height/100)**2)
        form.instance.points = 0
        return super().form_valid(form)
