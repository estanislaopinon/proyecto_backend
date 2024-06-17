from django import forms
from pokemon.models import Pokemon


class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = [
            'name',
            'number',
            'type',
            # 'subtype',
            'level',
        ]
