from rest_framework import serializers
from autos.models import Marca, Auto, Usuario, PropiedadAuto


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        # fields = ['name', 'number', 'collection', 'is_backlight']
        fields = '__all__'


class AutoSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()

    class Meta:
        model = Auto
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class PropiedadAutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropiedadAuto
        fields = '__all__'
