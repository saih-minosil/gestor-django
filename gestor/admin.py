from django.contrib import admin
from .models import  ListaSenales,ListaEstaciones,ListaRemotas,ListaRemotasTarjetas,ListaSenalesAnalogicas,ListaSenalesDigitales,ListaRemotasConf,Rios
from .models import Poblaciones,ListaSenalesDigdobles,TiposSenales, UnidadesIngenieria,ListaSenalesLimitevariables,ListaSenalesCalculadas
from .models import ListaOrdenes
from main_app import models_comun,models_intranet,models_hist
from django import forms
# Register your models here.
from datetime import datetime
from django.db.models import Max
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.core.exceptions import (
    ObjectDoesNotExist
)


from pprint import pp
class GestorAdminSite(admin.AdminSite):
    site_header="Gestor de las Bases de datos"
    site_title="Gestor de las Bases de datos"
    index_title="Editar Bases de Datos"


    def get_app_list(self, request,app_label = None):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        ordering = {                        
            "Estaciones": 0,
            "Remotas": 1,
            "Señales":2,
            "Ordenes":3,
            "Poblaciones": 4,
            "Rios":5,
            "Tipos de señal":6,
            "Unidades de medida":7,            
            "FormatosDigitales":9
        }
        app_dict = self._build_app_dict(request)       
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
        # Sort the models followinf the ordering within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: ordering[x['name']])

        return app_list

    def each_context(self,request):
        con = super().each_context(request)

        #con['available_apps'][0]["name"]="Bases de datos"
        #con['title']="Gestion de Bases de Datos"
        #con['subtitle']="Subtitulo!"
        return con     

gestor_admin_site = GestorAdminSite(name="Configuracion de la red SAIH")


@admin.action(description="Traspasar a la Intranet")
def traspaso_a_intranet(modeladmin, request,queryset):
    for obj in queryset:   
        class_name=obj.__class__.__name__
        
        if class_name == "ListaSenales":
            newobj=models_intranet.ListaSenales_I()
            lsa_obj=ListaSenalesAnalogicas.objects.get(lsa_tag=obj.ls_tag)
            estacion=models_intranet.ListaEstaciones_I.objects.get(le_codigo_txt=obj.ls_remota.lr_estacion.le_codigo_txt)
            newobj.from_gestor(obj,lsa_obj,estacion)    
        elif class_name == "ListaEstaciones":
            newobj=models_intranet.ListaEstaciones_I()
            newobj.from_gestor(obj=obj)            
        elif class_name == "ListaRemotas":
            newobj=models_intranet.ListaEstacionesRemotas_I()
        #    newobj.from_gestor(obj)
        else:       
            class_ = getattr(models_intranet, class_name) 
            newobj=class_()                     
            models_intranet.copy_object(orig=obj,dest=newobj)        
        try:
            newobj.save()
            messages.success(request, f"{obj} actualizado ") #Uno por cada, mejorable
        except Exception as e:
            print(e.__class__)    
            messages.error(request, f"Error actualizando {obj} : {e}") #Uno por cada, mejorable
        finally:
            messages.info(request, f"Se intenta actualizar algo :{obj} ") #Uno por cada, mejorable

@admin.action(description="Borrar de la Intranet")
def borrar_de_intranet(modeladmin, request,queryset):
    for obj in queryset:   
        class_ = getattr(models_intranet, obj.__class__.__name__+"_I") 
        try:
            newobj=class_.objects.get(pk=obj.pk)       
            newobj.delete()
            messages.success(request, f"{obj} borrado")    #Uno por cada, mejorable
        except ObjectDoesNotExist as e:            
            messages.error(request, f"Error borrando {obj} : el objecto no existe") #Uno por cada,mejorable       
        except Exception as e:
            print(e.__class__)    
            messages.error(request, f"Error borrando {obj} : {e}") #Uno por cada, mejorable

