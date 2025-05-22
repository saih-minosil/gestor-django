from django.db import models
from .models_comun import copy_object,copy_from_different_object, ListaZonas,Provincias,Poblaciones,TiposConsolidacion,NaturalezaSenales,TiposEstaciones,Rios,Comunidades


####################################################################################################################################################################
############################################################ CAMPOS CHOICES #####################################################################################
##################################################################################################################################################################
'''
choice_comunidades={1:"ANDALUCIA" ,2:"ARAGON" ,3:"ASTURIAS" ,4:"ILLES BALEARS" ,5:"CANARIAS" ,6:"CANTABRIA" ,7:"CASTILLA-LEON" ,8:"CASTILLA-LA MANCHA" ,9:"CATALUÑA" ,10:"CEUTA",
                    11:"EXTREMADURA" ,  12:"GALICIA" ,13:"MADRID" ,14:"MELILLA" ,15:"MURCIA" ,16:"NAVARRA" ,17:"PAIS VASCO" ,18:"RIOJA" ,19:"VALENCIA" ,60:"ANDORRA"}
choice_zonas={1:"MIÑO ALTO" ,2:"MIÑO BAJO" ,3:"SIL SUPERIOR" ,4:"SIL INFERIOR" ,5:"CABE" ,6:"LIMIA" ,11:"GALICIA COSTA" ,13:"CASTILLA Y LEÓN" ,14:"CANTÁBRICO" }
choice_actividades={1:"Docencia / Investigación" ,2:"Administraciones Públicas" ,3:"Generación Energía" ,4:"Estudiantes" ,5:"Deportes / Ocio (Medio Natural)" ,
                    6:"Consultorías / Ingenierías" ,7:"Empresas Obra Civil" ,8:"Particulares" ,99:"Otros"}
choice_rios={1:"ARENTEIRO" ,2:"ARNOIA" ,3:"AVIA" ,4:"AYO. BARREDOS" ,5:"AZUMARA" ,6:"BIBEI" ,7:"BOEZA" ,8:"BURBIA" ,9:"CABE" ,10:"CABRERA" ,11:"CALDO" ,12:"CAMBA" ,13:"CUA" ,15:"XARES" ,
             16:"LADRA" ,17:"LIMIA" ,18:"LOR" ,19:"LOURO" ,20:"MAO" ,21:"MIÑO" ,22:"NARLA" ,23:"NEIRA" ,24:"PARGA" ,25:"SALAS" ,26:"SARRIA" ,27:"SELMO" ,28:"SER" ,29:"SIL" ,30:"TEA" ,
             31:"UMA" ,32:"VALSECO" ,36:"DEVA" ,59:"CARES" ,74:"XALLAS" ,75:"COBO" ,76:"ORDUNTE" ,78:"FORCADAS" ,80:"VEDUIDO" ,81:"EUME" ,82:"TAMBRE" ,84:"ULLA" ,86:"CENZA" ,87:"NAVEA" ,
             88:"EDRADA" ,90:"OITAVEN" ,91:"LOÑA" ,95:"MERO" ,98:"ANLLO" ,99:"FERREIRA" ,100:"BARXAS" ,101:"TREMOR" ,102:"LABRADA" ,103:"CONSO" ,104:"CABO" ,105:"AYO. BRAÑA" ,
             106:"ORALLO" ,107:"REGO DE MOREDA" ,108:"BUBAL" ,109:"ASMA" ,110:"PESQUEIRAS" ,111:"LOUREIRO" ,112:"REGO DO MUIÑO" ,113:"LEIRA" ,114:"CERVES" ,115:"EDO" ,116:"BARBANTIÑO" ,
             117:"FRAGOSO" ,118:"DO FOXO" ,119:"TUÑO" ,120:"CEREIXO" ,121:"PONTE DE ENVIANDE" ,122:"CHAMOSO" ,123:"BAYO" ,124:"VALCARCE" ,125:"QUIROGA" ,126:"CARBALLO" ,127:"EIRÓS" ,
             128:"CERNADO" ,129:"PONTICELA" ,130:"CASOIO" ,131:"DURRIA" ,132:"LA SEITA" ,133:"MATALAVILLA" ,134:"SALENTINOS" ,135:"VALDEINFIERNO" ,136:"SIETERRABOS" ,137:"CAMPO" ,
             138:"VALDEPRADO" ,139:"NOCEDA" ,140:"SAN MIGUEL" ,141:"RABAL" ,142:"VALDUEZA" ,143:"VIÑAO" ,144:"BARRA" ,145:"VILLAR" ,146:"VALDESIRGAS" ,147:"AYO. RIAL" ,148:"SAÁ" ,
             149:"TAMUXE" ,150:"LOBIOS" ,}       

choice_tipos_estaciones={
"A":"AFORO" ,"AB":"ABASTECIMIENTO" ,"C":"CONDUCCION O TRASVASE" ,"CH":"CONCESION HIDROELECTRICA" ,"E":"EMBALSE" ,"EM":"EMBALSE MANUAL" ,"M":"ESTACION METEOROLOGICA" ,
"N":"NIVEL" ,"P":"PUNTO PLUVIOMETRICO" ,"Q":"ESTACION DE CALIDAD" ,"R":"ZONA REGABLE" ,"V":"VERTIDO" ,"ZM":"PIEZOMETRO " }   

choice_tipos_almacenamiento={"0505":"Cincominutal" ,"0515":"Cincominutal con almacenamiento quinceminutal" ,"1010":"Cada 10 minutos" ,"1515":"Quinceminutal" ,
                             "2424":"Cada 24 horas" ,"3030":"Cada 30 minutos" ,"6060":"Cada 60 minutos" }     

choice_tipos_calidades={
1:"Validado" ,2:"Bueno" ,3:"No Dato " ,4:"Mala" ,5:"Deficiente Grado 1" ,6:"Deficiente Grado 2" ,7:"Deficiente Grado 3" ,8:"Deficiente Grado 4"}                                

choice_naturalezas={1:"Analógica" ,2:"Digital" ,3:"Digital Doble"}
'''
choice_grupos_tipos_senales={
    "C":"Caudales" ,"E":"Embalses" ,"M":"Meteorologicas" ,"N":"Niveles" ,"O":"Otras" ,"P":"Pluviometria" ,"Q":"Calidad" ,
}

