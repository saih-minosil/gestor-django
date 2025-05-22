from django.http import JsonResponse
from .models_intranet import  ListaSenales_I,DatosQuinceminutales,TiposSenales
from .models_hist import ConsAnoN,ConsAnoH,DatosTreal,DatosValid,ListaSenales_H,ConsMes_H, ConsDia_H, createTablaDatosTreal, createTablaDatosValid
from utm import conversion
from datetime import datetime,timedelta
from .constants import calidades_buenas_treal,calidades_buenas_consolidado,calidades_buenas_consolidado_diario
import os
import json
import pytz
import csv
from pytz import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models.query import QuerySet
from django.db import transaction


dicc_senales={"DatosQuinceminutales":DatosQuinceminutales,"DatosTreal":DatosTreal,"DatosValid":DatosValid,"ConsMes":ConsMes_H,"ConsDia":ConsDia_H,"ConsAnoN":ConsAnoN,"ConsAnoH":ConsAnoH}

dicc_calidades_buenas={
    "DatosQuinceminutales":calidades_buenas_treal,
    "DatosTreal":calidades_buenas_treal,
    "DatosValid":calidades_buenas_treal,
    "ConsDia":calidades_buenas_consolidado_diario,
    "ConsMes":calidades_buenas_consolidado,
    "ConsAnoN":calidades_buenas_consolidado,
    "ConsAnoH":calidades_buenas_consolidado
}
def get_tabla(fecha_ini,fecha_fin,origen):
    mesano=""
    ano=""
    if fecha_ini.year != fecha_fin.year:
        if origen=="DatosTreal":                    
                nombre_tabla = "DATOS_TREAL"
        else:
                nombre_tabla = "DATOS_VALID"
    else:
        if fecha_ini.month==fecha_fin.month:
            mesano=f"{fecha_ini.month:02d}{fecha_ini.year%100:02d}"
        else:
            ano=fecha_ini.year    
        if origen=="DatosTreal":
            if mesano:
                nombre_tabla = f"DATOS_TREAL_{mesano}"
            else:
                nombre_tabla = f"DATOS_TRA_{ano}"
        else:
            if mesano:
                nombre_tabla = f"DATOS_VALID_{mesano}"
            else:
                nombre_tabla = f"DATOS_VAA_{ano}"
    if origen=="DatosTreal":
        tabla=createTablaDatosTreal(nombre_tabla)
    else:
        tabla=createTablaDatosValid(nombre_tabla)
    return tabla

def datos_senal(request,origen,tag_txt,fecha_ini,fecha_fin,es_tabla=0):
    datos=[]
    fecha_ini=datetime.strptime(fecha_ini,"%Y-%m-%dT%H:%M")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%dT%H:%M")
    lista_valores=[]
    lista_etiquetas=[]
    lista_calidades=[]
    tabla=dicc_senales[origen]
    calidades_buenas=dicc_calidades_buenas[origen]
    senal=ListaSenales_I.objects.get(ls_tag_txt=tag_txt)
    senal_dict={'id_senal':senal.ls_tag_txt,'descripcion':senal.ls_descripcion,'tipo_senal':senal.ls_tipo_senal.ts_descripcion,'unid_ing_id':senal.ls_unid_ing_id,'unid_ing_nombre':senal.ls_unid_ing.ui_codigo_corto}
    if origen == "DatosQuinceminutales": #Columnas ho_tag_txt, ...
        values=tabla.objects.filter(ho_tag_txt=tag_txt,ho_fecha_hora__gte=fecha_ini,ho_fecha_hora__lte=fecha_fin).values()
        for value in values:
            hora_timestamp=datetime.timestamp(value["ho_fecha_hora"])   
            if value["ho_calidad"] in calidades_buenas: 
                lista_etiquetas.append(hora_timestamp)
                lista_valores.append(float("{:.3f}".format(value["ho_valor_horario"])))
                lista_calidades.append(value["ho_calidad"])
            else:
                if not senal.ls_estacion_txt_id.startswith('H') and not senal.ls_estacion_txt_id.startswith('PZ'):                    
                    lista_etiquetas.append(hora_timestamp)
                    lista_valores.append(float("{:.3f}".format(value["ho_valor_horario"])))
                    lista_calidades.append(value["ho_calidad"])
    elif origen in (["ConsAnoN","ConsAnoH","ConsMes","ConsDia","DatosTreal","DatosValid"]): #Columnas CC
        id_senal=ListaSenales_I.objects.filter(ls_tag_txt=tag_txt).first().ls_recid
        if origen.startswith("Datos"):  #Para datos de la historica, cargar solo la tabla del mes o del año (mucho mas rapido)
            tabla=get_tabla(fecha_ini,fecha_fin,origen)
            #tabla._meta.db_table=nombre_tabla
        print(f"SELECT * FROM {tabla._meta.db_table} WHERE CC_IDSENAL = {id_senal} AND CC_FECHA BETWEEN '{fecha_ini}' AND '{fecha_fin}' ")
        order_by = "-cc_fecha" if es_tabla else "cc_fecha"
        values = tabla.objects.filter(cc_idsenal=id_senal,cc_fecha__gte=fecha_ini,
                                                     cc_fecha__lte=fecha_fin).order_by(order_by)
        for value in values:            
            hora_timestamp = datetime.timestamp(value.cc_fecha)
            lista_etiquetas.append(hora_timestamp)
            lista_valores.append(float("{:.3f}".format(value.cc_valor)) if value.cc_calidad in calidades_buenas and value.cc_valor is not None else 0)
            lista_calidades.append(value.cc_calidad)
            datos.append([hora_timestamp,value.cc_valor,value.cc_calidad])

    else:   #DATOS DE LA BBDD HISTORICA?
        print("El origen de los datos no existe")
    if not es_tabla:
        if lista_valores:
            return JsonResponse({"senal":senal_dict,"etiquetas":lista_etiquetas,"valores":lista_valores,"calidades":lista_calidades})
        else:
            return JsonResponse({"senal":senal_dict,"etiquetas":[],"valores":[],"calidades":[],"error":"No hay datos de los campos elegidos"})
    else:
        if values:
            return JsonResponse({"datos":datos})
        else:    
            return JsonResponse({"datos":[],"error":"No hay datos de los campos elegidos"})