@admin.action(description="Borrar de la Historica")
def borrar_de_historica(modeladmin, request,queryset):
    for obj in queryset:   
        class_ = getattr(models_hist, obj.__class__.__name__) 
        try:
            newobj=class_.objects.get(pk=obj.pk)       
            newobj.delete()
            messages.success(request, f"{obj} borrado")    #Uno por cada, mejorable
        except ObjectDoesNotExist as e:            
            messages.error(request, f"Error borrando {obj} : el objecto no existe") #Uno por cada,mejorable       
        except Exception as e:
            print(e.__class__)    
            messages.error(request, f"Error borrando {obj} : {e}") #Uno por cada, mejorable            

@admin.action(description="Traspasar a la Historica")
def traspaso_a_historica(modeladmin, request,queryset):
    for obj in queryset:   
        class_name=obj.__class__.__name__        
        if class_name == "ListaSenales":
            newobj=models_hist.ListaSenales_H()
            #lsa_obj=ListaSenalesAnalogicas.objects.get(lsa_tag=obj.ls_tag)
            #estacion=models_hist.ListaEstaciones_H.objects.get(le_codigo_txt=obj.ls_remota.lr_estacion.le_codigo_txt)
            newobj.from_gestor(obj)    
        elif class_name == "ListaEstaciones":
            newobj=models_hist.ListaEstaciones_H()
            newobj.from_gestor(obj)  
            pp(obj.__dict__)          
        elif class_name == "ListaRemotas":
            newobj=models_hist.ListaRemotas_H()
            newobj.from_gestor(obj)  
        else:    
            class_ = getattr(models_hist, class_name) 
            newobj=class_()                        
            models_hist.copy_object(orig=obj,dest=newobj)        
        #try:
        newobj.save()
        messages.success(request, f"{obj} actualizado ") #Uno por cada, mejorable
        #except Exception as e:
        #    print(e.__class__)    
        #    messages.error(request, f"Error actualizando {obj} : {e}") #Uno por cada, mejorable


    '''Save model para todas:
    al guardar actualiza fmodif
    '''


############################################## INLINES REMOTAS ########################################################

class ListaRemotasConfsInlineAdmin(admin.StackedInline):
    extra=0
    model=ListaRemotasConf
    fieldsets=[("Datos Tecnicos",
        {
            "fields" : [("lrc_num_remota","lrc_zona_com",),
                        ("lrc_modelo","lrc_direccion_ip",)
            ]
        }
    ),    
    ("Valores maximos",
        {
            "fields" : [("lrc_max_tarjetas","lrc_max_factores","lrc_max_tags"),
                        ("lrc_max_contadores","lrc_max_tomamuestras","lrc_max_enclavamientos"),
                        ("lrc_max_rebotes","lrc_max_ent_analog","lrc_max_ent_digital"),
                        ("lrc_max_ent_binarias","lrc_max_ent_grays","lrc_max_ent_bnc"),
                        ("lrc_max_ent_digdobles","lrc_max_sal_analog","lrc_max_sal_digital"),
                        ("lrc_max_db","lrc_max_sizedb","lrc_temp_inhibicion"),
                        ("lrc_observaciones")
            ]
        }
    )]

class TarjetasForm(forms.ModelForm):        
    class Meta:
        model=ListaRemotasTarjetas
        fields=["lrt_codigo","lrt_nombre","lrt_modelo","lrt_tipo","lr_dir_control","lr_dir_datos","lrt_numdatos","lrt_signo","lr_dir_ip"]       

    def clean(self): #formulario
        if self.data['listaremotastarjetas_set-0-pk'] is None:
            pass
        if self.data['listaremotastarjetas_set-0-pk'] == "":            
            pk=f"({self.cleaned_data['lrt_codigo'].lr_codigo},\'{self.cleaned_data['lrt_nombre']}\')"            
            self.data['listaremotastarjetas_set-0-pk'] = pk
        else:
            pk= self.data['listaremotastarjetas_set-0-pk']    
        cleaned_data=super().clean()
        cleaned_data['pk']=pk
        self.errors.pop('pk', None)
        return(cleaned_data)

