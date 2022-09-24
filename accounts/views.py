from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm



class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("home")
