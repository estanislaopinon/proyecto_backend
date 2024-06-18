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


def get_all_marca():
    marcas = Marca.objects.all().order_by('nombre')
    marcas_serializers = MarcaSerializer(marcas, many=True)
    return marcas_serializers.data


def get_all_usuario():
    usuarios = Usuario.objects.all().order_by('nombre')
    usuarios_serializers = UsuarioSerializer(usuarios, many=True)
    return usuarios_serializers.data


def get_all_propiedadAuto():
    propiedadauto = PropiedadAuto.objects.all().order_by('usuario')
    propiedadauto_serializers = PropiedadAutoSerializer(
        propiedadauto, many=True)
    return propiedadauto_serializers.data


def index_autos(request):
    autos = get_all_autos()
    return render(request, 'index_auto.html', {'autos': autos})
# Create your views here.


def index_marca(request):
    marcas = get_all_marca()
    return render(request, 'index_marca.html', {'marcas': marcas})


def index_usuario(request):
    usuarios = Usuario.objects.all().order_by('nombre')
    return render(request, 'index_usuario.html', {'usuarios': usuarios})


def index_propiedadauto(request):
    propiedadauto = PropiedadAuto.objects.all().order_by('usuario')
    return render(request, 'index_propiedad_auto.html', {'propiedadAuto': propiedadauto})


def autos_rest(request):
    autos = get_all_autos()
    return JsonResponse(autos, safe=False)


def marcas_rest(request):
    marcas = get_all_marca()
    return JsonResponse(marcas, safe=False)


def usuario_rest(request):
    usuarios = get_all_usuario()
    return JsonResponse(usuarios, safe=False)


def propiedadauto_rest(request):
    propiedadauto = get_all_propiedadAuto()
    return JsonResponse(propiedadauto, safe=False)


class NewAutoView(CreateView):
    form_class = AutoForm
    template_name = 'new_auto.html'
    success_url = '/index_auto/'


class NewMarcaView(CreateView):
    form_class = MarcaForm
    template_name = 'new_marca.html'
    success_url = '/index_marca/'


class NewUsuarioView(CreateView):
    form_class = UsuarioForm
    template_name = 'new_usuario.html'
    success_url = '/index_usuario/'


class NewPropiedadAutoView(CreateView):
    model = PropiedadAuto
    form_class = PropidedadAutoForm
    template_name = 'new_propiedadauto.html'
    success_url = '/index_propiedad_auto/'


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