def grafica_simple_old(request,cod_senal):
    senal=ListaSenales_I.objects.get(ls_tag_txt=cod_senal)
    senal_dict={'id_senal':senal.ls_tag_txt,'descripcion':senal.ls_descripcion,'tipo_senal':senal.ls_tipo_senal.ts_descripcion,'unid_ing':senal.ls_unid_ing_id}
    lista_valores=[]
    lista_etiquetas=[]
    fecha_hace_un_mes=datetime.now()-timedelta(days=28)
    values=DatosQuinceminutales.objects.filter(ho_tag_txt=cod_senal,ho_fecha_hora__gte=fecha_hace_un_mes).values()
    for value in values:
        hora_timestamp=datetime.timestamp(value["ho_fecha_hora"])
        lista_etiquetas.append(hora_timestamp)
        lista_valores.append(float("{:.3f}".format(value["ho_valor_horario"]))if value["ho_calidad"]in calidades_buenas_treal else 0)
    grafica=[lista_etiquetas,lista_valores]
    return JsonResponse({"senal":senal_dict,"grafica":grafica})

def grafica_simple(request,cod_senal):
    fecha_hace_un_mes=datetime.now()-timedelta(days=28)
    hoy=datetime.now()
    datos=datos_senal(request,"DatosQuinceminutales",cod_senal,datetime.strftime(fecha_hace_un_mes,"%Y-%m-%dT%H:%M"),datetime.strftime(hoy,"%Y-%m-%dT%H:%M"))
    return datos

def graficas_predefinidas_estacion(request,codigo_estacion_txt): #POR AHORA NO HAY TIPO ( TIPO ES PARA DISTINGUIR CALIDAD DE HIDROLOGIA )    

    senales = ListaSenales_I.objects.all().filter(ls_estacion_txt_id=codigo_estacion_txt)
    print(senales)
    senales_preseleccionadas={}
    tipo_estacion=senales[0].ls_estacion_txt.le_tipo_estacion_id
    tipos_senales = TiposSenales.objects.all().filter(ts_grupo_web__isnull=False).order_by('ts_orden')
    print(tipos_senales)
    print(tipos_senales[0].__dict__)
    print(senales[0].ls_tipo_senal_id)
    print(senales[0].ls_tipo_senal)
    print(tipo_estacion)
    if tipo_estacion=='A' or tipo_estacion=='N': #Hidrologia
        cods=[senales.filter(ls_tipo_senal_id="NRIO").first().ls_tag_txt,senales.filter(ls_tipo_senal_id="QRIO").first().ls_tag_txt]
        print(cods)
        senales_preseleccionadas={
            cods[0]:{"codigo":cods[0],"color":"Blue","linea":[20,5],"lado":0},
            cods[1]:{"codigo":cods[1],"color":"Purple","linea":[4,4],"lado":1},
        }
        print(senales_preseleccionadas)
    elif tipo_estacion=='P':
        cods=[senales.filter(ls_tipo_senal_id="PCINC").first().ls_tag_txt,senales.filter(ls_tipo_senal_id="PADIA").first().ls_tag_txt]
        senales_preseleccionadas={
            cods[0]:{"codigo":cods[0],"color":"Blue","linea":[4,4],"lado":0},
            cods[1]:{"codigo":cods[1],"color":"Purple","linea":[20,4,4,4],"lado":1},
        }   
    elif tipo_estacion=='M':
        tipos_senales_grafica_meteo=['TEMEX','HUMRE','RADIA','EVAPO','PCINC','PADIA']
        cods=[]
        for tipo in tipos_senales_grafica_meteo:
            cods.append(senales.filter(ls_tipo_senal_id=tipo).first().ls_tag_txt)
        senales_preseleccionadas={
            cods[0]:{"codigo":cods[0],"color":"Orange","linea":[4,4],"lado":0},
            cods[1]:{"codigo":cods[1],"color":"Cyan","linea":[0],"lado":0},
            cods[2]:{"codigo":cods[2],"color":"Red","linea":[0],"lado":1},
            cods[3]:{"codigo":cods[3],"color":"Gray","linea":[4,4],"lado":1},
            cods[4]:{"codigo":cods[4],"color":"Blue","linea":[20,4,4,4],"lado":1},
            cods[5]:{"codigo":cods[5],"color":"Purple","linea":[20,4,4,4],"lado":1},            
        }   
    elif tipo_estacion=='E':
        tipos_senales_grafica_meteo=['NEMBA','VEMBA']
        cods=[]
        for tipo in tipos_senales_grafica_meteo:
            cods.append(senales.filter(ls_tipo_senal_id=tipo).first().ls_tag_txt)
        senales_preseleccionadas={
            cods[0]:{"codigo":cods[0],"color":"Blue","linea":[0],"lado":0},
            cods[1]:{"codigo":cods[1],"color":"Red","linea":[0],"lado":1},            
        }   
    elif tipo_estacion=='CH':
        tipos_senales_grafica_meteo=['NEMBA','VEMBA']
        cods=[]
        for tipo in tipos_senales_grafica_meteo:
            cods.append(senales.filter(ls_tipo_senal_id=tipo).first().ls_tag_txt)
        senales_preseleccionadas={
            cods[0]:{"codigo":cods[0],"color":"Blue","linea":[0],"lado":0},
            cods[1]:{"codigo":cods[1],"color":"Red","linea":[0],"lado":1},            
        }       
    return JsonResponse(senales_preseleccionadas)    

