from django import forms
from funko_api.models import Funko,  Athlete


class FunkoForm(forms.ModelForm):
    class Meta:
        model = Funko
        fields = [
            'name',
            'number',
            'collection',
            'is_backlight',
        ]


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = [
            'name',
            'sport_type',
            'nationality',
            'gender',
        ]
