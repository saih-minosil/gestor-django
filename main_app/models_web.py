from django.db import models
from .models_comun import copy_object,copy_from_different_object, ListaZonas,Provincias,Poblaciones,TiposConsolidacion,NaturalezaSenales,TiposEstaciones,Rios,Comunidades
from .models_intranet import TiposSenales, UnidadesIngenieria
############### REPETIDOS DE LA INTRANET ############################################################

class ListaEstaciones_W(models.Model):
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

class ListaSenales_W(models.Model):
    ls_tag_txt = models.CharField(db_column='LS_TAG_TXT', primary_key=True, max_length=16)  # Field name made lowercase.
    ls_descripcion = models.CharField(db_column='LS_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ls_estacion_txt =  models.ForeignKey(ListaEstaciones_W,db_column='LS_ESTACION_TXT', on_delete=models.DO_NOTHING)
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
    ls_alarma = models.CharField(db_column='LS_ALARMA', max_length=12, blank=True, null=True,default='NORMAL')  # Field name made lowercase.
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


class ListaEstacionesRemotas_W(models.Model):
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

class DatosHorarios_Web(models.Model):
    pk = models.CompositePrimaryKey('ho_tag_txt', 'ho_fecha_hora')
    ho_tag_txt = models.ForeignKey(ListaSenales_W,db_column='HO_TAG_TXT', on_delete=models.PROTECT)  # Field name made lowercase.
    ho_fecha_hora = models.DateTimeField(db_column='HO_FECHA_HORA')  # Field name made lowercase.
    ho_valor_horario = models.FloatField(db_column='HO_VALOR_HORARIO', blank=True, null=True)  # Field name made lowercase.
    ho_calidad = models.SmallIntegerField(db_column='HO_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_HORARIOS'
        unique_together = (('ho_tag_txt', 'ho_fecha_hora'),)


class DatosQuinceminutales_Web(models.Model):
    pk = models.CompositePrimaryKey('ho_tag_txt', 'ho_fecha_hora')
    ho_tag_txt = models.ForeignKey(ListaSenales_W,db_column='HO_TAG_TXT', on_delete=models.PROTECT)  # Field name made lowercase.
    ho_fecha_hora = models.DateTimeField(db_column='HO_FECHA_HORA')  # Field name made lowercase.
    ho_valor_horario = models.FloatField(db_column='HO_VALOR_HORARIO', blank=True, null=True)  # Field name made lowercase.
    ho_calidad = models.SmallIntegerField(db_column='HO_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_QUINCEMINUTALES'
        #unique_together = (('ho_tag_txt', 'ho_fecha_hora'),)
