# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Fewsseries(models.Model):
    pk = models.CompositePrimaryKey('SeriesID', 'Fecha', 'FechaForecast')
    seriesid = models.CharField(db_column='SeriesID', max_length=64)  # Field name made lowercase.
    fecha = models.CharField(db_column='Fecha', max_length=64)  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.
    marcador = models.SmallIntegerField(db_column='Marcador', blank=True, null=True)  # Field name made lowercase.
    fechaforecast = models.CharField(db_column='FechaForecast', max_length=64)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FewsSeries'
        unique_together = (('seriesid', 'fecha', 'fechaforecast'),)


class Infoestacion(models.Model):
    estacionid = models.CharField(db_column='EstacionID', primary_key=True, max_length=16, db_comment='Identificador único')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=64, db_comment='Nombre de la estación')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=64, db_comment='Código de la estación')  # Field name made lowercase.
    extendido = models.CharField(db_column='Extendido', max_length=128, db_comment='Nombre extendido/completo de la estación')  # Field name made lowercase.
    tipoestacion = models.CharField(db_column='TipoEstacion', max_length=128, blank=True, null=True, db_comment='Tipología de estación')  # Field name made lowercase.
    tipoinstrumentacion = models.CharField(db_column='TipoInstrumentacion', max_length=128, blank=True, null=True, db_comment='Tipología de instrumentación')  # Field name made lowercase.
    tipoalimentacion = models.CharField(db_column='TipoAlimentacion', max_length=64, blank=True, null=True, db_comment='Tipología de alimentación de energía')  # Field name made lowercase.
    tipocomunicacion = models.CharField(db_column='TipoComunicacion', max_length=64, blank=True, null=True, db_comment='Tipología de dispositivo de comunicación')  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden', blank=True, null=True, db_comment='Orden hidrológico de la estación')  # Field name made lowercase.
    rio = models.CharField(db_column='Rio', max_length=128, blank=True, null=True, db_comment='Río al que pertenece')  # Field name made lowercase.
    sistemaexplotacion = models.CharField(db_column='SistemaExplotacion', max_length=128, blank=True, null=True, db_comment='Sistema al que pertenece')  # Field name made lowercase.
    cuencavertiente = models.FloatField(db_column='CuencaVertiente', blank=True, null=True, db_comment='Área de la cuenca vertiente (Km2)')  # Field name made lowercase.
    toma = models.CharField(db_column='Toma', max_length=64, blank=True, null=True, db_comment='Cauce correspondiente a la toma')  # Field name made lowercase.
    municipio = models.CharField(db_column='Municipio', max_length=128, blank=True, null=True, db_comment='Municipio en el que se ubica')  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=32, blank=True, null=True, db_comment='Municipio en el que se ubica')  # Field name made lowercase.
    utmhemisferio = models.CharField(db_column='UTMHemisferio', max_length=1)  # Field name made lowercase.
    utmzona = models.IntegerField(db_column='UTMZona')  # Field name made lowercase.
    utmx = models.IntegerField(db_column='UTMX', blank=True, null=True, db_comment='Coordenada UTM - X')  # Field name made lowercase.
    utmy = models.IntegerField(db_column='UTMY', blank=True, null=True, db_comment='Coordenada UTM - Y')  # Field name made lowercase.
    latitud = models.FloatField(db_column='Latitud', blank=True, null=True, db_comment='Latitud de la posición')  # Field name made lowercase.
    longitud = models.FloatField(db_column='Longitud', blank=True, null=True, db_comment='Longitud de la posición')  # Field name made lowercase.
    altitud = models.FloatField(db_column='Altitud', blank=True, null=True, db_comment='Altitud de la posición')  # Field name made lowercase.
    publicar = models.TextField(db_column='Publicar', blank=True, null=True, db_comment='Indicador de publicación en web.')  # Field name made lowercase. This field type is a guess.
    ocultar = models.TextField(db_column='Ocultar', blank=True, null=True, db_comment='Indicador de ocultación / marcar como N/D')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'InfoEstacion'
        db_table_comment = 'Datos de estaciones'


