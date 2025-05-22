
from django.urls import path
from . import views
from . import requests

urlpatterns = [    
    path('/datos/<str:codigo_estacion_txt>',requests.grafica_estacion),
    path('',views.estaciones),
]