class ListaRemotasTarjetasInlineAdmin(admin.TabularInline):
#class ListaRemotasTarjetasInlineAdmin(admin.StackedInline):    
    model=ListaRemotasTarjetas
    extra=0
    form=TarjetasForm


class ListaSenalesInlineAdmin(admin.StackedInline):
    model=ListaSenales
    extra=0
    empty_value_display = "-"
    show_change_link=True
    #readonly_fields = ["ls_tag_txt"]
    fields=[()]

class ListaOrdenesInlineAdmin(admin.StackedInline):
    model=ListaOrdenes
    extra=0
    empty_value_display = "-"
    show_change_link=True
    #readonly_fields = ["ls_tag_txt"]
    fields=[()]
    
################################################# INLINES PARA SEÑALES ##########################################################################
class ListaSenalesAnalogicasInlineAdmin(admin.StackedInline):    
    extra=0
    model=ListaSenalesAnalogicas
    empty_value_display = "-"
    readonly_fields = ["lsa_tag"]
    fieldsets=[
        ("Formato de Valores",
            {                
                "fields" : [("lsa_unid_ing","lsa_digitos_enteros"),
                            ("lsa_digitos_decimales","lsa_tipo_almacenamiento"),
                ]
            }
        ),
        ("Valores para coherencia y validacion",
            {
                "fields":[ ("lsa_minimo","lsa_maximo"),]
            }
        ),
        ("Limites de Nivel",
            {
                "fields":[  ("lsa_lim_tv"),]
            }
        ),
        ("Alarmas",
            {
                "fields":[  ("lsa_lim_alto_alto_alto","lsa_gravedad_aaa","lsa_ver_intranet_aaa","lsa_ver_web_aaa","lsa_ver_pda_aaa"),
                            ("lsa_lim_alto_alto","lsa_gravedad_aa","lsa_ver_intranet_aa","lsa_ver_web_aa","lsa_ver_pda_aa"),
                            ("lsa_lim_alto","lsa_gravedad_a","lsa_ver_intranet_a","lsa_ver_web_a","lsa_ver_pda_a"),
                            ("lsa_lim_bajo","lsa_gravedad_b"),
                            ("lsa_lim_bajo_bajo","lsa_gravedad_bb"),
                            ("lsa_valor_histeresis"),
                          ]
            }
        ),
        ("Limites rampa",
            {
                "fields":[  ("lsa_lim_neg_rampa","lsa_gravedad_rn"),
                            ("lsa_lim_pos_rampa","lsa_gravedad_rp"),
                            ("lsa_lim_rampa_histeresis")
                          ]
            }
        ),
    ]
   

class ListaSenalesDigitalesInlineAdmin(admin.StackedInline):    
    extra=0
    model=ListaSenalesDigitales        
    fields=[("lsd_es_alarma","lsd_valor_activacion","lsd_gravedad"),
    ("lsd_logica_negativa","lsd_tmp_proceso"),
    ("lsd_texto_valor_0","lsd_texto_valor_1")]

class ListaSenalesDobleDigitalesInlineAdmin(admin.StackedInline):    
    extra=0
    model=ListaSenalesDigdobles       
    fields=[("ldd_es_alarma","ldd_valor_alarma","ldd_gravedad"),    
    ("ldd_texto_valor_0","ldd_texto_valor_1"),
     ("ldd_texto_valor_2","ldd_texto_valor_3")]   
   
class ListaSenalesCalculadasInlineAdmin(admin.StackedInline):
    extra=0
    model=ListaSenalesCalculadas
    fk_name='lsc_tag'
############# SEGURAMENTE HABRA QUE METERLE SU PROPIO FORMULARIO COMO A LAS LIMITE VARIABLES #####################

