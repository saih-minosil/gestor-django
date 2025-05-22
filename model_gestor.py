# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


from django.db import models
class CajetinesUnifilares(models.Model):
    pk = models.CompositePrimaryKey('cu_codigo_mapa','cu_estacion_txt') #Composite key test
    cu_codigo_mapa = models.CharField(db_column='CU_CODIGO_MAPA', primary_key=True, max_length=3)  # Field name made lowercase. The composite primary key (CU_CODIGO_MAPA, CU_ESTACION_TXT) found, that is not supported. The first column is selected.
    cu_estacion_txt = models.CharField(db_column='CU_ESTACION_TXT', max_length=4)  # Field name made lowercase.
    cu_icono_x = models.SmallIntegerField(db_column='CU_ICONO_X', blank=True, null=True)  # Field name made lowercase.
    cu_icono_y = models.SmallIntegerField(db_column='CU_ICONO_Y', blank=True, null=True)  # Field name made lowercase.
    cu_nombre_x = models.SmallIntegerField(db_column='CU_NOMBRE_X', blank=True, null=True)  # Field name made lowercase.
    cu_nombre_y = models.SmallIntegerField(db_column='CU_NOMBRE_Y', blank=True, null=True)  # Field name made lowercase.
    cu_tag = models.IntegerField(db_column='CU_TAG', blank=True, null=True)  # Field name made lowercase.
    cu_posicion_tag = models.SmallIntegerField(db_column='CU_POSICION_TAG', blank=True, null=True)  # Field name made lowercase.
    cu_lado_enlace = models.CharField(db_column='CU_LADO_ENLACE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cu_ver_mapa = models.SmallIntegerField(db_column='CU_VER_MAPA', blank=True, null=True)  # Field name made lowercase.
    cu_falta = models.DateTimeField(db_column='CU_FALTA', blank=True, null=True)  # Field name made lowercase.
    cu_fmodif = models.DateTimeField(db_column='CU_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'CAJETINES_UNIFILARES'
        unique_together = (('cu_codigo_mapa', 'cu_estacion_txt'),)


class CajetinesWeb(models.Model):
    cw_entorno = models.SmallIntegerField(db_column='CW_ENTORNO', primary_key=True)  # Field name made lowercase. The composite primary key (CW_ENTORNO, CW_TIPO_AREA, CW_CODIGO_MAPA, CW_ESTACION_TXT) found, that is not supported. The first column is selected.
    cw_tipo_area = models.CharField(db_column='CW_TIPO_AREA', max_length=3)  # Field name made lowercase.
    cw_codigo_mapa = models.CharField(db_column='CW_CODIGO_MAPA', max_length=3)  # Field name made lowercase.
    cw_estacion_txt = models.CharField(db_column='CW_ESTACION_TXT', max_length=4)  # Field name made lowercase.
    cw_tipo_cajetin = models.SmallIntegerField(db_column='CW_TIPO_CAJETIN', blank=True, null=True)  # Field name made lowercase.
    cw_x = models.FloatField(db_column='CW_X', blank=True, null=True)  # Field name made lowercase.
    cw_y = models.FloatField(db_column='CW_Y', blank=True, null=True)  # Field name made lowercase.
    cw_lado_enlace = models.CharField(db_column='CW_LADO_ENLACE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cw_tag_tendencia = models.IntegerField(db_column='CW_TAG_TENDENCIA', blank=True, null=True)  # Field name made lowercase.
    cw_ver_mapa = models.SmallIntegerField(db_column='CW_VER_MAPA', blank=True, null=True)  # Field name made lowercase.
    cw_falta = models.DateTimeField(db_column='CW_FALTA', blank=True, null=True)  # Field name made lowercase.
    cw_fmodif = models.DateTimeField(db_column='CW_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'CAJETINES_WEB'
        unique_together = (('cw_entorno', 'cw_tipo_area', 'cw_codigo_mapa', 'cw_estacion_txt'),)


class CajetinesWebTags(models.Model):
    cwt_entorno = models.SmallIntegerField(db_column='CWT_ENTORNO', primary_key=True)  # Field name made lowercase. The composite primary key (CWT_ENTORNO, CWT_TIPO_AREA, CWT_CODIGO_MAPA, CWT_ESTACION_TXT, CWT_TAG) found, that is not supported. The first column is selected.
    cwt_tipo_area = models.CharField(db_column='CWT_TIPO_AREA', max_length=3)  # Field name made lowercase.
    cwt_codigo_mapa = models.CharField(db_column='CWT_CODIGO_MAPA', max_length=3)  # Field name made lowercase.
    cwt_estacion_txt = models.CharField(db_column='CWT_ESTACION_TXT', max_length=4)  # Field name made lowercase.
    cwt_tag = models.IntegerField(db_column='CWT_TAG')  # Field name made lowercase.
    cwt_numorden = models.SmallIntegerField(db_column='CWT_NUMORDEN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'CAJETINES_WEB_TAGS'
        unique_together = (('cwt_entorno', 'cwt_tipo_area', 'cwt_codigo_mapa', 'cwt_estacion_txt', 'cwt_tag'),)


class Comunidades(models.Model):
    ca_codigo = models.SmallIntegerField(db_column='CA_CODIGO', primary_key=True, db_comment='Codigo de la comunidad autonoma')  # Field name made lowercase.
    ca_descripcion = models.CharField(db_column='CA_DESCRIPCION', max_length=50, blank=True, null=True, db_comment='Nombre de la comunidad autonom')  # Field name made lowercase.
    ca_falta = models.DateTimeField(db_column='CA_FALTA', blank=True, null=True)  # Field name made lowercase.
    ca_fmodif = models.DateTimeField(db_column='CA_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMUNIDADES'


class FactoresConversion(models.Model):
    fc_codigo = models.CharField(db_column='FC_CODIGO', primary_key=True, max_length=20)  # Field name made lowercase.
    fc_descripcion = models.CharField(db_column='FC_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fc_min_campo = models.FloatField(db_column='FC_MIN_CAMPO', blank=True, null=True)  # Field name made lowercase.
    fc_max_campo = models.FloatField(db_column='FC_MAX_CAMPO', blank=True, null=True)  # Field name made lowercase.
    fc_min_scada = models.FloatField(db_column='FC_MIN_SCADA', blank=True, null=True)  # Field name made lowercase.
    fc_max_scada = models.FloatField(db_column='FC_MAX_SCADA', blank=True, null=True)  # Field name made lowercase.
    fc_falta = models.DateTimeField(db_column='FC_FALTA', blank=True, null=True)  # Field name made lowercase.
    fc_fmodif = models.DateTimeField(db_column='FC_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FACTORES_CONVERSION'


class FactoresConversionRemota(models.Model):
    fc_codigo = models.CharField(db_column='FC_CODIGO', primary_key=True, max_length=10)  # Field name made lowercase.
    fc_descripcion = models.CharField(db_column='FC_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fc_x1 = models.FloatField(db_column='FC_X1', blank=True, null=True)  # Field name made lowercase.
    fc_x2 = models.FloatField(db_column='FC_X2', blank=True, null=True)  # Field name made lowercase.
    fc_x3 = models.FloatField(db_column='FC_X3', blank=True, null=True)  # Field name made lowercase.
    fc_x4 = models.FloatField(db_column='FC_X4', blank=True, null=True)  # Field name made lowercase.
    fc_ui_rango_bajo = models.FloatField(db_column='FC_UI_RANGO_BAJO', blank=True, null=True)  # Field name made lowercase.
    fc_ui_rango_alto = models.FloatField(db_column='FC_UI_RANGO_ALTO', blank=True, null=True)  # Field name made lowercase.
    fc_decimal = models.SmallIntegerField(db_column='FC_DECIMAL', blank=True, null=True)  # Field name made lowercase.
    fc_falta = models.DateTimeField(db_column='FC_FALTA', blank=True, null=True)  # Field name made lowercase.
    fc_fmodif = models.DateTimeField(db_column='FC_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FACTORES_CONVERSION_REMOTA'


class FormatosDigitales(models.Model):
    fd_estado0 = models.CharField(db_column='FD_ESTADO0', primary_key=True, max_length=24)  # Field name made lowercase. The composite primary key (FD_ESTADO0, FD_ESTADO1) found, that is not supported. The first column is selected.
    fd_estado1 = models.CharField(db_column='FD_ESTADO1', max_length=24)  # Field name made lowercase.
    fd_estado2 = models.CharField(db_column='FD_ESTADO2', max_length=24, blank=True, null=True)  # Field name made lowercase.
    fd_estado3 = models.CharField(db_column='FD_ESTADO3', max_length=24, blank=True, null=True)  # Field name made lowercase.
    fd_formato_valor = models.CharField(db_column='FD_FORMATO_VALOR', max_length=16, blank=True, null=True)  # Field name made lowercase.
    fd_hay_estado0 = models.SmallIntegerField(db_column='FD_HAY_ESTADO0', blank=True, null=True)  # Field name made lowercase.
    fd_hay_estado1 = models.SmallIntegerField(db_column='FD_HAY_ESTADO1', blank=True, null=True)  # Field name made lowercase.
    fd_falta = models.DateTimeField(db_column='FD_FALTA', blank=True, null=True)  # Field name made lowercase.
    fd_fmodif = models.DateTimeField(db_column='FD_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FORMATOS_DIGITALES'
        unique_together = (('fd_estado0', 'fd_estado1'),)

class GruposTiposSenales(models.Model):
    gs_codigo = models.CharField(db_column='GS_CODIGO', primary_key=True, max_length=5)  # Field name made lowercase.
    gs_descripcion = models.CharField(db_column='GS_DESCRIPCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gs_orden = models.SmallIntegerField(db_column='GS_ORDEN', blank=True, null=True)  # Field name made lowercase.
    gs_falta = models.DateTimeField(db_column='GS_FALTA', blank=True, null=True)  # Field name made lowercase.
    gs_fmodif = models.DateTimeField(db_column='GS_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GRUPOS_TIPOS_SENALES'


class ListaEstaciones(models.Model):
    le_codigo = models.IntegerField(db_column='LE_CODIGO', primary_key=True)  # Field name made lowercase.
    le_codigo_txt = models.CharField(db_column='LE_CODIGO_TXT', max_length=4)  # Field name made lowercase.
    le_tipo_estacion = models.CharField(db_column='LE_TIPO_ESTACION', max_length=2)  # Field name made lowercase.
    le_bloquear = models.SmallIntegerField(db_column='LE_BLOQUEAR', blank=True, null=True)  # Field name made lowercase.
    le_zona = models.SmallIntegerField(db_column='LE_ZONA')  # Field name made lowercase.
    le_nombre = models.CharField(db_column='LE_NOMBRE', max_length=30)  # Field name made lowercase.
    le_nombre_corto = models.CharField(db_column='LE_NOMBRE_CORTO', max_length=18)  # Field name made lowercase.
    le_comu_auto = models.SmallIntegerField(db_column='LE_COMU_AUTO', blank=True, null=True)  # Field name made lowercase.
    le_provincia = models.SmallIntegerField(db_column='LE_PROVINCIA', blank=True, null=True)  # Field name made lowercase.
    le_municipio = models.IntegerField(db_column='LE_MUNICIPIO', blank=True, null=True)  # Field name made lowercase.
    le_rio = models.IntegerField(db_column='LE_RIO', blank=True, null=True)  # Field name made lowercase.
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
    le_falta = models.DateTimeField(db_column='LE_FALTA', blank=True, null=True)  # Field name made lowercase.
    le_fmodif = models.DateTimeField(db_column='LE_FMODIF', blank=True, null=True)  # Field name made lowercase.
    le_fbaja = models.DateTimeField(db_column='LE_FBAJA', blank=True, null=True)  # Field name made lowercase.
    le_ver_pda = models.SmallIntegerField(db_column='LE_VER_PDA', blank=True, null=True)  # Field name made lowercase.
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


class ListaEstacionesAreas(models.Model):
    lea_codigo = models.IntegerField(db_column='LEA_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (LEA_CODIGO, LEA_AREA, LEA_NUMORDEN) found, that is not supported. The first column is selected.
    lea_area = models.CharField(db_column='LEA_AREA', max_length=3)  # Field name made lowercase.
    lea_numorden = models.SmallIntegerField(db_column='LEA_NUMORDEN')  # Field name made lowercase.
    lea_tag = models.IntegerField(db_column='LEA_TAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_ESTACIONES_AREAS'
        unique_together = (('lea_codigo', 'lea_area', 'lea_numorden'),)


class ListaEstacionesCaudales(models.Model):
    lq_codigo = models.IntegerField(db_column='LQ_CODIGO', primary_key=True)  # Field name made lowercase.
    lq_control_qe = models.CharField(db_column='LQ_CONTROL_QE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lq_control_qc = models.CharField(db_column='LQ_CONTROL_QC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lq_control_qu = models.CharField(db_column='LQ_CONTROL_QU', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lq_control_qt = models.CharField(db_column='LQ_CONTROL_QT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lq_dispositivos_qe = models.CharField(db_column='LQ_DISPOSITIVOS_QE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lq_fe_resolucion_dv = models.DateTimeField(db_column='LQ_FE_RESOLUCION_DV', blank=True, null=True)  # Field name made lowercase.
    lq_mes1_dv = models.DecimalField(db_column='LQ_MES1_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes2_dv = models.DecimalField(db_column='LQ_MES2_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes3_dv = models.DecimalField(db_column='LQ_MES3_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes4_dv = models.DecimalField(db_column='LQ_MES4_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes5_dv = models.DecimalField(db_column='LQ_MES5_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes6_dv = models.DecimalField(db_column='LQ_MES6_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes7_dv = models.DecimalField(db_column='LQ_MES7_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes8_dv = models.DecimalField(db_column='LQ_MES8_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes9_dv = models.DecimalField(db_column='LQ_MES9_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes10_dv = models.DecimalField(db_column='LQ_MES10_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes11_dv = models.DecimalField(db_column='LQ_MES11_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes12_dv = models.DecimalField(db_column='LQ_MES12_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_porce_dv = models.DecimalField(db_column='LQ_PORCE_DV', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lq_fe_resolucion_eco = models.DateTimeField(db_column='LQ_FE_RESOLUCION_ECO', blank=True, null=True)  # Field name made lowercase.
    lq_mes1_eco = models.DecimalField(db_column='LQ_MES1_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes2_eco = models.DecimalField(db_column='LQ_MES2_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes3_eco = models.DecimalField(db_column='LQ_MES3_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes4_eco = models.DecimalField(db_column='LQ_MES4_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes5_eco = models.DecimalField(db_column='LQ_MES5_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes6_eco = models.DecimalField(db_column='LQ_MES6_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes7_eco = models.DecimalField(db_column='LQ_MES7_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes8_eco = models.DecimalField(db_column='LQ_MES8_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes9_eco = models.DecimalField(db_column='LQ_MES9_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes10_eco = models.DecimalField(db_column='LQ_MES10_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes11_eco = models.DecimalField(db_column='LQ_MES11_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes12_eco = models.DecimalField(db_column='LQ_MES12_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_porce_eco = models.DecimalField(db_column='LQ_PORCE_ECO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lq_fe_bombeado = models.DateTimeField(db_column='LQ_FE_BOMBEADO', blank=True, null=True)  # Field name made lowercase.
    lq_qmax_concesion_b = models.DecimalField(db_column='LQ_QMAX_CONCESION_B', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_fe_escalapeces = models.DateTimeField(db_column='LQ_FE_ESCALAPECES', blank=True, null=True)  # Field name made lowercase.
    lq_qmax_ep = models.DecimalField(db_column='LQ_QMAX_EP', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_qmin_eq = models.DecimalField(db_column='LQ_QMIN_EQ', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_fe_trasvasado = models.DateTimeField(db_column='LQ_FE_TRASVASADO', blank=True, null=True)  # Field name made lowercase.
    lq_qmax_concesion_t = models.DecimalField(db_column='LQ_QMAX_CONCESION_T', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_observ_eco = models.CharField(db_column='LQ_OBSERV_ECO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lq_observ_dv = models.CharField(db_column='LQ_OBSERV_DV', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lq_observ_b = models.CharField(db_column='LQ_OBSERV_B', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lq_observ_t = models.CharField(db_column='LQ_OBSERV_T', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_ESTACIONES_CAUDALES'


class ListaEstacionesCaudales2(models.Model):
    lq_codigo = models.IntegerField(db_column='LQ_CODIGO')  # Field name made lowercase.
    lq_control_qe = models.CharField(db_column='LQ_CONTROL_QE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lq_control_qc = models.CharField(db_column='LQ_CONTROL_QC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lq_control_qu = models.CharField(db_column='LQ_CONTROL_QU', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lq_control_qt = models.CharField(db_column='LQ_CONTROL_QT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lq_dispositivos_qe = models.CharField(db_column='LQ_DISPOSITIVOS_QE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lq_fe_resolucion_dv = models.DateTimeField(db_column='LQ_FE_RESOLUCION_DV', blank=True, null=True)  # Field name made lowercase.
    lq_mes1_dv = models.DecimalField(db_column='LQ_MES1_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes2_dv = models.DecimalField(db_column='LQ_MES2_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes3_dv = models.DecimalField(db_column='LQ_MES3_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes4_dv = models.DecimalField(db_column='LQ_MES4_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes5_dv = models.DecimalField(db_column='LQ_MES5_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes6_dv = models.DecimalField(db_column='LQ_MES6_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes7_dv = models.DecimalField(db_column='LQ_MES7_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes8_dv = models.DecimalField(db_column='LQ_MES8_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes9_dv = models.DecimalField(db_column='LQ_MES9_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes10_dv = models.DecimalField(db_column='LQ_MES10_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes11_dv = models.DecimalField(db_column='LQ_MES11_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes12_dv = models.DecimalField(db_column='LQ_MES12_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_porce_dv = models.DecimalField(db_column='LQ_PORCE_DV', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lq_fe_resolucion_eco = models.DateTimeField(db_column='LQ_FE_RESOLUCION_ECO', blank=True, null=True)  # Field name made lowercase.
    lq_mes1_eco = models.DecimalField(db_column='LQ_MES1_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes2_eco = models.DecimalField(db_column='LQ_MES2_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes3_eco = models.DecimalField(db_column='LQ_MES3_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes4_eco = models.DecimalField(db_column='LQ_MES4_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes5_eco = models.DecimalField(db_column='LQ_MES5_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes6_eco = models.DecimalField(db_column='LQ_MES6_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes7_eco = models.DecimalField(db_column='LQ_MES7_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes8_eco = models.DecimalField(db_column='LQ_MES8_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes9_eco = models.DecimalField(db_column='LQ_MES9_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes10_eco = models.DecimalField(db_column='LQ_MES10_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes11_eco = models.DecimalField(db_column='LQ_MES11_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_mes12_eco = models.DecimalField(db_column='LQ_MES12_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_porce_eco = models.DecimalField(db_column='LQ_PORCE_ECO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lq_fe_bombeado = models.DateTimeField(db_column='LQ_FE_BOMBEADO', blank=True, null=True)  # Field name made lowercase.
    lq_qmax_concesion_b = models.DecimalField(db_column='LQ_QMAX_CONCESION_B', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_fe_escalapeces = models.DateTimeField(db_column='LQ_FE_ESCALAPECES', blank=True, null=True)  # Field name made lowercase.
    lq_qmax_ep = models.DecimalField(db_column='LQ_QMAX_EP', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_qmin_eq = models.DecimalField(db_column='LQ_QMIN_EQ', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_fe_trasvasado = models.DateTimeField(db_column='LQ_FE_TRASVASADO', blank=True, null=True)  # Field name made lowercase.
    lq_qmax_concesion_t = models.DecimalField(db_column='LQ_QMAX_CONCESION_T', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lq_observ_eco = models.CharField(db_column='LQ_OBSERV_ECO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lq_observ_dv = models.CharField(db_column='LQ_OBSERV_DV', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lq_observ_b = models.CharField(db_column='LQ_OBSERV_B', max_length=100, blank=True, null=True)  # Field name made lowercase.
    lq_observ_t = models.CharField(db_column='LQ_OBSERV_T', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_ESTACIONES_CAUDALES2'


class ListaEstacionesDerivaciones(models.Model):
    led_codigo = models.IntegerField(db_column='LED_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (LED_CODIGO, LED_TIPO_DERIVACION, LED_NOMBRE) found, that is not supported. The first column is selected.
    led_tipo_derivacion = models.CharField(db_column='LED_TIPO_DERIVACION', max_length=20)  # Field name made lowercase.
    led_nombre = models.CharField(db_column='LED_NOMBRE', max_length=20)  # Field name made lowercase.
    led_descripcion = models.CharField(db_column='LED_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    led_tipo_turbina = models.CharField(db_column='LED_TIPO_TURBINA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    led_qmax = models.DecimalField(db_column='LED_QMAX', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_qmin = models.DecimalField(db_column='LED_QMIN', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_potencia_nominal = models.DecimalField(db_column='LED_POTENCIA_NOMINAL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_qmax_entrada = models.DecimalField(db_column='LED_QMAX_ENTRADA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_potencia_total = models.DecimalField(db_column='LED_POTENCIA_TOTAL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_salto_bruto = models.DecimalField(db_column='LED_SALTO_BRUTO', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_produccion_media = models.DecimalField(db_column='LED_PRODUCCION_MEDIA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_h29_x_central = models.DecimalField(db_column='LED_H29_X_CENTRAL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_h29_y_central = models.DecimalField(db_column='LED_H29_Y_CENTRAL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_h29_z_central = models.DecimalField(db_column='LED_H29_Z_CENTRAL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_toma_tipo = models.CharField(db_column='LED_TOMA_TIPO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    led_toma_capacidad = models.DecimalField(db_column='LED_TOMA_CAPACIDAD', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_toma_cota = models.DecimalField(db_column='LED_TOMA_COTA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_toma_seccion = models.CharField(db_column='LED_TOMA_SECCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    led_toma_lon_canal = models.DecimalField(db_column='LED_TOMA_LON_CANAL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_toma_lon_tuberia = models.DecimalField(db_column='LED_TOMA_LON_TUBERIA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_toma_chimenea = models.CharField(db_column='LED_TOMA_CHIMENEA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    led_toma_corriente = models.CharField(db_column='LED_TOMA_CORRIENTE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    led_toma_provincia = models.CharField(db_column='LED_TOMA_PROVINCIA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    led_toma_municipio = models.CharField(db_column='LED_TOMA_MUNICIPIO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    led_toma_h29_x = models.DecimalField(db_column='LED_TOMA_H29_X', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_toma_h29_y = models.DecimalField(db_column='LED_TOMA_H29_Y', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_toma_h29_z = models.DecimalField(db_column='LED_TOMA_H29_Z', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_rest_corriente = models.CharField(db_column='LED_REST_CORRIENTE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    led_rest_provincia = models.CharField(db_column='LED_REST_PROVINCIA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    led_rest_municipio = models.CharField(db_column='LED_REST_MUNICIPIO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    led_rest_h29_x = models.DecimalField(db_column='LED_REST_H29_X', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_rest_h29_y = models.DecimalField(db_column='LED_REST_H29_Y', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_rest_h29_z = models.DecimalField(db_column='LED_REST_H29_Z', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_tipo_conduccion = models.CharField(db_column='LED_TIPO_CONDUCCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    led_seccion = models.CharField(db_column='LED_SECCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    led_lon_trasvase = models.DecimalField(db_column='LED_LON_TRASVASE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_capacidad = models.DecimalField(db_column='LED_CAPACIDAD', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_superficie = models.DecimalField(db_column='LED_SUPERFICIE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    led_poblaciones_ab = models.CharField(db_column='LED_POBLACIONES_AB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    led_habitantes_ab = models.CharField(db_column='LED_HABITANTES_AB', max_length=20, blank=True, null=True)  # Field name made lowercase.
    led_toma_secciontoma = models.CharField(db_column='LED_TOMA_SECCIONTOMA', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_ESTACIONES_DERIVACIONES'
        unique_together = (('led_codigo', 'led_tipo_derivacion', 'led_nombre'),)


class ListaEstacionesPresas(models.Model):
    lep_codigo = models.IntegerField(db_column='LEP_CODIGO', primary_key=True)  # Field name made lowercase.
    lep_tipo_explotacion = models.CharField(db_column='LEP_TIPO_EXPLOTACION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_tipo_presa = models.CharField(db_column='LEP_TIPO_PRESA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_granpresa = models.SmallIntegerField(db_column='LEP_GRANPRESA', blank=True, null=True)  # Field name made lowercase.
    lep_tipo_gestor = models.CharField(db_column='LEP_TIPO_GESTOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_registroseg = models.CharField(db_column='LEP_REGISTROSEG', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_riesgopotencial = models.CharField(db_column='LEP_RIESGOPOTENCIAL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_dispositivo_qeco = models.CharField(db_column='LEP_DISPOSITIVO_QECO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_ffin_obras = models.DateTimeField(db_column='LEP_FFIN_OBRAS', blank=True, null=True)  # Field name made lowercase.
    lep_fclasificacion = models.DateTimeField(db_column='LEP_FCLASIFICACION', blank=True, null=True)  # Field name made lowercase.
    lep_fnormasexp = models.DateTimeField(db_column='LEP_FNORMASEXP', blank=True, null=True)  # Field name made lowercase.
    lep_tipo_compuerta_1 = models.CharField(db_column='LEP_TIPO_COMPUERTA_1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_cap_aliv_1 = models.DecimalField(db_column='LEP_CAP_ALIV_1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lep_cota_aliv_1 = models.DecimalField(db_column='LEP_COTA_ALIV_1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lep_nvanos_aliv_1 = models.IntegerField(db_column='LEP_NVANOS_ALIV_1', blank=True, null=True)  # Field name made lowercase.
    lep_tipo_compuerta_2 = models.CharField(db_column='LEP_TIPO_COMPUERTA_2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_cap_aliv_2 = models.DecimalField(db_column='LEP_CAP_ALIV_2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lep_cota_aliv_2 = models.DecimalField(db_column='LEP_COTA_ALIV_2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lep_nvanos_aliv_2 = models.IntegerField(db_column='LEP_NVANOS_ALIV_2', blank=True, null=True)  # Field name made lowercase.
    lep_tipo_compuerta_3 = models.CharField(db_column='LEP_TIPO_COMPUERTA_3', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_cap_aliv_3 = models.DecimalField(db_column='LEP_CAP_ALIV_3', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lep_cota_aliv_3 = models.DecimalField(db_column='LEP_COTA_ALIV_3', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lep_nvanos_aliv_3 = models.IntegerField(db_column='LEP_NVANOS_ALIV_3', blank=True, null=True)  # Field name made lowercase.
    lep_tipo_desague_1 = models.CharField(db_column='LEP_TIPO_DESAGUE_1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_tipo_valvula_1 = models.CharField(db_column='LEP_TIPO_VALVULA_1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_cap_desague_1 = models.DecimalField(db_column='LEP_CAP_DESAGUE_1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lep_cota_eje_1 = models.DecimalField(db_column='LEP_COTA_EJE_1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lep_ncon_des_1 = models.IntegerField(db_column='LEP_NCON_DES_1', blank=True, null=True)  # Field name made lowercase.
    lep_tipo_desague_2 = models.CharField(db_column='LEP_TIPO_DESAGUE_2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_tipo_valvula_2 = models.CharField(db_column='LEP_TIPO_VALVULA_2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_cap_desague_2 = models.DecimalField(db_column='LEP_CAP_DESAGUE_2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lep_cota_eje_2 = models.DecimalField(db_column='LEP_COTA_EJE_2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lep_ncon_des_2 = models.IntegerField(db_column='LEP_NCON_DES_2', blank=True, null=True)  # Field name made lowercase.
    lep_tipo_toma = models.CharField(db_column='LEP_TIPO_TOMA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_seccion_toma = models.CharField(db_column='LEP_SECCION_TOMA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_cap_toma = models.DecimalField(db_column='LEP_CAP_TOMA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lep_cota_toma = models.DecimalField(db_column='LEP_COTA_TOMA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lep_tipo_escalapeces = models.CharField(db_column='LEP_TIPO_ESCALAPECES', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_cota_escalapeces = models.DecimalField(db_column='LEP_COTA_ESCALAPECES', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lep_observaciones = models.CharField(db_column='LEP_OBSERVACIONES', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_ESTACIONES_PRESAS'


class ListaMails(models.Model):
    lm_codigo = models.IntegerField(db_column='LM_CODIGO', primary_key=True)  # Field name made lowercase.
    lm_descripcion = models.CharField(db_column='LM_DESCRIPCION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lm_formato = models.CharField(db_column='LM_FORMATO', max_length=5)  # Field name made lowercase.
    lm_asunto = models.CharField(db_column='LM_ASUNTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lm_texto = models.CharField(db_column='LM_TEXTO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lm_param1 = models.CharField(db_column='LM_PARAM1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lm_param2 = models.CharField(db_column='LM_PARAM2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lm_param3 = models.CharField(db_column='LM_PARAM3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lm_param4 = models.CharField(db_column='LM_PARAM4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lm_param5 = models.CharField(db_column='LM_PARAM5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lm_param6 = models.CharField(db_column='LM_PARAM6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lm_param7 = models.CharField(db_column='LM_PARAM7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lm_param8 = models.CharField(db_column='LM_PARAM8', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lm_falta = models.DateTimeField(db_column='LM_FALTA', blank=True, null=True)  # Field name made lowercase.
    lm_fmodif = models.DateTimeField(db_column='LM_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_MAILS'

class ListaOrdenes(models.Model):
    lo_tag = models.IntegerField(db_column='LO_TAG', primary_key=True)  # Field name made lowercase.
    lo_descripcion = models.CharField(db_column='LO_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lo_tag_txt = models.CharField(db_column='LO_TAG_TXT', max_length=16)  # Field name made lowercase.
    lo_remota = models.IntegerField(db_column='LO_REMOTA')  # Field name made lowercase.
    lo_num_senal = models.IntegerField(db_column='LO_NUM_SENAL', blank=True, null=True)  # Field name made lowercase.
    lo_tipo_orden = models.CharField(db_column='LO_TIPO_ORDEN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lo_naturaleza = models.SmallIntegerField(db_column='LO_NATURALEZA', blank=True, null=True)  # Field name made lowercase.
    lo_conf_remota = models.SmallIntegerField(db_column='LO_CONF_REMOTA', blank=True, null=True)  # Field name made lowercase.
    lo_conf_scada = models.SmallIntegerField(db_column='LO_CONF_SCADA', blank=True, null=True)  # Field name made lowercase.
    lo_conf_historia = models.SmallIntegerField(db_column='LO_CONF_HISTORIA', blank=True, null=True)  # Field name made lowercase.
    lo_texto_valor_0 = models.CharField(db_column='LO_TEXTO_VALOR_0', max_length=24, blank=True, null=True)  # Field name made lowercase.
    lo_texto_valor_1 = models.CharField(db_column='LO_TEXTO_VALOR_1', max_length=24, blank=True, null=True)  # Field name made lowercase.
    lo_tarjeta = models.CharField(db_column='LO_TARJETA', max_length=6, blank=True, null=True)  # Field name made lowercase.
    lo_entrada = models.SmallIntegerField(db_column='LO_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    lo_modo = models.SmallIntegerField(db_column='LO_MODO', blank=True, null=True)  # Field name made lowercase.
    lo_tipo_contacto = models.SmallIntegerField(db_column='LO_TIPO_CONTACTO', blank=True, null=True)  # Field name made lowercase.
    lo_tiempo = models.SmallIntegerField(db_column='LO_TIEMPO', blank=True, null=True)  # Field name made lowercase.
    lo_descripcion1 = models.CharField(db_column='LO_DESCRIPCION1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lo_descripcion2 = models.CharField(db_column='LO_DESCRIPCION2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lo_falta = models.DateTimeField(db_column='LO_FALTA', blank=True, null=True)  # Field name made lowercase.
    lo_fmodif = models.DateTimeField(db_column='LO_FMODIF', blank=True, null=True)  # Field name made lowercase.
    lo_fbaja = models.DateTimeField(db_column='LO_FBAJA', blank=True, null=True)  # Field name made lowercase.
    lo_recid = models.IntegerField(db_column='LO_RECID', blank=True, null=True)  # Field name made lowercase.
    lo_origen = models.CharField(db_column='LO_ORIGEN', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_ORDENES'


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
    lp_falta = models.DateTimeField(db_column='LP_FALTA', blank=True, null=True)  # Field name made lowercase.
    lp_fmodif = models.DateTimeField(db_column='LP_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_PERSONAS'


class ListaRemotas(models.Model):
    lr_codigo = models.IntegerField(db_column='LR_CODIGO', primary_key=True)  # Field name made lowercase.
    lr_tipo_estacion = models.CharField(db_column='LR_TIPO_ESTACION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lr_nombre = models.CharField(db_column='LR_NOMBRE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lr_nombre_corto = models.CharField(db_column='LR_NOMBRE_CORTO', max_length=18, blank=True, null=True)  # Field name made lowercase.
    lr_estacion = models.IntegerField(db_column='LR_ESTACION')  # Field name made lowercase.
    lr_codigo_txt = models.CharField(db_column='LR_CODIGO_TXT', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lr_zona = models.SmallIntegerField(db_column='LR_ZONA')  # Field name made lowercase.
    lr_recid = models.IntegerField(db_column='LR_RECID', blank=True, null=True)  # Field name made lowercase.
    lr_infoplus = models.SmallIntegerField(db_column='LR_INFOPLUS', blank=True, null=True)  # Field name made lowercase.
    lr_remota_fisica = models.IntegerField(db_column='LR_REMOTA_FISICA', blank=True, null=True)  # Field name made lowercase.
    lr_tag_comunica = models.IntegerField(db_column='LR_TAG_COMUNICA', blank=True, null=True)  # Field name made lowercase.
    lr_saih_saica = models.SmallIntegerField(db_column='LR_SAIH_SAICA', blank=True, null=True)  # Field name made lowercase.
    lr_conf_remota = models.SmallIntegerField(db_column='LR_CONF_REMOTA', blank=True, null=True)  # Field name made lowercase.
    lr_remota_principal = models.SmallIntegerField(db_column='LR_REMOTA_PRINCIPAL', blank=True, null=True)  # Field name made lowercase.
    lr_tiene_pluv = models.SmallIntegerField(db_column='LR_TIENE_PLUV', blank=True, null=True)  # Field name made lowercase.
    lr_equipo_mant = models.IntegerField(db_column='LR_EQUIPO_MANT', blank=True, null=True)  # Field name made lowercase.
    lr_num_orden = models.IntegerField(db_column='LR_NUM_ORDEN', blank=True, null=True)  # Field name made lowercase.
    lr_rio = models.IntegerField(db_column='LR_RIO', blank=True, null=True)  # Field name made lowercase.
    lr_empresa_suminis = models.IntegerField(db_column='LR_EMPRESA_SUMINIS', blank=True, null=True)  # Field name made lowercase.
    lr_num_poliza = models.CharField(db_column='LR_NUM_POLIZA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lr_tipo_acceso = models.CharField(db_column='LR_TIPO_ACCESO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lr_desc_tipo_acceso = models.CharField(db_column='LR_DESC_TIPO_ACCESO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lr_persona_contacto = models.IntegerField(db_column='LR_PERSONA_CONTACTO', blank=True, null=True)  # Field name made lowercase.
    lr_observaciones = models.CharField(db_column='LR_OBSERVACIONES', max_length=400, blank=True, null=True)  # Field name made lowercase.
    lr_utm_huso = models.IntegerField(db_column='LR_UTM_HUSO', blank=True, null=True)  # Field name made lowercase.
    lr_utm_x = models.DecimalField(db_column='LR_UTM_X', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_utm_y = models.DecimalField(db_column='LR_UTM_Y', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_utm_z = models.DecimalField(db_column='LR_UTM_Z', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_superficie = models.DecimalField(db_column='LR_SUPERFICIE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_longitud = models.DecimalField(db_column='LR_LONGITUD', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_estacion = models.DecimalField(db_column='LR_COTA_ESTACION', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_max = models.DecimalField(db_column='LR_COTA_MAX', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_vol_max = models.DecimalField(db_column='LR_VOL_MAX', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_men = models.DecimalField(db_column='LR_COTA_MEN', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_lecho = models.DecimalField(db_column='LR_COTA_LECHO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_toma = models.DecimalField(db_column='LR_COTA_TOMA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_tiempo_concentracion = models.DecimalField(db_column='LR_TIEMPO_CONCENTRACION', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_des_izq = models.DecimalField(db_column='LR_COTA_DES_IZQ', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_des_der = models.DecimalField(db_column='LR_COTA_DES_DER', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_caseta = models.DecimalField(db_column='LR_COTA_CASETA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_caudal_diseno = models.DecimalField(db_column='LR_CAUDAL_DISENO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_qmedio_emplaz = models.DecimalField(db_column='LR_QMEDIO_EMPLAZ', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_caudal_q2 = models.DecimalField(db_column='LR_CAUDAL_Q2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_caudal_q5 = models.DecimalField(db_column='LR_CAUDAL_Q5', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_caudal_q10 = models.DecimalField(db_column='LR_CAUDAL_Q10', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_caudal_q25 = models.DecimalField(db_column='LR_CAUDAL_Q25', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_caudal_q100 = models.DecimalField(db_column='LR_CAUDAL_Q100', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_caudal_q500 = models.DecimalField(db_column='LR_CAUDAL_Q500', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_cauce = models.DecimalField(db_column='LR_COTA_CAUCE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_aliviadero = models.DecimalField(db_column='LR_COTA_ALIVIADERO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
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
    lr_period_nap = models.DecimalField(db_column='LR_PERIOD_NAP', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_nae = models.DecimalField(db_column='LR_COTA_NAE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_vol_nae = models.DecimalField(db_column='LR_VOL_NAE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_caudal_nae = models.DecimalField(db_column='LR_CAUDAL_NAE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_period_nae = models.DecimalField(db_column='LR_PERIOD_NAE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_escala_max = models.DecimalField(db_column='LR_ESCALA_MAX', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_capacidad_max = models.DecimalField(db_column='LR_CAPACIDAD_MAX', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_vol_util = models.DecimalField(db_column='LR_VOL_UTIL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_p24h_r2 = models.DecimalField(db_column='LR_P24H_R2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_p24h_r5 = models.DecimalField(db_column='LR_P24H_R5', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_p24h_r10 = models.DecimalField(db_column='LR_P24H_R10', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_p24h_r25 = models.DecimalField(db_column='LR_P24H_R25', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_p24h_r100 = models.DecimalField(db_column='LR_P24H_R100', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_p24h_r500 = models.DecimalField(db_column='LR_P24H_R500', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_falta = models.DateTimeField(db_column='LR_FALTA', blank=True, null=True)  # Field name made lowercase.
    lr_fmodif = models.DateTimeField(db_column='LR_FMODIF', blank=True, null=True)  # Field name made lowercase.
    lr_fbaja = models.DateTimeField(db_column='LR_FBAJA', blank=True, null=True)  # Field name made lowercase.
    lr_vol_min_util = models.DecimalField(db_column='LR_VOL_MIN_UTIL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_coef_erep = models.DecimalField(db_column='LR_COEF_EREP', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lr_caudal_punta = models.DecimalField(db_column='LR_CAUDAL_PUNTA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_fcaudal_punta = models.DateTimeField(db_column='LR_FCAUDAL_PUNTA', blank=True, null=True)  # Field name made lowercase.
    lr_resguardo_nmn = models.DecimalField(db_column='LR_RESGUARDO_NMN', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_superficie_nmn = models.DecimalField(db_column='LR_SUPERFICIE_NMN', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_longitud_emb = models.DecimalField(db_column='LR_LONGITUD_EMB', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_longitud_coronacion = models.DecimalField(db_column='LR_LONGITUD_CORONACION', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_hipotesis_qnap = models.CharField(db_column='LR_HIPOTESIS_QNAP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lr_hipotesis_qnae = models.CharField(db_column='LR_HIPOTESIS_QNAE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lr_caudal_ecologico = models.DecimalField(db_column='LR_CAUDAL_ECOLOGICO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_concesion = models.DecimalField(db_column='LR_CONCESION', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_REMOTAS'


class ListaRemotasConf(models.Model):
    lrc_codigo = models.IntegerField(db_column='LRC_CODIGO', primary_key=True)  # Field name made lowercase.
    lrc_num_remota = models.IntegerField(db_column='LRC_NUM_REMOTA', blank=True, null=True)  # Field name made lowercase.
    lrc_zona_com = models.IntegerField(db_column='LRC_ZONA_COM', blank=True, null=True)  # Field name made lowercase.
    lrc_direccion_ip = models.CharField(db_column='LRC_DIRECCION_IP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lrc_modelo = models.CharField(db_column='LRC_MODELO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lrc_max_tarjetas = models.IntegerField(db_column='LRC_MAX_TARJETAS', blank=True, null=True)  # Field name made lowercase.
    lrc_max_factores = models.IntegerField(db_column='LRC_MAX_FACTORES', blank=True, null=True)  # Field name made lowercase.
    lrc_max_tags = models.IntegerField(db_column='LRC_MAX_TAGS', blank=True, null=True)  # Field name made lowercase.
    lrc_max_ent_digital = models.IntegerField(db_column='LRC_MAX_ENT_DIGITAL', blank=True, null=True)  # Field name made lowercase.
    lrc_max_ent_analog = models.IntegerField(db_column='LRC_MAX_ENT_ANALOG', blank=True, null=True)  # Field name made lowercase.
    lrc_max_sal_analog = models.IntegerField(db_column='LRC_MAX_SAL_ANALOG', blank=True, null=True)  # Field name made lowercase.
    lrc_max_sal_digital = models.IntegerField(db_column='LRC_MAX_SAL_DIGITAL', blank=True, null=True)  # Field name made lowercase.
    lrc_max_ent_binarias = models.IntegerField(db_column='LRC_MAX_ENT_BINARIAS', blank=True, null=True)  # Field name made lowercase.
    lrc_max_ent_grays = models.IntegerField(db_column='LRC_MAX_ENT_GRAYS', blank=True, null=True)  # Field name made lowercase.
    lrc_max_ent_bnc = models.IntegerField(db_column='LRC_MAX_ENT_BNC', blank=True, null=True)  # Field name made lowercase.
    lrc_max_ent_digdobles = models.IntegerField(db_column='LRC_MAX_ENT_DIGDOBLES', blank=True, null=True)  # Field name made lowercase.
    lrc_max_contadores = models.IntegerField(db_column='LRC_MAX_CONTADORES', blank=True, null=True)  # Field name made lowercase.
    lrc_max_db = models.IntegerField(db_column='LRC_MAX_DB', blank=True, null=True)  # Field name made lowercase.
    lrc_max_sizedb = models.IntegerField(db_column='LRC_MAX_SIZEDB', blank=True, null=True)  # Field name made lowercase.
    lrc_max_tomamuestras = models.IntegerField(db_column='LRC_MAX_TOMAMUESTRAS', blank=True, null=True)  # Field name made lowercase.
    lrc_max_enclavamientos = models.IntegerField(db_column='LRC_MAX_ENCLAVAMIENTOS', blank=True, null=True)  # Field name made lowercase.
    lrc_max_rebotes = models.IntegerField(db_column='LRC_MAX_REBOTES', blank=True, null=True)  # Field name made lowercase.
    lrc_temp_inhibicion = models.IntegerField(db_column='LRC_TEMP_INHIBICION', blank=True, null=True)  # Field name made lowercase.
    lrc_observaciones = models.CharField(db_column='LRC_OBSERVACIONES', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_REMOTAS_CONF'


class ListaRemotasFicheros(models.Model):
    lrf_cod_remota = models.IntegerField(db_column='LRF_COD_REMOTA', primary_key=True)  # Field name made lowercase. The composite primary key (LRF_COD_REMOTA, LRF_TIPO_FICHERO, LRF_COD_FICHERO) found, that is not supported. The first column is selected.
    lrf_tipo_fichero = models.CharField(db_column='LRF_TIPO_FICHERO', max_length=7)  # Field name made lowercase.
    lrf_cod_fichero = models.DecimalField(db_column='LRF_COD_FICHERO', max_digits=18, decimal_places=0)  # Field name made lowercase.
    lrf_nombre_fichero = models.CharField(db_column='LRF_NOMBRE_FICHERO', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_REMOTAS_FICHEROS'
        unique_together = (('lrf_cod_remota', 'lrf_tipo_fichero', 'lrf_cod_fichero'),)


class ListaRemotasOtrosserv(models.Model):
    lro_cod_remota = models.IntegerField(db_column='LRO_COD_REMOTA', primary_key=True)  # Field name made lowercase. The composite primary key (LRO_COD_REMOTA, LRO_COD_EQUIPO) found, that is not supported. The first column is selected.
    lro_cod_equipo = models.IntegerField(db_column='LRO_COD_EQUIPO')  # Field name made lowercase.
    lro_tipo_equipo = models.IntegerField(db_column='LRO_TIPO_EQUIPO', blank=True, null=True)  # Field name made lowercase.
    lro_desc_equipo = models.CharField(db_column='LRO_DESC_EQUIPO', max_length=400, blank=True, null=True)  # Field name made lowercase.
    lro_cod_empresa = models.IntegerField(db_column='LRO_COD_EMPRESA', blank=True, null=True)  # Field name made lowercase.
    lro_observaciones = models.CharField(db_column='LRO_OBSERVACIONES', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_REMOTAS_OTROSSERV'
        unique_together = (('lro_cod_remota', 'lro_cod_equipo'),)


class ListaRemotasTarjetas(models.Model):
    lrt_codigo = models.IntegerField(db_column='LRT_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (LRT_CODIGO, LRT_NOMBRE) found, that is not supported. The first column is selected.
    lrt_nombre = models.CharField(db_column='LRT_NOMBRE', max_length=6)  # Field name made lowercase.
    lrt_modelo = models.CharField(db_column='LRT_MODELO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lrt_tipo = models.IntegerField(db_column='LRT_TIPO', blank=True, null=True)  # Field name made lowercase.
    lrt_dir_control = models.CharField(db_column='LRT_DIR_CONTROL', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lrt_dir_datos = models.CharField(db_column='LRT_DIR_DATOS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lrt_numdatos = models.IntegerField(db_column='LRT_NUMDATOS', blank=True, null=True)  # Field name made lowercase.
    lrt_signo = models.SmallIntegerField(db_column='LRT_SIGNO', blank=True, null=True)  # Field name made lowercase.
    lrt_dir_ip = models.CharField(db_column='LRT_DIR_IP', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_REMOTAS_TARJETAS'
        unique_together = (('lrt_codigo', 'lrt_nombre'),)


class ListaSenales(models.Model):
    ls_tag = models.IntegerField(db_column='LS_TAG', primary_key=True)  # Field name made lowercase.
    ls_descripcion = models.CharField(db_column='LS_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ls_tag_txt = models.CharField(db_column='LS_TAG_TXT', max_length=16)  # Field name made lowercase.
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
    ls_hora_cons = models.CharField(db_column='LS_HORA_CONS', max_length=5, blank=True, null=True)  # Field name made lowercase.
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
    ls_falta = models.DateTimeField(db_column='LS_FALTA', blank=True, null=True)  # Field name made lowercase.
    ls_fmodif = models.DateTimeField(db_column='LS_FMODIF', blank=True, null=True)  # Field name made lowercase.
    ls_fbaja = models.DateTimeField(db_column='LS_FBAJA', blank=True, null=True)  # Field name made lowercase.
    ls_ver_web = models.SmallIntegerField(db_column='LS_VER_WEB', blank=True, null=True)  # Field name made lowercase.
    ls_ver_intranet = models.SmallIntegerField(db_column='LS_VER_INTRANET', blank=True, null=True)  # Field name made lowercase.
    ls_ver_pda = models.SmallIntegerField(db_column='LS_VER_PDA', blank=True, null=True)  # Field name made lowercase.
    ls_fews = models.SmallIntegerField(db_column='LS_FEWS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_SENALES'




class ListaSenalesAnalogicas(models.Model):
    lsa_tag = models.IntegerField(db_column='LSA_TAG', primary_key=True)  # Field name made lowercase.
    lsa_unid_ing = models.CharField(db_column='LSA_UNID_ING', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lsa_digitos_enteros = models.SmallIntegerField(db_column='LSA_DIGITOS_ENTEROS', blank=True, null=True)  # Field name made lowercase.
    lsa_digitos_decimales = models.SmallIntegerField(db_column='LSA_DIGITOS_DECIMALES', blank=True, null=True)  # Field name made lowercase.
    lsa_factor_scada = models.CharField(db_column='LSA_FACTOR_SCADA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lsa_tipo_almacenamiento = models.CharField(db_column='LSA_TIPO_ALMACENAMIENTO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsa_minimo = models.FloatField(db_column='LSA_MINIMO', blank=True, null=True)  # Field name made lowercase.
    lsa_maximo = models.FloatField(db_column='LSA_MAXIMO', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_alto_alto_alto = models.FloatField(db_column='LSA_LIM_ALTO_ALTO_ALTO', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_alto_alto = models.FloatField(db_column='LSA_LIM_ALTO_ALTO', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_alto = models.FloatField(db_column='LSA_LIM_ALTO', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_bajo = models.FloatField(db_column='LSA_LIM_BAJO', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_bajo_bajo = models.FloatField(db_column='LSA_LIM_BAJO_BAJO', blank=True, null=True)  # Field name made lowercase.
    lsa_valor_histeresis = models.FloatField(db_column='LSA_VALOR_HISTERESIS', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_neg_rampa = models.FloatField(db_column='LSA_LIM_NEG_RAMPA', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_pos_rampa = models.FloatField(db_column='LSA_LIM_POS_RAMPA', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_rampa_histeresis = models.FloatField(db_column='LSA_LIM_RAMPA_HISTERESIS', blank=True, null=True)  # Field name made lowercase.
    lsa_gravedad_aaa = models.CharField(db_column='LSA_GRAVEDAD_AAA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsa_gravedad_aa = models.CharField(db_column='LSA_GRAVEDAD_AA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsa_gravedad_a = models.CharField(db_column='LSA_GRAVEDAD_A', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsa_gravedad_b = models.CharField(db_column='LSA_GRAVEDAD_B', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsa_gravedad_bb = models.CharField(db_column='LSA_GRAVEDAD_BB', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsa_gravedad_rn = models.CharField(db_column='LSA_GRAVEDAD_RN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsa_gravedad_rp = models.CharField(db_column='LSA_GRAVEDAD_RP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsa_ver_web_a = models.SmallIntegerField(db_column='LSA_VER_WEB_A', blank=True, null=True)  # Field name made lowercase.
    lsa_ver_web_aa = models.SmallIntegerField(db_column='LSA_VER_WEB_AA', blank=True, null=True)  # Field name made lowercase.
    lsa_ver_web_aaa = models.SmallIntegerField(db_column='LSA_VER_WEB_AAA', blank=True, null=True)  # Field name made lowercase.
    lsa_ver_intranet_a = models.SmallIntegerField(db_column='LSA_VER_INTRANET_A', blank=True, null=True)  # Field name made lowercase.
    lsa_ver_intranet_aa = models.SmallIntegerField(db_column='LSA_VER_INTRANET_AA', blank=True, null=True)  # Field name made lowercase.
    lsa_ver_intranet_aaa = models.SmallIntegerField(db_column='LSA_VER_INTRANET_AAA', blank=True, null=True)  # Field name made lowercase.
    lsa_ver_pda_a = models.SmallIntegerField(db_column='LSA_VER_PDA_A', blank=True, null=True)  # Field name made lowercase.
    lsa_ver_pda_aa = models.SmallIntegerField(db_column='LSA_VER_PDA_AA', blank=True, null=True)  # Field name made lowercase.
    lsa_ver_pda_aaa = models.SmallIntegerField(db_column='LSA_VER_PDA_AAA', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_tv = models.SmallIntegerField(db_column='LSA_LIM_TV', blank=True, null=True)  # Field name made lowercase.
    lsa_criterio_tv = models.CharField(db_column='LSA_CRITERIO_TV', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_SENALES_ANALOGICAS'



class ListaSenalesAnalogicasUmbrales(models.Model):
    lsa_tag = models.IntegerField(db_column='LSA_TAG')  # Field name made lowercase.
    lsa_unid_ing = models.CharField(db_column='LSA_UNID_ING', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lsa_digitos_enteros = models.SmallIntegerField(db_column='LSA_DIGITOS_ENTEROS', blank=True, null=True)  # Field name made lowercase.
    lsa_digitos_decimales = models.SmallIntegerField(db_column='LSA_DIGITOS_DECIMALES', blank=True, null=True)  # Field name made lowercase.
    lsa_factor_scada = models.CharField(db_column='LSA_FACTOR_SCADA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lsa_tipo_almacenamiento = models.CharField(db_column='LSA_TIPO_ALMACENAMIENTO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsa_minimo = models.FloatField(db_column='LSA_MINIMO', blank=True, null=True)  # Field name made lowercase.
    lsa_maximo = models.FloatField(db_column='LSA_MAXIMO', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_alto_alto_alto = models.FloatField(db_column='LSA_LIM_ALTO_ALTO_ALTO', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_alto_alto = models.FloatField(db_column='LSA_LIM_ALTO_ALTO', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_alto = models.FloatField(db_column='LSA_LIM_ALTO', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_bajo = models.FloatField(db_column='LSA_LIM_BAJO', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_bajo_bajo = models.FloatField(db_column='LSA_LIM_BAJO_BAJO', blank=True, null=True)  # Field name made lowercase.
    lsa_valor_histeresis = models.FloatField(db_column='LSA_VALOR_HISTERESIS', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_neg_rampa = models.FloatField(db_column='LSA_LIM_NEG_RAMPA', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_pos_rampa = models.FloatField(db_column='LSA_LIM_POS_RAMPA', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_rampa_histeresis = models.FloatField(db_column='LSA_LIM_RAMPA_HISTERESIS', blank=True, null=True)  # Field name made lowercase.
    lsa_gravedad_aaa = models.CharField(db_column='LSA_GRAVEDAD_AAA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsa_gravedad_aa = models.CharField(db_column='LSA_GRAVEDAD_AA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsa_gravedad_a = models.CharField(db_column='LSA_GRAVEDAD_A', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsa_gravedad_b = models.CharField(db_column='LSA_GRAVEDAD_B', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsa_gravedad_bb = models.CharField(db_column='LSA_GRAVEDAD_BB', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsa_gravedad_rn = models.CharField(db_column='LSA_GRAVEDAD_RN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsa_gravedad_rp = models.CharField(db_column='LSA_GRAVEDAD_RP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsa_ver_web_a = models.SmallIntegerField(db_column='LSA_VER_WEB_A', blank=True, null=True)  # Field name made lowercase.
    lsa_ver_web_aa = models.SmallIntegerField(db_column='LSA_VER_WEB_AA', blank=True, null=True)  # Field name made lowercase.
    lsa_ver_web_aaa = models.SmallIntegerField(db_column='LSA_VER_WEB_AAA', blank=True, null=True)  # Field name made lowercase.
    lsa_ver_intranet_a = models.SmallIntegerField(db_column='LSA_VER_INTRANET_A', blank=True, null=True)  # Field name made lowercase.
    lsa_ver_intranet_aa = models.SmallIntegerField(db_column='LSA_VER_INTRANET_AA', blank=True, null=True)  # Field name made lowercase.
    lsa_ver_intranet_aaa = models.SmallIntegerField(db_column='LSA_VER_INTRANET_AAA', blank=True, null=True)  # Field name made lowercase.
    lsa_ver_pda_a = models.SmallIntegerField(db_column='LSA_VER_PDA_A', blank=True, null=True)  # Field name made lowercase.
    lsa_ver_pda_aa = models.SmallIntegerField(db_column='LSA_VER_PDA_AA', blank=True, null=True)  # Field name made lowercase.
    lsa_ver_pda_aaa = models.SmallIntegerField(db_column='LSA_VER_PDA_AAA', blank=True, null=True)  # Field name made lowercase.
    lsa_lim_tv = models.SmallIntegerField(db_column='LSA_LIM_TV', blank=True, null=True)  # Field name made lowercase.
    lsa_criterio_tv = models.CharField(db_column='LSA_CRITERIO_TV', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_SENALES_ANALOGICAS_UMBRALES'


class ListaSenalesCalculadas(models.Model):
    pk=models.CompositePrimaryKey('lsc_tag','lsc_fecha_inicio')
    lsc_tag = models.ForeignKey(ListaSenales,on_delete=models.DO_NOTHING,db_column='LSC_TAG')  # Field name made lowercase. The composite primary key (LSC_TAG, LSC_FECHA_INICIO) found, that is not supported. The first column is selected.
    lsc_fecha_inicio = models.DateTimeField(db_column='LSC_FECHA_INICIO')  # Field name made lowercase.
    lsc_fecha_fin = models.DateTimeField(db_column='LSC_FECHA_FIN', blank=True, null=True)  # Field name made lowercase.
    lsc_version = models.CharField(db_column='LSC_VERSION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lsc_fichero = models.CharField(db_column='LSC_FICHERO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lsc_tipo_calculo = models.SmallIntegerField(db_column='LSC_TIPO_CALCULO', blank=True, null=True)  # Field name made lowercase.
    lsc_tag_campo = models.IntegerField(db_column='LSC_TAG_CAMPO', blank=True, null=True)  # Field name made lowercase.
    lsc_tag_campo_2 = models.IntegerField(db_column='LSC_TAG_CAMPO_2', blank=True, null=True)  # Field name made lowercase.
    ''' NO SE USAN POR AHORA
    lsc_tabla = models.CharField(db_column='LSC_TABLA', max_length=12, blank=True, null=True)  # Field name made lowercase.
    lsc_cota_min_formula = models.DecimalField(db_column='LSC_COTA_MIN_FORMULA', max_digits=34, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    lsc_coef0 = models.DecimalField(db_column='LSC_COEF0', max_digits=34, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    lsc_coef1 = models.DecimalField(db_column='LSC_COEF1', max_digits=34, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    lsc_coef2 = models.DecimalField(db_column='LSC_COEF2', max_digits=34, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    lsc_coef3 = models.DecimalField(db_column='LSC_COEF3', max_digits=34, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    lsc_coef4 = models.DecimalField(db_column='LSC_COEF4', max_digits=34, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    lsc_coef5 = models.DecimalField(db_column='LSC_COEF5', max_digits=34, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    lsc_coef6 = models.DecimalField(db_column='LSC_COEF6', max_digits=34, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    lsc_coef7 = models.DecimalField(db_column='LSC_COEF7', max_digits=34, decimal_places=30, blank=True, null=True)  # Field name made lowercase.
    '''
    
    class Meta:
        managed = False
        db_table = 'LISTA_SENALES_CALCULADAS'
        unique_together = (('lsc_tag', 'lsc_fecha_inicio'),)


class ListaSenalesDigdobles(models.Model):
    ldd_tag = models.IntegerField(db_column='LDD_TAG', primary_key=True)  # Field name made lowercase.
    ldd_texto_valor_0 = models.CharField(db_column='LDD_TEXTO_VALOR_0', max_length=24, blank=True, null=True)  # Field name made lowercase.
    ldd_texto_valor_1 = models.CharField(db_column='LDD_TEXTO_VALOR_1', max_length=24, blank=True, null=True)  # Field name made lowercase.
    ldd_texto_valor_2 = models.CharField(db_column='LDD_TEXTO_VALOR_2', max_length=24, blank=True, null=True)  # Field name made lowercase.
    ldd_texto_valor_3 = models.CharField(db_column='LDD_TEXTO_VALOR_3', max_length=24, blank=True, null=True)  # Field name made lowercase.
    ldd_es_alarma = models.SmallIntegerField(db_column='LDD_ES_ALARMA', blank=True, null=True)  # Field name made lowercase.
    ldd_valor_alarma = models.SmallIntegerField(db_column='LDD_VALOR_ALARMA', blank=True, null=True)  # Field name made lowercase.
    ldd_gravedad = models.CharField(db_column='LDD_GRAVEDAD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ldd_digital1 = models.IntegerField(db_column='LDD_DIGITAL1', blank=True, null=True)  # Field name made lowercase.
    ldd_digital2 = models.IntegerField(db_column='LDD_DIGITAL2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_SENALES_DIGDOBLES'


class ListaSenalesDigitales(models.Model):
    lsd_tag = models.IntegerField(db_column='LSD_TAG', primary_key=True)  # Field name made lowercase.
    lsd_texto_valor_0 = models.CharField(db_column='LSD_TEXTO_VALOR_0', max_length=24, blank=True, null=True)  # Field name made lowercase.
    lsd_texto_valor_1 = models.CharField(db_column='LSD_TEXTO_VALOR_1', max_length=24, blank=True, null=True)  # Field name made lowercase.
    lsd_es_alarma = models.SmallIntegerField(db_column='LSD_ES_ALARMA', blank=True, null=True)  # Field name made lowercase.
    lsd_valor_activacion = models.SmallIntegerField(db_column='LSD_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.
    lsd_gravedad = models.CharField(db_column='LSD_GRAVEDAD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lsd_logica_negativa = models.SmallIntegerField(db_column='LSD_LOGICA_NEGATIVA', blank=True, null=True)  # Field name made lowercase.
    lsd_tmp_proceso = models.CharField(db_column='LSD_TMP_PROCESO', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_SENALES_DIGITALES'


class ListaSenalesLimitevariables(models.Model):
    
    lsl_tag = models.IntegerField(db_column='LSL_TAG', primary_key=True)  # Field name made lowercase. The composite primary key (LSL_TAG, LSL_ALARMA, LSL_DIA, LSL_MES) found, that is not supported. The first column is selected.
    lsl_alarma = models.CharField(db_column='LSL_ALARMA', max_length=4)  # Field name made lowercase.
    lsl_dia = models.SmallIntegerField(db_column='LSL_DIA')  # Field name made lowercase.
    lsl_mes = models.SmallIntegerField(db_column='LSL_MES')  # Field name made lowercase.
    lsl_valor = models.FloatField(db_column='LSL_VALOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_SENALES_LIMITEVARIABLES'
        unique_together = (('lsl_tag', 'lsl_alarma', 'lsl_dia', 'lsl_mes'),)


class ListaSenalesZonas(models.Model):
    lsz_tag = models.SmallIntegerField(db_column='LSZ_TAG', primary_key=True)  # Field name made lowercase. The composite primary key (LSZ_TAG, LSZ_TIPO_ZONA, LSZ_ZONA) found, that is not supported. The first column is selected.
    lsz_tipo_zona = models.CharField(db_column='LSZ_TIPO_ZONA', max_length=3)  # Field name made lowercase.
    lsz_zona = models.SmallIntegerField(db_column='LSZ_ZONA')  # Field name made lowercase.
    lsz_afecta_color = models.SmallIntegerField(db_column='LSZ_AFECTA_COLOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_SENALES_ZONAS'
        unique_together = (('lsz_tag', 'lsz_tipo_zona', 'lsz_zona'),)


class ListaZonas(models.Model):
    lz_codigo = models.SmallIntegerField(db_column='LZ_CODIGO', primary_key=True)  # Field name made lowercase.
    lz_descripcion = models.CharField(db_column='LZ_DESCRIPCION', max_length=16, blank=True, null=True)  # Field name made lowercase.
    lz_superficie = models.DecimalField(db_column='LZ_SUPERFICIE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lz_confederacion = models.SmallIntegerField(db_column='LZ_CONFEDERACION', blank=True, null=True)  # Field name made lowercase.
    lz_cod_ser = models.CharField(db_column='LZ_COD_SER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lz_falta = models.DateTimeField(db_column='LZ_FALTA', blank=True, null=True)  # Field name made lowercase.
    lz_fmodif = models.DateTimeField(db_column='LZ_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_ZONAS'


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


class Menuitems(models.Model):
    mei_codigo = models.IntegerField(db_column='MEI_CODIGO', blank=True, null=True)  # Field name made lowercase.
    mei_texto = models.CharField(db_column='MEI_TEXTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mei_padre_id = models.IntegerField(db_column='MEI_PADRE_ID', blank=True, null=True)  # Field name made lowercase.
    mei_posicion = models.IntegerField(db_column='MEI_POSICION', blank=True, null=True)  # Field name made lowercase.
    mei_icono = models.CharField(db_column='MEI_ICONO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mei_habilitado = models.BooleanField(db_column='MEI_HABILITADO', blank=True, null=True)  # Field name made lowercase.
    mei_url = models.CharField(db_column='MEI_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mei_fecha_creacion = models.DateTimeField(db_column='MEI_FECHA_CREACION', blank=True, null=True)  # Field name made lowercase.
    mei_tooltip = models.CharField(db_column='MEI_TOOLTIP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mei_menu = models.CharField(db_column='MEI_MENU', max_length=10, blank=True, null=True)  # Field name made lowercase.
    mei_pantalla = models.CharField(db_column='MEI_PANTALLA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mei_aspx = models.CharField(db_column='MEI_ASPX', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mei_conta = models.AutoField(db_column='MEI_CONTA', primary_key=True)  # Field name made lowercase.
    mei_tipousuario = models.IntegerField(db_column='MEI_TIPOUSUARIO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MENUITEMS'


class Menus(models.Model):
    me_menu = models.IntegerField(db_column='ME_MENU', blank=True, null=True)  # Field name made lowercase.
    me_texto = models.CharField(db_column='ME_TEXTO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    me_tipo = models.CharField(db_column='ME_TIPO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    me_dinamico = models.BooleanField(db_column='ME_DINAMICO', blank=True, null=True)  # Field name made lowercase.
    me_alineacion = models.CharField(db_column='ME_ALINEACION', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MENUS'


class MenuSql(models.Model):
    pd_tabla = models.CharField(db_column='PD_TABLA', primary_key=True, max_length=20)  # Field name made lowercase.
    pd_sql = models.CharField(db_column='PD_SQL', max_length=400, blank=True, null=True)  # Field name made lowercase.
    pd_datakeys = models.CharField(db_column='PD_DATAKEYS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pd_campos = models.CharField(db_column='PD_CAMPOS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pd_url = models.CharField(db_column='PD_URL', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MENU_SQL'


class ModalidadesAlarmas(models.Model):
    ma_alarma = models.CharField(db_column='MA_ALARMA', primary_key=True, max_length=1)  # Field name made lowercase.
    ma_txt_alarma = models.CharField(db_column='MA_TXT_ALARMA', max_length=8)  # Field name made lowercase.
    ma_falta = models.DateTimeField(db_column='MA_FALTA', blank=True, null=True)  # Field name made lowercase.
    ma_fmodif = models.DateTimeField(db_column='MA_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MODALIDADES_ALARMAS'

class NaturalezaSenales(models.Model):
    ns_codigo = models.SmallIntegerField(db_column='NS_CODIGO', primary_key=True)  # Field name made lowercase.
    ns_nombre = models.CharField(db_column='NS_NOMBRE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ns_falta = models.DateTimeField(db_column='NS_FALTA', blank=True, null=True)  # Field name made lowercase.
    ns_fmodif = models.DateTimeField(db_column='NS_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NATURALEZA_SENALES'

class Poblaciones(models.Model):
    po_codigo = models.IntegerField(db_column='PO_CODIGO', primary_key=True)  # Field name made lowercase.
    po_provincia = models.SmallIntegerField(db_column='PO_PROVINCIA', blank=True, null=True)  # Field name made lowercase.
    po_descripcion = models.CharField(db_column='PO_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    po_falta = models.DateTimeField(db_column='PO_FALTA', blank=True, null=True)  # Field name made lowercase.
    po_fmodif = models.DateTimeField(db_column='PO_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'POBLACIONES'

class Provincias(models.Model):
    pr_codigo = models.SmallIntegerField(db_column='PR_CODIGO', primary_key=True)  # Field name made lowercase.
    pr_descripcion = models.CharField(db_column='PR_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pr_comunidad = models.SmallIntegerField(db_column='PR_COMUNIDAD', blank=True, null=True)  # Field name made lowercase.
    pr_falta = models.DateTimeField(db_column='PR_FALTA', blank=True, null=True)  # Field name made lowercase.
    pr_fmodif = models.DateTimeField(db_column='PR_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROVINCIAS'

class PuestosTrabajo(models.Model):
    pt_codigo = models.IntegerField(db_column='PT_CODIGO', primary_key=True)  # Field name made lowercase.
    pt_descripcion = models.CharField(db_column='PT_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pt_cod_cargo = models.CharField(db_column='PT_COD_CARGO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pt_cod_puesto_superior = models.IntegerField(db_column='PT_COD_PUESTO_SUPERIOR', blank=True, null=True)  # Field name made lowercase.
    pt_telefono1 = models.CharField(db_column='PT_TELEFONO1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    pt_telefono2 = models.CharField(db_column='PT_TELEFONO2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    pt_telefono3 = models.CharField(db_column='PT_TELEFONO3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    pt_orden = models.IntegerField(db_column='PT_ORDEN', blank=True, null=True)  # Field name made lowercase.
    pt_cod_perso = models.IntegerField(db_column='PT_COD_PERSO', blank=True, null=True)  # Field name made lowercase.
    pt_tipo_telefono3 = models.CharField(db_column='PT_TIPO_TELEFONO3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pt_fmodif = models.DateTimeField(db_column='PT_FMODIF', blank=True, null=True)  # Field name made lowercase.
    pt_falta = models.DateTimeField(db_column='PT_FALTA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PUESTOS_TRABAJO'


class Rios(models.Model):
    ri_codigo = models.IntegerField(db_column='RI_CODIGO', primary_key=True)  # Field name made lowercase.
    ri_descripcion = models.CharField(db_column='RI_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ri_falta = models.DateTimeField(db_column='RI_FALTA', blank=True, null=True)  # Field name made lowercase.
    ri_fmodif = models.DateTimeField(db_column='RI_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIOS'


class SequiaNiveles(models.Model):
    sn_codigo = models.SmallIntegerField(db_column='SN_CODIGO', primary_key=True)  # Field name made lowercase.
    sn_descripcion = models.CharField(db_column='SN_DESCRIPCION', max_length=30)  # Field name made lowercase.
    sn_valor_ini = models.DecimalField(db_column='SN_VALOR_INI', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sn_valor_fin = models.DecimalField(db_column='SN_VALOR_FIN', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sn_falta = models.DateTimeField(db_column='SN_FALTA', blank=True, null=True)  # Field name made lowercase.
    sn_fmodif = models.DateTimeField(db_column='SN_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SEQUIA_NIVELES'


class TextosWeb(models.Model):
    tw_dominio = models.CharField(db_column='TW_DOMINIO', primary_key=True, max_length=50)  # Field name made lowercase. The composite primary key (TW_DOMINIO, TW_TIPO, TW_ITEM, TW_ORDEN) found, that is not supported. The first column is selected.
    tw_tipo = models.CharField(db_column='TW_TIPO', max_length=50)  # Field name made lowercase.
    tw_item = models.CharField(db_column='TW_ITEM', max_length=50)  # Field name made lowercase.
    tw_orden = models.SmallIntegerField(db_column='TW_ORDEN')  # Field name made lowercase.
    tw_texto_spa = models.CharField(db_column='TW_TEXTO_SPA', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    tw_texto_gal = models.CharField(db_column='TW_TEXTO_GAL', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    tw_texto_eus = models.CharField(db_column='TW_TEXTO_EUS', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    tw_es_html = models.SmallIntegerField(db_column='TW_ES_HTML', blank=True, null=True)  # Field name made lowercase.
    tw_falta = models.DateTimeField(db_column='TW_FALTA', blank=True, null=True)  # Field name made lowercase.
    tw_fmodif = models.DateTimeField(db_column='TW_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TEXTOS_WEB'
        unique_together = (('tw_dominio', 'tw_tipo', 'tw_item', 'tw_orden'),)


class TiposAlarmas(models.Model):
    ta_codigo = models.SmallIntegerField(db_column='TA_CODIGO', primary_key=True)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ta_falta = models.DateTimeField(db_column='TA_FALTA', blank=True, null=True)  # Field name made lowercase.
    ta_fmodif = models.DateTimeField(db_column='TA_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_ALARMAS'


class TiposAlmacenamiento(models.Model):
    ta_codigo = models.CharField(db_column='TA_CODIGO', max_length=5)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ta_periodo = models.IntegerField(db_column='TA_PERIODO', blank=True, null=True)  # Field name made lowercase.
    ta_almacen = models.IntegerField(db_column='TA_ALMACEN', blank=True, null=True)  # Field name made lowercase.
    ta_falta = models.DateTimeField(db_column='TA_FALTA', blank=True, null=True)  # Field name made lowercase.
    ta_fmodif = models.DateTimeField(db_column='TA_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_ALMACENAMIENTO'


class TiposAreas(models.Model):
    ta_codigo = models.CharField(db_column='TA_CODIGO', max_length=3)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ta_falta = models.DateTimeField(db_column='TA_FALTA', blank=True, null=True)  # Field name made lowercase.
    ta_fmodif = models.DateTimeField(db_column='TA_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_AREAS'


class TiposAvisos(models.Model):
    ta_codigo = models.SmallIntegerField(db_column='TA_CODIGO', primary_key=True)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ta_falta = models.DateTimeField(db_column='TA_FALTA', blank=True, null=True)  # Field name made lowercase.
    ta_fmodif = models.DateTimeField(db_column='TA_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_AVISOS'


class TiposCajetines(models.Model):
    tc_codigo = models.SmallIntegerField(db_column='TC_CODIGO', primary_key=True)  # Field name made lowercase.
    tc_ancho_tag = models.SmallIntegerField(db_column='TC_ANCHO_TAG', blank=True, null=True)  # Field name made lowercase.
    tc_alto_tag = models.SmallIntegerField(db_column='TC_ALTO_TAG', blank=True, null=True)  # Field name made lowercase.
    tc_tags_fila = models.SmallIntegerField(db_column='TC_TAGS_FILA', blank=True, null=True)  # Field name made lowercase.
    tc_filas = models.SmallIntegerField(db_column='TC_FILAS', blank=True, null=True)  # Field name made lowercase.
    tc_falta = models.DateTimeField(db_column='TC_FALTA', blank=True, null=True)  # Field name made lowercase.
    tc_fmodif = models.DateTimeField(db_column='TC_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'TIPOS_CAJETINES'


class TiposCalidades(models.Model):
    tca_codigo = models.SmallIntegerField(db_column='TCA_CODIGO', primary_key=True)  # Field name made lowercase.
    tca_descripcion = models.CharField(db_column='TCA_DESCRIPCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tca_porcen_ini = models.SmallIntegerField(db_column='TCA_PORCEN_INI', blank=True, null=True)  # Field name made lowercase.
    tca_porcen_fin = models.SmallIntegerField(db_column='TCA_PORCEN_FIN', blank=True, null=True)  # Field name made lowercase.
    tca_falta = models.DateTimeField(db_column='TCA_FALTA', blank=True, null=True)  # Field name made lowercase.
    tca_fmodif = models.DateTimeField(db_column='TCA_FMODIF', blank=True, null=True)  # Field name made lowercase.
    tca_tipo = models.CharField(db_column='TCA_TIPO', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_CALIDADES'


class TiposConsolidacion(models.Model):
    tc_codigo = models.SmallIntegerField(db_column='TC_CODIGO', primary_key=True)  # Field name made lowercase.
    tc_descripcion = models.CharField(db_column='TC_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tc_falta = models.DateTimeField(db_column='TC_FALTA', blank=True, null=True)  # Field name made lowercase.
    tc_fmodif = models.DateTimeField(db_column='TC_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_CONSOLIDACION'


class TiposEquipos(models.Model):
    te_codigo = models.IntegerField(db_column='TE_CODIGO', primary_key=True)  # Field name made lowercase.
    te_descripcion = models.CharField(db_column='TE_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    te_fmodif = models.DateTimeField(db_column='TE_FMODIF', blank=True, null=True)  # Field name made lowercase.
    te_falta = models.DateTimeField(db_column='TE_FALTA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_EQUIPOS'


class TiposEstaciones(models.Model):
    te_codigo = models.CharField(db_column='TE_CODIGO', primary_key=True, max_length=2)  # Field name made lowercase.
    te_descripcion = models.CharField(db_column='TE_DESCRIPCION', max_length=32, blank=True, null=True)  # Field name made lowercase.
    te_falta = models.DateTimeField(db_column='TE_FALTA', blank=True, null=True)  # Field name made lowercase.
    te_fmodif = models.DateTimeField(db_column='TE_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_ESTACIONES'


class TiposFuentes(models.Model):
    tf_codigo = models.CharField(db_column='TF_CODIGO', primary_key=True, max_length=5)  # Field name made lowercase.
    tf_descripcion = models.CharField(db_column='TF_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tf_fmodif = models.DateTimeField(db_column='TF_FMODIF', blank=True, null=True)  # Field name made lowercase.
    tf_falta = models.DateTimeField(db_column='TF_FALTA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_FUENTES'


class TiposSenales(models.Model):
    ts_codigo = models.CharField(db_column='TS_CODIGO', primary_key=True, max_length=5)  # Field name made lowercase. The composite primary key (TS_CODIGO, TS_NATURALEZA) found, that is not supported. The first column is selected.
    ts_descripcion = models.CharField(db_column='TS_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ts_naturaleza = models.SmallIntegerField(db_column='TS_NATURALEZA')  # Field name made lowercase.
    ts_falta = models.DateTimeField(db_column='TS_FALTA', blank=True, null=True)  # Field name made lowercase.
    ts_fmodif = models.DateTimeField(db_column='TS_FMODIF', blank=True, null=True)  # Field name made lowercase.
    ts_nombre_corto = models.CharField(db_column='TS_NOMBRE_CORTO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ts_orden = models.SmallIntegerField(db_column='TS_ORDEN', blank=True, null=True)  # Field name made lowercase.
    ts_acumula = models.SmallIntegerField(db_column='TS_ACUMULA', blank=True, null=True)  # Field name made lowercase.
    ts_grupo_web = models.CharField(db_column='TS_GRUPO_WEB', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_SENALES'
        unique_together = (('ts_codigo', 'ts_naturaleza'),)

class UnidadesIngenieria(models.Model):
    ui_codigo = models.CharField(db_column='UI_CODIGO', primary_key=True, max_length=10)  # Field name made lowercase.
    ui_descripcion = models.CharField(db_column='UI_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ui_codigo_corto = models.CharField(db_column='UI_CODIGO_CORTO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ui_orden = models.SmallIntegerField(db_column='UI_ORDEN', blank=True, null=True)  # Field name made lowercase.
    ui_falta = models.DateTimeField(db_column='UI_FALTA', blank=True, null=True)  # Field name made lowercase.
    ui_fmodif = models.DateTimeField(db_column='UI_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UNIDADES_INGENIERIA'


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
    uw_falta = models.DateTimeField(db_column='UW_FALTA', blank=True, null=True)  # Field name made lowercase.
    uw_fmodif = models.DateTimeField(db_column='UW_FMODIF', blank=True, null=True)  # Field name made lowercase.
    uw_fbaja = models.DateTimeField(db_column='UW_FBAJA', blank=True, null=True)  # Field name made lowercase.
    uw_accesibilidad = models.SmallIntegerField(db_column='UW_ACCESIBILIDAD', blank=True, null=True)  # Field name made lowercase.
    uw_acceso_conf1 = models.SmallIntegerField(db_column='UW_ACCESO_CONF1', blank=True, null=True)  # Field name made lowercase.
    uw_acceso_conf2 = models.SmallIntegerField(db_column='UW_ACCESO_CONF2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIOS_WEB'



class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
