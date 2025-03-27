from django.shortcuts import render
from .models import FewsSeries,InfoEstacion,InfoVariable,VariableForecast
from django.db.models import Max

def estaciones(request):
    estaciones=VariableForecast.objects.all().order_by('estacion')#.values('le_codigo_txt','le_nombre','le_rio','le_tipologia','le_tipo_sensor')
    #for estacion in estaciones:
    #    if estacion.estacion[0:1]=='PZ':
    #        tipo_estacion=estacion.estacion[0:1]    
    #    elif estacion.estacion[0:1]=='CH':
    #        tipo_estacion=estacion.estacion[1]    
    #    else:    
    #        tipo_estacion=estacion.estacionid[0]
    #    estacion.tipo_estacion=tipo_estacion
    print(estaciones)
    return render(request,'estaciones_saih.html',{"estaciones":estaciones})    