class LimiteVariableForm(forms.ModelForm):        
    class Meta:
        model=ListaSenalesLimitevariables
        fields=["lsl_tag","lsl_alarma","lsl_dia","lsl_mes","lsl_valor"]       

    def clean(self): #formulario
        if self.data['listasenaleslimitevariables_set-0-pk'] is None:
            pass
        if self.data['listasenaleslimitevariables_set-0-pk'] == "":            
            pk=f"({self.cleaned_data['lsl_tag'].lr_codigo},{self.cleaned_data['lsl_alarma']},{self.cleaned_data['lsl_mes']})"            
            self.data['listasenaleslimitevariables_set-0-pk'] = pk
        else:
            pk= self.data['listasenaleslimitevariables_set-0-pk']    
        cleaned_data=super().clean()
        cleaned_data['pk']=pk
        self.errors.pop('pk', None)
        return(cleaned_data)

class ListaSenalesLimiteVariableInlineAdmin(admin.TabularInline):    
    model=ListaSenalesLimitevariables
    extra=0
    form=LimiteVariableForm    
       

################################################ INLINES PARA ESTACION #################################################################
class ListaRemotasInlineAdmin(admin.StackedInline):
    model=ListaRemotas
    empty_value_display = "-"
    fieldsets=[("Datos Globales",
        {
            "fields" : [("lr_codigo","lr_tipo_estacion"),
                        ("lr_nombre_corto","lr_nombre"),
                        ("lr_estacion","lr_tag_comunica"),
                        ("lr_remota_fisica","lr_remota_principal"),
                        ("lr_infoplus","lr_saih_saica","lr_conf_remota","lr_tiene_pluv"),            
                        ("lr_zona","lr_rio")]

        }
    )]
    #list_display=["lr_codigo_txt","lr_nombre","tipo","estacion"]
    #inlines=[ListaRemotasConfsInlineAdmin,ListaRemotasTarjetasInlineAdmin,ListaSenalesInlineAdmin]
    extra=0
    readonly_fields=('lr_codigo','lr_tipo_estacion','lr_zona','lr_rio')
    #empty_value_display = "-"
    show_change_link=True


    @admin.display(ordering="lr_tipo_estacion")
    def tipo(self,obj):
        return obj.lr_tipo_estacion

    @admin.display(ordering="lr_estacion_id")
    def estacion(self,obj):
        return obj.lr_estacion

    def __init__(self,parent_model,admin_site):
        super().__init__(parent_model,admin_site)
        #pp(self.__dict__)

    def get_formset(self,request,obj=None,**kwargs):
        formset=super().get_formset(request,obj,**kwargs)
        #pp(formset.form.__dict__)
        #pp(obj.__dict__)
        #if(obj.)
        return formset


'''
############################################################################################################################################
                                                                    Admins
#########################################################################################################################################
'''

