from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse
from autos.models import Auto, Marca, Usuario, PropiedadAuto
from autos.forms import AutoForm, MarcaForm, UsuarioForm, PropidedadAutoForm
from autos.serializers import MarcaSerializer, AutoSerializer, UsuarioSerializer, PropiedadAutoSerializer
from django.middleware.csrf import get_token


def get_all_autos():
    autos = Auto.objects.all().order_by('modelo')
    autos_serializers = AutoSerializer(autos, many=True)
    return autos_serializers.data


def index(request):
    autos = get_all_autos()
    return render(request, 'index_auto.html', {'autos': autos})
# Create your views here.


def autos_rest(request):
    autos = get_all_autos()
    return JsonResponse(autos, safe=False)


class NewAutoView(CreateView):
    form_class = AutoForm
    template_name = 'new_auto.html'
    success_url = '/index_auto/'

# def add_auto_view(request):

#     if request.method == 'POST':
#         auto_form = AutoForm(request.POST)
#         if auto_form.is_valid():
#             auto = auto_form.save()
#             return redirect('index_auto')
#     if request.method == 'GET':
#         auto_form = AutoForm()
#         csrf_token = get_token(request)
#         html_form = f"""
#             <form method="post">
#             <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
#                 {auto_form.as_p()}
#                 <button type="submit">Submit</button>
#             </form>
#         """
#         return HttpResponse(html_form)
