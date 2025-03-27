from intranetsaih.settings import TIME_ZONE
from .models import VariableForecast,FewsSeries,InfoVariable,InfoEstacion
from django.db.models import Max,Min
from datetime import timedelta,datetime,timezone
from django.http import JsonResponse
from itertools import chain
#result_list = list(chain(page_list, article_list, post_list))

def calcular_ts(fecha):
    print(datetime.strptime(fecha,'%Y-%m-%d %H:%M:%S'))
    print(datetime.strptime(fecha,'%Y-%m-%d %H:%M:%S').tzinfo)
    fecha_dt=datetime.strptime(fecha,'%Y-%m-%d %H:%M:%S')
    fecha_tz=fecha_dt.replace(tzinfo=timezone.utc)
    return datetime.timestamp(fecha_tz)


def grafica_estacion(request,codigo_estacion_txt):
    datos_estacion=VariableForecast.objects.filter(estacion_id=codigo_estacion_txt).first()    
    estacion=InfoEstacion.objects.filter(estacionid=codigo_estacion_txt).values('estacionid','extendido')[0]
    observada=datos_estacion.variableobservada
    observada_aportacion=datos_estacion.estacion_id+"_I.obs"
    historica=datos_estacion.estacion_id + "_Discharge"
    forecast=datos_estacion.variableforecast
    senal=datos_estacion.variableid
    dict_senal={}
    datos_senal=InfoVariable.objects.get(variableid=senal)
    dict_senal['activacion']=datos_senal.alertabajo
    dict_senal['prealerta']=datos_senal.alertaalto
    dict_senal['alerta']=datos_senal.alarmaalto
    dict_senal['unidad']=datos_senal.unidad
    dict_senal['tipo']=codigo_estacion_txt[0]
    fecha_inicial=datetime.now()-timedelta(days=3)    
    fecha_ultima_prediccion=FewsSeries.objects.filter(seriesid=forecast).aggregate(Max('fechaforecast'))['fechaforecast__max']    
    valores_observada=FewsSeries.objects.filter(seriesid=observada,fecha__gte=fecha_inicial)
    valores_historica=FewsSeries.objects.filter(seriesid=historica,fecha__gte=fecha_inicial)    
    valores_forecast=FewsSeries.objects.filter(seriesid=forecast,fechaforecast=fecha_ultima_prediccion,fecha__gte=fecha_inicial)
    valores_obs_dict={}
    valores_obs_aport_dict={}
    valores_hist_dict={}
    valores_forecast_dict={}
    timestamps_dict={}
    for valor_obs in valores_observada:
        valores_obs_dict[calcular_ts(valor_obs.fecha)]=valor_obs.valor
        timestamps_dict[calcular_ts(valor_obs.fecha)]=1
    for valor_hist in valores_historica:
        valores_hist_dict[calcular_ts(valor_hist.fecha)]=valor_hist.valor
        timestamps_dict[calcular_ts(valor_hist.fecha)]=1
    for valor_forecast in valores_forecast:
        valores_forecast_dict[calcular_ts(valor_forecast.fecha)]=valor_forecast.valor
        timestamps_dict[calcular_ts(valor_forecast.fecha)]=1
    ################ EXTRA PARA EMBALSES ############################################################################
    if codigo_estacion_txt[0]=='E': #Si es embalse obtiene las aportaciones
        valores_observada_aportacion=FewsSeries.objects.filter(seriesid=observada_aportacion,fecha__gte=fecha_inicial)
        for valor_obs_a in valores_observada_aportacion:
            valores_obs_aport_dict[datetime.timestamp(datetime.strptime(valor_obs_a.fecha,'%Y-%m-%d %H:%M:%S'))]=valor_obs_a.valor
            timestamps_dict[datetime.timestamp(datetime.strptime(valor_obs_a.fecha,'%Y-%m-%d %H:%M:%S'))]=1
    
    
    lista_valores_obs=[]
    lista_valores_obs_aport=[]
    lista_valores_hist=[]
    lista_valores_forecast=[]
    lista_etiquetas=list(timestamps_dict.keys())
    lista_etiquetas.sort()
    for t in lista_etiquetas:        
        lista_valores_obs.append(float("{:.3f}".format(valores_obs_dict[t])) if t in valores_obs_dict else None)
        lista_valores_hist.append(float("{:.3f}".format(valores_hist_dict[t]))if t in valores_hist_dict else None)
        lista_valores_forecast.append(float("{:.3f}".format(valores_forecast_dict[t])) if t in valores_forecast_dict else None)
        if valores_obs_aport_dict:
            lista_valores_obs_aport.append(float("{:.3f}".format(valores_obs_aport_dict[t])) if t in valores_obs_aport_dict else None)
    grafica=[lista_etiquetas,lista_valores_obs,lista_valores_obs_aport,lista_valores_hist,lista_valores_forecast]
    return JsonResponse({"estacion":estacion,"senal":dict_senal,"grafica":grafica,"fecha_prediccion":fecha_ultima_prediccion})