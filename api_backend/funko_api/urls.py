from django.urls import path
from funko_api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('funkos_rest/', views.funkos_rest, name='funkos_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
    path('add_funko/', views.add_funko_view, name='add_funko'),
    path('add_user/', views.add_user_view, name='add_user'),
    path('pokemons_rest/', views.pokemons_rest, name='pokemons_rest'),
    path('athlete_rest/', views.athlete_rest, name='athlete_rest')
]
