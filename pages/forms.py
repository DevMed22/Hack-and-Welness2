from django import forms
from accounts.models import Hero

class CheckForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = (
            'Breakfast',
            'Dinner',
            'Lunch',
            'Workouthome',
            'WakeEarly',
            'SleepEarly',
            'Run',
            'Gym'
        )