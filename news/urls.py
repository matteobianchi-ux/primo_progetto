from django.urls import path
from .views import home, ArticoloDetailView, listaArticoli

app_name='news'

urlpatterns=[
    path('', home, name="homeview"),
    path("articolo/<int:pk>", ArticoloDetailView, name="articolo_detail"),
    path('lista_articoli/', listaArticoli, name='lista_articoli'),
    path('lista_articoli/<int:pk>', listaArticoli, name='lista_articoli_giornalista'),
]