def csv_senal(request,origen,tag_txt,fecha_ini,fecha_fin):
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": f'attachment; filename="{tag_txt}_{origen}.csv"'},
    )
    writer = csv.writer(response,delimiter=';')
    datos=json.loads(datos_senal(request,origen,tag_txt,fecha_ini,fecha_fin).content)
    for i in range(len(datos["etiquetas"])):
        if datos["calidades"][i] in dicc_calidades_buenas[origen]: #SI ES BUENA
            writer.writerow([datetime.fromtimestamp(datos["etiquetas"][i]).strftime("%d/%m/%Y %H:%M"), datos["valores"][i]])    
    return response

def datos_senal_csv(request,origen,tag_txt,fecha_ini,fecha_fin,solo_datos_buenos=False):
    filas=[]
    datos=json.loads(datos_senal(request,origen,tag_txt,fecha_ini,fecha_fin).content)
    for i in range(len(datos["etiquetas"])):
        if solo_datos_buenos:
            if datos["calidades"][i] in dicc_calidades_buenas[origen]: #SI ES BUENA
                filas.append([tag_txt,datetime.fromtimestamp(datos["etiquetas"][i]).strftime("%d/%m/%Y %H:%M"), datos["valores"][i]])
        else:
            filas.append([tag_txt,datetime.fromtimestamp(datos["etiquetas"][i]).strftime("%d/%m/%Y %H:%M"), datos["valores"][i], datos["calidades"][i]])
    return JsonResponse({"cod_senal":tag_txt,"filas":filas})
       

def lista_senales(request):
    lista_senales=[]
    senales=list(ListaSenales_I.objects.all().values("ls_tag_txt","ls_descripcion"))
    for senal in senales:
        lista_senales.append({"codigo":senal["ls_tag_txt"],"descripcion":senal["ls_descripcion"]})
    return JsonResponse(lista_senales,safe=False)

@csrf_exempt
def modificar_bd(request):        
    senal=request.POST["select_senal"]
    print("REQUEST POST DICT: ")
    print(request.POST)
    keys=list(filter(lambda x: x.endswith("_valor"),request.POST.keys()))
    fecha_ini=datetime.strptime(request.POST["fecha_ini"], "%Y-%m-%dT%H:%M")
    fecha_fin = datetime.strptime(request.POST["fecha_fin"], "%Y-%m-%dT%H:%M")
    timestamps=list(map(lambda x: x[:10],keys))
    datetimes=list(map(lambda x: datetime.fromtimestamp(int(x)),timestamps))
    id_senal=ListaSenales_I.objects.filter(ls_tag_txt=senal).first().ls_recid
    
    tabla=get_tabla(fecha_ini,fecha_fin,"DatosValid")
    values = tabla.objects.filter(cc_idsenal=id_senal,cc_fecha__in=datetimes)
    datos=[]
    for ts in timestamps:
        dt=datetime.fromtimestamp(int(ts))
        valor=request.POST[ts+"_valor"]
        calidad=request.POST[ts+"_calidad"]
        print(f"{dt} : {valor} Q {calidad}")
        dato=values.get(cc_fecha=dt)
        #if not dato:
        #    dato=DatosValid(cc_idsenal=id_senal,cc_fecha=dt)
        dato.cc_valor=valor
        dato.cc_calidad=calidad
        print(dato)
        datos.append(dato)
    print(values)
    with transaction.atomic():
        for dato in datos:
            print(dato)
            print(f"{dato.cc_fecha} : {dato.cc_valor} Q {dato.cc_calidad}")
        dato.save()
    

        
    return JsonResponse({"status":"ok","message":"Datos modificados correctamente","num_updates":len(datos)})
        