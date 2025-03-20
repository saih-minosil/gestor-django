"""
URL configuration for gestor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from . import requests

urlpatterns = [
    path('',views.mapa),
    path('mapas',views.mapa),
    path('estacion/<str:codigo_estacion_txt>',views.estacion),
    path('estacion_popup/<str:codigo_estacion_txt>',views.estacion_popup),
    path('estaciones',views.estaciones),
    path('estaciones_tabla/<str:tipo>,<int:zona>',views.estaciones_filtrar),
    path('senal/<str:tag_txt>',views.senal),
    path('senales',views.senales),
    path('senales_estacion/<str:codigo_estacion_txt>',views.senales_de_una_estacion),
    path('grafica_simple/<str:cod_senal>',requests.grafica_simple),
    path('graficas_app',views.graficas_app),
    path('graficas',views.graficas),
    path('graficas_estacion/<str:codigo_estacion_txt>',views.graficas_de_una_estacion),
    path('datos_senal/<str:origen>,<str:tag_txt>,<str:fecha_ini>,<str:fecha_fin>',requests.datos_senal),
    path('info_senales_grafica/<str:codigo_estacion_txt>',requests.graficas_predefinidas_estacion)

]