class Infovariable(models.Model):
    variableid = models.CharField(db_column='VariableID', primary_key=True, max_length=24, db_comment='Identificador único')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=64, db_comment='Nombre de la variable')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=64, db_comment='Código / Abreviatura de la variable')  # Field name made lowercase.
    extendido = models.CharField(db_column='Extendido', max_length=256, db_comment='Nombre extendido/completo de la variable')  # Field name made lowercase.
    estacion = models.ForeignKey(Infoestacion, models.DO_NOTHING, db_column='Estacion', db_comment='Estación a la que pertenece')  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=16, blank=True, null=True, db_comment='Unidades de medida')  # Field name made lowercase.
    tipohidrologico = models.CharField(db_column='TipoHidrologico', max_length=64, blank=True, null=True, db_comment='Tipología de la variable')  # Field name made lowercase.
    acumulador = models.TextField(db_column='Acumulador', blank=True, null=True, db_comment='Indicador dato acumulador/contador')  # Field name made lowercase. This field type is a guess.
    alarmabajo = models.FloatField(db_column='AlarmaBajo', blank=True, null=True, db_comment='Alarma por valor muy bajo')  # Field name made lowercase.
    alertabajo = models.FloatField(db_column='AlertaBajo', blank=True, null=True, db_comment='Alerta por valor bajo')  # Field name made lowercase.
    alertaalto = models.FloatField(db_column='AlertaAlto', blank=True, null=True, db_comment='Alarma por valor alto')  # Field name made lowercase.
    alarmaalto = models.FloatField(db_column='AlarmaAlto', blank=True, null=True, db_comment='Alerta por valor muy alto')  # Field name made lowercase.
    limiteminimo = models.FloatField(db_column='LimiteMinimo', blank=True, null=True, db_comment='Valor mínimo aceptable')  # Field name made lowercase.
    limitemaximo = models.FloatField(db_column='LimiteMaximo', blank=True, null=True, db_comment='Valor máximo aceptable')  # Field name made lowercase.
    limitecambio = models.FloatField(db_column='LimiteCambio', blank=True, null=True, db_comment='Valor de cambio máximo aceptable')  # Field name made lowercase.
    entidadorigen = models.CharField(db_column='EntidadOrigen', max_length=64, blank=True, null=True, db_comment='Entidad de la que procede la información')  # Field name made lowercase.
    frecuencia = models.IntegerField(db_column='Frecuencia', blank=True, null=True)  # Field name made lowercase.
    resumir = models.TextField(db_column='Resumir', blank=True, null=True, db_comment='Indicador de generación de medias')  # Field name made lowercase. This field type is a guess.
    publicar = models.TextField(db_column='Publicar', blank=True, null=True, db_comment='Indicador de publicación en web')  # Field name made lowercase. This field type is a guess.
    ocultar = models.TextField(db_column='Ocultar', blank=True, null=True, db_comment='Indicador de ocultación / marcar como N/D')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'InfoVariable'
        db_table_comment = 'Datos de variables'


class Variableforecast(models.Model):
    pk = models.CompositePrimaryKey('VariableObservada', 'VariableForecast')
    estacion = models.CharField(db_column='Estacion', max_length=16)  # Field name made lowercase.
    variableobservada = models.CharField(db_column='VariableObservada', max_length=64)  # Field name made lowercase.
    variableforecast = models.CharField(db_column='VariableForecast', max_length=128)  # Field name made lowercase.
    variableid = models.CharField(db_column='VariableID', max_length=16)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=64, blank=True, null=True)  # Field name made lowercase.
    extendido = models.CharField(db_column='Extendido', max_length=128, blank=True, null=True)  # Field name made lowercase.
    alarmaalto = models.FloatField(db_column='AlarmaAlto', blank=True, null=True)  # Field name made lowercase.
    alarmabajo = models.FloatField(db_column='AlarmaBajo', blank=True, null=True)  # Field name made lowercase.
    alertaalto = models.FloatField(db_column='AlertaAlto', blank=True, null=True)  # Field name made lowercase.
    alertabajo = models.FloatField(db_column='AlertaBajo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VariableForecast'
        unique_together = (('variableobservada', 'variableforecast'),)
