from django.urls import path
from autos import views

urlpatterns = [
    path('index_auto/', views.index, name='index_auto'),
    path('autos_rest/', views.autos_rest, name='autos_rest'),
    path('new_auto/', views.NewAutoView.as_view(), name='new_auto'),
    # path('add_auto/', views.add_auto_view, name='add_auto'),
]
