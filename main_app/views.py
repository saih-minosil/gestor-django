from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Max,Min
from django.template.loader import get_template
from .models import ListaEstaciones, ListaSenales,DatosHorarios,DatosQuinceminutales,TiposSenales,ConsMes, ConsDia
from .constants import calidades_buenas_treal,calidades_buenas_consolidado,calidades_buenas_consolidado_diario
from utm import conversion
from datetime import datetime,timedelta
import os
import json
import pytz
from pytz import timezone

colores_estados={1:'#C4D3EE',8:'#ff0000',4:'#333333'}
colores_alarmas={"BAJO BAJO":"#a07755" ,"BAJO":"#ff00ff","NORMAL":"#00ff00","ALTO":"#ffff00","ALTO ALTO":"ff7700","ALTO ALTO ALTO":"#ff0000"}
tz = pytz.timezone('Europe/London')

class CuadroEstacion():
    def __init__(self,codigo_estacion_txt):
        estacion=ListaEstaciones.objects.get(le_codigo_txt=codigo_estacion_txt)
        self.codigo=codigo_estacion_txt
        self.nombre=estacion.le_nombre
        self.tipo=estacion.le_tipo_estacion
        if self.codigo.startswith('PZ'):
            self.tipo='PZ'
        self.color_estacion=colores_estados[estacion.le_estado]
        self.filas=[]
        if self.tipo=='P' or self.tipo=='M':
            self.tipos_senales=['PA01H','PA12H','PA24H']
        elif self.tipo=='N' or self.tipo=='A':
            self.tipos_senales = ['NRIO', 'QRIO','MPTT','MPPH','MPO2','A3AT','MPCT','TUTU']
        elif self.tipo=='E':
            self.tipos_senales =['NEMBA', 'VEMBA', 'APORT','QTSAL','QSALR','QALIV','QTURP','QDSF','PORCE']
        elif self.tipo=='CH':
            self.tipos_senales = ['NEMBA', 'VEMBA','QTURP','QECOL']
        elif self.tipo == 'PZ':
            self.tipos_senales = ['PMSNM', 'NPZM']
        else:
            self.tipos_senales = []        
        senales=ListaSenales.objects.filter(ls_estacion_txt=codigo_estacion_txt).filter(ls_tipo_senal__in=self.tipos_senales).values('ls_tag_txt','ls_descripcion','ls_unid_ing','ls_recid','ls_alarma','ls_tipo_almacenamiento')
        self.lista_senales=[]
        print(senales)
        if senales :            
            if self.tipo=='PZ': #NI  PIEZO (furuto)
                tabla=DatosHorarios
            else:
                tabla=DatosQuinceminutales
            for senal in senales:
                if self.tipo !='CH' or senal['ls_tipo_almacenamiento']!='6060':
                    fecha_ultimo_valor =  tabla.objects.filter(ho_tag_txt=senal['ls_tag_txt']).filter(ho_calidad__in=calidades_buenas_treal).aggregate(
                        Max('ho_fecha_hora'))['ho_fecha_hora__max']
                    print(fecha_ultimo_valor)    
                    #Si la fecha del ultimo valor es de las ultimas 6 horas, o si es piezo y la fecha es de los ultimos 4 dias
                    if fecha_ultimo_valor:
                        #if fecha_ultimo_valor.tzinfo is None or fecha_ultimo_valor.tzinfo.utcoffset(fecha_ultimo_valor) is None:
                        #    fecha_ultimo_valor=tz.localize(fecha_ultimo_valor)
                        time_diff= datetime.now()-fecha_ultimo_valor
                        print(time_diff)
                        if self.tipo=='PZ' or self.tipo=='CH':
                            max_time_diff=timedelta(days=4)
                        else:
                            max_time_diff=timedelta(hours=6)                    
                        if time_diff< max_time_diff:
                        #and (fecha_ultimo_valor >= datetime.now()-timedelta(hours=6) or (self.tipo=='PZ' and fecha_ultimo_valor.date() >= datetime.now().date()-timedelta(days=4))):
                            if senal['ls_alarma']:
                                senal['color_alarma'] = colores_alarmas[senal['ls_alarma']]
                            ultimo_dato=tabla.objects.filter(ho_tag_txt=senal['ls_tag_txt']).filter(ho_fecha_hora=fecha_ultimo_valor)
                            print(ultimo_dato)

                            if ultimo_dato :
                                senal['ultimo_valor']="{:.2f}".format(ultimo_dato.first().ho_valor_horario)
                                senal['unidad']=senal['ls_unid_ing']
                                self.lista_senales.append(senal)


    def render(self):
        template = get_template("widgets/popup_mapa.html")
        return template.render({"senales":self.lista_senales,"estacion":{"codigo":self.codigo,"nombre":self.nombre,"color":self.color_estacion }},None)


