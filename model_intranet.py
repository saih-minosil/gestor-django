# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CajetinesUnifilares(models.Model):
    pk = models.CompositePrimaryKey('CU_CODIGO_MAPA', 'CU_ESTACION_TXT')
    cu_codigo_mapa = models.CharField(db_column='CU_CODIGO_MAPA', max_length=3)  # Field name made lowercase.
    cu_estacion_txt = models.CharField(db_column='CU_ESTACION_TXT', max_length=4)  # Field name made lowercase.
    cu_icono_x = models.SmallIntegerField(db_column='CU_ICONO_X', blank=True, null=True)  # Field name made lowercase.
    cu_icono_y = models.SmallIntegerField(db_column='CU_ICONO_Y', blank=True, null=True)  # Field name made lowercase.
    cu_nombre_x = models.SmallIntegerField(db_column='CU_NOMBRE_X', blank=True, null=True)  # Field name made lowercase.
    cu_nombre_y = models.SmallIntegerField(db_column='CU_NOMBRE_Y', blank=True, null=True)  # Field name made lowercase.
    cu_tag = models.CharField(db_column='CU_TAG', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cu_posicion_tag = models.SmallIntegerField(db_column='CU_POSICION_TAG', blank=True, null=True)  # Field name made lowercase.
    cu_lado_enlace = models.CharField(db_column='CU_LADO_ENLACE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cu_ver_mapa = models.SmallIntegerField(db_column='CU_VER_MAPA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAJETINES_UNIFILARES'
        unique_together = (('cu_codigo_mapa', 'cu_estacion_txt'),)


class CajetinesWeb(models.Model):
    pk = models.CompositePrimaryKey('CW_ENTORNO', 'CW_TIPO_AREA', 'CW_CODIGO_MAPA', 'CW_ESTACION_TXT')
    cw_entorno = models.SmallIntegerField(db_column='CW_ENTORNO')  # Field name made lowercase.
    cw_tipo_area = models.CharField(db_column='CW_TIPO_AREA', max_length=3)  # Field name made lowercase.
    cw_codigo_mapa = models.CharField(db_column='CW_CODIGO_MAPA', max_length=3)  # Field name made lowercase.
    cw_estacion_txt = models.CharField(db_column='CW_ESTACION_TXT', max_length=4)  # Field name made lowercase.
    cw_tipo_cajetin = models.SmallIntegerField(db_column='CW_TIPO_CAJETIN', blank=True, null=True)  # Field name made lowercase.
    cw_x = models.FloatField(db_column='CW_X', blank=True, null=True)  # Field name made lowercase.
    cw_y = models.FloatField(db_column='CW_Y', blank=True, null=True)  # Field name made lowercase.
    cw_lado_enlace = models.CharField(db_column='CW_LADO_ENLACE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cw_tag_tendencia = models.CharField(db_column='CW_TAG_TENDENCIA', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cw_ver_mapa = models.SmallIntegerField(db_column='CW_VER_MAPA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAJETINES_WEB'
        unique_together = (('cw_entorno', 'cw_tipo_area', 'cw_codigo_mapa', 'cw_estacion_txt'),)


class CajetinesWebTags(models.Model):
    pk = models.CompositePrimaryKey('CWT_ENTORNO', 'CWT_TIPO_AREA', 'CWT_CODIGO_MAPA', 'CWT_ESTACION_TXT', 'CWT_TAG')
    cwt_entorno = models.SmallIntegerField(db_column='CWT_ENTORNO')  # Field name made lowercase.
    cwt_tipo_area = models.CharField(db_column='CWT_TIPO_AREA', max_length=3)  # Field name made lowercase.
    cwt_codigo_mapa = models.CharField(db_column='CWT_CODIGO_MAPA', max_length=3)  # Field name made lowercase.
    cwt_estacion_txt = models.CharField(db_column='CWT_ESTACION_TXT', max_length=4)  # Field name made lowercase.
    cwt_tag = models.CharField(db_column='CWT_TAG', max_length=12)  # Field name made lowercase.
    cwt_numorden = models.SmallIntegerField(db_column='CWT_NUMORDEN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAJETINES_WEB_TAGS'
        unique_together = (('cwt_entorno', 'cwt_tipo_area', 'cwt_codigo_mapa', 'cwt_estacion_txt', 'cwt_tag'),)


class Comunidades(models.Model):
    ca_codigo = models.SmallIntegerField(db_column='CA_CODIGO', primary_key=True)  # Field name made lowercase.
    ca_descripcion = models.CharField(db_column='CA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMUNIDADES'


class ConfiguracionWeb(models.Model):
    num_dias = models.SmallIntegerField(db_column='NUM_DIAS', blank=True, null=True)  # Field name made lowercase.
    ultimo_traspaso = models.DateTimeField(db_column='ULTIMO_TRASPASO', blank=True, null=True)  # Field name made lowercase.
    ultimo_pendiente = models.DateTimeField(db_column='ULTIMO_PENDIENTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONFIGURACION_WEB'


class ConsDia(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor_min = models.FloatField(db_column='CC_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
    cc_f_valor_min = models.DateTimeField(db_column='CC_F_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_max = models.FloatField(db_column='CC_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
    cc_f_valor_max = models.DateTimeField(db_column='CC_F_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
    cc_valor_ultimo = models.FloatField(db_column='CC_VALOR_ULTIMO', blank=True, null=True)  # Field name made lowercase.
    cc_valor_gradiente = models.FloatField(db_column='CC_VALOR_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_porcen = models.FloatField(db_column='CC_PORCEN', blank=True, null=True)  # Field name made lowercase.
    cc_f_gradiente = models.DateTimeField(db_column='CC_F_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
    cc_volumen = models.FloatField(db_column='CC_VOLUMEN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONS_DIA'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class ConsMes(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor_min = models.FloatField(db_column='CC_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
    cc_f_valor_min = models.DateTimeField(db_column='CC_F_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_max = models.FloatField(db_column='CC_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
    cc_f_valor_max = models.DateTimeField(db_column='CC_F_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
    cc_valor_ultimo = models.FloatField(db_column='CC_VALOR_ULTIMO', blank=True, null=True)  # Field name made lowercase.
    cc_valor_gradiente = models.FloatField(db_column='CC_VALOR_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_porcen = models.FloatField(db_column='CC_PORCEN', blank=True, null=True)  # Field name made lowercase.
    cc_f_gradiente = models.DateTimeField(db_column='CC_F_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
    cc_volumen = models.FloatField(db_column='CC_VOLUMEN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONS_MES'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosHorarios(models.Model):
    pk = models.CompositePrimaryKey('HO_TAG_TXT', 'HO_FECHA_HORA')
    ho_tag_txt = models.CharField(db_column='HO_TAG_TXT', max_length=12)  # Field name made lowercase.
    ho_fecha_hora = models.DateTimeField(db_column='HO_FECHA_HORA')  # Field name made lowercase.
    ho_valor_horario = models.FloatField(db_column='HO_VALOR_HORARIO', blank=True, null=True)  # Field name made lowercase.
    ho_calidad = models.SmallIntegerField(db_column='HO_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_HORARIOS'
        unique_together = (('ho_tag_txt', 'ho_fecha_hora'),)


class DatosQuinceminutales(models.Model):
    pk = models.CompositePrimaryKey('HO_TAG_TXT', 'HO_FECHA_HORA')
    ho_tag_txt = models.CharField(db_column='HO_TAG_TXT', max_length=12)  # Field name made lowercase.
    ho_fecha_hora = models.DateTimeField(db_column='HO_FECHA_HORA')  # Field name made lowercase.
    ho_valor_horario = models.FloatField(db_column='HO_VALOR_HORARIO', blank=True, null=True)  # Field name made lowercase.
    ho_calidad = models.SmallIntegerField(db_column='HO_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_QUINCEMINUTALES'
        unique_together = (('ho_tag_txt', 'ho_fecha_hora'),)


class DatosQuinceminutales20122015(models.Model):
    pk = models.CompositePrimaryKey('HO_TAG_TXT', 'HO_FECHA_HORA')
    ho_tag_txt = models.CharField(db_column='HO_TAG_TXT', max_length=12)  # Field name made lowercase.
    ho_fecha_hora = models.DateTimeField(db_column='HO_FECHA_HORA')  # Field name made lowercase.
    ho_valor_horario = models.FloatField(db_column='HO_VALOR_HORARIO', blank=True, null=True)  # Field name made lowercase.
    ho_calidad = models.SmallIntegerField(db_column='HO_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_QUINCEMINUTALES_2012-2015'
        unique_together = (('ho_tag_txt', 'ho_fecha_hora'),)


class DatosQuinceminutales2015(models.Model):
    pk = models.CompositePrimaryKey('HO_TAG_TXT', 'HO_FECHA_HORA')
    ho_tag_txt = models.CharField(db_column='HO_TAG_TXT', max_length=12)  # Field name made lowercase.
    ho_fecha_hora = models.DateTimeField(db_column='HO_FECHA_HORA')  # Field name made lowercase.
    ho_valor_horario = models.FloatField(db_column='HO_VALOR_HORARIO', blank=True, null=True)  # Field name made lowercase.
    ho_calidad = models.SmallIntegerField(db_column='HO_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_QUINCEMINUTALES_2015'
        unique_together = (('ho_tag_txt', 'ho_fecha_hora'),)


class DatosQuinceminutales2016(models.Model):
    pk = models.CompositePrimaryKey('HO_TAG_TXT', 'HO_FECHA_HORA')
    ho_tag_txt = models.CharField(db_column='HO_TAG_TXT', max_length=12)  # Field name made lowercase.
    ho_fecha_hora = models.DateTimeField(db_column='HO_FECHA_HORA')  # Field name made lowercase.
    ho_valor_horario = models.FloatField(db_column='HO_VALOR_HORARIO', blank=True, null=True)  # Field name made lowercase.
    ho_calidad = models.SmallIntegerField(db_column='HO_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_QUINCEMINUTALES_2016'
        unique_together = (('ho_tag_txt', 'ho_fecha_hora'),)


class DatosQuinceminutales2017(models.Model):
    pk = models.CompositePrimaryKey('HO_TAG_TXT', 'HO_FECHA_HORA')
    ho_tag_txt = models.CharField(db_column='HO_TAG_TXT', max_length=12)  # Field name made lowercase.
    ho_fecha_hora = models.DateTimeField(db_column='HO_FECHA_HORA')  # Field name made lowercase.
    ho_valor_horario = models.FloatField(db_column='HO_VALOR_HORARIO', blank=True, null=True)  # Field name made lowercase.
    ho_calidad = models.SmallIntegerField(db_column='HO_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_QUINCEMINUTALES_2017'
        unique_together = (('ho_tag_txt', 'ho_fecha_hora'),)


class DatosQuinceminutales2018(models.Model):
    pk = models.CompositePrimaryKey('HO_TAG_TXT', 'HO_FECHA_HORA')
    ho_tag_txt = models.CharField(db_column='HO_TAG_TXT', max_length=12)  # Field name made lowercase.
    ho_fecha_hora = models.DateTimeField(db_column='HO_FECHA_HORA')  # Field name made lowercase.
    ho_valor_horario = models.FloatField(db_column='HO_VALOR_HORARIO', blank=True, null=True)  # Field name made lowercase.
    ho_calidad = models.SmallIntegerField(db_column='HO_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_QUINCEMINUTALES_2018'
        unique_together = (('ho_tag_txt', 'ho_fecha_hora'),)


class DatosQuinceminutales2019(models.Model):
    pk = models.CompositePrimaryKey('HO_TAG_TXT', 'HO_FECHA_HORA')
    ho_tag_txt = models.CharField(db_column='HO_TAG_TXT', max_length=12)  # Field name made lowercase.
    ho_fecha_hora = models.DateTimeField(db_column='HO_FECHA_HORA')  # Field name made lowercase.
    ho_valor_horario = models.FloatField(db_column='HO_VALOR_HORARIO', blank=True, null=True)  # Field name made lowercase.
    ho_calidad = models.SmallIntegerField(db_column='HO_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_QUINCEMINUTALES_2019'
        unique_together = (('ho_tag_txt', 'ho_fecha_hora'),)


class DatosQuinceminutales2020(models.Model):
    pk = models.CompositePrimaryKey('HO_TAG_TXT', 'HO_FECHA_HORA')
    ho_tag_txt = models.CharField(db_column='HO_TAG_TXT', max_length=12)  # Field name made lowercase.
    ho_fecha_hora = models.DateTimeField(db_column='HO_FECHA_HORA')  # Field name made lowercase.
    ho_valor_horario = models.FloatField(db_column='HO_VALOR_HORARIO', blank=True, null=True)  # Field name made lowercase.
    ho_calidad = models.SmallIntegerField(db_column='HO_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_QUINCEMINUTALES_2020'
        unique_together = (('ho_tag_txt', 'ho_fecha_hora'),)


class DatosQuinceminutales2021(models.Model):
    pk = models.CompositePrimaryKey('HO_TAG_TXT', 'HO_FECHA_HORA')
    ho_tag_txt = models.CharField(db_column='HO_TAG_TXT', max_length=12)  # Field name made lowercase.
    ho_fecha_hora = models.DateTimeField(db_column='HO_FECHA_HORA')  # Field name made lowercase.
    ho_valor_horario = models.FloatField(db_column='HO_VALOR_HORARIO', blank=True, null=True)  # Field name made lowercase.
    ho_calidad = models.SmallIntegerField(db_column='HO_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_QUINCEMINUTALES_2021'
        unique_together = (('ho_tag_txt', 'ho_fecha_hora'),)


class DatosQuinceminutales20222(models.Model):
    pk = models.CompositePrimaryKey('HO_TAG_TXT', 'HO_FECHA_HORA')
    ho_tag_txt = models.CharField(db_column='HO_TAG_TXT', max_length=12)  # Field name made lowercase.
    ho_fecha_hora = models.DateTimeField(db_column='HO_FECHA_HORA')  # Field name made lowercase.
    ho_valor_horario = models.FloatField(db_column='HO_VALOR_HORARIO', blank=True, null=True)  # Field name made lowercase.
    ho_calidad = models.SmallIntegerField(db_column='HO_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_QUINCEMINUTALES_2022_2'
        unique_together = (('ho_tag_txt', 'ho_fecha_hora'),)


class GruposTiposSenales(models.Model):
    gs_codigo = models.CharField(db_column='GS_CODIGO', primary_key=True, max_length=5)  # Field name made lowercase.
    gs_descripcion = models.CharField(db_column='GS_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gs_orden = models.SmallIntegerField(db_column='GS_ORDEN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GRUPOS_TIPOS_SENALES'


class ListaActividades(models.Model):
    la_codigo = models.SmallIntegerField(db_column='LA_CODIGO', primary_key=True)  # Field name made lowercase.
    la_descripcion = models.CharField(db_column='LA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_ACTIVIDADES'


class ListaEmpresas(models.Model):
    le_codigo = models.IntegerField(db_column='LE_CODIGO', primary_key=True)  # Field name made lowercase.
    le_nombre = models.CharField(db_column='LE_NOMBRE', max_length=100)  # Field name made lowercase.
    le_nif = models.CharField(db_column='LE_NIF', max_length=15, blank=True, null=True)  # Field name made lowercase.
    le_direccion = models.CharField(db_column='LE_DIRECCION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    le_cp = models.CharField(db_column='LE_CP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    le_poblacion = models.IntegerField(db_column='LE_POBLACION', blank=True, null=True)  # Field name made lowercase.
    le_provincia = models.SmallIntegerField(db_column='LE_PROVINCIA', blank=True, null=True)  # Field name made lowercase.
    le_telefono1 = models.CharField(db_column='LE_TELEFONO1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    le_telefono2 = models.CharField(db_column='LE_TELEFONO2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    le_fax = models.CharField(db_column='LE_FAX', max_length=15, blank=True, null=True)  # Field name made lowercase.
    le_persona_contacto = models.IntegerField(db_column='LE_PERSONA_CONTACTO', blank=True, null=True)  # Field name made lowercase.
    le_cargo = models.CharField(db_column='LE_CARGO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    le_correo = models.CharField(db_column='LE_CORREO', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_EMPRESAS'


class ListaEstaciones(models.Model):
    le_codigo_txt = models.CharField(db_column='LE_CODIGO_TXT', primary_key=True, max_length=4)  # Field name made lowercase.
    le_tipo_estacion = models.CharField(db_column='LE_TIPO_ESTACION', max_length=2)  # Field name made lowercase.
    le_zona = models.SmallIntegerField(db_column='LE_ZONA')  # Field name made lowercase.
    le_nombre = models.CharField(db_column='LE_NOMBRE', max_length=30)  # Field name made lowercase.
    le_nombre_corto = models.CharField(db_column='LE_NOMBRE_CORTO', max_length=18)  # Field name made lowercase.
    le_comu_auto = models.SmallIntegerField(db_column='LE_COMU_AUTO', blank=True, null=True)  # Field name made lowercase.
    le_provincia = models.SmallIntegerField(db_column='LE_PROVINCIA', blank=True, null=True)  # Field name made lowercase.
    le_municipio = models.IntegerField(db_column='LE_MUNICIPIO', blank=True, null=True)  # Field name made lowercase.
    le_rio = models.IntegerField(db_column='LE_RIO', blank=True, null=True)  # Field name made lowercase.
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


class ListaEstacionesCaudales(models.Model):
    lq_codigo_txt = models.CharField(db_column='LQ_CODIGO_TXT', primary_key=True, max_length=4)  # Field name made lowercase.
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
        managed = False
        db_table = 'LISTA_ESTACIONES_CAUDALES'


class ListaEstacionesDerivaciones(models.Model):
    pk = models.CompositePrimaryKey('LED_CODIGO_TXT', 'LED_TIPO_DERIVACION', 'LED_NOMBRE')
    led_codigo_txt = models.CharField(db_column='LED_CODIGO_TXT', max_length=4)  # Field name made lowercase.
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
        managed = False
        db_table = 'LISTA_ESTACIONES_DERIVACIONES'
        unique_together = (('led_codigo_txt', 'led_tipo_derivacion', 'led_nombre'),)


class ListaEstacionesPresas(models.Model):
    lep_codigo_txt = models.CharField(db_column='LEP_CODIGO_TXT', primary_key=True, max_length=4)  # Field name made lowercase.
    lep_tipo_explotacion = models.CharField(db_column='LEP_TIPO_EXPLOTACION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_tipo_presa = models.CharField(db_column='LEP_TIPO_PRESA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lep_granpresa = models.CharField(db_column='LEP_GRANPRESA', max_length=2, blank=True, null=True)  # Field name made lowercase.
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
        managed = False
        db_table = 'LISTA_ESTACIONES_PRESAS'


class ListaEstacionesRemotas(models.Model):
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


class ListaResumenNiveles(models.Model):
    pk = models.CompositePrimaryKey('LRN_ENTORNO', 'LRN_CONFEDERACION', 'LRN_ESTACION_TXT', 'LRN_TAG_TXT')
    lrn_entorno = models.SmallIntegerField(db_column='LRN_ENTORNO')  # Field name made lowercase.
    lrn_confederacion = models.SmallIntegerField(db_column='LRN_CONFEDERACION')  # Field name made lowercase.
    lrn_estacion_txt = models.CharField(db_column='LRN_ESTACION_TXT', max_length=4)  # Field name made lowercase.
    lrn_tag_txt = models.CharField(db_column='LRN_TAG_TXT', max_length=12)  # Field name made lowercase.
    lrn_orden = models.SmallIntegerField(db_column='LRN_ORDEN', blank=True, null=True)  # Field name made lowercase.
    lrn_tipo = models.CharField(db_column='LRN_TIPO', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_RESUMEN_NIVELES'
        unique_together = (('lrn_entorno', 'lrn_confederacion', 'lrn_estacion_txt', 'lrn_tag_txt'),)


class ListaResumenNivelesCopia(models.Model):
    pk = models.CompositePrimaryKey('LRN_ENTORNO', 'LRN_CONFEDERACION', 'LRN_ESTACION_TXT', 'LRN_TAG_TXT')
    lrn_entorno = models.SmallIntegerField(db_column='LRN_ENTORNO')  # Field name made lowercase.
    lrn_confederacion = models.SmallIntegerField(db_column='LRN_CONFEDERACION')  # Field name made lowercase.
    lrn_estacion_txt = models.CharField(db_column='LRN_ESTACION_TXT', max_length=4)  # Field name made lowercase.
    lrn_tag_txt = models.CharField(db_column='LRN_TAG_TXT', max_length=12)  # Field name made lowercase.
    lrn_orden = models.SmallIntegerField(db_column='LRN_ORDEN', blank=True, null=True)  # Field name made lowercase.
    lrn_tipo = models.CharField(db_column='LRN_TIPO', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_RESUMEN_NIVELES_COPIA'
        unique_together = (('lrn_entorno', 'lrn_confederacion', 'lrn_estacion_txt', 'lrn_tag_txt'),)


class ListaSenales(models.Model):
    ls_tag_txt = models.CharField(db_column='LS_TAG_TXT', primary_key=True, max_length=16)  # Field name made lowercase.
    ls_descripcion = models.CharField(db_column='LS_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ls_estacion_txt = models.CharField(db_column='LS_ESTACION_TXT', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ls_tipo_senal = models.CharField(db_column='LS_TIPO_SENAL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_naturaleza = models.SmallIntegerField(db_column='LS_NATURALEZA', blank=True, null=True)  # Field name made lowercase.
    ls_recid = models.IntegerField(db_column='LS_RECID')  # Field name made lowercase.
    ls_origen = models.CharField(db_column='LS_ORIGEN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ls_max_grafico = models.FloatField(db_column='LS_MAX_GRAFICO', blank=True, null=True)  # Field name made lowercase.
    ls_min_grafico = models.FloatField(db_column='LS_MIN_GRAFICO', blank=True, null=True)  # Field name made lowercase.
    ls_tiempo_grafico = models.CharField(db_column='LS_TIEMPO_GRAFICO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ls_unid_ing = models.CharField(db_column='LS_UNID_ING', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ls_digitos_enteros = models.SmallIntegerField(db_column='LS_DIGITOS_ENTEROS', blank=True, null=True)  # Field name made lowercase.
    ls_digitos_decimales = models.SmallIntegerField(db_column='LS_DIGITOS_DECIMALES', blank=True, null=True)  # Field name made lowercase.
    ls_tipo_almacenamiento = models.CharField(db_column='LS_TIPO_ALMACENAMIENTO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_alarma = models.CharField(db_column='LS_ALARMA', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ls_tendencia = models.CharField(db_column='LS_TENDENCIA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ls_tipo_consolidacion = models.SmallIntegerField(db_column='LS_TIPO_CONSOLIDACION', blank=True, null=True)  # Field name made lowercase.
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
        managed = False
        db_table = 'LISTA_SENALES'


class ListaSenalesWeb(models.Model):
    ls_tag_txt = models.CharField(db_column='LS_TAG_TXT', primary_key=True, max_length=16)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_SENALES_WEB'


class ListaZonas(models.Model):
    lz_codigo = models.SmallIntegerField(db_column='LZ_CODIGO', primary_key=True)  # Field name made lowercase.
    lz_descripcion = models.CharField(db_column='LZ_DESCRIPCION', max_length=16)  # Field name made lowercase.
    lz_confederacion = models.SmallIntegerField(db_column='LZ_CONFEDERACION', blank=True, null=True)  # Field name made lowercase.
    lz_superficie = models.DecimalField(db_column='LZ_SUPERFICIE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_ZONAS'


class MapasWeb(models.Model):
    pk = models.CompositePrimaryKey('MW_ENTORNO', 'MW_CODIGO')
    mw_entorno = models.SmallIntegerField(db_column='MW_ENTORNO')  # Field name made lowercase.
    mw_codigo = models.CharField(db_column='MW_CODIGO', max_length=3)  # Field name made lowercase.
    mw_utm_x = models.FloatField(db_column='MW_UTM_X', blank=True, null=True)  # Field name made lowercase.
    mw_utm_y = models.FloatField(db_column='MW_UTM_Y', blank=True, null=True)  # Field name made lowercase.
    mw_utms_por_pixel = models.FloatField(db_column='MW_UTMS_POR_PIXEL', blank=True, null=True)  # Field name made lowercase.
    mw_descripcion = models.CharField(db_column='MW_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MAPAS_WEB'
        unique_together = (('mw_entorno', 'mw_codigo'),)


class Moviles(models.Model):
    identificador = models.CharField(db_column='IDENTIFICADOR', primary_key=True, max_length=255)  # Field name made lowercase.
    ancho_util = models.IntegerField(db_column='ANCHO_UTIL', blank=True, null=True)  # Field name made lowercase.
    ancho_pantalla = models.IntegerField(db_column='ANCHO_PANTALLA', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    soporta_image_maps = models.IntegerField(db_column='SOPORTA_IMAGE_MAPS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVILES'


class NaturalezaSenales(models.Model):
    ns_codigo = models.SmallIntegerField(db_column='NS_CODIGO', primary_key=True)  # Field name made lowercase.
    ns_nombre = models.CharField(db_column='NS_NOMBRE', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NATURALEZA_SENALES'


class Poblaciones(models.Model):
    po_codigo = models.IntegerField(db_column='PO_CODIGO', primary_key=True)  # Field name made lowercase.
    po_provincia = models.SmallIntegerField(db_column='PO_PROVINCIA', blank=True, null=True)  # Field name made lowercase.
    po_descripcion = models.CharField(db_column='PO_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'POBLACIONES'


class Provincias(models.Model):
    pr_codigo = models.SmallIntegerField(db_column='PR_CODIGO', primary_key=True)  # Field name made lowercase.
    pr_descripcion = models.CharField(db_column='PR_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pr_comunidad = models.SmallIntegerField(db_column='PR_COMUNIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROVINCIAS'


class Rios(models.Model):
    ri_codigo = models.IntegerField(db_column='RI_CODIGO', primary_key=True)  # Field name made lowercase.
    ri_descripcion = models.CharField(db_column='RI_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIOS'


class TablaLuis(models.Model):
    luis_clave = models.SmallIntegerField(db_column='LUIS_CLAVE', primary_key=True)  # Field name made lowercase.
    luis_texto = models.CharField(db_column='LUIS_TEXTO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    luis_texto2 = models.CharField(db_column='LUIS_TEXTO2', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TABLA_LUIS'


class TextosWeb(models.Model):
    pk = models.CompositePrimaryKey('DOMINIO', 'TIPO', 'ITEM', 'ORDEN')
    dominio = models.CharField(db_column='DOMINIO', max_length=50)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=50)  # Field name made lowercase.
    item = models.CharField(db_column='ITEM', max_length=50)  # Field name made lowercase.
    orden = models.SmallIntegerField(db_column='ORDEN')  # Field name made lowercase.
    texto_spa = models.CharField(db_column='TEXTO_SPA', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    texto_gal = models.CharField(db_column='TEXTO_GAL', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    texto_eus = models.CharField(db_column='TEXTO_EUS', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    es_html = models.SmallIntegerField(db_column='ES_HTML', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEXTOS_WEB'
        unique_together = (('dominio', 'tipo', 'item', 'orden'),)


class TiposAlmacenamiento(models.Model):
    ta_codigo = models.CharField(db_column='TA_CODIGO', primary_key=True, max_length=5)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ta_periodo = models.IntegerField(db_column='TA_PERIODO', blank=True, null=True)  # Field name made lowercase.
    ta_almacen = models.IntegerField(db_column='TA_ALMACEN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_ALMACENAMIENTO'


class TiposAreas(models.Model):
    ta_codigo = models.CharField(db_column='TA_CODIGO', primary_key=True, max_length=3)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_AREAS'


class TiposCajetines(models.Model):
    tc_codigo = models.SmallIntegerField(db_column='TC_CODIGO', primary_key=True)  # Field name made lowercase.
    tc_ancho_tag = models.SmallIntegerField(db_column='TC_ANCHO_TAG', blank=True, null=True)  # Field name made lowercase.
    tc_alto_tag = models.SmallIntegerField(db_column='TC_ALTO_TAG', blank=True, null=True)  # Field name made lowercase.
    tc_tags_fila = models.SmallIntegerField(db_column='TC_TAGS_FILA', blank=True, null=True)  # Field name made lowercase.
    tc_filas = models.SmallIntegerField(db_column='TC_FILAS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_CAJETINES'


class TiposCalidades(models.Model):
    tca_codigo = models.SmallIntegerField(db_column='TCA_CODIGO', primary_key=True)  # Field name made lowercase.
    tca_descripcion = models.CharField(db_column='TCA_DESCRIPCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tca_porcen_ini = models.SmallIntegerField(db_column='TCA_PORCEN_INI', blank=True, null=True)  # Field name made lowercase.
    tca_porcen_fin = models.SmallIntegerField(db_column='TCA_PORCEN_FIN', blank=True, null=True)  # Field name made lowercase.
    tca_tipo = models.CharField(db_column='TCA_TIPO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tca_falta = models.DateTimeField(db_column='TCA_FALTA', blank=True, null=True)  # Field name made lowercase.
    tca_fmodif = models.DateTimeField(db_column='TCA_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_CALIDADES'


class TiposEstaciones(models.Model):
    te_codigo = models.CharField(db_column='TE_CODIGO', primary_key=True, max_length=2)  # Field name made lowercase.
    te_descripcion = models.CharField(db_column='TE_DESCRIPCION', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_ESTACIONES'


class TiposSenales(models.Model):
    pk = models.CompositePrimaryKey('TS_CODIGO', 'TS_NATURALEZA')
    ts_codigo = models.CharField(db_column='TS_CODIGO', max_length=5)  # Field name made lowercase.
    ts_descripcion = models.CharField(db_column='TS_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ts_naturaleza = models.SmallIntegerField(db_column='TS_NATURALEZA')  # Field name made lowercase.
    ts_nombre_corto = models.CharField(db_column='TS_NOMBRE_CORTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
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

    class Meta:
        managed = False
        db_table = 'UNIDADES_INGENIERIA'


class UsuariosWeb(models.Model):
    nombreusuario = models.CharField(db_column='NOMBREUSUARIO', primary_key=True, max_length=30)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='CIUDAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='PROVINCIA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='PAIS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    actividad = models.SmallIntegerField(db_column='ACTIVIDAD', blank=True, null=True)  # Field name made lowercase.
    codigo_movil = models.CharField(db_column='CODIGO_MOVIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    estado = models.SmallIntegerField(db_column='ESTADO', blank=True, null=True)  # Field name made lowercase.
    acceso_datos_historicos = models.SmallIntegerField(db_column='ACCESO_DATOS_HISTORICOS', blank=True, null=True)  # Field name made lowercase.
    acceso_datos_quinceminutales = models.SmallIntegerField(db_column='ACCESO_DATOS_QUINCEMINUTALES', blank=True, null=True)  # Field name made lowercase.
    acceso_informes_privados = models.SmallIntegerField(db_column='ACCESO_INFORMES_PRIVADOS', blank=True, null=True)  # Field name made lowercase.
    acceso_administrador = models.SmallIntegerField(db_column='ACCESO_ADMINISTRADOR', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='OBSERVACIONES', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    otra_actividad = models.CharField(db_column='OTRA_ACTIVIDAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pantalla_accesibilidad = models.SmallIntegerField(db_column='PANTALLA_ACCESIBILIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIOS_WEB'


class UsuariosWebDatos(models.Model):
    pk = models.CompositePrimaryKey('NOMBREUSUARIO', 'TIPO_DATO', 'CODIGO')
    nombreusuario = models.CharField(db_column='NOMBREUSUARIO', max_length=30)  # Field name made lowercase.
    tipo_dato = models.CharField(db_column='TIPO_DATO', max_length=10)  # Field name made lowercase.
    codigo = models.CharField(db_column='CODIGO', max_length=12)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIOS_WEB_DATOS'
        unique_together = (('nombreusuario', 'tipo_dato', 'codigo'),)


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
