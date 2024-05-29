from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from funko_api.forms import FunkoForm, PokemonForm, AthleteForm


from funko_api.models import Funko, Pokemon, Athlete
from funko_api.serializers import FunkoSerializer, PokemonSerializer, AthleteSerializer
from django.middleware.csrf import get_token

# Create your views here.


def get_all_funkos():
    funkos = Funko.objects.all().order_by('number')
    funkos_serializers = FunkoSerializer(funkos, many=True)
    return funkos_serializers.data


# def index(request):
#    funkos = get_all_funkos()
#    return render(request, 'index.html', {'funkos': funkos})


def funkos_rest(request):
    funkos = get_all_funkos()
    return JsonResponse(funkos, safe=False)


def users_rest(request):
    return JsonResponse("OK", safe=False)


def add_funko_view(request):

    if request.method == 'POST':
        funko_form = FunkoForm(request.POST)
        if funko_form.is_valid():
            funko = funko_form.save()
            return HttpResponseRedirect('/')
    if request.method == 'GET':
        funko_form = FunkoForm()
        csrf_token = get_token(request)
        html_form = f"""
            <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                {funko_form.as_p()}
                <button type="submit">Submit</button>
            </form>
        """
        return HttpResponse(html_form)

# ------! POKEMONS !---------


def get_all_pokemons():
    pokemons = Pokemon.objects.all().order_by('name')
    pokemons_serializers = PokemonSerializer(pokemons, many=True)
    return pokemons_serializers.data


def index(request):
    athlete = get_all_athlete()
    funkos = get_all_funkos()
    pokemons = get_all_pokemons()
    return render(request, 'index.html', {'pokemons': pokemons, 'funkos': funkos, 'athlete': athlete})


def pokemons_rest(request):
    pokemons = get_all_pokemons()
    return JsonResponse(pokemons, safe=False)


def get_all_athlete():
    athlete = Athlete.objects.all().order_by('nationality')
    athlete_serializers = AthleteSerializer(athlete, many=True)
    return athlete_serializers.data


def athlete_rest(request):
    athlete = get_all_athlete()
    return JsonResponse(athlete, safe=False)
