from django import forms
from funko_api.models import Funko, User


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
