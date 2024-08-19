from django.urls import path

from . import views

app_name = 'encuesta'

urlpatterns = [
    #path('', views.index, name='index'),
    #path('enviar', views.enviar, name='enviar'),
    #path('', views.tomar_datos, name='tomar_datos'),
    #path('operador', views.operador, name='operador'),
    path('', views.VolumenCilindro, name='VolumenCilindro'),
    path('volumen', views.calcular, name='calcular'),
]