#################################################################################################################################
############################################## LISTAS NO TAN SIMPLES ############################################################
#################################################################################################################################
'''
class ListaPersonas(models.Model):
    lp_codigo = models.IntegerField(db_column='LP_CODIGO', primary_key=True)  # Field name made lowercase.
    lp_nombre = models.CharField(db_column='LP_NOMBRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lp_nif = models.CharField(db_column='LP_NIF', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lp_direccion = models.CharField(db_column='LP_DIRECCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lp_cp = models.CharField(db_column='LP_CP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lp_poblacion = models.IntegerField(db_column='LP_POBLACION', blank=True, null=True)  # Field name made lowercase.
    lp_provincia = models.SmallIntegerField(db_column='LP_PROVINCIA', blank=True, null=True)  # Field name made lowercase.
    lp_telefono1 = models.CharField(db_column='LP_TELEFONO1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lp_telefono2 = models.CharField(db_column='LP_TELEFONO2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lp_movil1 = models.CharField(db_column='LP_MOVIL1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lp_movil2 = models.CharField(db_column='LP_MOVIL2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lp_tipo_perso = models.CharField(db_column='LP_TIPO_PERSO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lp_cargo = models.CharField(db_column='LP_CARGO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lp_correo = models.CharField(db_column='LP_CORREO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'LISTA_PERSONAS'
'''
class UnidadesIngenieria(models.Model):
    ui_codigo = models.CharField(db_column='UI_CODIGO', primary_key=True, max_length=10)  # Field name made lowercase.
    ui_descripcion = models.CharField(db_column='UI_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ui_codigo_corto = models.CharField(db_column='UI_CODIGO_CORTO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ui_orden = models.SmallIntegerField(db_column='UI_ORDEN', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'UNIDADES_INGENIERIA'

class TiposSenales(models.Model):
    ts_codigo = models.CharField(db_column='TS_CODIGO', max_length=5, primary_key=True)  # Field name made lowercase.
    ts_descripcion = models.CharField(db_column='TS_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ts_naturaleza = models.SmallIntegerField(db_column='TS_NATURALEZA')  # Field name made lowercase.
    ts_nombre_corto = models.CharField(db_column='TS_NOMBRE_CORTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ts_orden = models.SmallIntegerField(db_column='TS_ORDEN', blank=True, null=True)  # Field name made lowercase.
    ts_acumula = models.SmallIntegerField(db_column='TS_ACUMULA', blank=True, null=True)  # Field name made lowercase.
    ts_grupo_web = models.CharField(db_column='TS_GRUPO_WEB', max_length=5, blank=True, null=True,choices=choice_grupos_tipos_senales)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_SENALES'
    #    unique_together = (('ts_codigo', 'ts_naturaleza'),)

    def __str__(self):
        return str(self.ts_nombre_corto)       

        
                   

#########################################################################################################################################
######################################### LISTAS PRINCIPALES  ###########################################################################
#########################################################################################################################################
#######################################(ESTACIONES Y SEÑALES #######)####################################################################
#########################################################################################################################################


class ListaEstaciones_I(models.Model):
    le_codigo_txt = models.CharField(db_column='LE_CODIGO_TXT', primary_key=True, max_length=4)  # Field name made lowercase.
    le_tipo_estacion = models.ForeignKey(TiposEstaciones,db_column='LE_TIPO_ESTACION', max_length=2,verbose_name="Tipo de Estacion",on_delete=models.DO_NOTHING)	  # Field name made lowercase.
    le_zona = models.ForeignKey(ListaZonas,on_delete=models.DO_NOTHING,db_column="LE_ZONA")
    le_nombre = models.CharField(db_column='LE_NOMBRE', max_length=30)  # Field name made lowercase.
    le_nombre_corto = models.CharField(db_column='LE_NOMBRE_CORTO', max_length=18)  # Field name made lowercase.
    le_comu_auto = models.ForeignKey(Comunidades, on_delete=models.DO_NOTHING, db_column="LE_COMU_AUTO",verbose_name="Comunidad autonoma")	    
    le_provincia = models.ForeignKey(Provincias, on_delete=models.DO_NOTHING, db_column="LE_PROVINCIA")
    le_municipio = models.ForeignKey(Poblaciones, on_delete=models.DO_NOTHING, db_column="LE_MUNICIPIO")
    le_rio = models.ForeignKey(Rios, on_delete=models.DO_NOTHING, db_column="LE_RIO",verbose_name="Rio")	
    le_utm_huso = models.IntegerField(db_column='LE_UTM_HUSO', blank=True, null=True)  # Field name made lowercase.
    le_utm_x = models.DecimalField(db_column='LE_UTM_X', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_utm_y = models.DecimalField(db_column='LE_UTM_Y', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_utm_z = models.DecimalField(db_column='LE_UTM_Z', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_ver_web = models.SmallIntegerField(db_column='LE_VER_WEB', blank=True, null=True)  # Field name made lowercase.
    le_ver_intranet = models.SmallIntegerField(db_column='LE_VER_INTRANET', blank=True, null=True)  # Field name made lowercase.
    le_ver_pda = models.SmallIntegerField(db_column='LE_VER_PDA', blank=True, null=True)  # Field name made lowercase.
    le_estado = models.SmallIntegerField(db_column='LE_ESTADO', blank=True, null=True)  # Field name made lowercase.
    le_vol_max = models.DecimalField(db_column='LE_VOL_MAX', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_cota_coronacion = models.DecimalField(db_column='LE_COTA_CORONACION', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_cota_nmn = models.DecimalField(db_column='LE_COTA_NMN', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_cota_nap = models.DecimalField(db_column='LE_COTA_NAP', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_cota_nae = models.DecimalField(db_column='LE_COTA_NAE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_cota_max = models.DecimalField(db_column='LE_COTA_MAX', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_superficie = models.DecimalField(db_column='LE_SUPERFICIE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_tipologia = models.CharField(db_column='LE_TIPOLOGIA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    le_tipo_sensor = models.CharField(db_column='LE_TIPO_SENSOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    le_codigo_roea = models.CharField(db_column='LE_CODIGO_ROEA', max_length=6, blank=True, null=True)  # Field name made lowercase.
    le_ver_codigo_roea = models.SmallIntegerField(db_column='LE_VER_CODIGO_ROEA', blank=True, null=True)  # Field name made lowercase.
    le_ver_estadisticas = models.SmallIntegerField(db_column='LE_VER_ESTADISTICAS', blank=True, null=True)  # Field name made lowercase.
    le_codigo_saica = models.CharField(db_column='LE_CODIGO_SAICA', max_length=4, blank=True, null=True)  # Field name made lowercase.
    le_h29_x = models.DecimalField(db_column='LE_H29_X', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_h29_y = models.DecimalField(db_column='LE_H29_Y', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_h29_z = models.DecimalField(db_column='LE_H29_Z', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_expediente = models.CharField(db_column='LE_EXPEDIENTE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    le_titular_concesion = models.IntegerField(db_column='LE_TITULAR_CONCESION', blank=True, null=True)  # Field name made lowercase.
    le_fecha_concesion = models.DateTimeField(db_column='LE_FECHA_CONCESION', blank=True, null=True)  # Field name made lowercase.
    le_ffin_obras = models.DateTimeField(db_column='LE_FFIN_OBRAS', blank=True, null=True)  # Field name made lowercase.
    le_arrendatario = models.DecimalField(db_column='LE_ARRENDATARIO', max_digits=6, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    le_registroseg = models.CharField(db_column='LE_REGISTROSEG', max_length=30, blank=True, null=True)  # Field name made lowercase.
    le_riesgopotencial = models.CharField(db_column='LE_RIESGOPOTENCIAL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    le_fnormasexp = models.DateTimeField(db_column='LE_FNORMASEXP', blank=True, null=True)  # Field name made lowercase.
    le_fclasificacion = models.DateTimeField(db_column='LE_FCLASIFICACION', blank=True, null=True)  # Field name made lowercase.
    le_faprobacion_pe = models.DateTimeField(db_column='LE_FAPROBACION_PE', blank=True, null=True)  # Field name made lowercase.
    le_fimplantacion_pe = models.DateTimeField(db_column='LE_FIMPLANTACION_PE', blank=True, null=True)  # Field name made lowercase.
    le_puntosaviso = models.DecimalField(db_column='LE_PUNTOSAVISO', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    le_director_pe = models.CharField(db_column='LE_DIRECTOR_PE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    le_represante_pe = models.CharField(db_column='LE_REPRESANTE_PE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    le_direccion_cc = models.CharField(db_column='LE_DIRECCION_CC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    le_telefono_cc = models.CharField(db_column='LE_TELEFONO_CC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    le_fax_cc = models.CharField(db_column='LE_FAX_CC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    le_correo_cc = models.CharField(db_column='LE_CORREO_CC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    le_masa_codigo = models.CharField(db_column='LE_MASA_CODIGO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    le_masa_nombre = models.CharField(db_column='LE_MASA_NOMBRE', max_length=70, blank=True, null=True)  # Field name made lowercase.
    le_masa_categoria = models.CharField(db_column='LE_MASA_CATEGORIA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    le_masa_naturaleza = models.CharField(db_column='LE_MASA_NATURALEZA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    le_masa_est_eco = models.CharField(db_column='LE_MASA_EST_ECO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    le_masa_est_quim = models.CharField(db_column='LE_MASA_EST_QUIM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    le_masa_est_glob = models.CharField(db_column='LE_MASA_EST_GLOB', max_length=30, blank=True, null=True)  # Field name made lowercase.
    le_masa_tipo = models.CharField(db_column='LE_MASA_TIPO', max_length=70, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_ESTACIONES'

    def __str__(self):
        return str(self.le_nombre)  

    def from_gestor(self,obj):
        copy_object(orig=obj,dest=self)
        #self.le_tipo_estacion=obj.le_tipo_estacion_id
        #self.le_zona=obj.le_zona_id
        #self.le_comu_auto=obj.le_comu_auto_id
        #self.le_rio=obj.le_rio_id
        self.le_codigo_roea=obj.le_codigo_ant
        #copy_from_different_object(orig=obj_lsa,dest=self,orig_prefix="lsa",dest_prefix="ls")
        #self.ls_estacion_txt=estacion
        #alarma,tendencia          

class ListaSenales_I(models.Model):
    ls_tag_txt = models.CharField(db_column='LS_TAG_TXT', primary_key=True, max_length=16)  # Field name made lowercase.
    ls_descripcion = models.CharField(db_column='LS_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ls_estacion_txt =  models.ForeignKey(ListaEstaciones_I,db_column='LS_ESTACION_TXT', on_delete=models.DO_NOTHING)
    ls_tipo_senal = models.ForeignKey(TiposSenales,db_column='LS_TIPO_SENAL', on_delete=models.DO_NOTHING)
    ls_naturaleza = models.ForeignKey(NaturalezaSenales, models.DO_NOTHING, db_column='LS_NATURALEZA', blank=True, null=True)  # Field name made lowercase.
    ls_recid = models.IntegerField(db_column='LS_RECID', blank=True, null=True)  # Field name made lowercase.
    ls_origen = models.CharField(db_column='LS_ORIGEN', max_length=10, blank=True,         null=True)  # Field name made lowercase.
    ls_tipo_consolidacion = models.ForeignKey(TiposConsolidacion, models.DO_NOTHING, db_column='LS_TIPO_CONSOLIDACION', blank=True, null=True)  # Field name made lowercase.
    ls_max_grafico = models.FloatField(db_column='LS_MAX_GRAFICO', blank=True, null=True)  # Field name made lowercase.
    ls_min_grafico = models.FloatField(db_column='LS_MIN_GRAFICO', blank=True, null=True)  # Field name made lowercase.
    ls_tiempo_grafico = models.CharField(db_column='LS_TIEMPO_GRAFICO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ls_unid_ing = models.ForeignKey(UnidadesIngenieria,db_column='LS_UNID_ING', on_delete=models.DO_NOTHING)  # Field name made lowercase.
    ls_digitos_enteros = models.SmallIntegerField(db_column='LS_DIGITOS_ENTEROS', blank=True, null=True)  # Field name made lowercase.
    ls_digitos_decimales = models.SmallIntegerField(db_column='LS_DIGITOS_DECIMALES', blank=True, null=True)  # Field name made lowercase.
    ls_tipo_almacenamiento = models.CharField(db_column='LS_TIPO_ALMACENAMIENTO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_alarma = models.CharField(db_column='LS_ALARMA', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ls_tendencia = models.CharField(db_column='LS_TENDENCIA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ls_ver_web = models.SmallIntegerField(db_column='LS_VER_WEB', blank=True, null=True)  # Field name made lowercase.
    ls_ver_intranet = models.SmallIntegerField(db_column='LS_VER_INTRANET', blank=True, null=True)  # Field name made lowercase.
    ls_ver_pda = models.SmallIntegerField(db_column='LS_VER_PDA', blank=True, null=True)  # Field name made lowercase.
    ls_lim_alto_alto_alto = models.FloatField(db_column='LS_LIM_ALTO_ALTO_ALTO', blank=True, null=True)  # Field name made lowercase.
    ls_lim_alto_alto = models.FloatField(db_column='LS_LIM_ALTO_ALTO', blank=True, null=True)  # Field name made lowercase.
    ls_lim_alto = models.FloatField(db_column='LS_LIM_ALTO', blank=True, null=True)  # Field name made lowercase.
    ls_ver_web_a = models.SmallIntegerField(db_column='LS_VER_WEB_A', blank=True, null=True)  # Field name made lowercase.
    ls_ver_web_aa = models.SmallIntegerField(db_column='LS_VER_WEB_AA', blank=True, null=True)  # Field name made lowercase.
    ls_ver_web_aaa = models.SmallIntegerField(db_column='LS_VER_WEB_AAA', blank=True, null=True)  # Field name made lowercase.
    ls_ver_intranet_a = models.SmallIntegerField(db_column='LS_VER_INTRANET_A', blank=True, null=True)  # Field name made lowercase.
    ls_ver_intranet_aa = models.SmallIntegerField(db_column='LS_VER_INTRANET_AA', blank=True, null=True)  # Field name made lowercase.
    ls_ver_intranet_aaa = models.SmallIntegerField(db_column='LS_VER_INTRANET_AAA', blank=True, null=True)  # Field name made lowercase.
    ls_ver_pda_a = models.SmallIntegerField(db_column='LS_VER_PDA_A', blank=True, null=True)  # Field name made lowercase.
    ls_ver_pda_aa = models.SmallIntegerField(db_column='LS_VER_PDA_AA', blank=True, null=True)  # Field name made lowercase.
    ls_ver_pda_aaa = models.SmallIntegerField(db_column='LS_VER_PDA_AAA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_SENALES'

    def __str__(self):
        return str(self.ls_tag_txt) + " : " + str(self.ls_descripcion)

    def from_gestor(self,obj_ls,obj_lsa,estacion):
        copy_object(orig=obj_ls,dest=self)
        copy_from_different_object(orig=obj_lsa,dest=self,orig_prefix="lsa",dest_prefix="ls")
        self.ls_estacion_txt=estacion
        #alarma,tendencia


class ListaEstacionesRemotas_I(models.Model):
    lr_codigo_txt = models.CharField(db_column='LR_CODIGO_TXT', primary_key=True, max_length=4)  # Field name made lowercase.
    lr_superficie = models.DecimalField(db_column='LR_SUPERFICIE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_coronacion = models.DecimalField(db_column='LR_COTA_CORONACION', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_altura_cauce = models.DecimalField(db_column='LR_ALTURA_CAUCE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_altura_cimientos = models.DecimalField(db_column='LR_ALTURA_CIMIENTOS', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_min_epl = models.DecimalField(db_column='LR_COTA_MIN_EPL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_vol_min_epl = models.DecimalField(db_column='LR_VOL_MIN_EPL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_nmn = models.DecimalField(db_column='LR_COTA_NMN', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_vol_nmn = models.DecimalField(db_column='LR_VOL_NMN', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_nap = models.DecimalField(db_column='LR_COTA_NAP', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_vol_nap = models.DecimalField(db_column='LR_VOL_NAP', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_caudal_nap = models.DecimalField(db_column='LR_CAUDAL_NAP', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_nae = models.DecimalField(db_column='LR_COTA_NAE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_caudal_nae = models.DecimalField(db_column='LR_CAUDAL_NAE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_vol_util = models.DecimalField(db_column='LR_VOL_UTIL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_caudal_punta = models.DecimalField(db_column='LR_CAUDAL_PUNTA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_fcaudal_punta = models.DateTimeField(db_column='LR_FCAUDAL_PUNTA', blank=True, null=True)  # Field name made lowercase.
    lr_hipotesis_qnap = models.CharField(db_column='LR_HIPOTESIS_QNAP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lr_hipotesis_qnae = models.CharField(db_column='LR_HIPOTESIS_QNAE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lr_resguardo_nmn = models.DecimalField(db_column='LR_RESGUARDO_NMN', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_superficie_nmn = models.DecimalField(db_column='LR_SUPERFICIE_NMN', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_longitud_emb = models.DecimalField(db_column='LR_LONGITUD_EMB', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_longitud_coronacion = models.DecimalField(db_column='LR_LONGITUD_CORONACION', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_ESTACIONES_REMOTAS'

    def __str__(self):
        return str(self.lr_codigo_txt)

    
###########################


########################################################### DATOS ###############################################################

#### ___________________________ DE LA INTRANET (15MIUNTALES Y HORARIOS) ___________________________________________________######
class DatosHorarios(models.Model):
    pk = models.CompositePrimaryKey('ho_tag_txt', 'ho_fecha_hora')
    ho_tag_txt = models.ForeignKey(ListaSenales_I,db_column='HO_TAG_TXT', on_delete=models.PROTECT)  # Field name made lowercase.
    ho_fecha_hora = models.DateTimeField(db_column='HO_FECHA_HORA')  # Field name made lowercase.
    ho_valor_horario = models.FloatField(db_column='HO_VALOR_HORARIO', blank=True, null=True)  # Field name made lowercase.
    ho_calidad = models.SmallIntegerField(db_column='HO_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_HORARIOS'
        unique_together = (('ho_tag_txt', 'ho_fecha_hora'),)


class DatosQuinceminutales(models.Model):
    pk = models.CompositePrimaryKey('ho_tag_txt', 'ho_fecha_hora')
    ho_tag_txt = models.ForeignKey(ListaSenales_I,db_column='HO_TAG_TXT', on_delete=models.PROTECT)  # Field name made lowercase.
    ho_fecha_hora = models.DateTimeField(db_column='HO_FECHA_HORA')  # Field name made lowercase.
    ho_valor_horario = models.FloatField(db_column='HO_VALOR_HORARIO', blank=True, null=True)  # Field name made lowercase.
    ho_calidad = models.SmallIntegerField(db_column='HO_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_QUINCEMINUTALES'
        #unique_together = (('ho_tag_txt', 'ho_fecha_hora'),)

'''
class ConsDia(models.Model):
    pk = models.CompositePrimaryKey('cc_idsenal', 'cc_fecha')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor_min = models.FloatField(db_column='CC_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
    cc_f_valor_min = models.DateTimeField(db_column='CC_F_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_max = models.FloatField(db_column='CC_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
    cc_f_valor_max = models.DateTimeField(db_column='CC_F_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
    cc_valor_ultimo = models.FloatField(db_column='CC_VALOR_ULTIMO', blank=True, null=True)  # Field name made lowercase.
    cc_valor_gradiente = models.FloatField(db_column='CC_VALOR_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.ForeignKey('TiposCalidades', models.DO_NOTHING, db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_porcen = models.FloatField(db_column='CC_PORCEN', blank=True, null=True)  # Field name made lowercase.
    cc_f_gradiente = models.DateTimeField(db_column='CC_F_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
    cc_volumen = models.FloatField(db_column='CC_VOLUMEN', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'CONS_DIA'
        unique_together = (('cc_idsenal', 'cc_fecha'),)
    def __str__(self):
        return str(self.cc_idsenal) + "." + str(self.cc_fecha)


class ConsMes(models.Model):
    pk = models.CompositePrimaryKey('cc_idsenal', 'cc_fecha')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor_min = models.FloatField(db_column='CC_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
    cc_f_valor_min = models.DateTimeField(db_column='CC_F_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_max = models.FloatField(db_column='CC_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
    cc_f_valor_max = models.DateTimeField(db_column='CC_F_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
    cc_valor_ultimo = models.FloatField(db_column='CC_VALOR_ULTIMO', blank=True, null=True)  # Field name made lowercase.
    cc_valor_gradiente = models.FloatField(db_column='CC_VALOR_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.ForeignKey('TiposCalidades', models.DO_NOTHING, db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_porcen = models.FloatField(db_column='CC_PORCEN', blank=True, null=True)  # Field name made lowercase.
    cc_f_gradiente = models.DateTimeField(db_column='CC_F_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
    cc_volumen = models.FloatField(db_column='CC_VOLUMEN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONS_MES'
        unique_together = (('cc_idsenal', 'cc_fecha'),)
'''
