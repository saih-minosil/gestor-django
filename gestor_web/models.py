from django.db import models

########################################################################################################################
##############################################     WEB       ##############################################################
########################################################################################################################
class TiposCajetines(models.Model):
    tc_codigo = models.SmallIntegerField(db_column='TC_CODIGO', primary_key=True)  # Field name made lowercase.
    tc_ancho_tag = models.SmallIntegerField(db_column='TC_ANCHO_TAG', blank=True,
                                            null=True)  # Field name made lowercase.
    tc_alto_tag = models.SmallIntegerField(db_column='TC_ALTO_TAG', blank=True,
                                           null=True)  # Field name made lowercase.
    tc_tags_fila = models.SmallIntegerField(db_column='TC_TAGS_FILA', blank=True,
                                            null=True)  # Field name made lowercase.
    tc_filas = models.SmallIntegerField(db_column='TC_FILAS', blank=True, null=True)  # Field name made lowercase.
    tc_falta = models.DateTimeField(db_column='TC_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    tc_fmodif = models.DateTimeField(db_column='TC_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TIPOS_CAJETINES'


class MapasWeb(models.Model):
    mw_entorno = models.SmallIntegerField(db_column='MW_ENTORNO', primary_key=True)  # Field name made lowercase. The composite primary key (MW_ENTORNO, MW_CODIGO) found, that is not supported. The first column is selected.
    mw_codigo = models.CharField(db_column='MW_CODIGO', max_length=3)  # Field name made lowercase.
    mw_utm_x = models.FloatField(db_column='MW_UTM_X', blank=True, null=True)  # Field name made lowercase.
    mw_utm_y = models.FloatField(db_column='MW_UTM_Y', blank=True, null=True)  # Field name made lowercase.
    mw_utms_por_pixel = models.FloatField(db_column='MW_UTMS_POR_PIXEL', blank=True, null=True)  # Field name made lowercase.
    mw_descripcion = models.CharField(db_column='MW_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mw_falta = models.DateTimeField(db_column='MW_FALTA', blank=True, null=True)  # Field name made lowercase.
    mw_fmodif = models.DateTimeField(db_column='MW_FMODIF', blank=True, null=True)  # Field name made lowercase.
    mw_confederacion = models.SmallIntegerField(db_column='MW_CONFEDERACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAPAS_WEB'
        unique_together = (('mw_entorno', 'mw_codigo'),)


class CajetinesUnifilares(models.Model):
    pk = models.CompositePrimaryKey("cu_codigo_mapa", "cu_estacion_txt")
    #cu_codigo_mapa = models.CharField(db_column='CU_CODIGO_MAPA',  max_length=3)  # Field name made lowercase. The composite primary key (CU_CODIGO_MAPA, CU_ESTACION_TXT) found, that is not supported. The first column is selected.
    cu_codigo_mapa = models.ForeignKey(MapasWeb,db_column='CU_CODIGO_MAPA', on_delete=models.DO_NOTHING)
    cu_estacion_txt = models.CharField(db_column='CU_ESTACION_TXT', max_length=4)  # Field name made lowercase.
    cu_icono_x = models.SmallIntegerField(db_column='CU_ICONO_X', blank=True, null=True)  # Field name made lowercase.
    cu_icono_y = models.SmallIntegerField(db_column='CU_ICONO_Y', blank=True, null=True)  # Field name made lowercase.
    cu_nombre_x = models.SmallIntegerField(db_column='CU_NOMBRE_X', blank=True, null=True)  # Field name made lowercase.
    cu_nombre_y = models.SmallIntegerField(db_column='CU_NOMBRE_Y', blank=True, null=True)  # Field name made lowercase.
    cu_tag = models.IntegerField(db_column='CU_TAG', blank=True, null=True)  # Field name made lowercase.
    cu_posicion_tag = models.SmallIntegerField(db_column='CU_POSICION_TAG', blank=True, null=True)  # Field name made lowercase.
    cu_lado_enlace = models.CharField(db_column='CU_LADO_ENLACE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cu_ver_mapa = models.SmallIntegerField(db_column='CU_VER_MAPA', blank=True, null=True)  # Field name made lowercase.
    cu_falta = models.DateTimeField(db_column='CU_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    cu_fmodif = models.DateTimeField(db_column='CU_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAJETINES_UNIFILARES'
        unique_together = (('cu_codigo_mapa', 'cu_estacion_txt'),)

    def __str__(self):
        return str(self.cu_codigo_mapa) + '_' + str(self.cu_estacion_txt)


class CajetinesWeb(models.Model):
    pk = models.CompositePrimaryKey("cw_entorno", "cw_tipo_area", "cw_codigo_mapa","cw_estacion_txt")
    cw_entorno = models.SmallIntegerField(db_column='CW_ENTORNO')  # Field name made lowercase. The composite primary key (CW_ENTORNO, CW_TIPO_AREA, CW_CODIGO_MAPA, CW_ESTACION_TXT) found, that is not supported. The first column is selected.
    cw_tipo_area = models.CharField(db_column='CW_TIPO_AREA', max_length=3)  # Field name made lowercase.
    #cw_codigo_mapa = models.CharField(db_column='CW_CODIGO_MAPA', max_length=3)  # Field name made lowercase.
    cw_codigo_mapa = models.ForeignKey(MapasWeb, db_column='CW_CODIGO_MAPA', on_delete=models.DO_NOTHING)
    cw_estacion_txt = models.CharField(db_column='CW_ESTACION_TXT', max_length=4)  # Field name made lowercase.
    #cw_tipo_cajetin = models.SmallIntegerField(db_column='CW_TIPO_CAJETIN', blank=True, null=True)  # Field name made lowercase.
    cw_tipo_cajetin = models.ForeignKey(TiposCajetines,db_column='CW_TIPO_CAJETIN', on_delete=models.DO_NOTHING)  # Field name made lowercase.
    cw_x = models.FloatField(db_column='CW_X', blank=True, null=True)  # Field name made lowercase.
    cw_y = models.FloatField(db_column='CW_Y', blank=True, null=True)  # Field name made lowercase.
    cw_lado_enlace = models.CharField(db_column='CW_LADO_ENLACE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cw_tag_tendencia = models.IntegerField(db_column='CW_TAG_TENDENCIA', blank=True, null=True)  # Field name made lowercase.
    cw_ver_mapa = models.SmallIntegerField(db_column='CW_VER_MAPA', blank=True, null=True)  # Field name made lowercase.
    cw_falta = models.DateTimeField(db_column='CW_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    cw_fmodif = models.DateTimeField(db_column='CW_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAJETINES_WEB'
        unique_together = (('cw_entorno', 'cw_tipo_area', 'cw_codigo_mapa', 'cw_estacion_txt'),)


class CajetinesWebTags(models.Model):
    pk = models.CompositePrimaryKey("cwt_entorno", "cwt_tipo_area", "cwt_codigo_mapa", "cwt_estacion_txt","cwt_tag")
    cwt_entorno = models.SmallIntegerField(db_column='CWT_ENTORNO')  # Field name made lowercase. The composite primary key (CWT_ENTORNO, CWT_TIPO_AREA, CWT_CODIGO_MAPA, CWT_ESTACION_TXT, CWT_TAG) found, that is not supported. The first column is selected.
    cwt_tipo_area = models.CharField(db_column='CWT_TIPO_AREA', max_length=3)  # Field name made lowercase.
    #cwt_codigo_mapa = models.CharField(db_column='CWT_CODIGO_MAPA', max_length=3)  # Field name made lowercase.
    cwt_codigo_mapa = models.ForeignKey(MapasWeb, db_column='CWT_CODIGO_MAPA', on_delete=models.DO_NOTHING)
    cwt_estacion_txt = models.CharField(db_column='CWT_ESTACION_TXT', max_length=4)  # Field name made lowercase.
    cwt_tag = models.IntegerField(db_column='CWT_TAG')  # Field name made lowercase.
    cwt_numorden = models.SmallIntegerField(db_column='CWT_NUMORDEN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAJETINES_WEB_TAGS'
        unique_together = (('cwt_entorno', 'cwt_tipo_area', 'cwt_codigo_mapa', 'cwt_estacion_txt', 'cwt_tag'),)


class UsuariosWeb(models.Model):
    uw_nombreusuario = models.CharField(db_column='UW_NOMBREUSUARIO', primary_key=True, max_length=30)  # Field name made lowercase.
    uw_password = models.CharField(db_column='UW_PASSWORD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    uw_ciudad = models.CharField(db_column='UW_CIUDAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uw_provincia = models.CharField(db_column='UW_PROVINCIA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    uw_pais = models.CharField(db_column='UW_PAIS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    uw_email = models.CharField(db_column='UW_EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uw_actividad = models.SmallIntegerField(db_column='UW_ACTIVIDAD', blank=True, null=True)  # Field name made lowercase.
    uw_codigo_movil = models.CharField(db_column='UW_CODIGO_MOVIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    uw_estado = models.SmallIntegerField(db_column='UW_ESTADO', blank=True, null=True)  # Field name made lowercase.
    uw_acceso_datos_historicos = models.SmallIntegerField(db_column='UW_ACCESO_DATOS_HISTORICOS', blank=True, null=True)  # Field name made lowercase.
    uw_acceso_datos_quinceminutales = models.SmallIntegerField(db_column='UW_ACCESO_DATOS_QUINCEMINUTALES', blank=True, null=True)  # Field name made lowercase.
    uw_acceso_informes_privados = models.SmallIntegerField(db_column='UW_ACCESO_INFORMES_PRIVADOS', blank=True, null=True)  # Field name made lowercase.
    uw_acceso_administrador = models.SmallIntegerField(db_column='UW_ACCESO_ADMINISTRADOR', blank=True, null=True)  # Field name made lowercase.
    uw_observaciones = models.CharField(db_column='UW_OBSERVACIONES', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    uw_otra_actividad = models.CharField(db_column='UW_OTRA_ACTIVIDAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uw_falta = models.DateTimeField(db_column='UW_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    uw_fmodif = models.DateTimeField(db_column='UW_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.
    uw_fbaja = models.DateTimeField(db_column='UW_FBAJA', blank=True, null=True, editable=False)  # Field name made lowercase.
    uw_accesibilidad = models.SmallIntegerField(db_column='UW_ACCESIBILIDAD', blank=True, null=True)  # Field name made lowercase.
    uw_acceso_conf1 = models.SmallIntegerField(db_column='UW_ACCESO_CONF1', blank=True, null=True)  # Field name made lowercase.
    uw_acceso_conf2 = models.SmallIntegerField(db_column='UW_ACCESO_CONF2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIOS_WEB'


class TextosWeb(models.Model):
    tw_dominio = models.CharField(db_column='TW_DOMINIO', primary_key=True, max_length=50)  # Field name made lowercase. The composite primary key (TW_DOMINIO, TW_TIPO, TW_ITEM, TW_ORDEN) found, that is not supported. The first column is selected.
    tw_tipo = models.CharField(db_column='TW_TIPO', max_length=50)  # Field name made lowercase.
    tw_item = models.CharField(db_column='TW_ITEM', max_length=50)  # Field name made lowercase.
    tw_orden = models.SmallIntegerField(db_column='TW_ORDEN')  # Field name made lowercase.
    tw_texto_spa = models.CharField(db_column='TW_TEXTO_SPA', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    tw_texto_gal = models.CharField(db_column='TW_TEXTO_GAL', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    tw_texto_eus = models.CharField(db_column='TW_TEXTO_EUS', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    tw_es_html = models.SmallIntegerField(db_column='TW_ES_HTML', blank=True, null=True)  # Field name made lowercase.
    tw_falta = models.DateTimeField(db_column='TW_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    tw_fmodif = models.DateTimeField(db_column='TW_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TEXTOS_WEB'
        unique_together = (('tw_dominio', 'tw_tipo', 'tw_item', 'tw_orden'),)



########################################################################################################################
########################################################################################################################

class ListaEstaciones(models.Model):
    le_codigo = models.IntegerField(db_column='LE_CODIGO', primary_key=True)  # Field name made lowercase.
    le_codigo_txt = models.CharField(db_column='LE_CODIGO_TXT', max_length=4)  # Field name made lowercase.
    le_tipo_estacion = models.CharField(db_column='LE_TIPO_ESTACION', max_length=2)  # Field name made lowercase.
    le_bloquear = models.SmallIntegerField(db_column='LE_BLOQUEAR', blank=True, null=True)  # Field name made lowercase.
    le_zona = models.SmallIntegerField(db_column='LE_ZONA')  # Field name made lowercase.
    #le_zona = models.ForeignKey(ListaZonas,on_delete=models.DO_NOTHING,db_column="LE_ZONA")
    le_nombre = models.CharField(db_column='LE_NOMBRE', max_length=30)  # Field name made lowercase.
    le_nombre_corto = models.CharField(db_column='LE_NOMBRE_CORTO', max_length=18)  # Field name made lowercase.
    le_comu_auto = models.SmallIntegerField(db_column='LE_COMU_AUTO', blank=True, null=True)  # Field name made lowercase.
    #le_comu_auto = models.ForeignKey(Comunidades, on_delete=models.DO_NOTHING, db_column="LE_COMU_AUTO")
    le_provincia = models.SmallIntegerField(db_column='LE_PROVINCIA', blank=True, null=True)  # Field name made lowercase.
    #le_provincia = models.ForeignKey(Provincias, on_delete=models.DO_NOTHING, db_column="LE_PROVINCIA")
    le_municipio = models.IntegerField(db_column='LE_MUNICIPIO', blank=True, null=True)  # Field name made lowercase.
    #le_municipio = models.ForeignKey(Poblaciones, on_delete=models.DO_NOTHING, db_column="LE_MUNICIPIO")
    le_rio = models.IntegerField(db_column='LE_RIO', blank=True, null=True)  # Field name made lowercase.
    #le_rio= models.ForeignKey(Rios, on_delete=models.DO_NOTHING, db_column="LE_RIO")
    le_recid = models.IntegerField(db_column='LE_RECID', blank=True, null=True)  # Field name made lowercase.
    le_utm_huso = models.IntegerField(db_column='LE_UTM_HUSO', blank=True, null=True)  # Field name made lowercase.
    le_utm_x = models.DecimalField(db_column='LE_UTM_X', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_utm_y = models.DecimalField(db_column='LE_UTM_Y', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_utm_z = models.DecimalField(db_column='LE_UTM_Z', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_infoplus = models.SmallIntegerField(db_column='LE_INFOPLUS', blank=True, null=True)  # Field name made lowercase.
    le_ver_web = models.SmallIntegerField(db_column='LE_VER_WEB', blank=True, null=True)  # Field name made lowercase.
    le_ver_intranet = models.SmallIntegerField(db_column='LE_VER_INTRANET', blank=True, null=True)  # Field name made lowercase.
    le_datos_manuales = models.SmallIntegerField(db_column='LE_DATOS_MANUALES', blank=True, null=True)  # Field name made lowercase.
    le_datos_automaticos = models.SmallIntegerField(db_column='LE_DATOS_AUTOMATICOS', blank=True, null=True)  # Field name made lowercase.
    le_codigo_ant = models.CharField(db_column='LE_CODIGO_ANT', max_length=6, blank=True, null=True)  # Field name made lowercase.
    le_provee_info = models.CharField(db_column='LE_PROVEE_INFO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    le_tipo_dato = models.SmallIntegerField(db_column='LE_TIPO_DATO', blank=True, null=True)  # Field name made lowercase.
    le_datos_8h = models.SmallIntegerField(db_column='LE_DATOS_8H', blank=True, null=True)  # Field name made lowercase.
    le_datos_dm = models.SmallIntegerField(db_column='LE_DATOS_DM', blank=True, null=True)  # Field name made lowercase.
    le_posicion = models.SmallIntegerField(db_column='LE_POSICION', blank=True, null=True)  # Field name made lowercase.
    le_rangomes_1 = models.CharField(db_column='LE_RANGOMES_1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    le_rangomes_2 = models.CharField(db_column='LE_RANGOMES_2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    le_rangomes_3 = models.CharField(db_column='LE_RANGOMES_3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    le_rangomes_4 = models.CharField(db_column='LE_RANGOMES_4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    le_rangomes_5 = models.CharField(db_column='LE_RANGOMES_5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    le_rangomes_6 = models.CharField(db_column='LE_RANGOMES_6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    le_rangomes_7 = models.CharField(db_column='LE_RANGOMES_7', max_length=10, blank=True, null=True)  # Field name made lowercase.
    le_rangomes_8 = models.CharField(db_column='LE_RANGOMES_8', max_length=10, blank=True, null=True)  # Field name made lowercase.
    le_rangomes_9 = models.CharField(db_column='LE_RANGOMES_9', max_length=10, blank=True, null=True)  # Field name made lowercase.
    le_rangomes_10 = models.CharField(db_column='LE_RANGOMES_10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    le_rangomes_11 = models.CharField(db_column='LE_RANGOMES_11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    le_rangomes_12 = models.CharField(db_column='LE_RANGOMES_12', max_length=10, blank=True, null=True)  # Field name made lowercase.
    le_tipologia = models.CharField(db_column='LE_TIPOLOGIA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    le_tipo_sensor = models.CharField(db_column='LE_TIPO_SENSOR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    le_falta = models.DateTimeField(db_column='LE_FALTA', blank=True, null=True,editable=False)  # Field name made lowercase.
    le_fmodif = models.DateTimeField(db_column='LE_FMODIF', blank=True, null=True,editable=False)  # Field name made lowercase.
    le_fbaja = models.DateTimeField(db_column='LE_FBAJA', blank=True, null=True,editable=False)  # Field name made lowercase.
    #le_ver_pda = models.SmallIntegerField(db_column='LE_VER_PDA', blank=True, null=True)  # Field name made lowercase.
    le_superficie = models.DecimalField(db_column='LE_SUPERFICIE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_fuera_servicio = models.SmallIntegerField(db_column='LE_FUERA_SERVICIO', blank=True, null=True)  # Field name made lowercase.
    le_ver_estadisticas = models.SmallIntegerField(db_column='LE_VER_ESTADISTICAS', blank=True, null=True)  # Field name made lowercase.
    le_ver_codigo_roea = models.SmallIntegerField(db_column='LE_VER_CODIGO_ROEA', blank=True, null=True)  # Field name made lowercase.
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
        managed = True
        db_table = 'LISTA_ESTACIONES'

    def __str__(self):
        return str(self.le_codigo_txt) + " : " + str(self.le_nombre)

class ListaSenales(models.Model):
    ls_tag = models.IntegerField(db_column='LS_TAG', primary_key=True,editable=False)  # Field name made lowercase.
    ls_descripcion = models.CharField(db_column='LS_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ls_tag_txt = models.CharField(db_column='LS_TAG_TXT', max_length=16)  # Field name made lowercase.
    #ls_remota = models.ForeignKey(ListaRemotas, on_delete=models.CASCADE,db_column="ls_remota")
    ls_remota = models.IntegerField(db_column='LS_REMOTA')  # Field name made lowercase.
    ls_num_senal = models.IntegerField(db_column='LS_NUM_SENAL', blank=True, null=True)  # Field name made lowercase.
    ls_clase_senal = models.CharField(db_column='LS_CLASE_SENAL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_tipo_senal = models.CharField(db_column='LS_TIPO_SENAL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_tipo_alarma = models.SmallIntegerField(db_column='LS_TIPO_ALARMA', blank=True, null=True)  # Field name made lowercase.
    ls_naturaleza = models.SmallIntegerField(db_column='LS_NATURALEZA', blank=True, null=True)  # Field name made lowercase.
    ls_recid = models.IntegerField(db_column='LS_RECID', blank=True, null=True)  # Field name made lowercase.
    ls_recid_ch = models.IntegerField(db_column='LS_RECID_CH', blank=True, null=True)  # Field name made lowercase.
    ls_origen = models.CharField(db_column='LS_ORIGEN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ls_marca_cons = models.SmallIntegerField(db_column='LS_MARCA_CONS', blank=True, null=True)  # Field name made lowercase.

    ls_tipo_consolidacion = models.SmallIntegerField(db_column='LS_TIPO_CONSOLIDACION', blank=True, null=True)  # Field name made lowercase.
    ls_tag_cons_1 = models.IntegerField(db_column='LS_TAG_CONS_1', blank=True, null=True)  # Field name made lowercase.
    ls_tag_cons_2 = models.IntegerField(db_column='LS_TAG_CONS_2', blank=True, null=True)  # Field name made lowercase.
    ls_hora_cons = models.CharField(db_column='LS_HORA_CONS', max_length=5, blank=True, null=True, editable=False)  # Field name made lowercase.
    ls_curvaref = models.SmallIntegerField(db_column='LS_CURVAREF', blank=True, null=True)  # Field name made lowercase.
    ls_conf_remota = models.SmallIntegerField(db_column='LS_CONF_REMOTA', blank=True, null=True)  # Field name made lowercase.
    ls_conf_scada = models.SmallIntegerField(db_column='LS_CONF_SCADA', blank=True, null=True)  # Field name made lowercase.
    ls_conf_historia = models.SmallIntegerField(db_column='LS_CONF_HISTORIA', blank=True, null=True)  # Field name made lowercase.
    ls_min_grafico = models.FloatField(db_column='LS_MIN_GRAFICO', blank=True, null=True)  # Field name made lowercase.
    ls_max_grafico = models.FloatField(db_column='LS_MAX_GRAFICO', blank=True, null=True)  # Field name made lowercase.
    ls_tiempo_grafico = models.CharField(db_column='LS_TIEMPO_GRAFICO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ls_fuente = models.CharField(db_column='LS_FUENTE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_factor_manual = models.FloatField(db_column='LS_FACTOR_MANUAL', blank=True, null=True)  # Field name made lowercase.
    ls_columna = models.IntegerField(db_column='LS_COLUMNA', blank=True, null=True)  # Field name made lowercase.
    ls_orden = models.IntegerField(db_column='LS_ORDEN', blank=True, null=True)  # Field name made lowercase.
    ls_falta = models.DateTimeField(db_column='LS_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    ls_fmodif = models.DateTimeField(db_column='LS_FMODIF', blank=True, null=True,editable=False)  # Field name made lowercase.
    ls_fbaja = models.DateTimeField(db_column='LS_FBAJA', blank=True, null=True,editable=False)  # Field name made lowercase.
    ls_ver_web = models.SmallIntegerField(db_column='LS_VER_WEB', blank=True, null=True)  # Field name made lowercase.
    ls_ver_intranet = models.SmallIntegerField(db_column='LS_VER_INTRANET', blank=True, null=True)  # Field name made lowercase.
    ls_ver_pda = models.SmallIntegerField(db_column='LS_VER_PDA', blank=True, null=True)  # Field name made lowercase.
    ls_fews = models.SmallIntegerField(db_column='LS_FEWS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_SENALES'

    def __str__(self):
        return str(self.ls_tag_txt) + " : " + str(self.ls_descripcion)

