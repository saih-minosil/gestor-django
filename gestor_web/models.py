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