class ListaSenalesAdmin(admin.ModelAdmin):
    empty_value_display = "-"
    readonly_fields = ["ls_tag"]
    fieldsets=[("Datos Globales",
        {
            "fields" : [("ls_tag_txt"),("ls_tipo_senal","ls_descripcion","ls_origen","ls_naturaleza"),("ls_fews","ls_conf_scada","ls_conf_remota","ls_conf_historia","ls_ver_intranet","ls_ver_web","ls_ver_pda","ls_marca_cons")]
        }
    ),(
        "Datos generales",
        {
            "fields" : [("ls_remota"),("ls_clase_senal","ls_tipo_alarma","ls_fuente"),("ls_factor_manual","ls_columna","ls_orden"),("ls_min_grafico","ls_max_grafico","ls_tiempo_grafico")]
        }
    )]
    list_display=["ls_tag_txt","ls_descripcion","ls_remota__lr_estacion"]
    #inlines=[ListaSenalesAnalogicasInlineAdmin,ListaSenalesDigitalesInlineAdmin,ListaSenalesDobleDigitalesInlineAdmin]
    list_filter=["ls_naturaleza"] 
    show_facets = admin.ShowFacets.ALWAYS
    search_fields = ["ls_tag_txt","ls_descripcion"]   
    actions = [traspaso_a_intranet,traspaso_a_historica]
    
    @admin.display(ordering="ls_remota__lr_estacion")
    def estacion(self,obj):
        return obj.ls_remota.lr_estacion

    
    def get_inlines(self,request, obj=None):    
        inlines=[]
        if obj==None:
            return inlines    
        if obj.ls_naturaleza.ns_codigo==1:
            inlines.append(ListaSenalesAnalogicasInlineAdmin)
        elif obj.ls_naturaleza.ns_codigo==2:
            inlines.append(ListaSenalesDigitalesInlineAdmin)
        elif obj.ls_naturaleza.ns_codigo==3:
            inlines.append(ListaSenalesDobleDigitalesInlineAdmin)
        if(ListaSenalesCalculadas.objects.filter(lsc_tag=obj.ls_tag)):
            inlines.append(ListaSenalesCalculadasInlineAdmin)        
        if(ListaSenalesLimitevariables.objects.filter(lsl_tag=obj.ls_tag)):
            inlines.append(ListaSenalesLimiteVariableInlineAdmin)
        return inlines

    def save_model(self, request, obj, form, change):
        ultimo_id =  ListaSenales.objects.aggregate(Max('ls_tag'))['ls_tag__max']        
        ultimo_recid_hist = models_hist.ListaSenales_H.objects.aggregate(Max('ls_tag'))['ls_tag__max']        
        ultimo_recid_gest = ListaSenales.objects.aggregate(Max('ls_recid'))['ls_recid__max']        
        if change: #Update
            obj.ls_modif=datetime.now()
        else: #Insert
            obj.ls_falta=datetime.now()    
            obj.ls_tag=ultimo_id+1
            obj.ls_recid=max(ultimo_recid_hist,ultimo_recid_gest) +1
        super().save_model(request, obj, form, change)

    actions = [traspaso_a_intranet,traspaso_a_historica,borrar_de_intranet,borrar_de_historica]        

    #def save_related(self,request, form, formsets, change):
    #    super().save_related(request, form, formsets, change)   
    #    print(form.instance)



class ListaRemotasAdmin(admin.ModelAdmin):
    empty_value_display = "-"
    #form=ListaRemotasForm
    
    fieldsets=[("Datos Globales",
        {
            "fields" : [#("lr_codigo_txt","lr_tipo_estacion"),
                        ("lr_nombre_corto","lr_nombre"),
                        ("lr_estacion","lr_tag_comunica"),
                        ("lr_remota_fisica","lr_remota_principal"),
                        ("lr_infoplus","lr_saih_saica","lr_conf_remota","lr_tiene_pluv")]
        }
    ),(
        "Ubicacion",
        {
            "fields" : [#("lr_zona","lr_rio"),
                        ("lr_utm_huso","lr_utm_x","lr_utm_y","lr_utm_z"),
                        ("lr_cota_estacion","lr_longitud"),
                        ("lr_superficie","lr_vol_max"),
                        ("lr_cota_men","lr_cota_max"),
                        ("lr_cota_lecho","lr_tiempo_concentracion"),
                        ("lr_cota_toma"),]
        }
    )]
    list_display=["lr_codigo_txt","lr_nombre","tipo","estacion"]
    inlines=[ListaRemotasConfsInlineAdmin,ListaRemotasTarjetasInlineAdmin,ListaSenalesInlineAdmin,ListaOrdenesInlineAdmin]
    actions = [traspaso_a_intranet,traspaso_a_historica,borrar_de_intranet,borrar_de_historica]

    def save_model(self, request, obj, form, change):        
        if change:
            obj.lr_fmodif=datetime.now()
        else:
            obj.lr_falta=datetime.now()            
        super().save_model(request, obj, form, change) 

    #def save_related(self,request, form, formsets, change):
    #    print("SAVING RELATED...")
    #    super().save_related(request,form,formsets,change)    

    @admin.display(ordering="lr_tipo_estacion")
    def tipo(self,obj):
        return obj.lr_tipo_estacion

    @admin.display(ordering="lr_estacion_id")
    def estacion(self,obj):
        return obj.lr_estacion

    search_fields = ["lr_codigo_txt","lr_nombre","lr_estacion__le_codigo_txt"]    




