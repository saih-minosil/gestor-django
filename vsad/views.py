from django.shortcuts import render
from .models import FewsSeries,InfoEstacion,InfoVariable,VariableForecast
from django.db.models import Max

def estacion(request,codigo_estacion_txt):
    estacion=InfoEstacion.objects.get(estacionid=codigo_estacion_txt)
    historica=VariableForecast.objects.filter(estacion_id=codigo_estacion_txt).first()
    forecast=historica.variableforecast
    fecha_ultima_prediccion=FewsSeries.objects.filter(seriesid=forecast).aggregate(Max('fechaforecast'))['fechaforecast__max']
    return render(request, 'prediccion.html', {"estacion": estacion,"historica":historica,"fecha_prediccion":fecha_ultima_prediccion}) 

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

def estacion_antigua(request,codigo_estacion_txt):
    print("estacion antigua")
    estacion=InfoEstacion.objects.get(estacionid=codigo_estacion_txt)
    historica=VariableForecast.objects.filter(estacion_id=codigo_estacion_txt).first()
    forecast=historica.variableforecast
    fecha_ultima_prediccion=FewsSeries.objects.filter(seriesid=forecast).aggregate(Max('fechaforecast'))['fechaforecast__max']
    return render(request, 'prediccion.html', {"estacion": estacion,"historica":historica,"fecha_prediccion":fecha_ultima_prediccion}) 