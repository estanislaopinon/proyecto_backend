from django.urls import path
from autos import views

urlpatterns = [
    path('index_auto/', views.index_autos, name='index_auto'),
    path('autos_rest/', views.autos_rest, name='autos_rest'),
    path('new_auto/', views.NewAutoView.as_view(), name='new_auto'),
    path('index_marca/', views.index_marca, name='index_marca'),
    path('marcas_rest/', views.marcas_rest, name='marcas_rest'),
    path('new_marca/', views.NewMarcaView.as_view(), name='new_marca'),
    # path('add_auto/', views.add_auto_view, name='add_auto'),
]
