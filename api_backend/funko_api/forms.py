from django import forms
from funko_api.models import Funko, User, Athlete


class FunkoForm(forms.ModelForm):
    class Meta:
        model = Funko
        fields = [
            'name',
            'number',
            'collection',
            'is_backlight',
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'funkos'
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
