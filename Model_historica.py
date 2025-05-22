# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CabFichero(models.Model):
    pk = models.CompositePrimaryKey('CF_TAG', 'CF_VERSION')
    cf_tag = models.IntegerField(db_column='CF_TAG')  # Field name made lowercase.
    cf_version = models.CharField(db_column='CF_VERSION', max_length=6)  # Field name made lowercase.
    cf_fecha_inicio = models.DateTimeField(db_column='CF_FECHA_INICIO', blank=True, null=True)  # Field name made lowercase.
    cf_fecha_fin = models.DateTimeField(db_column='CF_FECHA_FIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAB_FICHERO'
        unique_together = (('cf_tag', 'cf_version'),)


class CaudalMaximo(models.Model):
    nombre_estacion = models.CharField(db_column='NOMBRE_ESTACION', primary_key=True, max_length=4)  # Field name made lowercase.
    fecha_inicio_periodo = models.DateTimeField(db_column='FECHA_INICIO_PERIODO', blank=True, null=True)  # Field name made lowercase.
    fecha_caudal_maximo = models.DateTimeField(db_column='FECHA_CAUDAL_MAXIMO', blank=True, null=True)  # Field name made lowercase.
    valor_maximo_caudal = models.FloatField(db_column='VALOR_MAXIMO_CAUDAL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAUDAL_MAXIMO'


class Comunidades(models.Model):
    ca_codigo = models.SmallIntegerField(db_column='CA_CODIGO', primary_key=True, db_comment='Codigo de la comunidad autonom')  # Field name made lowercase.
    ca_descripcion = models.CharField(db_column='CA_DESCRIPCION', max_length=50, blank=True, null=True, db_comment='Nombre de la comunidad autonom')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMUNIDADES'


class ConceptosAcuse(models.Model):
    ca_codigo = models.SmallIntegerField(db_column='CA_CODIGO', primary_key=True)  # Field name made lowercase.
    ca_descripcion = models.CharField(db_column='CA_DESCRIPCION', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONCEPTOS_ACUSE'


class ConfiguracionAlarmas(models.Model):
    cal_codigo = models.SmallIntegerField(db_column='CAL_CODIGO', primary_key=True)  # Field name made lowercase.
    cal_tmp_aviso_voz = models.SmallIntegerField(db_column='CAL_TMP_AVISO_VOZ', blank=True, null=True)  # Field name made lowercase.
    cal_tmp_aviso_sms = models.SmallIntegerField(db_column='CAL_TMP_AVISO_SMS', blank=True, null=True)  # Field name made lowercase.
    cal_puesto_ultimo_recurso = models.ForeignKey('PuestosTrabajo', models.DO_NOTHING, db_column='CAL_PUESTO_ULTIMO_RECURSO', blank=True, null=True)  # Field name made lowercase.
    cal_contador_aviso = models.IntegerField(db_column='CAL_CONTADOR_AVISO', blank=True, null=True)  # Field name made lowercase.
    cal_servidor_smtp = models.CharField(db_column='CAL_SERVIDOR_SMTP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cal_usuario_smtp = models.CharField(db_column='CAL_USUARIO_SMTP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cal_password_smtp = models.CharField(db_column='CAL_PASSWORD_SMTP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cal_correo_retorno = models.CharField(db_column='CAL_CORREO_RETORNO', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONFIGURACION_ALARMAS'


class ConsAnoH(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.ForeignKey('ListaSenales', models.DO_NOTHING, db_column='CC_IDSENAL')  # Field name made lowercase.
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
        db_table = 'CONS_ANO_H'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class ConsAnoN(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.ForeignKey('ListaSenales', models.DO_NOTHING, db_column='CC_IDSENAL')  # Field name made lowercase.
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
        db_table = 'CONS_ANO_N'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class ConsDia(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.ForeignKey('ListaSenales', models.DO_NOTHING, db_column='CC_IDSENAL')  # Field name made lowercase.
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
    cc_traspaso_web = models.SmallIntegerField(db_column='CC_TRASPASO_WEB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONS_DIA'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class ConsMes(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.ForeignKey('ListaSenales', models.DO_NOTHING, db_column='CC_IDSENAL')  # Field name made lowercase.
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
    cc_traspaso_web = models.SmallIntegerField(db_column='CC_TRASPASO_WEB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONS_MES'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class ContactosPactuacion(models.Model):
    pk = models.CompositePrimaryKey('CPA_CODIGO', 'CPA_COD_PUESTO')
    cpa_codigo = models.ForeignKey('PlanesActuacion', models.DO_NOTHING, db_column='CPA_CODIGO')  # Field name made lowercase.
    cpa_cod_puesto = models.ForeignKey('PuestosTrabajo', models.DO_NOTHING, db_column='CPA_COD_PUESTO')  # Field name made lowercase.
    cpa_orden_aviso = models.SmallIntegerField(db_column='CPA_ORDEN_AVISO', blank=True, null=True)  # Field name made lowercase.
    cpa_observaciones = models.CharField(db_column='CPA_OBSERVACIONES', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTACTOS_PACTUACION'
        unique_together = (('cpa_codigo', 'cpa_orden_aviso'), ('cpa_codigo', 'cpa_cod_puesto'),)


class ContactosPactuacionAutomaticos(models.Model):
    pk = models.CompositePrimaryKey('CPAA_CODIGO', 'CPAA_COD_PUESTO')
    cpaa_codigo = models.ForeignKey('PlanesActuacionAutomaticos', models.DO_NOTHING, db_column='CPAA_CODIGO')  # Field name made lowercase.
    cpaa_cod_puesto = models.ForeignKey('PuestosTrabajo', models.DO_NOTHING, db_column='CPAA_COD_PUESTO')  # Field name made lowercase.
    cpaa_observaciones = models.CharField(db_column='CPAA_OBSERVACIONES', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTACTOS_PACTUACION_AUTOMATICOS'
        unique_together = (('cpaa_codigo', 'cpaa_cod_puesto'),)


class CronologicoAvisos(models.Model):
    pk = models.CompositePrimaryKey('CA_SENAL', 'CA_CONT_IP21', 'CA_FECHA')
    ca_senal = models.IntegerField(db_column='CA_SENAL')  # Field name made lowercase.
    ca_cont_ip21 = models.IntegerField(db_column='CA_CONT_IP21')  # Field name made lowercase.
    ca_fecha = models.DateTimeField(db_column='CA_FECHA')  # Field name made lowercase.
    ca_tipo_aviso = models.ForeignKey('TiposAvisos', models.DO_NOTHING, db_column='CA_TIPO_AVISO')  # Field name made lowercase.
    ca_alarma = models.CharField(db_column='CA_ALARMA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ca_estado_aparicion = models.CharField(db_column='CA_ESTADO_APARICION', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ca_accion = models.CharField(db_column='CA_ACCION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ca_valor = models.DecimalField(db_column='CA_VALOR', max_digits=20, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    ca_usuario = models.CharField(db_column='CA_USUARIO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ca_tipo_plan = models.CharField(db_column='CA_TIPO_PLAN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ca_plan_actuacion = models.CharField(db_column='CA_PLAN_ACTUACION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ca_orden_aviso = models.SmallIntegerField(db_column='CA_ORDEN_AVISO', blank=True, null=True)  # Field name made lowercase.
    ca_puesto_trabajo = models.CharField(db_column='CA_PUESTO_TRABAJO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ca_persona = models.CharField(db_column='CA_PERSONA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ca_acciones = models.CharField(db_column='CA_ACCIONES', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ca_cont_aviso = models.IntegerField(db_column='CA_CONT_AVISO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRONOLOGICO_AVISOS'
        unique_together = (('ca_senal', 'ca_cont_ip21', 'ca_fecha'),)


class CronologicoFax(models.Model):
    pk = models.CompositePrimaryKey('CF_SISTEMA', 'CF_ID_FAX', 'CF_FECHA')
    cf_sistema = models.CharField(db_column='CF_SISTEMA', max_length=10)  # Field name made lowercase.
    cf_id_fax = models.IntegerField(db_column='CF_ID_FAX')  # Field name made lowercase.
    cf_fecha = models.DateTimeField(db_column='CF_FECHA')  # Field name made lowercase.
    cf_plantilla = models.CharField(db_column='CF_PLANTILLA', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRONOLOGICO_FAX'
        unique_together = (('cf_sistema', 'cf_id_fax', 'cf_fecha'),)


class CronologicoMails(models.Model):
    pk = models.CompositePrimaryKey('CM_SISTEMA', 'CM_ID_MAIL', 'CM_FECHA')
    cm_sistema = models.CharField(db_column='CM_SISTEMA', max_length=50)  # Field name made lowercase.
    cm_id_mail = models.IntegerField(db_column='CM_ID_MAIL')  # Field name made lowercase.
    cm_fecha = models.DateTimeField(db_column='CM_FECHA')  # Field name made lowercase.
    cm_direccion = models.CharField(db_column='CM_DIRECCION', max_length=50)  # Field name made lowercase.
    cm_asunto = models.CharField(db_column='CM_ASUNTO', max_length=100)  # Field name made lowercase.
    cm_mensaje = models.CharField(db_column='CM_MENSAJE', max_length=500)  # Field name made lowercase.
    cm_estado = models.CharField(db_column='CM_ESTADO', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRONOLOGICO_MAILS'
        unique_together = (('cm_sistema', 'cm_id_mail', 'cm_fecha'),)


class CronologicoMailsPrueba(models.Model):
    pk = models.CompositePrimaryKey('CM_SISTEMA', 'CM_ID_MAIL', 'CM_FECHA')
    cm_sistema = models.CharField(db_column='CM_SISTEMA', max_length=50)  # Field name made lowercase.
    cm_id_mail = models.IntegerField(db_column='CM_ID_MAIL')  # Field name made lowercase.
    cm_fecha = models.DateTimeField(db_column='CM_FECHA')  # Field name made lowercase.
    cm_direccion = models.CharField(db_column='CM_DIRECCION', max_length=50)  # Field name made lowercase.
    cm_asunto = models.CharField(db_column='CM_ASUNTO', max_length=100)  # Field name made lowercase.
    cm_mensaje = models.CharField(db_column='CM_MENSAJE', max_length=500)  # Field name made lowercase.
    cm_estado = models.CharField(db_column='CM_ESTADO', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRONOLOGICO_MAILS_prueba'
        unique_together = (('cm_sistema', 'cm_id_mail', 'cm_fecha'),)


class CronologicoMensajesSms(models.Model):
    pk = models.CompositePrimaryKey('CM_SISTEMA', 'CM_ID_SMS', 'CM_FECHA')
    cm_sistema = models.ForeignKey('EstadoMensajesSms', models.DO_NOTHING, db_column='CM_SISTEMA')  # Field name made lowercase.
    cm_id_sms = models.ForeignKey('EstadoMensajesSms', models.DO_NOTHING, db_column='CM_ID_SMS', related_name='cronologicomensajessms_cm_id_sms_set')  # Field name made lowercase.
    cm_fecha = models.DateTimeField(db_column='CM_FECHA')  # Field name made lowercase.
    cm_telefono = models.CharField(db_column='CM_TELEFONO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cm_mensaje = models.CharField(db_column='CM_MENSAJE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cm_acuse = models.BooleanField(db_column='CM_ACUSE')  # Field name made lowercase.
    cm_id_gprs = models.CharField(db_column='CM_ID_GPRS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cm_estado = models.CharField(db_column='CM_ESTADO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CRONOLOGICO_MENSAJES_SMS'
        unique_together = (('cm_sistema', 'cm_id_sms', 'cm_fecha'),)


class CurvasAjuste(models.Model):
    ca_codigo = models.CharField(db_column='CA_CODIGO', primary_key=True, max_length=10)  # Field name made lowercase.
    ca_descripcion = models.CharField(db_column='CA_DESCRIPCION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ca_varx = models.CharField(db_column='CA_VARX', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ca_vary = models.CharField(db_column='CA_VARY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ca_fecha_datos = models.DateTimeField(db_column='CA_FECHA_DATOS', blank=True, null=True)  # Field name made lowercase.
    ca_alin_fecha = models.DateTimeField(db_column='CA_ALIN_FECHA', blank=True, null=True)  # Field name made lowercase.
    ca_alin_coefa = models.DecimalField(db_column='CA_ALIN_COEFA', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_alin_coefb = models.DecimalField(db_column='CA_ALIN_COEFB', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_alin_cuaderr = models.DecimalField(db_column='CA_ALIN_CUADERR', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    ca_apot_fecha = models.DateTimeField(db_column='CA_APOT_FECHA', blank=True, null=True)  # Field name made lowercase.
    ca_apot_coefa = models.DecimalField(db_column='CA_APOT_COEFA', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_apot_coefb = models.DecimalField(db_column='CA_APOT_COEFB', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_apot_cuaderr = models.DecimalField(db_column='CA_APOT_CUADERR', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    ca_aexp_fecha = models.DateTimeField(db_column='CA_AEXP_FECHA', blank=True, null=True)  # Field name made lowercase.
    ca_aexp_coefa = models.DecimalField(db_column='CA_AEXP_COEFA', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_aexp_coefb = models.DecimalField(db_column='CA_AEXP_COEFB', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_aexp_cuaderr = models.DecimalField(db_column='CA_AEXP_CUADERR', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    ca_alog_fecha = models.DateTimeField(db_column='CA_ALOG_FECHA', blank=True, null=True)  # Field name made lowercase.
    ca_alog_coefa = models.DecimalField(db_column='CA_ALOG_COEFA', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_alog_coefb = models.DecimalField(db_column='CA_ALOG_COEFB', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_alog_cuaderr = models.DecimalField(db_column='CA_ALOG_CUADERR', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    ca_apol_fecha = models.DateTimeField(db_column='CA_APOL_FECHA', blank=True, null=True)  # Field name made lowercase.
    ca_apol_grado = models.SmallIntegerField(db_column='CA_APOL_GRADO', blank=True, null=True)  # Field name made lowercase.
    ca_apol_coef0 = models.DecimalField(db_column='CA_APOL_COEF0', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_apol_coef1 = models.DecimalField(db_column='CA_APOL_COEF1', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_apol_coef2 = models.DecimalField(db_column='CA_APOL_COEF2', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_apol_coef3 = models.DecimalField(db_column='CA_APOL_COEF3', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_apol_coef4 = models.DecimalField(db_column='CA_APOL_COEF4', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_apol_coef5 = models.DecimalField(db_column='CA_APOL_COEF5', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_apol_coef6 = models.DecimalField(db_column='CA_APOL_COEF6', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_apol_coef7 = models.DecimalField(db_column='CA_APOL_COEF7', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_apol_coef8 = models.DecimalField(db_column='CA_APOL_COEF8', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_apol_coef9 = models.DecimalField(db_column='CA_APOL_COEF9', max_digits=30, decimal_places=20, blank=True, null=True)  # Field name made lowercase.
    ca_apol_cuaderr = models.DecimalField(db_column='CA_APOL_CUADERR', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CURVAS_AJUSTE'


class CurvasAjusteDatos(models.Model):
    pk = models.CompositePrimaryKey('CAD_CODIGO', 'CAD_NUMPUNTO')
    cad_codigo = models.CharField(db_column='CAD_CODIGO', max_length=10)  # Field name made lowercase.
    cad_numpunto = models.IntegerField(db_column='CAD_NUMPUNTO')  # Field name made lowercase.
    cad_x = models.DecimalField(db_column='CAD_X', max_digits=11, decimal_places=4)  # Field name made lowercase.
    cad_y = models.DecimalField(db_column='CAD_Y', max_digits=11, decimal_places=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CURVAS_AJUSTE_DATOS'
        unique_together = (('cad_codigo', 'cad_numpunto'),)


class CurvasReferencia(models.Model):
    pk = models.CompositePrimaryKey('CR_IDSENAL', 'CR_NUMCURVA', 'CR_MES_H')
    cr_idsenal = models.SmallIntegerField(db_column='CR_IDSENAL')  # Field name made lowercase.
    cr_numcurva = models.SmallIntegerField(db_column='CR_NUMCURVA')  # Field name made lowercase.
    cr_mes_h = models.SmallIntegerField(db_column='CR_MES_H')  # Field name made lowercase.
    cr_valormedio = models.FloatField(db_column='CR_VALORMEDIO', blank=True, null=True)  # Field name made lowercase.
    cr_valorminimo = models.FloatField(db_column='CR_VALORMINIMO', blank=True, null=True)  # Field name made lowercase.
    cr_valormaximo = models.FloatField(db_column='CR_VALORMAXIMO', blank=True, null=True)  # Field name made lowercase.
    cr_nummuestras = models.SmallIntegerField(db_column='CR_NUMMUESTRAS', blank=True, null=True)  # Field name made lowercase.
    cr_ultimo_anyo = models.SmallIntegerField(db_column='CR_ULTIMO_ANYO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CURVAS_REFERENCIA'
        unique_together = (('cr_idsenal', 'cr_numcurva', 'cr_mes_h'),)


class DatosEventos0109(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0109'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0110(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0110'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0111(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0111'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0112(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0112'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0113(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0113'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0114(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0114'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0115(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0115'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0116(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0116'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0117(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0117'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0118(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0118'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0119(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0119'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0120(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0120'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0121(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0121'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0122(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0122'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0123(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0123'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0124(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0124'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0125(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0125'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0209(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0209'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0210(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0210'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0211(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0211'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0212(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0212'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0213(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0213'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0214(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0214'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0215(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0215'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0216(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0216'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0217(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0217'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0218(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0218'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0219(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0219'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0220(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0220'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0221(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0221'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0222(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0222'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0223(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0223'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0224(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0224'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0225(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0225'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0309(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0309'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0310(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0310'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0311(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0311'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0312(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0312'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0313(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0313'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0314(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0314'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0315(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0315'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0316(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0316'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0317(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0317'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0318(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0318'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0319(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0319'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0320(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0320'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0321(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0321'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0322(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0322'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0323(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0323'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0324(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0324'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0325(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0325'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0409(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0409'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0410(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0410'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0411(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0411'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0412(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0412'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0413(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0413'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0414(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0414'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0415(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0415'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0416(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0416'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0417(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0417'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0418(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0418'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0419(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0419'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0420(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0420'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0421(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0421'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0422(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0422'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0423(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0423'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0424(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0424'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0509(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0509'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0510(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0510'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0511(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0511'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0512(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0512'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0513(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0513'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0514(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0514'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0515(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0515'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0516(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0516'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0517(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0517'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0518(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0518'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0519(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0519'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0520(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0520'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0521(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0521'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0522(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0522'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0523(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0523'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0524(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0524'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0609(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0609'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0610(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0610'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0611(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0611'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0612(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0612'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0613(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0613'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0614(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0614'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0615(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0615'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0616(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0616'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0617(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0617'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0618(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0618'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0619(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0619'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0620(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0620'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0621(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0621'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0622(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0622'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0623(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0623'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0624(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0624'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0708(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0708'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0709(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0709'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0710(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0710'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0711(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0711'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0712(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0712'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0713(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0713'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0714(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0714'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0715(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0715'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0716(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0716'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0717(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0717'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0718(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0718'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0719(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0719'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0720(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0720'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0721(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0721'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0722(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0722'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0723(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0723'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0724(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0724'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0808(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0808'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0809(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0809'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0810(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0810'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0811(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0811'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0812(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0812'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0813(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0813'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0814(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0814'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0815(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0815'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0816(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0816'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0817(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0817'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0818(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0818'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0819(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0819'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0820(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0820'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0821(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0821'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0822(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0822'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0823(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0823'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0824(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0824'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0908(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0908'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0909(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0909'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0910(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0910'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0911(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0911'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0912(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0912'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0913(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0913'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0914(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0914'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0915(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0915'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0916(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0916'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0917(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0917'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0918(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0918'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0919(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0919'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0920(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0920'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0921(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0921'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0922(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0922'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0923(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0923'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos0924(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_0924'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1008(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1008'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1009(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1009'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1010(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1010'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1011(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1011'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1012(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1012'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1013(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1013'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1014(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1014'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1015(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1015'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1016(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1016'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1017(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1017'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1018(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1018'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1019(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1019'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1020(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1020'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1021(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1021'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1022(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1022'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1023(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1023'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1024(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1024'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1108(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1108'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1109(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1109'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1110(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1110'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1111(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1111'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1112(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1112'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1113(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1113'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1114(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1114'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1115(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1115'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1116(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1116'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1117(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1117'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1118(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1118'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1119(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1119'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1120(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1120'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1121(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1121'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1122(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1122'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1123(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1123'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1124(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1124'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1208(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1208'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1209(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1209'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1210(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1210'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1211(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1211'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1212(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1212'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1213(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1213'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1214(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1214'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1215(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1215'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1216(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1216'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1216(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1216_'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1217(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1217'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1218(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1218'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1219(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1219'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1220(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1220'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1221(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1221'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1222(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1222'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1223(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1223'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosEventos1224(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA', 'CC_CONTADOR')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_contador = models.IntegerField(db_column='CC_CONTADOR')  # Field name made lowercase.
    cc_tipo = models.CharField(db_column='CC_TIPO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.SmallIntegerField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_txt = models.CharField(db_column='CC_VALOR_TXT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cc_valor_activacion = models.SmallIntegerField(db_column='CC_VALOR_ACTIVACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_EVENTOS_1224'
        unique_together = (('cc_idsenal', 'cc_fecha', 'cc_contador'),)


class DatosManualesAforos(models.Model):
    pk = models.CompositePrimaryKey('DMA_IDSENAL', 'DMA_FECHA')
    dma_idsenal = models.ForeignKey('ListaSenales', models.DO_NOTHING, db_column='DMA_IDSENAL')  # Field name made lowercase.
    dma_fecha = models.DateTimeField(db_column='DMA_FECHA')  # Field name made lowercase.
    dma_valormedio = models.FloatField(db_column='DMA_VALORMEDIO')  # Field name made lowercase.
    dma_valorminimo = models.FloatField(db_column='DMA_VALORMINIMO', blank=True, null=True)  # Field name made lowercase.
    dma_valormaximo = models.FloatField(db_column='DMA_VALORMAXIMO', blank=True, null=True)  # Field name made lowercase.
    dma_volumen = models.FloatField(db_column='DMA_VOLUMEN', blank=True, null=True)  # Field name made lowercase.
    dma_validado = models.SmallIntegerField(db_column='DMA_VALIDADO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_MANUALES_AFOROS'
        unique_together = (('dma_idsenal', 'dma_fecha'),)


class DatosManualesEmbalses(models.Model):
    pk = models.CompositePrimaryKey('DME_IDSENAL', 'DME_FECHA')
    dme_idsenal = models.ForeignKey('ListaSenales', models.DO_NOTHING, db_column='DME_IDSENAL')  # Field name made lowercase.
    dme_fecha = models.DateTimeField(db_column='DME_FECHA')  # Field name made lowercase.
    dme_valor = models.FloatField(db_column='DME_VALOR')  # Field name made lowercase.
    dme_volumen = models.FloatField(db_column='DME_VOLUMEN', blank=True, null=True)  # Field name made lowercase.
    dme_validado = models.SmallIntegerField(db_column='DME_VALIDADO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_MANUALES_EMBALSES'
        unique_together = (('dme_idsenal', 'dme_fecha'),)


class DatosManualesEmbalsesPrueba(models.Model):
    pk = models.CompositePrimaryKey('DME_IDSENAL', 'DME_FECHA')
    dme_idsenal = models.ForeignKey('ListaSenales', models.DO_NOTHING, db_column='DME_IDSENAL')  # Field name made lowercase.
    dme_fecha = models.DateTimeField(db_column='DME_FECHA')  # Field name made lowercase.
    dme_valor = models.FloatField(db_column='DME_VALOR')  # Field name made lowercase.
    dme_volumen = models.FloatField(db_column='DME_VOLUMEN', blank=True, null=True)  # Field name made lowercase.
    dme_validado = models.SmallIntegerField(db_column='DME_VALIDADO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_MANUALES_EMBALSES_PRUEBA'
        unique_together = (('dme_idsenal', 'dme_fecha'),)


class DatosManualesPluvio(models.Model):
    pk = models.CompositePrimaryKey('DMP_IDSENAL', 'DMP_FECHA')
    dmp_idsenal = models.ForeignKey('ListaSenales', models.DO_NOTHING, db_column='DMP_IDSENAL')  # Field name made lowercase.
    dmp_fecha = models.DateTimeField(db_column='DMP_FECHA')  # Field name made lowercase.
    dmp_valor = models.FloatField(db_column='DMP_VALOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_MANUALES_PLUVIO'
        unique_together = (('dmp_idsenal', 'dmp_fecha'),)


class DatosTemporal(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TEMPORAL'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0108(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0108'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0109(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0109'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0110(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0110'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0111(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0111'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0112(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0112'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0113(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0113'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0114(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0114'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0115(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0115'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0116(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0116'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0117(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0117'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0118(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0118'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0119(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0119'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0120(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0120'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0121(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0121'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0122(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0122'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0123(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0123'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0124(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0124'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0125(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0125'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0207(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0207'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0208(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0208'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0209(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0209'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0210(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0210'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0211(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0211'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0212(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0212'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0213(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0213'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0214(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0214'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0215(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0215'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0216(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0216'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0217(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0217'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0218(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0218'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0219(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0219'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0220(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0220'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0221(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0221'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0222(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0222'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0223(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0223'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0224(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0224'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0225(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0225'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0307(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0307'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0308(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0308'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0309(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0309'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0310(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0310'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0311(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0311'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0312(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0312'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0313(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0313'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0314(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0314'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0315(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0315'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0316(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0316'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0317(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0317'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0318(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0318'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0319(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0319'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0320(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0320'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0321(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0321'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0322(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0322'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0323(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0323'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0324(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0324'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0325(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0325'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0407(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0407'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0408(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0408'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0409(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0409'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0410(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0410'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0411(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0411'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0412(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0412'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0413(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0413'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0414(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0414'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0415(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0415'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0416(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0416'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0417(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0417'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0417Prueba(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0417_prueba'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0418(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0418'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0419(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0419'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0420(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0420'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0421(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0421'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0422(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0422'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0423(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0423'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0424(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0424'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0507(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0507'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0508(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0508'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0509(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0509'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0510(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0510'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0511(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0511'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0512(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0512'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0513(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0513'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0514(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0514'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0515(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0515'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0516(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0516'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0517(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0517'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0518(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0518'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0519(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0519'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0520(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0520'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0521(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0521'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0522(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0522'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0523(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0523'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0524(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0524'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0607(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0607'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0608(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0608'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0609(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0609'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0610(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0610'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0611(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0611'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0612(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0612'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0613(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0613'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0614(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0614'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0615(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0615'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0616(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0616'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0617(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0617'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0618(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0618'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0619(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0619'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0620(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0620'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0621(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0621'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0622(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0622'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0623(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0623'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0624(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0624'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0707(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0707'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0708(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0708'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0709(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0709'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0710(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0710'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0711(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0711'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0712(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0712'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0713(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0713'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0714(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0714'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0715(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0715'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0716(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0716'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0716Prueba(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0716_prueba'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0717(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0717'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0718(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0718'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0719(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0719'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0720(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0720'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0721(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0721'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0722(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0722'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0723(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0723'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0724(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0724'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0807(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0807'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0808(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0808'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0809(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0809'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0810(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0810'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0811(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0811'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0812(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0812'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0813(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0813'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0814(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0814'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0815(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0815'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0816(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0816'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0817(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0817'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0818(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0818'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0819(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0819'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0820(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0820'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0821(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0821'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0822(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0822'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0823(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0823'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0824(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0824'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0906(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0906'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0907(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0907'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0908(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0908'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0909(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0909'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0910(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0910'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0911(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0911'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0912(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0912'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0913(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0913'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0914(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0914'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0915(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0915'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0916(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0916'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0916Prueba(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0916_PRUEBA'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0917(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0917'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0918(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0918'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0919(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0919'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0920(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0920'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0921(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0921'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0922(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0922'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0923(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0923'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal0924(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_0924'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1006(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1006'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1007(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1007'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1008(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1008'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1009(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1009'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1010(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1010'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1011(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1011'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1012(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1012'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1013(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1013'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1014(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1014'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1015(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1015'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1016(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1016'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1017(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1017'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1018(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1018'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1019(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1019'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1020(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1020'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1021(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1021'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1022(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1022'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1023(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1023'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1024(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1024'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1106(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1106'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1107(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1107'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1108(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1108'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1109(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1109'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1110(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1110'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1111(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1111'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1112(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1112'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1113(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1113'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1114(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1114'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1115(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1115'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1116(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1116'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1117(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1117'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1118(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1118'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1119(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1119'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1120(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1120'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1121(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1121'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1122(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1122'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1123(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1123'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1124(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1124'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1207(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1207'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1208(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1208'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1209(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1209'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1210(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1210'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1211(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1211'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1212(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1212'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1213(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1213'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1214(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1214'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1215(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1215'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1216(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1216'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1217(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1217'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1218(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1218'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1219(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1219'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1220(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1220'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1221(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1221'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1222(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1222'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1223(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1223'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosTreal1224(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL_1224'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0101(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0101'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0102(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0102'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0103(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0103'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0104(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0104'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0105(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0105'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0106(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0106'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0108(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0108'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0109(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0109'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0110(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0110'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0111(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0111'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0112(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0112'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0113(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0113'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0114(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0114'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0115(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0115'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0116(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0116'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0117(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0117'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0118(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0118'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0119(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0119'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0120(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0120'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0121(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0121'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0122(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0122'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0123(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0123'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0124(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0124'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0125(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0125'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0201(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0201'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0202(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0202'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0203(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0203'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0204(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0204'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0205(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0205'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0206(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0206'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0207(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0207'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0208(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0208'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0209(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0209'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0210(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0210'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0211(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0211'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0212(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0212'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0213(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0213'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0214(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0214'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0215(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0215'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0216(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0216'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0217(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0217'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0218(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0218'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0219(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0219'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0220(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0220'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0221(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0221'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0222(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0222'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0223(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0223'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0224(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0224'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0225(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0225'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0301(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0301'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0302(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0302'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0303(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0303'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0304(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0304'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0305(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0305'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0306(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0306'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0307(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0307'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0308(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0308'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0309(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0309'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0310(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0310'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0311(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0311'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0312(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0312'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0313(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0313'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0314(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0314'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0315(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0315'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0316(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0316'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0317(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0317'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0318(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0318'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0319(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0319'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0320(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0320'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0321(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0321'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0322(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0322'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0323(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0323'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0324(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0324'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0325(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0325'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0401(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0401'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0402(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0402'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0403(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0403'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0404(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0404'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0405(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0405'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0406(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0406'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0407(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0407'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0408(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0408'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0409(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0409'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0410(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0410'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0411(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0411'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0412(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0412'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0413(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0413'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0414(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0414'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0415(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0415'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0416(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0416'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0417(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0417'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0417Prueba(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0417_PRUEBA'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0418(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0418'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0419(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0419'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0420(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0420'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0421(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0421'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0422(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0422'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0423(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0423'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0424(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0424'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0501(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0501'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0502(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0502'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0503(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0503'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0504(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0504'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0505(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0505'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0506(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0506'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0507(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0507'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0508(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0508'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0509(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0509'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0510(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0510'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0511(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0511'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0512(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0512'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0513(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0513'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0514(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0514'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0515(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0515'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0516(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0516'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0517(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0517'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0518(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0518'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0519(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0519'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0520(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0520'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0521(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0521'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0522(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0522'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0523(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0523'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0524(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0524'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0601(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0601'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0602(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0602'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0603(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0603'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0604(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0604'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0605(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0605'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0606(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0606'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0607(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0607'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0608(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0608'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0609(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0609'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0610(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0610'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0611(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0611'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0612(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0612'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0613(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0613'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0614(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0614'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0615(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0615'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0616(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0616'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0617(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0617'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0618(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0618'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0619(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0619'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0620(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0620'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0621(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0621'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0622(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0622'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0623(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0623'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0624(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0624'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0701(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0701'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0702(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0702'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0703(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0703'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0704(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0704'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0705(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0705'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0707(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0707'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0708(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0708'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0709(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0709'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0710(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0710'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0711(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0711'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0712(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0712'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0713(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0713'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0714(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0714'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0715(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0715'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0716(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0716'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0717(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0717'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0718(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0718'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0719(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0719'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0720(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0720'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0721(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0721'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0722(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0722'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0723(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0723'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0724(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0724'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0801(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0801'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0802(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0802'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0803(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0803'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0804(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0804'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0805(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0805'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0807(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0807'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0808(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0808'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0809(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0809'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0810(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0810'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0811(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0811'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0812(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0812'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0813(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0813'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0814(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0814'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0815(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0815'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0816(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0816'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0817(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0817'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0818(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0818'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0819(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0819'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0820(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0820'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0821(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0821'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0822(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0822'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0823(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0823'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0824(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0824'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0901(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0901'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0902(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0902'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0903(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0903'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0904(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0904'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0905(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0905'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0906(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0906'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0907(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0907'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0908(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0908'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0909(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0909'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0910(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0910'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0911(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0911'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0912(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0912'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0913(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0913'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0914(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0914'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0915(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0915'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0916(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0916'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0917(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0917'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0918(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0918'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0919(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0919'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0920(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0920'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0921(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0921'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0922(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0922'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0923(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0923'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid0924(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_0924'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1001(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1001'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1002(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1002'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1003(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1003'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1004(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1004'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1005(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1005'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1006(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1006'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1007(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1007'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1008(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1008'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1009(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1009'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1010(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1010'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1011(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1011'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1012(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1012'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1013(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1013'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1014(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1014'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1015(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1015'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1016(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1016'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1017(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1017'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1018(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1018'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1019(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1019'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1020(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1020'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1021(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1021'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1022(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1022'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1023(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1023'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1024(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1024'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1101(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1101'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1102(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1102'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1103(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1103'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1104(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1104'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1105(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1105'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1106(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1106'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1107(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1107'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1108(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1108'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1109(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1109'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1110(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1110'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1111(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1111'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1112(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1112'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1113(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1113'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1114(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1114'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1115(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1115'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1116(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1116'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1117(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1117'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1118(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1118'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1119(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1119'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1120(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1120'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1121(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1121'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1122(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1122'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1123(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1123'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1124(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1124'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1201(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1201'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1202(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1202'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1203(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1203'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1204(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1204'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1205(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1205'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1206(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1206'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1207(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1207'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1208(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1208'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1209(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1209'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1210(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1210'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1211(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1211'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1212(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1212'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1213(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1213'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1214(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1214'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1215(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.SmallIntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1215'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1216(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1216'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1217(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1217'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1218(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1218'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1219(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1219'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1220(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1220'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1221(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1221'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1222(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1222'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1223(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1223'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class DatosValid1224(models.Model):
    pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
    cc_idsenal = models.IntegerField(db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID_1224'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class Dual(models.Model):
    noborrar = models.CharField(db_column='NOBORRAR', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DUAL'


class EquiposMantenimiento(models.Model):
    em_codigo = models.IntegerField(db_column='EM_CODIGO', primary_key=True)  # Field name made lowercase.
    em_descripcion = models.CharField(db_column='EM_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EQUIPOS_MANTENIMIENTO'


class EstadosAlarmas(models.Model):
    pk = models.CompositePrimaryKey('EA_ALARMA', 'EA_ESTADO')
    ea_alarma = models.ForeignKey('ModalidadesAlarmas', models.DO_NOTHING, db_column='EA_ALARMA')  # Field name made lowercase.
    ea_estado = models.SmallIntegerField(db_column='EA_ESTADO')  # Field name made lowercase.
    ea_txt_estado = models.CharField(db_column='EA_TXT_ESTADO', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTADOS_ALARMAS'
        unique_together = (('ea_alarma', 'ea_estado'),)


class EstadosValidacion(models.Model):
    va_estado = models.IntegerField(db_column='VA_ESTADO', primary_key=True)  # Field name made lowercase.
    va_descripcion = models.CharField(db_column='VA_DESCRIPCION', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTADOS_VALIDACION'


class EstadoMensajesMail(models.Model):
    pk = models.CompositePrimaryKey('EM_SISTEMA', 'EM_ID_MAIL')
    em_sistema = models.CharField(db_column='EM_SISTEMA', max_length=20)  # Field name made lowercase.
    em_id_mail = models.IntegerField(db_column='EM_ID_MAIL')  # Field name made lowercase.
    em_direccion = models.CharField(db_column='EM_DIRECCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    em_mensaje = models.CharField(db_column='EM_MENSAJE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    em_asunto = models.CharField(db_column='EM_ASUNTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    em_estado = models.CharField(db_column='EM_ESTADO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    em_fecha = models.DateTimeField(db_column='EM_FECHA', blank=True, null=True)  # Field name made lowercase.
    em_formato = models.CharField(db_column='EM_FORMATO', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTADO_MENSAJES_MAIL'
        unique_together = (('em_sistema', 'em_id_mail'),)


class EstadoMensajesMailPrueba(models.Model):
    pk = models.CompositePrimaryKey('EM_SISTEMA', 'EM_ID_MAIL')
    em_sistema = models.CharField(db_column='EM_SISTEMA', max_length=20)  # Field name made lowercase.
    em_id_mail = models.IntegerField(db_column='EM_ID_MAIL')  # Field name made lowercase.
    em_direccion = models.CharField(db_column='EM_DIRECCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    em_mensaje = models.CharField(db_column='EM_MENSAJE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    em_asunto = models.CharField(db_column='EM_ASUNTO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    em_estado = models.CharField(db_column='EM_ESTADO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    em_fecha = models.DateTimeField(db_column='EM_FECHA', blank=True, null=True)  # Field name made lowercase.
    em_formato = models.CharField(db_column='EM_FORMATO', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTADO_MENSAJES_MAIL_prueba'
        unique_together = (('em_sistema', 'em_id_mail'),)


class EstadoMensajesSms(models.Model):
    pk = models.CompositePrimaryKey('EM_SISTEMA', 'EM_ID_SMS')
    em_sistema = models.CharField(db_column='EM_SISTEMA', max_length=20)  # Field name made lowercase.
    em_id_sms = models.IntegerField(db_column='EM_ID_SMS')  # Field name made lowercase.
    em_telefono = models.CharField(db_column='EM_TELEFONO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    em_mensaje = models.CharField(db_column='EM_MENSAJE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    em_acuse = models.BooleanField(db_column='EM_ACUSE', blank=True, null=True)  # Field name made lowercase.
    em_id_gprs = models.CharField(db_column='EM_ID_GPRS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    em_estado = models.CharField(db_column='EM_ESTADO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    em_fecha = models.DateTimeField(db_column='EM_FECHA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTADO_MENSAJES_SMS'
        unique_together = (('em_sistema', 'em_id_sms'),)


class FactoresConversionUnidades(models.Model):
    pk = models.CompositePrimaryKey('FC_UNIDAD', 'FC_UNIDAD_REL')
    fc_unidad = models.CharField(db_column='FC_UNIDAD', max_length=50)  # Field name made lowercase.
    fc_descripcion = models.CharField(db_column='FC_DESCRIPCION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fc_unidad_rel = models.CharField(db_column='FC_UNIDAD_REL', max_length=50)  # Field name made lowercase.
    fc_factor = models.DecimalField(db_column='FC_FACTOR', max_digits=16, decimal_places=8)  # Field name made lowercase.
    fc_tipo = models.CharField(db_column='FC_TIPO', max_length=20)  # Field name made lowercase.
    fc_basico = models.CharField(db_column='FC_BASICO', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FACTORES_CONVERSION_UNIDADES'
        unique_together = (('fc_unidad', 'fc_unidad_rel'),)


class GestionAlarmas(models.Model):
    pk = models.CompositePrimaryKey('GA_SENAL', 'GA_CONT_IP21')
    ga_senal = models.ForeignKey('ListaSenales', models.DO_NOTHING, db_column='GA_SENAL')  # Field name made lowercase.
    ga_cont_ip21 = models.IntegerField(db_column='GA_CONT_IP21')  # Field name made lowercase.
    ga_alarma = models.SmallIntegerField(db_column='GA_ALARMA', blank=True, null=True)  # Field name made lowercase.
    ga_estado = models.SmallIntegerField(db_column='GA_ESTADO', blank=True, null=True)  # Field name made lowercase.
    ga_codigo_acuse = models.ForeignKey(ConceptosAcuse, models.DO_NOTHING, db_column='GA_CODIGO_ACUSE', blank=True, null=True)  # Field name made lowercase.
    ga_fecha_acuse = models.DateTimeField(db_column='GA_FECHA_ACUSE', blank=True, null=True)  # Field name made lowercase.
    ga_observaciones = models.CharField(db_column='GA_OBSERVACIONES', max_length=400, blank=True, null=True)  # Field name made lowercase.
    ga_usuario = models.CharField(db_column='GA_USUARIO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ga_fecha_recon = models.DateTimeField(db_column='GA_FECHA_RECON', blank=True, null=True)  # Field name made lowercase.
    ga_usuario_recon = models.CharField(db_column='GA_USUARIO_RECON', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ga_acuse_global = models.BooleanField(db_column='GA_ACUSE_GLOBAL', blank=True, null=True)  # Field name made lowercase.
    ga_modificado = models.BooleanField(db_column='GA_MODIFICADO', blank=True, null=True)  # Field name made lowercase.
    ga_valor_recon = models.DecimalField(db_column='GA_VALOR_RECON', max_digits=20, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    ga_prevision = models.CharField(db_column='GA_PREVISION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ga_alarma_confirmada = models.BooleanField(db_column='GA_ALARMA_CONFIRMADA', blank=True, null=True)  # Field name made lowercase.
    ga_aviso = models.SmallIntegerField(db_column='GA_AVISO', blank=True, null=True)  # Field name made lowercase.
    ga_tmp_pn = models.DateTimeField(db_column='GA_TMP_PN', blank=True, null=True)  # Field name made lowercase.
    ga_sms_pn = models.IntegerField(db_column='GA_SMS_PN', blank=True, null=True)  # Field name made lowercase.
    ga_orden_aviso_pn = models.SmallIntegerField(db_column='GA_ORDEN_AVISO_PN', blank=True, null=True)  # Field name made lowercase.
    ga_puesto_pn = models.CharField(db_column='GA_PUESTO_PN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ga_persona_pn = models.CharField(db_column='GA_PERSONA_PN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ga_actuaciones_pn = models.CharField(db_column='GA_ACTUACIONES_PN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ga_usuario_contacto_pn = models.CharField(db_column='GA_USUARIO_CONTACTO_PN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ga_fecha_contacto_pn = models.DateTimeField(db_column='GA_FECHA_CONTACTO_PN', blank=True, null=True)  # Field name made lowercase.
    ga_tmp_pp = models.DateTimeField(db_column='GA_TMP_PP', blank=True, null=True)  # Field name made lowercase.
    ga_sms_pp = models.IntegerField(db_column='GA_SMS_PP', blank=True, null=True)  # Field name made lowercase.
    ga_orden_aviso_pp = models.SmallIntegerField(db_column='GA_ORDEN_AVISO_PP', blank=True, null=True)  # Field name made lowercase.
    ga_puesto_pp = models.CharField(db_column='GA_PUESTO_PP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ga_persona_pp = models.CharField(db_column='GA_PERSONA_PP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ga_actuaciones_pp = models.CharField(db_column='GA_ACTUACIONES_PP', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ga_usuario_contacto_pp = models.CharField(db_column='GA_USUARIO_CONTACTO_PP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ga_fecha_contacto_pp = models.DateTimeField(db_column='GA_FECHA_CONTACTO_PP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GESTION_ALARMAS'
        unique_together = (('ga_senal', 'ga_cont_ip21'),)


class GraficasFavoritas(models.Model):
    id_grafica = models.IntegerField(db_column='ID_GRAFICA')  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    origen = models.CharField(db_column='ORIGEN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    titulo_general = models.CharField(db_column='TITULO_GENERAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    titulo_eje_izq = models.CharField(db_column='TITULO_EJE_IZQ', max_length=100, blank=True, null=True)  # Field name made lowercase.
    titulo_eje_der = models.CharField(db_column='TITULO_EJE_DER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    escala_eje_izq = models.CharField(db_column='ESCALA_EJE_IZQ', max_length=100, blank=True, null=True)  # Field name made lowercase.
    escala_eje_der = models.CharField(db_column='ESCALA_EJE_DER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    maximo_escala_manual_eje_izq = models.DecimalField(db_column='MAXIMO_ESCALA_MANUAL_EJE_IZQ', max_digits=9, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    minimo_escala_manual_eje_izq = models.DecimalField(db_column='MINIMO_ESCALA_MANUAL_EJE_IZQ', max_digits=9, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    maximo_escala_manual_eje_der = models.DecimalField(db_column='MAXIMO_ESCALA_MANUAL_EJE_DER', max_digits=9, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    minimo_escala_manual_eje_der = models.DecimalField(db_column='MINIMO_ESCALA_MANUAL_EJE_DER', max_digits=9, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    ventana = models.CharField(db_column='VENTANA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rejilla_x = models.IntegerField(db_column='REJILLA_X', blank=True, null=True)  # Field name made lowercase.
    rejilla_y = models.IntegerField(db_column='REJILLA_Y', blank=True, null=True)  # Field name made lowercase.
    imagen_fondo = models.CharField(db_column='IMAGEN_FONDO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    frecuencia = models.CharField(db_column='FRECUENCIA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GRAFICAS_FAVORITAS'


class GraficasFavoritasSenales(models.Model):
    id_grafica = models.IntegerField(db_column='ID_GRAFICA')  # Field name made lowercase.
    seleccionada = models.CharField(db_column='SELECCIONADA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='TAG', max_length=100, blank=True, null=True)  # Field name made lowercase.
    eje = models.CharField(db_column='EJE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='COLOR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tipo_linea = models.CharField(db_column='TIPO_LINEA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tipo_consolidado = models.CharField(db_column='TIPO_CONSOLIDADO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    consolidado = models.CharField(db_column='CONSOLIDADO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    linea_referencia = models.CharField(db_column='LINEA_REFERENCIA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    valor_manual_referencia = models.DecimalField(db_column='VALOR_MANUAL_REFERENCIA', max_digits=9, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    tipo_marca = models.CharField(db_column='TIPO_MARCA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    orden = models.IntegerField(db_column='ORDEN', blank=True, null=True)  # Field name made lowercase.
    naturaleza = models.IntegerField(db_column='NATURALEZA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GRAFICAS_FAVORITAS_SENALES'


class HistoriaAlarmas(models.Model):
    pk = models.CompositePrimaryKey('HA_SENAL', 'HA_CONT_IP21')
    ha_senal = models.ForeignKey('ListaSenales', models.DO_NOTHING, db_column='HA_SENAL')  # Field name made lowercase.
    ha_cont_ip21 = models.IntegerField(db_column='HA_CONT_IP21')  # Field name made lowercase.
    ha_log_time = models.DateTimeField(db_column='HA_LOG_TIME', blank=True, null=True)  # Field name made lowercase.
    ha_alarma = models.CharField(db_column='HA_ALARMA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ha_estado_aparicion = models.CharField(db_column='HA_ESTADO_APARICION', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ha_f_aparicion = models.DateTimeField(db_column='HA_F_APARICION', blank=True, null=True)  # Field name made lowercase.
    ha_valor_ap = models.DecimalField(db_column='HA_VALOR_AP', max_digits=20, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    ha_gravedad = models.CharField(db_column='HA_GRAVEDAD', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ha_f_reconocimiento = models.DateTimeField(db_column='HA_F_RECONOCIMIENTO', blank=True, null=True)  # Field name made lowercase.
    ha_usuario = models.CharField(db_column='HA_USUARIO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ha_valor_rec = models.DecimalField(db_column='HA_VALOR_REC', max_digits=20, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    ha_f_desaparicion = models.DateTimeField(db_column='HA_F_DESAPARICION', blank=True, null=True)  # Field name made lowercase.
    ha_valor_de = models.DecimalField(db_column='HA_VALOR_DE', max_digits=20, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HISTORIA_ALARMAS'
        unique_together = (('ha_senal', 'ha_cont_ip21'),)


class HistoriaEpisodiosCab(models.Model):
    hec_codigo = models.IntegerField(db_column='HEC_CODIGO', primary_key=True)  # Field name made lowercase.
    hec_nombre = models.CharField(db_column='HEC_NOMBRE', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    hec_descripcion = models.CharField(db_column='HEC_DESCRIPCION', max_length=256, blank=True, null=True)  # Field name made lowercase.
    hec_fecha_ini_epi = models.DateTimeField(db_column='HEC_FECHA_INI_EPI', blank=True, null=True)  # Field name made lowercase.
    hec_fecha_fin_epi = models.DateTimeField(db_column='HEC_FECHA_FIN_EPI', blank=True, null=True)  # Field name made lowercase.
    hec_rio = models.CharField(db_column='HEC_RIO', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HISTORIA_EPISODIOS_CAB'


class HistoriaEpisodiosLin(models.Model):
    pk = models.CompositePrimaryKey('HEL_CODIGO', 'HEL_IDSENAL', 'HEL_FECHA')
    hel_codigo = models.ForeignKey(HistoriaEpisodiosCab, models.DO_NOTHING, db_column='HEL_CODIGO')  # Field name made lowercase.
    hel_idsenal = models.ForeignKey('ListaSenales', models.DO_NOTHING, db_column='HEL_IDSENAL')  # Field name made lowercase.
    hel_fecha = models.DateTimeField(db_column='HEL_FECHA')  # Field name made lowercase.
    hel_valor = models.DecimalField(db_column='HEL_VALOR', max_digits=14, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    hel_calidad = models.CharField(db_column='HEL_CALIDAD', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HISTORIA_EPISODIOS_LIN'
        unique_together = (('hel_codigo', 'hel_idsenal', 'hel_fecha'),)


class InformesAutomaticos(models.Model):
    ia_idinforme = models.CharField(db_column='IA_IdInforme', primary_key=True, max_length=5)  # Field name made lowercase.
    ia_descipcion = models.CharField(db_column='IA_Descipcion', max_length=128, blank=True, null=True)  # Field name made lowercase.
    ia_absolutepathrpt = models.CharField(db_column='IA_AbsolutePathRPT', max_length=128)  # Field name made lowercase.
    ia_fechainicio = models.DateTimeField(db_column='IA_FechaInicio', blank=True, null=True)  # Field name made lowercase.
    ia_fechafin = models.DateTimeField(db_column='IA_FechaFin', blank=True, null=True)  # Field name made lowercase.
    ia_periodicidad = models.SmallIntegerField(db_column='IA_Periodicidad')  # Field name made lowercase.
    ia_unidaddetiempo = models.SmallIntegerField(db_column='IA_UnidadDeTiempo', blank=True, null=True)  # Field name made lowercase.
    ia_exportapdf = models.BooleanField(db_column='IA_ExportaPDF', blank=True, null=True)  # Field name made lowercase.
    ia_exportaexcel = models.BooleanField(db_column='IA_ExportaExcel', blank=True, null=True)  # Field name made lowercase.
    ia_parametro01 = models.CharField(db_column='IA_Parametro01', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ia_parametro02 = models.CharField(db_column='IA_Parametro02', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ia_parametro03 = models.CharField(db_column='IA_Parametro03', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ia_parametro04 = models.CharField(db_column='IA_Parametro04', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ia_parametro05 = models.CharField(db_column='IA_Parametro05', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ia_parametro06 = models.CharField(db_column='IA_Parametro06', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ia_parametro07 = models.CharField(db_column='IA_Parametro07', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ia_parametro08 = models.CharField(db_column='IA_Parametro08', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ia_absolutepathpdf = models.CharField(db_column='IA_AbsolutePathPDF', max_length=128, blank=True, null=True)  # Field name made lowercase.
    ia_odbcip21 = models.BooleanField(db_column='IA_ODBCIP21', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INFORMES_AUTOMATICOS'


class InformesCedex(models.Model):
    ic_codigo = models.IntegerField(db_column='IC_CODIGO', primary_key=True)  # Field name made lowercase.
    ic_estacion = models.IntegerField(db_column='IC_ESTACION', blank=True, null=True)  # Field name made lowercase.
    ic_cod_roea = models.CharField(db_column='IC_COD_ROEA', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ic_tipo = models.CharField(db_column='IC_TIPO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ic_nivel = models.IntegerField(db_column='IC_NIVEL', blank=True, null=True)  # Field name made lowercase.
    ic_caudal = models.IntegerField(db_column='IC_CAUDAL', blank=True, null=True)  # Field name made lowercase.
    ic_volumen = models.IntegerField(db_column='IC_VOLUMEN', blank=True, null=True)  # Field name made lowercase.
    ic_aport = models.IntegerField(db_column='IC_APORT', blank=True, null=True)  # Field name made lowercase.
    ic_caudal_sal = models.IntegerField(db_column='IC_CAUDAL_SAL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INFORMES_CEDEX'


class InformesExcelAutomaticos(models.Model):
    iea_codigo = models.CharField(db_column='IEA_CODIGO', primary_key=True, max_length=15)  # Field name made lowercase.
    iea_descripcion = models.CharField(db_column='IEA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iea_libro = models.CharField(db_column='IEA_LIBRO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    iea_hojainforme = models.CharField(db_column='IEA_HOJAINFORME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    iea_activado = models.BooleanField(db_column='IEA_ACTIVADO', blank=True, null=True)  # Field name made lowercase.
    iea_fechaejecucion = models.DateTimeField(db_column='IEA_FECHAEJECUCION', blank=True, null=True)  # Field name made lowercase.
    iea_numperiodos = models.SmallIntegerField(db_column='IEA_NUMPERIODOS', blank=True, null=True)  # Field name made lowercase.
    iea_tipoperiodo = models.SmallIntegerField(db_column='IEA_TIPOPERIODO', blank=True, null=True)  # Field name made lowercase.
    iea_directoriopdf = models.CharField(db_column='IEA_DIRECTORIOPDF', max_length=200, blank=True, null=True)  # Field name made lowercase.
    iea_nombrefilegen = models.CharField(db_column='IEA_NOMBREFILEGEN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iea_tipofilegen = models.SmallIntegerField(db_column='IEA_TIPOFILEGEN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INFORMES_EXCEL_AUTOMATICOS'


class InformesExcelAutomaticosDatos(models.Model):
    pk = models.CompositePrimaryKey('IEAD_CODIGO', 'IEAD_NUMHOJA')
    iead_codigo = models.CharField(db_column='IEAD_CODIGO', max_length=15)  # Field name made lowercase.
    iead_numhoja = models.SmallIntegerField(db_column='IEAD_NUMHOJA')  # Field name made lowercase.
    iead_hojadatos = models.CharField(db_column='IEAD_HOJADATOS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    iead_origendatos = models.SmallIntegerField(db_column='IEAD_ORIGENDATOS', blank=True, null=True)  # Field name made lowercase.
    iead_tags = models.CharField(db_column='IEAD_TAGS', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    iead_numintervalos = models.SmallIntegerField(db_column='IEAD_NUMINTERVALOS', blank=True, null=True)  # Field name made lowercase.
    iead_tipointervalo = models.SmallIntegerField(db_column='IEAD_TIPOINTERVALO', blank=True, null=True)  # Field name made lowercase.
    iead_horainicio = models.CharField(db_column='IEAD_HORAINICIO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    iead_horafin = models.CharField(db_column='IEAD_HORAFIN', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INFORMES_EXCEL_AUTOMATICOS_DATOS'
        unique_together = (('iead_codigo', 'iead_numhoja'),)


class InformesGrafVolEmb(models.Model):
    pk = models.CompositePrimaryKey('IGVE_ESTACION', 'IGVE_TAG_VOLUMEN')
    igve_estacion = models.IntegerField(db_column='IGVE_ESTACION')  # Field name made lowercase.
    igve_tag_volumen = models.IntegerField(db_column='IGVE_TAG_VOLUMEN')  # Field name made lowercase.
    igve_manual_auto = models.CharField(db_column='IGVE_MANUAL_AUTO', max_length=1)  # Field name made lowercase.
    igve_confederacion = models.CharField(db_column='IGVE_CONFEDERACION', max_length=50)  # Field name made lowercase.
    igve_por_defecto = models.CharField(db_column='IGVE_POR_DEFECTO', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INFORMES_GRAF_VOL_EMB'
        unique_together = (('igve_estacion', 'igve_tag_volumen'),)


class LinFichero(models.Model):
    pk = models.CompositePrimaryKey('LF_TAG', 'LF_VERSION', 'LF_LINEA')
    lf_tag = models.ForeignKey(CabFichero, models.DO_NOTHING, db_column='LF_TAG', to_field='CF_VERSION')  # Field name made lowercase.
    lf_version = models.ForeignKey(CabFichero, models.DO_NOTHING, db_column='LF_VERSION', to_field='CF_VERSION', related_name='linfichero_lf_version_set')  # Field name made lowercase.
    lf_linea = models.SmallIntegerField(db_column='LF_LINEA')  # Field name made lowercase.
    lf_x = models.DecimalField(db_column='LF_X', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lf_y = models.DecimalField(db_column='LF_Y', max_digits=12, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LIN_FICHERO'
        unique_together = (('lf_tag', 'lf_version', 'lf_linea'),)


class ListaAlarmas(models.Model):
    pk = models.CompositePrimaryKey('LA_SENAL', 'LA_ALARMA', 'LA_ESTADO')
    la_senal = models.ForeignKey('ListaSenales', models.DO_NOTHING, db_column='LA_SENAL')  # Field name made lowercase.
    la_alarma = models.ForeignKey(EstadosAlarmas, models.DO_NOTHING, db_column='LA_ALARMA', to_field='EA_ESTADO')  # Field name made lowercase.
    la_estado = models.ForeignKey(EstadosAlarmas, models.DO_NOTHING, db_column='LA_ESTADO', to_field='EA_ESTADO', related_name='listaalarmas_la_estado_set')  # Field name made lowercase.
    la_cod_normal = models.ForeignKey('PlanesActuacion', models.DO_NOTHING, db_column='LA_COD_NORMAL', blank=True, null=True)  # Field name made lowercase.
    la_cod_paralelo = models.ForeignKey('PlanesActuacion', models.DO_NOTHING, db_column='LA_COD_PARALELO', related_name='listaalarmas_la_cod_paralelo_set', blank=True, null=True)  # Field name made lowercase.
    la_cod_especial = models.ForeignKey('PlanesActuacion', models.DO_NOTHING, db_column='LA_COD_ESPECIAL', related_name='listaalarmas_la_cod_especial_set', blank=True, null=True)  # Field name made lowercase.
    la_fecha_ini = models.DateTimeField(db_column='LA_FECHA_INI', blank=True, null=True)  # Field name made lowercase.
    la_fecha_fin = models.DateTimeField(db_column='LA_FECHA_FIN', blank=True, null=True)  # Field name made lowercase.
    la_marca_anula = models.SmallIntegerField(db_column='LA_MARCA_ANULA', blank=True, null=True)  # Field name made lowercase.
    la_cod_automatico = models.ForeignKey('PlanesActuacionAutomaticos', models.DO_NOTHING, db_column='LA_COD_AUTOMATICO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_ALARMAS'
        unique_together = (('la_senal', 'la_alarma', 'la_estado'),)


class ListaCargos(models.Model):
    lc_codigo = models.CharField(db_column='LC_CODIGO', primary_key=True, max_length=2, db_comment='Codigo del cargo')  # Field name made lowercase.
    lc_descripcion = models.CharField(db_column='LC_DESCRIPCION', max_length=50, blank=True, null=True, db_comment='Descripcion del cargo')  # Field name made lowercase.
    lc_nivel = models.CharField(db_column='LC_NIVEL', max_length=10, blank=True, null=True, db_comment='Nivel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_CARGOS'


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
    le_codigo = models.IntegerField(db_column='LE_CODIGO', primary_key=True)  # Field name made lowercase.
    le_codigo_txt = models.CharField(db_column='LE_CODIGO_TXT', max_length=4)  # Field name made lowercase.
    le_tipo_estacion = models.CharField(db_column='LE_TIPO_ESTACION', max_length=2)  # Field name made lowercase.
    le_zona = models.ForeignKey('ListaZonas', models.DO_NOTHING, db_column='LE_ZONA')  # Field name made lowercase.
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
    le_datos_manuales = models.SmallIntegerField(db_column='LE_DATOS_MANUALES', blank=True, null=True)  # Field name made lowercase.
    le_fuera_servicio = models.SmallIntegerField(db_column='LE_FUERA_SERVICIO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_ESTACIONES'


class ListaEstacionesUpdate(models.Model):
    le_codigo = models.IntegerField(db_column='LE_CODIGO')  # Field name made lowercase.
    le_codigo_txt = models.CharField(db_column='LE_CODIGO_TXT', max_length=4)  # Field name made lowercase.
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

    class Meta:
        managed = False
        db_table = 'LISTA_ESTACIONES_UPDATE'


class ListaFax(models.Model):
    lf_codigo = models.IntegerField(db_column='LF_CODIGO', primary_key=True)  # Field name made lowercase.
    lf_descripcion = models.CharField(db_column='LF_DESCRIPCION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lf_fichero = models.CharField(db_column='LF_FICHERO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lf_param1 = models.CharField(db_column='LF_PARAM1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lf_param2 = models.CharField(db_column='LF_PARAM2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lf_param3 = models.CharField(db_column='LF_PARAM3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lf_param4 = models.CharField(db_column='LF_PARAM4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lf_param5 = models.CharField(db_column='LF_PARAM5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lf_param6 = models.CharField(db_column='LF_PARAM6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lf_param7 = models.CharField(db_column='LF_PARAM7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lf_param8 = models.CharField(db_column='LF_PARAM8', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_FAX'


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

    class Meta:
        managed = False
        db_table = 'LISTA_MAILS'


class ListaMensajes(models.Model):
    lm_codigo = models.IntegerField(db_column='LM_CODIGO', primary_key=True)  # Field name made lowercase.
    lm_descripcion = models.CharField(db_column='LM_DESCRIPCION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lm_texto = models.CharField(db_column='LM_TEXTO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lm_param1 = models.CharField(db_column='LM_PARAM1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lm_param2 = models.CharField(db_column='LM_PARAM2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lm_param3 = models.CharField(db_column='LM_PARAM3', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lm_param4 = models.CharField(db_column='LM_PARAM4', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lm_param5 = models.CharField(db_column='LM_PARAM5', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lm_param6 = models.CharField(db_column='LM_PARAM6', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lm_param7 = models.CharField(db_column='LM_PARAM7', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lm_param8 = models.CharField(db_column='LM_PARAM8', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_MENSAJES'


class ListaPersonas(models.Model):
    lp_codigo = models.IntegerField(db_column='LP_CODIGO', primary_key=True)  # Field name made lowercase.
    lp_nombre = models.CharField(db_column='LP_NOMBRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lp_nif = models.CharField(db_column='LP_NIF', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lp_direccion = models.CharField(db_column='LP_DIRECCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lp_cp = models.CharField(db_column='LP_CP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lp_poblacion = models.ForeignKey('Poblaciones', models.DO_NOTHING, db_column='LP_POBLACION', blank=True, null=True)  # Field name made lowercase.
    lp_provincia = models.SmallIntegerField(db_column='LP_PROVINCIA', blank=True, null=True)  # Field name made lowercase.
    lp_telefono1 = models.CharField(db_column='LP_TELEFONO1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lp_telefono2 = models.CharField(db_column='LP_TELEFONO2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lp_movil1 = models.CharField(db_column='LP_MOVIL1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lp_movil2 = models.CharField(db_column='LP_MOVIL2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lp_tipo_perso = models.CharField(db_column='LP_TIPO_PERSO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lp_cargo = models.ForeignKey(ListaCargos, models.DO_NOTHING, db_column='LP_CARGO', blank=True, null=True)  # Field name made lowercase.
    lp_num_corporativo = models.CharField(db_column='LP_NUM_CORPORATIVO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lp_correo = models.CharField(db_column='LP_CORREO', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_PERSONAS'


class ListaRemotas(models.Model):
    lr_codigo = models.IntegerField(db_column='LR_CODIGO', primary_key=True)  # Field name made lowercase.
    lr_tipo_estacion = models.CharField(db_column='LR_TIPO_ESTACION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lr_nombre = models.CharField(db_column='LR_NOMBRE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lr_nombre_corto = models.CharField(db_column='LR_NOMBRE_CORTO', max_length=18, blank=True, null=True)  # Field name made lowercase.
    lr_estacion = models.ForeignKey(ListaEstaciones, models.DO_NOTHING, db_column='LR_ESTACION')  # Field name made lowercase.
    lr_zona = models.ForeignKey('ListaZonas', models.DO_NOTHING, db_column='LR_ZONA')  # Field name made lowercase.
    lr_remota_principal = models.SmallIntegerField(db_column='LR_REMOTA_PRINCIPAL', blank=True, null=True)  # Field name made lowercase.
    lr_tiene_pluv = models.SmallIntegerField(db_column='LR_TIENE_PLUV', blank=True, null=True)  # Field name made lowercase.
    lr_equipo_mant = models.IntegerField(db_column='LR_EQUIPO_MANT', blank=True, null=True)  # Field name made lowercase.
    lr_num_orden = models.IntegerField(db_column='LR_NUM_ORDEN', blank=True, null=True)  # Field name made lowercase.
    lr_empresa_suminis = models.IntegerField(db_column='LR_EMPRESA_SUMINIS', blank=True, null=True)  # Field name made lowercase.
    lr_num_poliza = models.CharField(db_column='LR_NUM_POLIZA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lr_persona_contacto = models.IntegerField(db_column='LR_PERSONA_CONTACTO', blank=True, null=True)  # Field name made lowercase.
    lr_observaciones = models.CharField(db_column='LR_OBSERVACIONES', max_length=400, blank=True, null=True)  # Field name made lowercase.
    lr_utm_huso = models.IntegerField(db_column='LR_UTM_HUSO', blank=True, null=True)  # Field name made lowercase.
    lr_utm_x = models.DecimalField(db_column='LR_UTM_X', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_utm_y = models.DecimalField(db_column='LR_UTM_Y', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_utm_z = models.DecimalField(db_column='LR_UTM_Z', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_codigo_txt = models.CharField(db_column='LR_CODIGO_TXT', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lr_rio = models.IntegerField(db_column='LR_RIO', blank=True, null=True)  # Field name made lowercase.
    lr_superficie = models.DecimalField(db_column='LR_SUPERFICIE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_vol_max = models.DecimalField(db_column='LR_VOL_MAX', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_men = models.DecimalField(db_column='LR_COTA_MEN', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_lecho = models.DecimalField(db_column='LR_COTA_LECHO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_aliviadero = models.DecimalField(db_column='LR_COTA_ALIVIADERO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_coronacion = models.DecimalField(db_column='LR_COTA_CORONACION', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_toma = models.DecimalField(db_column='LR_COTA_TOMA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_estacion = models.DecimalField(db_column='LR_COTA_ESTACION', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_cota_max = models.DecimalField(db_column='LR_COTA_MAX', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
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
    lr_period_nae = models.DecimalField(db_column='LR_PERIOD_NAE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_caudal_nae = models.DecimalField(db_column='LR_CAUDAL_NAE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_qmax_aliv = models.DecimalField(db_column='LR_QMAX_ALIV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_qmax_turb = models.DecimalField(db_column='LR_QMAX_TURB', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_qmax_tomas = models.DecimalField(db_column='LR_QMAX_TOMAS', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_qmax_fondo = models.DecimalField(db_column='LR_QMAX_FONDO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_qmax_totsal = models.DecimalField(db_column='LR_QMAX_TOTSAL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_caudal_ecologico = models.DecimalField(db_column='LR_CAUDAL_ECOLOGICO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_concesion = models.DecimalField(db_column='LR_CONCESION', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_escala_max = models.DecimalField(db_column='LR_ESCALA_MAX', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_capacidad_max = models.DecimalField(db_column='LR_CAPACIDAD_MAX', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_vol_util = models.DecimalField(db_column='LR_VOL_UTIL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_p24h_r2 = models.DecimalField(db_column='LR_P24H_R2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_p24h_r5 = models.DecimalField(db_column='LR_P24H_R5', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_p24h_r10 = models.DecimalField(db_column='LR_P24H_R10', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_p24h_r25 = models.DecimalField(db_column='LR_P24H_R25', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_p24h_r100 = models.DecimalField(db_column='LR_P24H_R100', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_p24h_r500 = models.DecimalField(db_column='LR_P24H_R500', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lr_tag_comunica = models.IntegerField(db_column='LR_TAG_COMUNICA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_REMOTAS'


class ListaRemotasApoyo(models.Model):
    lra_cod_remota = models.IntegerField(db_column='LRA_COD_REMOTA', blank=True, null=True)  # Field name made lowercase.
    lra_tipo_equipo = models.CharField(db_column='LRA_TIPO_EQUIPO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lra_cod_puesto = models.DecimalField(db_column='LRA_COD_PUESTO', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lra_cod_empresa = models.DecimalField(db_column='LRA_COD_EMPRESA', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    lra_observaciones = models.CharField(db_column='LRA_OBSERVACIONES', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_REMOTAS_APOYO'


class ListaRemotasFicheros(models.Model):
    pk = models.CompositePrimaryKey('LRF_COD_REMOTA', 'LRF_TIPO_FICHERO', 'LRF_COD_FICHERO')
    lrf_cod_remota = models.IntegerField(db_column='LRF_COD_REMOTA')  # Field name made lowercase.
    lrf_tipo_fichero = models.CharField(db_column='LRF_TIPO_FICHERO', max_length=7)  # Field name made lowercase.
    lrf_cod_fichero = models.DecimalField(db_column='LRF_COD_FICHERO', max_digits=18, decimal_places=0)  # Field name made lowercase.
    lrf_nombre_fichero = models.CharField(db_column='LRF_NOMBRE_FICHERO', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_REMOTAS_FICHEROS'
        unique_together = (('lrf_cod_remota', 'lrf_tipo_fichero', 'lrf_cod_fichero'),)


class ListaRemotasOtrosserv(models.Model):
    pk = models.CompositePrimaryKey('LRO_COD_REMOTA', 'LRO_COD_EQUIPO')
    lro_cod_remota = models.IntegerField(db_column='LRO_COD_REMOTA')  # Field name made lowercase.
    lro_cod_equipo = models.IntegerField(db_column='LRO_COD_EQUIPO')  # Field name made lowercase.
    lro_tipo_equipo = models.IntegerField(db_column='LRO_TIPO_EQUIPO', blank=True, null=True)  # Field name made lowercase.
    lro_desc_equipo = models.CharField(db_column='LRO_DESC_EQUIPO', max_length=400, blank=True, null=True)  # Field name made lowercase.
    lro_cod_empresa = models.IntegerField(db_column='LRO_COD_EMPRESA', blank=True, null=True)  # Field name made lowercase.
    lro_observaciones = models.CharField(db_column='LRO_OBSERVACIONES', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_REMOTAS_OTROSSERV'
        unique_together = (('lro_cod_remota', 'lro_cod_equipo'),)


class ListaSenales(models.Model):
    ls_tag = models.IntegerField(db_column='LS_TAG', primary_key=True)  # Field name made lowercase.
    ls_descripcion = models.CharField(db_column='LS_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ls_tag_txt = models.CharField(db_column='LS_TAG_TXT', max_length=16)  # Field name made lowercase.
    ls_remota = models.ForeignKey(ListaRemotas, models.DO_NOTHING, db_column='LS_REMOTA')  # Field name made lowercase.
    ls_estacion = models.ForeignKey(ListaEstaciones, models.DO_NOTHING, db_column='LS_ESTACION', blank=True, null=True)  # Field name made lowercase.
    ls_tipo_senal = models.CharField(db_column='LS_TIPO_SENAL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_tipo_alarma = models.ForeignKey('TiposAlarmas', models.DO_NOTHING, db_column='LS_TIPO_ALARMA', blank=True, null=True)  # Field name made lowercase.
    ls_marca_cons = models.SmallIntegerField(db_column='LS_MARCA_CONS', blank=True, null=True)  # Field name made lowercase.
    ls_tipo_almacenamiento = models.CharField(db_column='LS_TIPO_ALMACENAMIENTO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_tipo_consolidacion = models.ForeignKey('TiposConsolidacion', models.DO_NOTHING, db_column='LS_TIPO_CONSOLIDACION', blank=True, null=True)  # Field name made lowercase.
    ls_tag_cons_1 = models.SmallIntegerField(db_column='LS_TAG_CONS_1', blank=True, null=True)  # Field name made lowercase.
    ls_tag_cons_2 = models.SmallIntegerField(db_column='LS_TAG_CONS_2', blank=True, null=True)  # Field name made lowercase.
    ls_hora_cons = models.CharField(db_column='LS_HORA_CONS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_curvaref = models.SmallIntegerField(db_column='LS_CURVAREF', blank=True, null=True)  # Field name made lowercase.
    ls_naturaleza = models.ForeignKey('NaturalezaSenales', models.DO_NOTHING, db_column='LS_NATURALEZA', blank=True, null=True)  # Field name made lowercase.
    ls_fecha_tr = models.DateTimeField(db_column='LS_FECHA_TR', blank=True, null=True)  # Field name made lowercase.
    ls_unid_ing = models.CharField(db_column='LS_UNID_ING', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ls_formato_valor = models.CharField(db_column='LS_FORMATO_VALOR', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ls_origen = models.CharField(db_column='LS_ORIGEN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ls_minimo = models.FloatField(db_column='LS_MINIMO', blank=True, null=True)  # Field name made lowercase.
    ls_maximo = models.FloatField(db_column='LS_MAXIMO', blank=True, null=True)  # Field name made lowercase.
    ls_fuente = models.CharField(db_column='LS_FUENTE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_factor = models.FloatField(db_column='LS_FACTOR', blank=True, null=True)  # Field name made lowercase.
    ls_columna = models.IntegerField(db_column='LS_COLUMNA', blank=True, null=True)  # Field name made lowercase.
    ls_orden = models.IntegerField(db_column='LS_ORDEN', blank=True, null=True)  # Field name made lowercase.
    ls_ultimo_valor = models.FloatField(db_column='LS_ULTIMO_VALOR', blank=True, null=True)  # Field name made lowercase.
    ls_lim_bajo_bajo = models.FloatField(db_column='LS_LIM_BAJO_BAJO', blank=True, null=True)  # Field name made lowercase.
    ls_lim_bajo = models.FloatField(db_column='LS_LIM_BAJO', blank=True, null=True)  # Field name made lowercase.
    ls_lim_alto = models.FloatField(db_column='LS_LIM_ALTO', blank=True, null=True)  # Field name made lowercase.
    ls_lim_alto_alto = models.FloatField(db_column='LS_LIM_ALTO_ALTO', blank=True, null=True)  # Field name made lowercase.
    ls_lim_alto_alto_alto = models.FloatField(db_column='LS_LIM_ALTO_ALTO_ALTO', blank=True, null=True)  # Field name made lowercase.
    ls_valor_digital = models.CharField(db_column='LS_VALOR_DIGITAL', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ls_ver_web_a = models.SmallIntegerField(db_column='LS_VER_WEB_A', blank=True, null=True)  # Field name made lowercase.
    ls_ver_web_aa = models.SmallIntegerField(db_column='LS_VER_WEB_AA', blank=True, null=True)  # Field name made lowercase.
    ls_ver_web_aaa = models.SmallIntegerField(db_column='LS_VER_WEB_AAA', blank=True, null=True)  # Field name made lowercase.
    ls_ver_intranet_a = models.SmallIntegerField(db_column='LS_VER_INTRANET_A', blank=True, null=True)  # Field name made lowercase.
    ls_ver_intranet_aa = models.SmallIntegerField(db_column='LS_VER_INTRANET_AA', blank=True, null=True)  # Field name made lowercase.
    ls_ver_intranet_aaa = models.SmallIntegerField(db_column='LS_VER_INTRANET_AAA', blank=True, null=True)  # Field name made lowercase.
    ls_ver_pda_a = models.SmallIntegerField(db_column='LS_VER_PDA_A', blank=True, null=True)  # Field name made lowercase.
    ls_ver_pda_aa = models.SmallIntegerField(db_column='LS_VER_PDA_AA', blank=True, null=True)  # Field name made lowercase.
    ls_ver_pda_aaa = models.SmallIntegerField(db_column='LS_VER_PDA_AAA', blank=True, null=True)  # Field name made lowercase.
    ls_fews = models.SmallIntegerField(db_column='LS_FEWS', blank=True, null=True)  # Field name made lowercase.
    ls_lim_tv = models.SmallIntegerField(db_column='LS_LIM_TV', blank=True, null=True)  # Field name made lowercase.
    ls_criterio_tv = models.CharField(db_column='LS_CRITERIO_TV', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_SENALES'


class ListaSenalesCalculadas(models.Model):
    pk = models.CompositePrimaryKey('lsc_tag', 'lsc_fecha_inicio')
    lsc_tag = models.IntegerField(db_column='LSC_TAG')  # Field name made lowercase.
    lsc_fecha_inicio = models.DateTimeField(db_column='LSC_FECHA_INICIO')  # Field name made lowercase.
    lsc_fecha_fin = models.DateTimeField(db_column='LSC_FECHA_FIN', blank=True, null=True)  # Field name made lowercase.
    lsc_version = models.CharField(db_column='LSC_VERSION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lsc_fichero = models.CharField(db_column='LSC_FICHERO', max_length=25, blank=True, null=True)  # Field name made lowercase.
    lsc_tipo_calculo = models.SmallIntegerField(db_column='LSC_TIPO_CALCULO', blank=True, null=True)  # Field name made lowercase.
    lsc_tag_campo = models.IntegerField(db_column='LSC_TAG_CAMPO', blank=True, null=True)  # Field name made lowercase.
    lsc_tag_campo_2 = models.IntegerField(db_column='LSC_TAG_CAMPO_2', blank=True, null=True)  # Field name made lowercase.
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

    class Meta:
        managed = False
        db_table = 'LISTA_SENALES_CALCULADAS'
        unique_together = (('lsc_tag', 'lsc_fecha_inicio'),)


class ListaSenalesLimitevariables(models.Model):
    pk = models.CompositePrimaryKey('lsl_tag', 'lsl_alarma', 'lsl_dia', 'lsl_mes')
    lsl_tag = models.IntegerField(db_column='LSL_TAG')  # Field name made lowercase.
    lsl_alarma = models.CharField(db_column='LSL_ALARMA', max_length=4)  # Field name made lowercase.
    lsl_dia = models.SmallIntegerField(db_column='LSL_DIA')  # Field name made lowercase.
    lsl_mes = models.SmallIntegerField(db_column='LSL_MES')  # Field name made lowercase.
    lsl_valor = models.FloatField(db_column='LSL_VALOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_SENALES_LIMITEVARIABLES'
        unique_together = (('lsl_tag', 'lsl_alarma', 'lsl_dia', 'lsl_mes'),)


class ListaSenalesUmbrales(models.Model):
    ls_tag = models.IntegerField(db_column='LS_TAG')  # Field name made lowercase.
    ls_descripcion = models.CharField(db_column='LS_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ls_tag_txt = models.CharField(db_column='LS_TAG_TXT', max_length=16)  # Field name made lowercase.
    ls_remota = models.IntegerField(db_column='LS_REMOTA')  # Field name made lowercase.
    ls_estacion = models.IntegerField(db_column='LS_ESTACION', blank=True, null=True)  # Field name made lowercase.
    ls_tipo_senal = models.CharField(db_column='LS_TIPO_SENAL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_tipo_alarma = models.SmallIntegerField(db_column='LS_TIPO_ALARMA', blank=True, null=True)  # Field name made lowercase.
    ls_marca_cons = models.SmallIntegerField(db_column='LS_MARCA_CONS', blank=True, null=True)  # Field name made lowercase.
    ls_tipo_almacenamiento = models.CharField(db_column='LS_TIPO_ALMACENAMIENTO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_tipo_consolidacion = models.SmallIntegerField(db_column='LS_TIPO_CONSOLIDACION', blank=True, null=True)  # Field name made lowercase.
    ls_tag_cons_1 = models.SmallIntegerField(db_column='LS_TAG_CONS_1', blank=True, null=True)  # Field name made lowercase.
    ls_tag_cons_2 = models.SmallIntegerField(db_column='LS_TAG_CONS_2', blank=True, null=True)  # Field name made lowercase.
    ls_hora_cons = models.CharField(db_column='LS_HORA_CONS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_curvaref = models.SmallIntegerField(db_column='LS_CURVAREF', blank=True, null=True)  # Field name made lowercase.
    ls_naturaleza = models.SmallIntegerField(db_column='LS_NATURALEZA', blank=True, null=True)  # Field name made lowercase.
    ls_fecha_tr = models.DateTimeField(db_column='LS_FECHA_TR', blank=True, null=True)  # Field name made lowercase.
    ls_unid_ing = models.CharField(db_column='LS_UNID_ING', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ls_formato_valor = models.CharField(db_column='LS_FORMATO_VALOR', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ls_origen = models.CharField(db_column='LS_ORIGEN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ls_minimo = models.FloatField(db_column='LS_MINIMO', blank=True, null=True)  # Field name made lowercase.
    ls_maximo = models.FloatField(db_column='LS_MAXIMO', blank=True, null=True)  # Field name made lowercase.
    ls_fuente = models.CharField(db_column='LS_FUENTE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_factor = models.FloatField(db_column='LS_FACTOR', blank=True, null=True)  # Field name made lowercase.
    ls_columna = models.IntegerField(db_column='LS_COLUMNA', blank=True, null=True)  # Field name made lowercase.
    ls_orden = models.IntegerField(db_column='LS_ORDEN', blank=True, null=True)  # Field name made lowercase.
    ls_ultimo_valor = models.FloatField(db_column='LS_ULTIMO_VALOR', blank=True, null=True)  # Field name made lowercase.
    ls_lim_bajo_bajo = models.FloatField(db_column='LS_LIM_BAJO_BAJO', blank=True, null=True)  # Field name made lowercase.
    ls_lim_bajo = models.FloatField(db_column='LS_LIM_BAJO', blank=True, null=True)  # Field name made lowercase.
    ls_lim_alto = models.FloatField(db_column='LS_LIM_ALTO', blank=True, null=True)  # Field name made lowercase.
    ls_lim_alto_alto = models.FloatField(db_column='LS_LIM_ALTO_ALTO', blank=True, null=True)  # Field name made lowercase.
    ls_lim_alto_alto_alto = models.FloatField(db_column='LS_LIM_ALTO_ALTO_ALTO', blank=True, null=True)  # Field name made lowercase.
    ls_valor_digital = models.CharField(db_column='LS_VALOR_DIGITAL', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ls_ver_web_a = models.SmallIntegerField(db_column='LS_VER_WEB_A', blank=True, null=True)  # Field name made lowercase.
    ls_ver_web_aa = models.SmallIntegerField(db_column='LS_VER_WEB_AA', blank=True, null=True)  # Field name made lowercase.
    ls_ver_web_aaa = models.SmallIntegerField(db_column='LS_VER_WEB_AAA', blank=True, null=True)  # Field name made lowercase.
    ls_ver_intranet_a = models.SmallIntegerField(db_column='LS_VER_INTRANET_A', blank=True, null=True)  # Field name made lowercase.
    ls_ver_intranet_aa = models.SmallIntegerField(db_column='LS_VER_INTRANET_AA', blank=True, null=True)  # Field name made lowercase.
    ls_ver_intranet_aaa = models.SmallIntegerField(db_column='LS_VER_INTRANET_AAA', blank=True, null=True)  # Field name made lowercase.
    ls_ver_pda_a = models.SmallIntegerField(db_column='LS_VER_PDA_A', blank=True, null=True)  # Field name made lowercase.
    ls_ver_pda_aa = models.SmallIntegerField(db_column='LS_VER_PDA_AA', blank=True, null=True)  # Field name made lowercase.
    ls_ver_pda_aaa = models.SmallIntegerField(db_column='LS_VER_PDA_AAA', blank=True, null=True)  # Field name made lowercase.
    ls_fews = models.SmallIntegerField(db_column='LS_FEWS', blank=True, null=True)  # Field name made lowercase.
    ls_lim_tv = models.SmallIntegerField(db_column='LS_LIM_TV', blank=True, null=True)  # Field name made lowercase.
    ls_criterio_tv = models.CharField(db_column='LS_CRITERIO_TV', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_SENALES_UMBRALES'


class ListaSensores(models.Model):
    pk = models.CompositePrimaryKey('LSE_CODIGO', 'LSE_NUMLINEA', 'LSE_TIPO_SENSOR')
    lse_codigo = models.IntegerField(db_column='LSE_CODIGO')  # Field name made lowercase.
    lse_numlinea = models.IntegerField(db_column='LSE_NUMLINEA')  # Field name made lowercase.
    lse_tipo_sensor = models.CharField(db_column='LSE_TIPO_SENSOR', max_length=8)  # Field name made lowercase.
    lse_numserie = models.CharField(db_column='LSE_NUMSERIE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lse_marca = models.CharField(db_column='LSE_MARCA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    lse_modelo = models.CharField(db_column='LSE_MODELO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    lse_finstal = models.DateTimeField(db_column='LSE_FINSTAL', blank=True, null=True)  # Field name made lowercase.
    lse_fdesinst = models.DateTimeField(db_column='LSE_FDESINST', blank=True, null=True)  # Field name made lowercase.
    lse_ubicacion = models.CharField(db_column='LSE_UBICACION', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lse_tag = models.CharField(db_column='LSE_TAG', max_length=12, blank=True, null=True)  # Field name made lowercase.
    lse_calibracion = models.CharField(db_column='LSE_CALIBRACION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lse_observaciones = models.CharField(db_column='LSE_OBSERVACIONES', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_SENSORES'
        unique_together = (('lse_codigo', 'lse_numlinea', 'lse_tipo_sensor'),)


class ListaZonas(models.Model):
    lz_codigo = models.SmallIntegerField(db_column='LZ_CODIGO', primary_key=True)  # Field name made lowercase.
    lz_descripcion = models.CharField(db_column='LZ_DESCRIPCION', max_length=16)  # Field name made lowercase.
    lz_confederacion = models.SmallIntegerField(db_column='LZ_CONFEDERACION', blank=True, null=True)  # Field name made lowercase.
    lz_cod_ser = models.CharField(db_column='LZ_COD_SER', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_ZONAS'


class ModalidadesAlarmas(models.Model):
    ma_alarma = models.SmallIntegerField(db_column='MA_ALARMA', primary_key=True)  # Field name made lowercase.
    ma_txt_alarma = models.CharField(db_column='MA_TXT_ALARMA', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MODALIDADES_ALARMAS'


class NaturalezaSenales(models.Model):
    ns_codigo = models.SmallIntegerField(db_column='NS_CODIGO', primary_key=True)  # Field name made lowercase.
    ns_nombre = models.CharField(db_column='NS_NOMBRE', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NATURALEZA_SENALES'


class ParametrosCalidad(models.Model):
    pc_parametro = models.CharField(db_column='PC_PARAMETRO', primary_key=True, max_length=12)  # Field name made lowercase.
    pc_descripcion = models.CharField(db_column='PC_DESCRIPCION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pc_valor_inicial = models.DecimalField(db_column='PC_VALOR_INICIAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pc_valor_final = models.DecimalField(db_column='PC_VALOR_FINAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PARAMETROS_CALIDAD'


class PlanesActuacion(models.Model):
    pa_codigo = models.SmallIntegerField(db_column='PA_CODIGO', primary_key=True)  # Field name made lowercase.
    pa_descripcion = models.CharField(db_column='PA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pa_observaciones = models.CharField(db_column='PA_OBSERVACIONES', max_length=400, blank=True, null=True)  # Field name made lowercase.
    pa_acciones = models.CharField(db_column='PA_ACCIONES', max_length=1200, blank=True, null=True)  # Field name made lowercase.
    pa_tipo = models.SmallIntegerField(db_column='PA_TIPO', blank=True, null=True)  # Field name made lowercase.
    pa_diagrama = models.CharField(db_column='PA_DIAGRAMA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pa_inforemota = models.BooleanField(db_column='PA_INFOREMOTA', blank=True, null=True)  # Field name made lowercase.
    pa_avisar = models.BooleanField(db_column='PA_AVISAR', blank=True, null=True)  # Field name made lowercase.
    pa_codigo_sms = models.ForeignKey(ListaMensajes, models.DO_NOTHING, db_column='PA_CODIGO_SMS', blank=True, null=True)  # Field name made lowercase.
    pa_codigo_mail = models.ForeignKey(ListaMails, models.DO_NOTHING, db_column='PA_CODIGO_MAIL', blank=True, null=True)  # Field name made lowercase.
    pa_codigo_fax = models.ForeignKey(ListaFax, models.DO_NOTHING, db_column='PA_CODIGO_FAX', blank=True, null=True)  # Field name made lowercase.
    pa_permite_diferido = models.BooleanField(db_column='PA_PERMITE_DIFERIDO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLANES_ACTUACION'


class PlanesActuacionAutomaticos(models.Model):
    paa_codigo = models.SmallIntegerField(db_column='PAA_CODIGO', primary_key=True)  # Field name made lowercase.
    paa_descripcion = models.CharField(db_column='PAA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    paa_hora_ini = models.DateTimeField(db_column='PAA_HORA_INI', blank=True, null=True)  # Field name made lowercase.
    paa_hora_fin = models.DateTimeField(db_column='PAA_HORA_FIN', blank=True, null=True)  # Field name made lowercase.
    paa_codigo_sms = models.ForeignKey(ListaMensajes, models.DO_NOTHING, db_column='PAA_CODIGO_SMS', blank=True, null=True)  # Field name made lowercase.
    paa_activo = models.SmallIntegerField(db_column='PAA_ACTIVO')  # Field name made lowercase.
    paa_codigo_mail = models.IntegerField(db_column='PAA_CODIGO_MAIL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLANES_ACTUACION_AUTOMATICOS'


class Poblaciones(models.Model):
    po_codigo = models.IntegerField(db_column='PO_CODIGO', primary_key=True, db_comment='Codigo de la poblacion')  # Field name made lowercase.
    po_provincia = models.ForeignKey('Provincias', models.DO_NOTHING, db_column='PO_PROVINCIA', blank=True, null=True, db_comment='Codigo de la provincia')  # Field name made lowercase.
    po_descricpion = models.CharField(db_column='PO_DESCRICPION', max_length=50, blank=True, null=True, db_comment='Nombre de la poblacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'POBLACIONES'


class Provincias(models.Model):
    pr_codigo = models.SmallIntegerField(db_column='PR_CODIGO', primary_key=True, db_comment='Codigo de la provincia')  # Field name made lowercase.
    pr_descripcion = models.CharField(db_column='PR_DESCRIPCION', max_length=50, blank=True, null=True, db_comment='Nombre de la provincia')  # Field name made lowercase.
    pr_comunidad = models.ForeignKey(Comunidades, models.DO_NOTHING, db_column='PR_COMUNIDAD', blank=True, null=True, db_comment='Codigo de la comunidad autonom')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROVINCIAS'


class PuestosTrabajo(models.Model):
    pt_codigo = models.IntegerField(db_column='PT_CODIGO', primary_key=True)  # Field name made lowercase.
    pt_descripcion = models.CharField(db_column='PT_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pt_cod_cargo = models.ForeignKey(ListaCargos, models.DO_NOTHING, db_column='PT_COD_CARGO', blank=True, null=True)  # Field name made lowercase.
    pt_cod_puesto_superior = models.IntegerField(db_column='PT_COD_PUESTO_SUPERIOR', blank=True, null=True)  # Field name made lowercase.
    pt_telefono1 = models.CharField(db_column='PT_TELEFONO1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    pt_telefono2 = models.CharField(db_column='PT_TELEFONO2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    pt_telefono3 = models.CharField(db_column='PT_TELEFONO3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    pt_orden = models.IntegerField(db_column='PT_ORDEN', blank=True, null=True)  # Field name made lowercase.
    pt_cod_perso = models.ForeignKey(ListaPersonas, models.DO_NOTHING, db_column='PT_COD_PERSO', blank=True, null=True)  # Field name made lowercase.
    pt_tipo_telefono3 = models.CharField(db_column='PT_TIPO_TELEFONO3', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PUESTOS_TRABAJO'


class RegConsolidacion(models.Model):
    pk = models.CompositePrimaryKey('RC_FECHA_COMP', 'RC_TIPO_COMP')
    rc_fecha_comp = models.DateTimeField(db_column='RC_FECHA_COMP')  # Field name made lowercase.
    rc_tipo_comp = models.CharField(db_column='RC_TIPO_COMP', max_length=1)  # Field name made lowercase.
    rc_proceso = models.CharField(db_column='RC_PROCESO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rc_estado_comp = models.CharField(db_column='RC_ESTADO_COMP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    rc_validada = models.CharField(db_column='RC_VALIDADA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rc_pendiente = models.CharField(db_column='RC_PENDIENTE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rc_num_nodisp = models.IntegerField(db_column='RC_NUM_NODISP', blank=True, null=True)  # Field name made lowercase.
    rc_num_malos = models.IntegerField(db_column='RC_NUM_MALOS', blank=True, null=True)  # Field name made lowercase.
    rc_num_comp = models.IntegerField(db_column='RC_NUM_COMP', blank=True, null=True)  # Field name made lowercase.
    rc_fecha = models.DateTimeField(db_column='RC_FECHA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REG_CONSOLIDACION'
        unique_together = (('rc_fecha_comp', 'rc_tipo_comp'),)


class RegConsLineas(models.Model):
    pk = models.CompositePrimaryKey('RC_FECHA_COMP', 'RC_TIPO_COMP', 'RC_TAG')
    rc_fecha_comp = models.DateTimeField(db_column='RC_FECHA_COMP')  # Field name made lowercase.
    rc_tipo_comp = models.CharField(db_column='RC_TIPO_COMP', max_length=1)  # Field name made lowercase.
    rc_tag = models.CharField(db_column='RC_TAG', max_length=16)  # Field name made lowercase.
    rc_error = models.CharField(db_column='RC_ERROR', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REG_CONS_LINEAS'
        unique_together = (('rc_fecha_comp', 'rc_tipo_comp', 'rc_tag'),)


class ResultadosValidacion(models.Model):
    pk = models.CompositePrimaryKey('VA_CODIGO', 'VA_ID_SENAL', 'VA_INI_INTERVAL', 'VA_TIPO_VALIDA')
    va_codigo = models.IntegerField(db_column='VA_CODIGO')  # Field name made lowercase.
    va_id_senal = models.IntegerField(db_column='VA_ID_SENAL')  # Field name made lowercase.
    va_ini_interval = models.DateTimeField(db_column='VA_INI_INTERVAL')  # Field name made lowercase.
    va_fin_interval = models.DateTimeField(db_column='VA_FIN_INTERVAL')  # Field name made lowercase.
    va_tipo_valida = models.IntegerField(db_column='VA_TIPO_VALIDA')  # Field name made lowercase.
    va_estado = models.IntegerField(db_column='VA_ESTADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESULTADOS_VALIDACION'
        unique_together = (('va_codigo', 'va_id_senal', 'va_ini_interval', 'va_tipo_valida'),)


class Rios(models.Model):
    ri_codigo = models.IntegerField(db_column='RI_CODIGO', primary_key=True)  # Field name made lowercase.
    ri_descripcion = models.CharField(db_column='RI_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIOS'


class SeleccionesFavoritas(models.Model):
    codigo = models.AutoField(db_column='CODIGO')  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    origendatos = models.SmallIntegerField(db_column='ORIGENDATOS', blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='TAGS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    frecuencia = models.IntegerField(db_column='FRECUENCIA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SELECCIONES_FAVORITAS'


class SequiaDatosinformes(models.Model):
    pk = models.CompositePrimaryKey('SDI_CONFEDERACION', 'SDI_TAG')
    sdi_confederacion = models.SmallIntegerField(db_column='SDI_CONFEDERACION', db_comment='Código de la Confederación: 1 ')  # Field name made lowercase.
    sdi_tag = models.SmallIntegerField(db_column='SDI_TAG', db_comment='Tag utilizado en el informe')  # Field name made lowercase.
    sdi_numorden = models.SmallIntegerField(db_column='SDI_NUMORDEN', blank=True, null=True, db_comment='Orden en que aparece en el inf')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SEQUIA_DATOSINFORMES'
        unique_together = (('sdi_confederacion', 'sdi_tag'),)


class SequiaHist(models.Model):
    pk = models.CompositePrimaryKey('SH_CODSISTEMA', 'SH_NUMINDICE', 'SH_ANO', 'SH_MES')
    sh_codsistema = models.ForeignKey('SequiaIndicesEstado', models.DO_NOTHING, db_column='SH_CODSISTEMA', to_field='SIE_NUMINDICE', db_comment='Código del Sistema')  # Field name made lowercase.
    sh_numindice = models.ForeignKey('SequiaIndicesEstado', models.DO_NOTHING, db_column='SH_NUMINDICE', to_field='SIE_NUMINDICE', related_name='sequiahist_sh_numindice_set', db_comment='Nº de índice')  # Field name made lowercase.
    sh_ano = models.SmallIntegerField(db_column='SH_ANO', db_comment='Año')  # Field name made lowercase.
    sh_mes = models.SmallIntegerField(db_column='SH_MES', db_comment='Mes: 1 -> Enero ; 12 -> Diciem')  # Field name made lowercase.
    sh_valor = models.FloatField(db_column='SH_VALOR', blank=True, null=True, db_comment='Valor histórico del índice de ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SEQUIA_HIST'
        unique_together = (('sh_codsistema', 'sh_numindice', 'sh_ano', 'sh_mes'),)


class SequiaIndicesEstado(models.Model):
    pk = models.CompositePrimaryKey('SIE_CODSISTEMA', 'SIE_NUMINDICE')
    sie_codsistema = models.SmallIntegerField(db_column='SIE_CODSISTEMA', db_comment='Código del Sistema')  # Field name made lowercase.
    sie_numindice = models.SmallIntegerField(db_column='SIE_NUMINDICE', db_comment='Nº de índice')  # Field name made lowercase.
    sie_descripcion = models.CharField(db_column='SIE_DESCRIPCION', max_length=50, blank=True, null=True, db_comment='Descripción del Índice de Esta')  # Field name made lowercase.
    sie_tipo = models.SmallIntegerField(db_column='SIE_TIPO', blank=True, null=True, db_comment='Tipo de índice: FLUYENTE, EMBA')  # Field name made lowercase.
    sie_tag = models.ForeignKey(ListaSenales, models.DO_NOTHING, db_column='SIE_TAG', blank=True, null=True, db_comment='Código de la señal utilizada p')  # Field name made lowercase.
    sie_indicecompuesto = models.SmallIntegerField(db_column='SIE_INDICECOMPUESTO', blank=True, null=True, db_comment='Para el caso de índices de est')  # Field name made lowercase.
    sie_factor = models.SmallIntegerField(db_column='SIE_FACTOR', blank=True, null=True, db_comment='Factor de Ponderación. Para el')  # Field name made lowercase.
    sie_defecto = models.BooleanField(db_column='SIE_DEFECTO', blank=True, null=True, db_comment='Indica si es el índice por def')  # Field name made lowercase.
    sie_semanal = models.BooleanField(db_column='SIE_SEMANAL', blank=True, null=True, db_comment='Indica si se ha de obtener el ')  # Field name made lowercase.
    sie_confederacion = models.SmallIntegerField(db_column='SIE_CONFEDERACION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SEQUIA_INDICES_ESTADO'
        unique_together = (('sie_codsistema', 'sie_numindice'),)


class SequiaNiveles(models.Model):
    sn_codigo = models.SmallIntegerField(db_column='SN_CODIGO', primary_key=True, db_comment='Identificador del nivel de seq')  # Field name made lowercase.
    sn_descripcion = models.CharField(db_column='SN_DESCRIPCION', max_length=30, db_comment='Descripción del tipo')  # Field name made lowercase.
    sn_valor_ini = models.DecimalField(db_column='SN_VALOR_INI', max_digits=3, decimal_places=2, blank=True, null=True, db_comment='Valor inicial del Rango de val')  # Field name made lowercase.
    sn_valor_fin = models.DecimalField(db_column='SN_VALOR_FIN', max_digits=3, decimal_places=2, blank=True, null=True, db_comment='Valor final del Rango de valor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SEQUIA_NIVELES'


class TagsInformes(models.Model):
    ti_iden = models.AutoField(db_column='TI_Iden', primary_key=True)  # Field name made lowercase.
    ti_remota = models.SmallIntegerField(db_column='TI_Remota', blank=True, null=True)  # Field name made lowercase.
    ti_tag1 = models.IntegerField(db_column='TI_Tag1', blank=True, null=True)  # Field name made lowercase.
    ti_tag2 = models.IntegerField(db_column='TI_Tag2', blank=True, null=True)  # Field name made lowercase.
    ti_tag3 = models.IntegerField(db_column='TI_Tag3', blank=True, null=True)  # Field name made lowercase.
    ti_tag4 = models.IntegerField(db_column='TI_Tag4', blank=True, null=True)  # Field name made lowercase.
    ti_informe = models.CharField(db_column='TI_Informe', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ti_orden = models.SmallIntegerField(db_column='TI_Orden', blank=True, null=True)  # Field name made lowercase.
    ti_ordentag = models.SmallIntegerField(db_column='TI_OrdenTag', blank=True, null=True)  # Field name made lowercase.
    ti_etiqueta = models.CharField(db_column='TI_Etiqueta', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAGS_INFORMES'


class TagsInformeEmbalseCab(models.Model):
    tiec_linea = models.IntegerField(db_column='TIEC_LINEA', primary_key=True)  # Field name made lowercase.
    tiec_descripcion = models.CharField(db_column='TIEC_DESCRIPCION', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tiec_unidad = models.CharField(db_column='TIEC_UNIDAD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tiec_bloque = models.IntegerField(db_column='TIEC_BLOQUE', blank=True, null=True)  # Field name made lowercase.
    tiec_orden = models.IntegerField(db_column='TIEC_ORDEN', blank=True, null=True)  # Field name made lowercase.
    tiec_tipo = models.IntegerField(db_column='TIEC_TIPO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAGS_INFORME_EMBALSE_CAB'


class TagsInformeEmbalseLin(models.Model):
    pk = models.CompositePrimaryKey('TIEL_REMOTA', 'TIEL_LINEA')
    tiel_remota = models.IntegerField(db_column='TIEL_REMOTA')  # Field name made lowercase.
    tiel_linea = models.IntegerField(db_column='TIEL_LINEA')  # Field name made lowercase.
    tiel_tag = models.IntegerField(db_column='TIEL_TAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAGS_INFORME_EMBALSE_LIN'
        unique_together = (('tiel_remota', 'tiel_linea'),)


class TagsSaihSaica(models.Model):
    tss_tag = models.SmallIntegerField(db_column='TSS_TAG', primary_key=True)  # Field name made lowercase.
    tss_tag_saica = models.CharField(db_column='TSS_TAG_SAICA', max_length=16)  # Field name made lowercase.
    tss_factor = models.DecimalField(db_column='TSS_FACTOR', max_digits=6, decimal_places=2)  # Field name made lowercase.
    tss_traspasar = models.SmallIntegerField(db_column='TSS_TRASPASAR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAGS_SAIH_SAICA'


class TagInformeEmbalse(models.Model):
    pk = models.CompositePrimaryKey('TIE_grupo', 'TIE_orden')
    tie_grupo = models.IntegerField(db_column='TIE_grupo')  # Field name made lowercase.
    tie_orden = models.IntegerField(db_column='TIE_orden')  # Field name made lowercase.
    tie_etiqueta = models.CharField(db_column='TIE_etiqueta', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tie_unidad = models.CharField(db_column='TIE_unidad', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tie_tipo = models.CharField(db_column='TIE_tipo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tie_calculo = models.IntegerField(db_column='TIE_calculo', blank=True, null=True)  # Field name made lowercase.
    tie_tag = models.IntegerField(db_column='TIE_tag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAG_INFORME_EMBALSE'
        unique_together = (('tie_grupo', 'tie_orden'),)


class TempLuis(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    calidad = models.SmallIntegerField(db_column='CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEMP_LUIS'


class TiposAlarmas(models.Model):
    ta_codigo = models.SmallIntegerField(db_column='TA_CODIGO', primary_key=True)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_ALARMAS'


class TiposAlmacenamiento(models.Model):
    ta_codigo = models.CharField(db_column='TA_CODIGO', primary_key=True, max_length=5)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ta_periodo = models.IntegerField(db_column='TA_PERIODO', blank=True, null=True)  # Field name made lowercase.
    ta_almacen = models.IntegerField(db_column='TA_ALMACEN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_ALMACENAMIENTO'


class TiposAvisos(models.Model):
    ta_codigo = models.SmallIntegerField(db_column='TA_CODIGO', primary_key=True)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_AVISOS'


class TiposCalidades(models.Model):
    tca_codigo = models.SmallIntegerField(db_column='TCA_CODIGO', primary_key=True)  # Field name made lowercase.
    tca_descripcion = models.CharField(db_column='TCA_DESCRIPCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tca_porcen_ini = models.SmallIntegerField(db_column='TCA_PORCEN_INI', blank=True, null=True)  # Field name made lowercase.
    tca_porcen_fin = models.SmallIntegerField(db_column='TCA_PORCEN_FIN', blank=True, null=True)  # Field name made lowercase.
    tca_tipo = models.CharField(db_column='TCA_TIPO', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_CALIDADES'


class TiposConsolidacion(models.Model):
    tc_codigo = models.SmallIntegerField(db_column='TC_CODIGO', primary_key=True)  # Field name made lowercase.
    tc_descripcion = models.CharField(db_column='TC_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_CONSOLIDACION'


class TiposEstaciones(models.Model):
    te_codigo = models.CharField(db_column='TE_CODIGO', primary_key=True, max_length=2)  # Field name made lowercase.
    te_descripcion = models.CharField(db_column='TE_DESCRIPCION', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_ESTACIONES'


class TiposSenales(models.Model):
    pk = models.CompositePrimaryKey('TS_CODIGO', 'TS_NATURALEZA')
    ts_codigo = models.CharField(db_column='TS_CODIGO', max_length=5)  # Field name made lowercase.
    ts_descripcion = models.CharField(db_column='TS_DESCRIPCION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ts_nombre = models.CharField(db_column='TS_NOMBRE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ts_naturaleza = models.ForeignKey(NaturalezaSenales, models.DO_NOTHING, db_column='TS_NATURALEZA')  # Field name made lowercase.
    ts_acumula = models.SmallIntegerField(db_column='TS_ACUMULA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_SENALES'
        unique_together = (('ts_codigo', 'ts_naturaleza'),)


class Validaciones(models.Model):
    va_codigo = models.IntegerField(db_column='VA_CODIGO', primary_key=True)  # Field name made lowercase.
    va_estado = models.IntegerField(db_column='VA_ESTADO', blank=True, null=True)  # Field name made lowercase.
    va_fini_valida = models.DateTimeField(db_column='VA_FINI_VALIDA', blank=True, null=True)  # Field name made lowercase.
    va_ffin_valida = models.DateTimeField(db_column='VA_FFIN_VALIDA', blank=True, null=True)  # Field name made lowercase.
    va_tipo_valida = models.IntegerField(db_column='VA_TIPO_VALIDA', blank=True, null=True)  # Field name made lowercase.
    va_remota = models.CharField(db_column='VA_REMOTA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    va_tipo_senal = models.CharField(db_column='VA_TIPO_SENAL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    va_senal = models.CharField(db_column='VA_SENAL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    va_fini_datos = models.DateTimeField(db_column='VA_FINI_DATOS', blank=True, null=True)  # Field name made lowercase.
    va_ffin_datos = models.DateTimeField(db_column='VA_FFIN_DATOS', blank=True, null=True)  # Field name made lowercase.
    va_maximo = models.FloatField(db_column='VA_MAXIMO', blank=True, null=True)  # Field name made lowercase.
    va_minimo = models.FloatField(db_column='VA_MINIMO', blank=True, null=True)  # Field name made lowercase.
    va_porcen_cambio = models.FloatField(db_column='VA_PORCEN_CAMBIO', blank=True, null=True)  # Field name made lowercase.
    va_margen = models.FloatField(db_column='VA_MARGEN', blank=True, null=True)  # Field name made lowercase.
    va_num_valores = models.IntegerField(db_column='VA_NUM_VALORES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VALIDACIONES'


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