def lorem(request):
    return render(request,'lorem.html')


def mapa(request):
    lista_estaciones = []
    dict_iconos= {"A":"iconoAforo", "N":"iconoNivel", "P":"iconoPluvio", "M":"iconoMeteo", "E":"iconoEmbalse","CH":"iconoEmbalse","V":"iconoVertido","Q":"iconoCalidad", "R":"iconoRiego", "PZ":"iconoPiezo"}
    estaciones = ListaEstaciones.objects.all().values('le_codigo_txt', 'le_utm_x', 'le_utm_y','le_tipo_estacion','le_nombre')
    for estacion in estaciones:
        codigo = estacion['le_codigo_txt']
        if codigo.startswith('PZ'):estacion['le_tipo_estacion']='PZ'
        if  (estacion['le_utm_x'] and estacion['le_utm_y']) :
            (x,y)= conversion.to_latlon(estacion['le_utm_x'],estacion['le_utm_y'], 30, 'T',strict=False)
            tipo=estacion['le_tipo_estacion']
            cuadro_estacion=""
            icono=dict_iconos[tipo]
            nombre=estacion['le_nombre']
            lista_estaciones.append({"x": float(x),"y": float(y), "codigo": codigo, "icono":icono, "nombre": nombre, "tipo": tipo, "cuadro":cuadro_estacion})
        else:
            pass
    estaciones_json=json.dumps(lista_estaciones)
    return render(request, 'mapa.html', context={"estaciones": estaciones_json})

def estaciones(request):
    estaciones=ListaEstaciones.objects.all().order_by('le_codigo_txt')#.values('le_codigo_txt','le_nombre','le_rio','le_tipologia','le_tipo_sensor')
    return render(request,'listaestaciones.html',{"estaciones":estaciones})

def estaciones_filtrar(request,tipo,zona):
    estaciones = (ListaEstaciones.objects.filter(le_tipo_estacion=tipo,le_zona=zona).order_by('le_codigo_txt'))
    return render(request,'widgets/tablaestaciones.html',{"estaciones":estaciones})

#Estacion con todos sus datos asociados para la ficha de estacion (Todas sus señales, valores en tiempo real y estadisticos

