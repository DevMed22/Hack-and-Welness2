from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Hero


class SignUpForm(UserCreationForm):
    class Meta:
        model = Hero
        fields = (
            'username',
            'email',
            'name',
            'height',
            'weight',
        )


class SignUpChangeForm(UserChangeForm):
    class Meta:
        model = Hero
        fields = (
            'username',
            'email',
            'name',
            'height',
            'weight',
        )