class ListaEstacionesAdmin(admin.ModelAdmin):    
    fieldsets=[("Datos Globales",
        {
            "fields" : [("le_codigo_txt","le_tipo_estacion","le_codigo_ant","le_codigo_saica"),
                        ("le_nombre_corto","le_nombre"),
                        ("le_superficie","le_tipo_sensor","le_tipologia"),
                        ("le_infoplus","le_datos_manuales","le_datos_automaticos","le_ver_web","le_ver_intranet",),
                        ("le_ver_pda","le_fuera_servicio","le_bloquear","le_ver_estadisticas","le_ver_codigo_roea",)]
        }
    ),(
        "Ubicacion",
        {            
            "fields" : [("le_zona","le_rio"),
                        ("le_utm_huso","le_utm_x","le_utm_y","le_utm_z"),
            ]                        
        }
    ),]

    masa_agua=(
        "Masa de agua",
        {            
            "fields" : [("le_masa_codigo","le_masa_nombre"),
                        ("le_masa_categoria","le_masa_naturaleza"),
                        ("le_masa_est_eco","le_masa_est_quim"),
                        ("le_masa_est_glob","le_masa_tipo")
            ]                        
        }
    )

    list_display=["le_codigo_txt","le_nombre","tipo"]
    list_filter=["le_tipo_estacion"] 
    search_fields = ["le_codigo_txt","le_nombre",]    
    inlines=[ListaRemotasInlineAdmin]
    show_facets = admin.ShowFacets.ALWAYS
    actions = [traspaso_a_intranet,traspaso_a_historica,borrar_de_intranet,borrar_de_historica]

    def get_fieldsets(self,request,obj=None):        
        #if obj==None:
        #    return [(None,{"":[]})]
        fieldsets=self.fieldsets.copy()    
        if obj and obj.le_tipo_estacion.te_codigo!='M' and obj.le_tipo_estacion.te_codigo!='P':
            fieldsets=self.fieldsets.copy()
            fieldsets.append(self.masa_agua)
        return fieldsets


    def save_model(self, request, obj, form, change):
        print("Guardando estacion")
        ultimo_id =  ListaEstaciones.objects.aggregate(Max('le_codigo'))['le_codigo__max']
        ultimo_recid_hist = models_hist.ListaEstaciones_H.objects.aggregate(Max('le_codigo'))['le_codigo__max']                
        ultimo_recid_gest = ListaEstaciones.objects.aggregate(Max('le_codigo'))['le_codigo__max']                
        print(f"ultimo_id: {ultimo_id}")        
        if change:
            obj.le_fmodif=datetime.now()
        else:
            obj.le_codigo=ultimo_id+1
            obj.le_recid=max(ultimo_recid_hist,ultimo_recid_gest) +1
            obj.le_falta=datetime.now()  
        super().save_model(request, obj, form, change)    

    def save_related(self,request, form,formsets, change):
        #pp(formsets[0].__dict__)
        total_forms=formsets[0].data["listaremotas_set-TOTAL_FORMS"][0]       
        #pp(formsets[0].data)

        for i in range(int(total_forms)):
            if formsets[0].data[f"listaremotas_set-{i}-lr_codigo"]=='': #INSERT
                print("INSERT!!\n")
                formsets[0].data[f"listaremotas_set-{i}-lr_falta"]=[datetime.now()]
                ultimo_id =  ListaEstaciones.objects.aggregate(Max('le_codigo'))['le_codigo__max']
                print(f"ultimo_id: {ultimo_id}")        
                formsets[0].data[f"listaremotas_set-{i}-lr_codigo"]=ultimo_id+1                
            else:
                formsets[0].data[f"listaremotas_set-{i}-lr_fmodif"]=datetime.now()                
        #pp(formsets[0].__dict__)
        super().save_related(request,form,formsets,change)    



    '''def save_model(self, request, obj, form, change):        
        if change:
            obj.lr_fmodif=datetime.now()
        else:
            obj.lr_falta=datetime.now()            
        super().save_model(request, obj, form, change) 
    '''

    @admin.display(ordering="lr_tipo_estacion")
    def tipo(self,obj):
        return obj.le_tipo_estacion