def estacion(request,codigo_estacion_txt):
    estacion=ListaEstaciones.objects.get(le_codigo_txt=codigo_estacion_txt)
    esquema_estacion='main_app/static/main_app/img/esquemas/'+estacion.le_codigo_txt+'.png'
    if(not os.path.isfile(os.path.realpath(esquema_estacion))):
        esquema_estacion=None
    if estacion.le_tipo_estacion=='CH':
        senales = (ListaSenales.objects.filter(ls_estacion_txt=codigo_estacion_txt).filter(ls_ver_intranet=1,ls_tipo_almacenamiento=1515).all().order_by('ls_tipo_senal__ts_orden')
               .distinct().values('ls_tag_txt', 'ls_descripcion', 'ls_tipo_senal','ls_tendencia','ls_unid_ing','ls_digitos_decimales','ls_recid','ls_unid_ing'))        
    else:
        senales = (ListaSenales.objects.filter(ls_estacion_txt=codigo_estacion_txt).filter(ls_ver_intranet=1).all().order_by('ls_tipo_senal__ts_orden')
               .distinct().values('ls_tag_txt', 'ls_descripcion', 'ls_tipo_senal','ls_tendencia','ls_unid_ing','ls_digitos_decimales','ls_recid','ls_unid_ing'))
    if(senales):
        senal=senales[0]#La fecha del ultimo valor será para la señal 1 la ultimna con calidad buena!!!
        fecha_actual=datetime.now()
        fecha_ultimo_valor = DatosQuinceminutales.objects.filter(ho_tag_txt=senal['ls_tag_txt']).filter(ho_calidad__in=calidades_buenas_treal).aggregate(Max('ho_fecha_hora'))['ho_fecha_hora__max']
        if fecha_ultimo_valor:
            if estacion.le_tipo_estacion=='CH' or estacion.le_codigo_txt.startswith('PZ'):
                maxdelta=timedelta(days=7)
            else:
                maxdelta=timedelta(hours=6)
            antiguedad_ultimo_dato=fecha_actual-fecha_ultimo_valor
            if  antiguedad_ultimo_dato> maxdelta:senales=[]        
            fecha_dia_anterior=fecha_ultimo_valor-timedelta(days=1)
            fecha_ultimo_dia = ConsDia.objects.filter(cc_idsenal=senal['ls_recid'])\
                .filter(cc_calidad__in=calidades_buenas_consolidado_diario)\
                .filter(cc_fecha__year=fecha_dia_anterior.year)\
                .filter(cc_fecha__month=fecha_dia_anterior.month)\
                .filter(cc_fecha__day=fecha_dia_anterior.day)\
                .aggregate(Max('cc_fecha'))['cc_fecha__max']
            print("Fecha_ultimo_dia : "+fecha_ultimo_dia.__str__())                
            fecha_mes_anterior = fecha_ultimo_valor-timedelta(days=fecha_ultimo_valor.day+1)
            fecha_ultimo_mes = ConsMes.objects.filter(cc_idsenal=senal['ls_recid'])\
                .filter(cc_calidad__in=calidades_buenas_consolidado)\
                .filter(cc_fecha__year=fecha_mes_anterior.year)\
                .filter(cc_fecha__month=fecha_mes_anterior.month)\
                .aggregate(Max('cc_fecha'))['cc_fecha__max']
            print("Fecha_ultimo_mes : "+fecha_ultimo_mes.__str__())    
            print("SELECT * FROM CONS_MES WHERE CC_FECHA = '"+ fecha_ultimo_mes.__str__()+"' and CC_IDSENAL = '"+ str(senal['ls_recid']) +"'")
            fecha_inicial = datetime.fromisoformat('2007-01-01 00:00.000')         
            for senal in senales:
                #---------------------------------------Tiempo real--------------------------------------------------------------
                if senal['ls_digitos_decimales'] is None:
                    senal['ls_digitos_decimales'] = 0
                senal['valor'] = DatosQuinceminutales.objects.filter(ho_tag_txt=senal['ls_tag_txt'],ho_fecha_hora=fecha_ultimo_valor).values().first()
                formato = "{:." + str(senal['ls_digitos_decimales']) + "f}"            
                senal['valor']['ho_valor'] = formato.format(senal['valor']['ho_valor_horario'])
                #-----------------------------------------Diaria-----------------------------------------------------------------
                senal['ultimo_dia'] = ConsDia.objects.filter(cc_idsenal=senal['ls_recid'],cc_fecha=fecha_ultimo_dia).first()
                if(senal['ultimo_dia']):
                    senal['ultimo_dia'].cc_valor = formato.format(senal['ultimo_dia'].cc_valor) if senal['ultimo_dia'].cc_valor else ""
                    if senal['ultimo_dia'].cc_valor_min :
                        senal['ultimo_dia'].cc_valor_min = formato.format(senal['ultimo_dia'].cc_valor_min)
                        senal['ultimo_dia'].cc_f_valor_min = senal['ultimo_dia'].cc_f_valor_min.strftime("%d/%m/%Y %H:%M")
                    else: 
                        senal['ultimo_dia'].cc_valor_min="Desconocido"
                        senal['ultimo_dia'].cc_f_valor_min="Desconocido"               
                    if senal['ultimo_dia'].cc_valor_max :
                        senal['ultimo_dia'].cc_valor_max = formato.format(senal['ultimo_dia'].cc_valor_max)
                        senal['ultimo_dia'].cc_f_valor_max = senal['ultimo_dia'].cc_f_valor_max.strftime("%d/%m/%Y %H:%M")
                    else :
                        senal['ultimo_dia'].cc_valor_max="Desconocido"
                        senal['ultimo_dia'].cc_f_valor_max="Desconocido"
                #----------------------------------------Mensual------------------------------------------------------------------
                senal['mes_anterior'] = ConsMes.objects.filter(cc_idsenal=senal['ls_recid'], cc_fecha=fecha_ultimo_mes).first()
                print(senal['mes_anterior'])
                if(senal['mes_anterior']):
                    senal['mes_anterior'].cc_valor = formato.format(senal['mes_anterior'].cc_valor) if senal['mes_anterior'].cc_valor else ""
                    if senal['mes_anterior'].cc_valor_min :
                        senal['mes_anterior'].cc_valor_min = formato.format(senal['mes_anterior'].cc_valor_min) 
                        senal['mes_anterior'].cc_f_valor_min = senal['mes_anterior'].cc_f_valor_min.strftime("%d/%m/%Y %H:%M")
                    else: 
                        senal['mes_anterior'].cc_valor_min="Desconocido"
                        senal['mes_anterior'].cc_f_valor_min="Desconocido"
                    if senal['mes_anterior'].cc_valor_max:
                        senal['mes_anterior'].cc_valor_max = formato.format(senal['mes_anterior'].cc_valor_max)    
                        senal['mes_anterior'].cc_f_valor_max = senal['mes_anterior'].cc_f_valor_max.strftime("%d/%m/%Y %H:%M")   
                    else: 
                        senal['mes_anterior'].cc_valor_max="Desconocido"
                        senal['mes_anterior'].cc_f_valor_max="Desconocido"                
                #-----------------------------------------Estadisticos totales (solo caudales y niveles) (SOLO A Y N; PERO N NO FUNCIONA)
                if senal['ls_tipo_senal']=="QRIO" or senal['ls_tipo_senal'] == "NRIO":
                    print(senal['ls_tipo_senal'])
                    senal['maximo'] = ConsMes.objects.filter(cc_idsenal=senal['ls_recid']).aggregate(Max('cc_valor_max'))['cc_valor_max__max']
                    senal['fecha_maximo'] = ConsMes.objects.filter(cc_idsenal=senal['ls_recid'],cc_valor_max=senal['maximo']).first().cc_f_valor_max
                    fecha_inicial = max(fecha_inicial , ConsMes.objects.filter(cc_idsenal=senal['ls_recid']).aggregate(Min('cc_fecha'))['cc_fecha__min']) #Cargar desde tabla de minimos
                    senal['maximo']=formato.format(senal['maximo']) if senal['maximo'] else ""
                    if(senal['fecha_maximo']):
                        senal['fecha_maximo']=senal['fecha_maximo'].strftime("%d/%m/%Y %H:%M")
                    print(senal['maximo'])
                    print(senal['fecha_maximo'])
            #-----------------------------------------------Formato fechas globales -------------------------------------------------------
            if fecha_ultimo_valor : fecha_ultimo_valor = fecha_ultimo_valor.strftime("%d/%m/%Y %H:%M")
            if fecha_ultimo_dia : fecha_ultimo_dia = fecha_ultimo_dia.strftime("%d/%m/%Y")
            if fecha_ultimo_mes : fecha_ultimo_mes = fecha_ultimo_mes.strftime("%m/%Y")
            if fecha_inicial : fecha_inicial = fecha_inicial.strftime("%m/%Y")
            fecha_actual=fecha_actual.strftime("%m/%Y")
            estacion_view = {"estacion": estacion,"esquema_estacion":esquema_estacion,"senales":senales, "fecha":fecha_ultimo_valor ,
                            "ultimo_dia":fecha_ultimo_dia,"ultimo_mes":fecha_ultimo_mes,"fecha_inicial":fecha_inicial,
                            "fecha_actual":fecha_actual}
            return render(request,'fichaestacion.html',{"estacion": estacion_view})                        
    estacion_view = {"estacion": estacion, "esquema_estacion": esquema_estacion}
    return render(request,'fichaestacion.html',{"estacion": estacion_view})

