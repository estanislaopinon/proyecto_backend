from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from funko_api.forms import FunkoForm, UserForm


from funko_api.models import Funko, User
from funko_api.serializers import FunkoSerializer, UserSerializer
from django.middleware.csrf import get_token

# Create your views here.


def get_all_funkos():
    funkos = Funko.objects.all().order_by('number')
    funkos_serializers = FunkoSerializer(funkos, many=True)
    return funkos_serializers.data


def index_funko(request):
    funkos = get_all_funkos()
    return render(request, 'index_funko.html', {'funkos': funkos})


def funkos_rest(request):
    funkos = get_all_funkos()
    return JsonResponse(funkos, safe=False)


def users_rest(request):
    return JsonResponse("OK", safe=False)


# def add_funko_view(request):

#     if request.method == 'POST':
#         funko_form = FunkoForm(request.POST)
#         if funko_form.is_valid():
#             funko = funko_form.save()
#             return redirect('index_funkos')
#     if request.method == 'GET':
#         funko_form = FunkoForm()
#         csrf_token = get_token(request)
#         html_form = f"""
#             <form method="post">
#             <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
#                 {funko_form.as_p()}
#                 <button type="submit">Submit</button>
#             </form>
#         """
#         return HttpResponse(html_form)


class NewFunkoView(CreateView):
    form_class = FunkoForm
    template_name = 'from_funko.html'
    success_url = '/index_funkos/'
# def add_user_view(request):

#     if request.method == 'POST':
#         user_form = UserForm(request.POST)
#         if user_form.is_valid():
#             user = user_form.save()
#             return HttpResponseRedirect('/')
#     if request.method == 'GET':
#         user_form = UserForm()
#         csrf_token = get_token(request)
#         html_form = f"""
#             <form method="post">
#             <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
#                 {user_form.as_p()}
#                 <button type="submit">Submit</button>
#             </form>
#         """
#         return HttpResponse(html_form)

# class NewUserView(CreateView):
#     form_class = UserForm
#     template_name = 'from_user.html'
#     success_url = '/users_rest/'


def index(request):
    funkos = get_all_funkos()
    return render(request, 'index.html', {'funkos': funkos})