class ListaOrdenesAdmin(admin.ModelAdmin):
    fieldsets=[(
        "Datos Globales",
        {"fields":[("lo_tipo_orden","lo_tag_txt"),("lo_descripcion"),("lo_conf_scada","lo_conf_remota","lo_conf_historia")]}
    ),(
        "Datos Generales",
        {"fields":[("lo_remota","lo_origen","lo_num_senal"),("lo_texto_valor_0","lo_texto_valor_1")]}
    ),(
        "Configuración Orden",
        {"fields":["lo_tarjeta","lo_entrada","lo_modo","lo_tiempo","lo_tipo_contacto"]}
    )]
    list_display=["lo_tag_txt","lo_descripcion","lo_tipo_orden","lo_remota"]
    search_fields = ["lo_tag_txt","lo_descripcion",]    

    def save_model(self, request, obj, form, change):        
        if change:
            obj.lo_fmodif=datetime.now()
        else:
            ultimo_id =  ListaOrdenes.objects.aggregate(Max('lo_tag'))['lo_tag__max']
            obj.lo_tag=ultimo_id+1
            obj.lo_falta=datetime.now()    
        super().save_model(request, obj, form, change)
'''

class FactoresConversionRemotaAdmin(admin.ModelAdmin):
    list_editable=[ "fc_descripcion","fc_x1","fc_x2","fc_x3","fc_x4","fc_ui_rango_bajo","fc_ui_rango_alto","fc_decimal"]
    list_display=[ "fc_codigo","fc_descripcion","fc_x1","fc_x2","fc_x3","fc_x4","fc_ui_rango_bajo","fc_ui_rango_alto","fc_decimal"]    
    list_display_links=[]

    def save_model(self, request, obj, form, change):        
        if change:
            obj.fc_fmodif=datetime.now()
        else:
            ultimo_id =  FactoresConversionRemota.objects.aggregate(Max('fc_codigo'))['fc_codigo__max']
            obj.fc_tag=ultimo_id+1
            obj.fc_falta=datetime.now()    
        super().save_model(request, obj, form, change)

class FormatosDigitalesAdmin(admin.ModelAdmin):
    list_editable=["fd_estado0","fd_estado1","fd_estado2","fd_estado3","fd_hay_estado0","fd_hay_estado1"]
    list_display=["fd_formato_valor","fd_estado0","fd_estado1","fd_estado2","fd_estado3","fd_hay_estado0","fd_hay_estado1"]
    list_display_links=[]


    def save_model(self, request, obj, form, change):        
        if change:
            obj.fd_fmodif=datetime.now()
        else:
            obj.fd_falta=datetime.now()    
        super().save_model(request, obj, form, change)
'''

