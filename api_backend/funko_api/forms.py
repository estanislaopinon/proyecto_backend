from django import forms
from funko_api.models import Funko, Pokemon, Athlete


class FunkoForm(forms.ModelForm):
    class Meta:
        model = Funko
        fields = [
            'name',
            'number',
            'collection',
            'is_backlight',
        ]


class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = [
            'name',
            'number',
            'type',
            'subtype',
            'level',
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
