from django.http import JsonResponse
from django.db.models import Max,Min
from django.template.loader import get_template
from .models import ListaEstaciones, ListaSenales,DatosHorarios,DatosQuinceminutales,TiposSenales,ConsMes, ConsDia,ConsAnoN,ConsAnoH,DatosTreal,DatosValid
from utm import conversion
from datetime import datetime,timedelta
from .constants import calidades_buenas_treal,calidades_buenas_consolidado,calidades_buenas_consolidado_diario
import os
import json
import pytz
from pytz import timezone


dicc_senales={"DatosQuinceminutales":DatosQuinceminutales,"DatosTreal":DatosTreal,"DatosValid":DatosValid,"ConsMes":ConsMes,"ConsDia":ConsDia,"ConsAnoN":ConsAnoN,"ConsAnoH":ConsAnoH}

dicc_calidades_buenas={
    "DatosQuinceminutales":calidades_buenas_treal,
    "DatosTreal":calidades_buenas_treal,
    "DatosValid":calidades_buenas_treal,
    "ConsDia":calidades_buenas_consolidado_diario,
    "ConsMes":calidades_buenas_consolidado,
    "ConsAnoN":calidades_buenas_consolidado,
    "ConsAnoH":calidades_buenas_consolidado
}

def datos_senal(request,origen,tag_txt,fecha_ini,fecha_fin):
    fecha_ini=datetime.strptime(fecha_ini,"%Y-%m-%dT%H:%M")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%dT%H:%M")
    lista_valores=[]
    lista_etiquetas=[]
    tabla=dicc_senales[origen]
    calidades_buenas=dicc_calidades_buenas[origen]
    senal=ListaSenales.objects.get(ls_tag_txt=tag_txt)
    senal_dict={'id_senal':senal.ls_tag_txt,'descripcion':senal.ls_descripcion,'tipo_senal':senal.ls_tipo_senal.ts_descripcion,'unid_ing_id':senal.ls_unid_ing_id,'unid_ing_nombre':senal.ls_unid_ing.ui_codigo_corto}
    if origen == "DatosQuinceminutales": #Columnas ho_tag_txt, ...
        values=tabla.objects.filter(ho_tag_txt=tag_txt,ho_fecha_hora__gte=fecha_ini,ho_fecha_hora__lte=fecha_fin).values()
        for value in values:
            hora_timestamp=datetime.timestamp(value["ho_fecha_hora"])
            lista_etiquetas.append(hora_timestamp)
            lista_valores.append(float("{:.3f}".format(value["ho_valor_horario"]))if value["ho_calidad"] in calidades_buenas else 0)
    elif origen in (["ConsAnoN","ConsAnoH","ConsMes","ConsDia","DatosTreal","DatosValid"]): #Columnas CC
        id_senal=ListaSenales.objects.filter(ls_tag_txt=tag_txt).first().ls_recid
        if origen.startswith("Datos"):  #Para datos de la historica, cargar solo la tabla del mes o del año (mas rapido)
            mesano=""
            ano=""
            if fecha_ini.year != fecha_fin.year:
                #Va a petar, demasiada informacion
                pass
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
                        nombre_tabla = f"Tabla = DATOS_VALID_{mesano}"
                    else:
                        nombre_tabla = f"Tabla = DATOS_VAA_{ano}"
                print(nombre_tabla)    
                DatosTreal._meta.db_table=nombre_tabla
        print(f"SELECT * FROM {tabla._meta.db_table} WHERE CC_IDSENAL = {id_senal} AND CC_FECHA BETWEEN '{fecha_ini}' AND '{fecha_fin}' ")
        values = tabla.objects.filter(cc_idsenal=id_senal,cc_fecha__gte=fecha_ini,
                                                     cc_fecha__lte=fecha_fin).order_by("cc_fecha")
        for value in values:
            hora_timestamp = datetime.timestamp(value.cc_fecha)
            lista_etiquetas.append(hora_timestamp)
            lista_valores.append(float("{:.3f}".format(value.cc_valor)) if value.cc_calidad_id in calidades_buenas and value.cc_valor is not None else 0)

    else:   #DATOS DE LA BBDD HISTORICA?
        print("El origen de los datos no existe")
    if lista_valores:
        return JsonResponse({"senal":senal_dict,"etiquetas":lista_etiquetas,"valores":lista_valores})
    else:
        return JsonResponse({"senal":senal_dict,"etiquetas":[],"valores":[],"error":"No hay datos de los campos elegidos"})

def grafica_simple(request,cod_senal):
    senal=ListaSenales.objects.get(ls_tag_txt=cod_senal)
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

def graficas_predefinidas_estacion(request,codigo_estacion_txt): #POR AHORA NO HAY TIPO ( TIPO ES PARA DISTINGUIR CALIDAD DE HIDROLOGIA )    
    senales = ListaSenales.objects.all().filter(ls_estacion_txt=codigo_estacion_txt)
    senales_preseleccionadas={}
    tipo_estacion=senales[0].ls_estacion_txt.le_tipo_estacion
    tipos_senales = TiposSenales.objects.all().filter(ts_grupo_web__isnull=False).order_by('ts_orden')
    if tipo_estacion=='A' or tipo_estacion=='N': #Hidrologia
        cods=[senales.filter(ls_tipo_senal_id="NRIO").first().ls_tag_txt,senales.filter(ls_tipo_senal_id="QRIO").first().ls_tag_txt]
        senales_preseleccionadas={
            cods[0]:{"codigo":cods[0],"color":"Blue","linea":[20,5],"lado":0},
            cods[1]:{"codigo":cods[1],"color":"Purple","linea":[4,4],"lado":1},
        }
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