class TiposSenalesAdmin(admin.ModelAdmin):
    list_display=["ts_codigo","ts_descripcion","ts_naturaleza","ts_nombre_corto","ts_orden","ts_acumula","ts_grupo_web"]
    list_editable=["ts_descripcion","ts_naturaleza","ts_nombre_corto","ts_orden","ts_acumula","ts_grupo_web"]
    list_display_links=[]
    list_filter=["ts_naturaleza"] 
    actions = [traspaso_a_intranet,borrar_de_intranet,traspaso_a_historica,borrar_de_historica]

    def save_model(self, request, obj, form, change):        
        if change:
            obj.ts_fmodif=datetime.now()
        else:
            obj.ts_falta=datetime.now()    
        super().save_model(request, obj, form, change)

class UnidadesIngenieriaAdmin(admin.ModelAdmin):
    list_display=["ui_codigo","ui_descripcion","ui_codigo_corto","ui_orden"]   
    list_editable=["ui_descripcion","ui_codigo_corto","ui_orden"]   
    list_display_links=[]
    actions = [traspaso_a_intranet,borrar_de_intranet]

    def save_model(self, request, obj, form, change):        
        if change:
            obj.ui_fmodif=datetime.now()
        else:
            obj.ui_falta=datetime.now()    
        super().save_model(request, obj, form, change)

class RiosAdmin(admin.ModelAdmin):
    actions = [traspaso_a_intranet,borrar_de_intranet,traspaso_a_historica,borrar_de_historica]
    list_display=["ri_codigo","ri_descripcion"]   
    list_editable=["ri_descripcion"]
    def save_model(self, request, obj, form, change):        
        if change:
            obj.ri_fmodif=datetime.now()
        else:
            obj.ri_falta=datetime.now()    
        super().save_model(request, obj, form, change)   


class PoblacionesAdmin(admin.ModelAdmin):
    list_display=["po_codigo","po_descripcion","po_provincia"]
    search_fields = ["po_descripcion"]    
    list_editable=["po_descripcion","po_provincia"]
    actions = [traspaso_a_intranet,borrar_de_intranet,traspaso_a_historica,borrar_de_historica]

    def save_model(self, request, obj, form, change):        
        if change:
            obj.po_fmodif=datetime.now()
        else:
            obj.po_falta=datetime.now()    
        super().save_model(request, obj, form, change)


'''
admin.site.register(ListaEstaciones,ListaEstacionesAdmin)
admin.site.register(ListaSenales,ListaSenalesAdmin)
admin.site.register(ListaRemotas,ListaRemotasAdmin)
admin.site.register(ListaOrdenes,ListaOrdenesAdmin)
admin.site.register(Rios)
admin.site.register(Poblaciones,PoblacionesAdmin)
admin.site.register(FactoresConversionRemota,FactoresConversionRemotaAdmin)
admin.site.register(FormatosDigitales,FormatosDigitalesAdmin)
admin.site.register(TiposSenales,TiposSenalesAdmin)
admin.site.register(UnidadesIngenieria,UnidadesIngenieriaAdmin)
'''

#Campos principales
gestor_admin_site.register(ListaEstaciones,ListaEstacionesAdmin)
gestor_admin_site.register(ListaSenales,ListaSenalesAdmin)
gestor_admin_site.register(ListaRemotas,ListaRemotasAdmin)
gestor_admin_site.register(ListaOrdenes,ListaOrdenesAdmin)
#gestor_admin_site.register(auth_views.UserModel)
#Otros
#####INTRANET + HISTORICA
#gestor_admin_site.register(Poblaciones,PoblacionesAdmin)
#gestor_admin_site.register(Rios)
#gestor_admin_site.register(TiposSenales,TiposSenalesAdmin)
#Solo Intranet
#gestor_admin_site.register(UnidadesIngenieria,UnidadesIngenieriaAdmin)


#### INFOPLUS
#gestor_admin_site.register(ListaOrdenes,ListaOrdenesAdmin)
#gestor_admin_site.register(FactoresConversionRemota,FactoresConversionRemotaAdmin)
#gestor_admin_site.register(FormatosDigitales,FormatosDigitalesAdmin)
