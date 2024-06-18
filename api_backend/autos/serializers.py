from rest_framework import serializers
from autos.models import Marca, Auto, Usuario, PropiedadAuto


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        # fields = ['name', 'number', 'collection', 'is_backlight']
        fields = ['nombre']


class AutoSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()

    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'anio', 'color']


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre', 'autos']


class PropiedadAutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropiedadAuto
        fields = ['usuario', 'auto', 'fecha_adquisicion']
