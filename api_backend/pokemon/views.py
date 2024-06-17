from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from pokemon.forms import PokemonForm
from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer
from django.middleware.csrf import get_token


def get_all_pokemons():
    pokemons = Pokemon.objects.all().order_by('name')
    pokemons_serializers = PokemonSerializer(pokemons, many=True)
    return pokemons_serializers.data


def pokemons_rest(request):
    pokemons = get_all_pokemons()
    return JsonResponse(pokemons, safe=False)


def index_pokemon(request):
    pokemons = get_all_pokemons()
    return render(request, 'index_pokemon.html', {'pokemons': pokemons})
# Create your views here.
