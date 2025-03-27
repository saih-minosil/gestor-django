
from django.urls import path
from . import views
from . import requests

urlpatterns = [    
    path('/<str:codigo_estacion_txt>',views.estacion),
    path('/datos/<str:codigo_estacion_txt>',requests.grafica_estacion),
    path('',views.estaciones),
    path('/antigua/<str:codigo_estacion_txt>',views.estacion_antigua),
]