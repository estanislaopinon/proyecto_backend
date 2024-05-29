from rest_framework import serializers
from funko_api.models import Funko, Pokemon


class FunkoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funko
        # fields = ['name', 'number', 'collection', 'is_backlight']
        fields = '__all__'


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['name', 'number', 'type', 'subtype', 'level']
