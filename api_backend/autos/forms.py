from django import forms
from autos.models import Auto, Marca, Usuario, PropiedadAuto


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = [
            'nombre',
        ]


class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = [
            'marca',
            'modelo',
            'anio',
            'color',
        ]


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'autos',
        ]


class PropidedadAutoForm(forms.ModelForm):
    class Meta:
        model = PropiedadAuto
        fields = [
            'usuario',
            'auto',
            'fecha_adquisicion',
        ]