def estacion_popup(request,codigo_estacion_txt):
    estacion=CuadroEstacion(codigo_estacion_txt)
    return HttpResponse(estacion.render())

def senales(request):
    senales = ListaSenales.objects.all()
    tipos_senales=TiposSenales.objects.all().filter(ts_grupo_web__isnull=False).order_by('ts_orden')
    return render(request, 'listasenales.html', {"senales" : senales, "tipos": tipos_senales})

def senales_de_una_estacion(request,codigo_estacion_txt):
    senales = ListaSenales.objects.all()
    tipos_senales = TiposSenales.objects.all().filter(ts_grupo_web__isnull=False).order_by('ts_orden')
    return render(request, 'listasenales.html', {"senales" : senales,"tipos": tipos_senales,"estacion": codigo_estacion_txt})

def senal(request,tag_txt):
    senal=ListaSenales.objects.get(ls_tag_txt=tag_txt)#.select_related('ls_tipo_senal').first()
    return render(request, 'fichasenal.html', {"senal": senal}) 

def graficas(request):
    senales = ListaSenales.objects.all()
    tipos_senales = TiposSenales.objects.all().filter(ts_grupo_web__isnull=False).order_by('ts_orden')
    return render(request, 'graficas.html',{"senales" : senales, "tipos": tipos_senales, "template": "layouts/base.html"})

def graficas_de_una_estacion(request,codigo_estacion_txt): #POR AHORA NO HAY TIPO ( TIPO ES PARA DISTINGUIR CALIDAD DE HIDROLOGIA )    
    return render(request, 'graficas_estacion.html',{"cod_estacion":codigo_estacion_txt,"tipo":None,"template": "layouts/base.html"})

def graficas_app(request):
    senales = ListaSenales.objects.all()
    tipos_senales = TiposSenales.objects.all().filter(ts_grupo_web__isnull=False).order_by('ts_orden')
    return render(request, 'graficas.html',{"senales" : senales, "tipos": tipos_senales, "template": "layouts/application.html"})

