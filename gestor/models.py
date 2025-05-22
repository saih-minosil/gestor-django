from django.db import models
from django import forms
from django.db.models.deletion import Collector
from django.db import (
    router,
    transaction,
)

from django.db.models.sql.constants import (
    GET_ITERATOR_CHUNK_SIZE,
    ROW_COUNT,
)
from django.db.models.sql.query import Query

from collections import Counter 
from functools import  reduce
from operator import attrgetter, or_

from django.db import models, transaction
from django.db.models import  signals, sql

from main_app.models_comun import copy_object,copy_from_different_object, ListaZonas,TiposConsolidacion,TiposEstaciones
from main_app.models_comun import TiposAlmacenamiento,GruposTiposSenales
from django.db.models import Max
from main_app import models_hist
from pprint import pp

#CHOICES

gravedades={"GRAVE":"Grave","LEVE":"Leve"}
tipologias={"Azud":"Azud","Caída libre":"Caída libre","Cauce natural":"Cauce natural","Pared gruesa":"Pared gruesa","Pozo piezométrico":"Pozo piezométrico","V-flat":"V-flat"}
tipos_sensores={"Boya / Contrapeso":"Boya / Contrapeso","Doppler":"Doppler","Piezorresistivo":"Piezorresistivo","Radar":"Radar","Ultrasonidos":"Ultrasonidos"}
origenes={"FICHERO":"Fichero","CALCULO":"Calculo","CAMPO":"Campo","MANUAL":"Manual"}
niveles_alarmas={"BB":"Muy bajo","B":"Bajo","A":"Activacion","AA":"PreAlerta","AAA":"Alerta"}
modos_ordenes={0:"ACTIVA",1:"NO ACTIVA"}
estado_digital_0={"-":"-","ABIERTA":"ABIERTA","APAGADO":"APAGADO","APAGAR":"APAGAR","ARMADO":"ARMADO","ARMAR":"ARMAR","ARRANCADO":"ARRANCADO","CERRADA":"CERRADA","CLAPETA":"CLAPETA",
"COMUNICA":"COMUNICA","DESACTIVA":"DESACTIVA","DESARMADA":"DESARMADA","DESCONECTAR":"DESCONECTAR","ENCENDIDO":"ENCENDIDO","FALLO":"FALLO","INACTIVA":"INACTIVA","MANIOBRA":"MANIOBRA",
"NO":"NO","NORMAL":"NORMAL","PARADO":"PARADO","PARAR":"PARAR","SALIENTE":"SALIENTE"}# Create your models here.
estado_digital_1={"ARMAR/DESARMAR":"ARMAR/DESARMAR","IN/DESINHIBIR":"IN/DESINHIBIR","RESETEAR":"RESETEAR","CERRADA":"CERRADA","ENCENDIDO":"ENCENDIDO","ENCENDER":"ENCENDER",
"DESARMADO":"DESARMADO","DESARMAR":"DESARMAR","PARADO":"PARADO","ABIERTA":"ABIERTA","COMPUERTA":"COMPUERTA","NO COMUNICA":"NO COMUNICA","ACTIVA":"ACTIVA","ARMADA":"ARMADA",
"CONECTAR":"CONECTAR","APAGADO":"APAGADO","NORMAL":"NORMAL","ABIERTO":"ABIERTO","SI":"SI","FALLO":"FALLO","PARAR":"PARAR","ARRANCADO":"ARRANCADO",
"ARRANCAR":"ARRANCAR","ENTRANTE":"ENTRANTE"}
tipos_ordenes={"TELEMANDO":"TELEMANDO","EMERGENCIA":"EMERGENCIA","CONTROL":"CONTROL"}


class CompositeDeleteQuery(Query):
    """A DELETE SQL query. modified for composite key"""
    compiler = "SQLDeleteCompiler"

    #def do_query(self, table, where, using):
    #    self.alias_map = {table: self.alias_map[table]}
    #    self.where = where
    #    return self.get_compiler(using).execute_sql(ROW_COUNT)

    def delete_batch(self, pk_list, using):
       
        # number of objects deleted
        num_deleted = 0
        field = self.get_meta().pk
        for offset in range(0, len(pk_list), GET_ITERATOR_CHUNK_SIZE):
            self.clear_where()
            if field.__class__.__name__=="CompositePrimaryKey":
                for i,f in enumerate(field.field_names):
                    self.add_filter(
                    f"{f}",
                    pk_list[offset][i],
                )
            else:    
                self.add_filter(
                    f"{field.attname}__in",
                    pk_list[offset : offset + GET_ITERATOR_CHUNK_SIZE],
                )
            num_deleted += self.do_query(
                self.get_meta().db_table, self.where, using=using
            )
        return num_deleted

class CompositeCollector(Collector):   
    def delete(self):
        # sort instance collections
        for model, instances in self.data.items():
            self.data[model] = sorted(instances, key=attrgetter("pk"))

        # if possible, bring the models in an order suitable for databases that
        # don't support transactions or cannot defer constraint checks until the
        # end of a transaction.
        self.sort()
        # number of objects deleted for each model label
        deleted_counter = Counter()

        # Optimize for the case with a single obj and no dependencies
        if len(self.data) == 1 and len(instances) == 1:
            instance = list(instances)[0]
            if self.can_fast_delete(instance):
                with transaction.mark_for_rollback_on_error(self.using):
                    count = CompositeDeleteQuery(model).delete_batch(
                        [instance.pk], self.using
                    )
                setattr(instance, model._meta.pk.attname, None)
                return count, {model._meta.label: count}

        with transaction.atomic(using=self.using, savepoint=False):
            # send pre_delete signals
            for model, obj in self.instances_with_model():
                if not model._meta.auto_created:
                    signals.pre_delete.send(
                        sender=model,
                        instance=obj,
                        using=self.using,
                        origin=self.origin,
                    )

            # fast deletes
            for qs in self.fast_deletes:
                count = qs._raw_delete(using=self.using)
                if count:
                    deleted_counter[qs.model._meta.label] += count

            # update fields
            for (field, value), instances_list in self.field_updates.items():
                updates = []
                objs = []
                for instances in instances_list:
                    if (
                        isinstance(instances, models.QuerySet)
                        and instances._result_cache is None
                    ):
                        updates.append(instances)
                    else:
                        objs.extend(instances)
                if updates:
                    combined_updates = reduce(or_, updates)
                    combined_updates.update(**{field.name: value})
                if objs:
                    model = objs[0].__class__
                    query = sql.UpdateQuery(model)
                    query.update_batch(
                        list({obj.pk for obj in objs}), {field.name: value}, self.using
                    )

            # reverse instance collections
            for instances in self.data.values():
                instances.reverse()

            # delete instances
            for model, instances in self.data.items():
                query = CompositeDeleteQuery(model)
                pk_list = [obj.pk for obj in instances]
                count = query.delete_batch(pk_list, self.using)
                if count:
                    deleted_counter[model._meta.label] += count

                if not model._meta.auto_created:
                    for obj in instances:
                        signals.post_delete.send(
                            sender=model,
                            instance=obj,
                            using=self.using,
                            origin=self.origin,
                        )

        for model, instances in self.data.items():
            for instance in instances:
                setattr(instance, model._meta.pk.attname, None)
        return sum(deleted_counter.values()), dict(deleted_counter)





########################################################################################################################
########################################  DATOS  #######################################################################
########################################################################################################################
''' ( referenciias)

'''


class Comunidades(models.Model):
    ca_codigo = models.SmallIntegerField(db_column='CA_CODIGO', primary_key=True, db_comment='Codigo de la comunidad autonoma')  # Field name made lowercase.
    ca_descripcion = models.CharField(db_column='CA_DESCRIPCION', max_length=50, blank=True, null=True, db_comment='Nombre de la comunidad autonom')  # Field name made lowercase.
    ca_falta = models.DateTimeField(db_column='CA_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    ca_fmodif = models.DateTimeField(db_column='CA_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMUNIDADES'

    def __str__(self):
        return str(self.ca_codigo) + ":" + str(self.ca_descripcion)


class Provincias(models.Model):
    pr_codigo = models.SmallIntegerField(db_column='PR_CODIGO', primary_key=True,verbose_name="Codigo provincia")  # Field name made lowercase.
    pr_descripcion = models.CharField(db_column='PR_DESCRIPCION', max_length=50, blank=True,
                                      null=True, verbose_name="Nombre provincia")  # Field name made lowercase.
    pr_comunidad = models.SmallIntegerField(db_column='PR_COMUNIDAD', blank=True,
                                            null=True, verbose_name="Comunidad")  # Field name made lowercase.
    pr_falta = models.DateTimeField(db_column='PR_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    pr_fmodif = models.DateTimeField(db_column='PR_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROVINCIAS'
        verbose_name='Provincia'
        verbose_name_plural='Provincias'

    def __str__(self):
        return str(self.pr_codigo) + ":" + str(self.pr_descripcion)

class TiposTarjetas(models.Model):
    tt_codigo = models.SmallIntegerField(db_column='TT_CODIGO', primary_key=True, verbose_name="Código")
    tt_nombre = models.CharField(db_column='TT_NOMBRE', max_length=20,verbose_name="Nombre")        
    tt_descripcion = models.CharField(db_column='TT_DESCRIPCION', max_length=200,verbose_name="Descripcion")
    
    class Meta:
        managed = False
        db_table = 'TIPOS_TARJETAS'
        verbose_name="Tipo de tarjeta"
        verbose_name_plural="Tipos de tarjeta"

    def __str__(self):
        return str(self.tt_nombre)            

class FormatosDigitales(models.Model):
    fd_estado0 = models.CharField(db_column='FD_ESTADO0', max_length=24,unique=True)  # Field name made lowercase. The composite primary key (FD_ESTADO0, FD_ESTADO1) found, that is not supported. The first column is selected.
    fd_estado1 = models.CharField(db_column='FD_ESTADO1', max_length=24,unique=True)  # Field name made lowercase.
    fd_estado2 = models.CharField(db_column='FD_ESTADO2', max_length=24, blank=True, null=True)  # Field name made lowercase.
    fd_estado3 = models.CharField(db_column='FD_ESTADO3', max_length=24, blank=True, null=True)  # Field name made lowercase.
    fd_formato_valor = models.CharField(db_column='FD_FORMATO_VALOR', max_length=16, blank=True, primary_key=True)  # Field name made lowercase.
    fd_hay_estado0 = models.SmallIntegerField(db_column='FD_HAY_ESTADO0', blank=True, null=True)  # Field name made lowercase.
    fd_hay_estado1 = models.SmallIntegerField(db_column='FD_HAY_ESTADO1', blank=True, null=True)  # Field name made lowercase.
    fd_falta = models.DateTimeField(db_column='FD_FALTA', blank=True, null=True)  # Field name made lowercase.
    fd_fmodif = models.DateTimeField(db_column='FD_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name='Formato digital'
        verbose_name_plural='Formatos digitales'
        managed = False
        db_table = 'FORMATOS_DIGITALES'
        unique_together = (('fd_estado0', 'fd_estado1'),)

'''
##############################################################################################################################################
##################################################   EDITABLES   #################################################################################
##############################################################################################################################################
##############################################################################################################################################
##############################################################################################################################################
'''

class Poblaciones(models.Model):
    po_codigo = models.IntegerField(db_column='PO_CODIGO', primary_key=True,verbose_name="Codigo población")  # Field name made lowercase.
    po_provincia  = models.ForeignKey(Provincias, db_column="PO_PROVINCIA", on_delete=models.DO_NOTHING, verbose_name="Provincia población")
    po_descripcion = models.CharField(db_column='PO_DESCRIPCION', max_length=50, blank=True,
                                      null=True, verbose_name = "Nombre población")  # Field name made lowercase.
    po_falta = models.DateTimeField(db_column='PO_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    po_fmodif = models.DateTimeField(db_column='PO_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'POBLACIONES'
        verbose_name='Poblacion'
        verbose_name_plural='Poblaciones'
        ordering=['po_codigo']

    def __str__(self):
        return str(self.po_descripcion)

class Rios(models.Model):
    ri_codigo = models.IntegerField(db_column='RI_CODIGO', primary_key=True)  # Field name made lowercase.
    ri_descripcion = models.CharField(db_column='RI_DESCRIPCION', max_length=50, blank=True,
                                      null=True)  # Field name made lowercase.
    ri_falta = models.DateTimeField(db_column='RI_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    ri_fmodif = models.DateTimeField(db_column='RI_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIOS'
        verbose_name='Rio'
        verbose_name_plural='Rios'
        ordering=['ri_codigo']

    def __str__(self):
        return str(self.ri_descripcion)
        

class TiposSenales(models.Model):
    ts_codigo = models.CharField(db_column='TS_CODIGO', primary_key=True, max_length=5,verbose_name="Codigo")   # Field name made lowercase. The composite primary key (TS_CODIGO, TS_NATURALEZA,found, that is not supported. The first column is selected.
    ts_descripcion = models.CharField(db_column='TS_DESCRIPCION', max_length=50, blank=True, null=True,verbose_name="Descripcion")  # Field name made lowercase.
    ts_naturaleza = models.ForeignKey('NaturalezaSenales',on_delete=models.DO_NOTHING,db_column='TS_NATURALEZA',verbose_name="Naturaleza")  # Field name made lowercase.
    ts_falta = models.DateTimeField(db_column='TS_FALTA', blank=True, null=True, editable=False,verbose_name="falta")  # Field name made lowercase.
    ts_fmodif = models.DateTimeField(db_column='TS_FMODIF', blank=True, null=True, editable=False,verbose_name="fmodif")  # Field name made lowercase.
    ts_nombre_corto = models.CharField(db_column='TS_NOMBRE_CORTO', max_length=10, blank=True, null=True,verbose_name="Nombre corto")  # Field name made lowercase.
    ts_orden = models.SmallIntegerField(db_column='TS_ORDEN', blank=True, null=True,verbose_name="Orden")  # Field name made lowercase.
    ts_acumula = models.SmallIntegerField(db_column='TS_ACUMULA', blank=True, null=True,verbose_name="Acumula")  # Field name made lowercase.
    ts_grupo_web = models.ForeignKey(GruposTiposSenales,on_delete=models.DO_NOTHING,db_column='TS_GRUPO_WEB', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_SENALES'
        unique_together = (('ts_codigo', 'ts_naturaleza'),)
        verbose_name="Tipo de señal"
        verbose_name_plural="Tipos de señal"
        ordering=['ts_codigo']

    def __str__(self):
        return str(self.ts_descripcion)


class UnidadesIngenieria(models.Model):
    ui_codigo = models.CharField(db_column='UI_CODIGO', primary_key=True, max_length=10,verbose_name="Codigo")  # Field name made lowercase.
    ui_descripcion = models.CharField(db_column='UI_DESCRIPCION', max_length=50, blank=True, null=True,verbose_name="Descripcion")  # Field name made lowercase.
    ui_codigo_corto = models.CharField(db_column='UI_CODIGO_CORTO', max_length=3, blank=True, null=True,verbose_name="Cóodigo corto")  # Field name made lowercase.
    ui_orden = models.SmallIntegerField(db_column='UI_ORDEN', blank=True, null=True,verbose_name="Orden")  # Field name made lowercase.
    ui_falta = models.DateTimeField(db_column='UI_FALTA', blank=True, null=True,verbose_name="falta")  # Field name made lowercase.
    ui_fmodif = models.DateTimeField(db_column='UI_FMODIF', blank=True, null=True,verbose_name="fmodif")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UNIDADES_INGENIERIA'
        verbose_name="Unidad de medida"
        verbose_name_plural="Unidades de medida"
        ordering=['ui_orden']


    def __str__(self):
        return str(self.ui_descripcion)    



########################################################################################################################
############################################   LISTAS          #########################################################
########################################################################################################################

class ListaEstaciones(models.Model):
    #GENERALES
    le_codigo = models.IntegerField(db_column='LE_CODIGO', primary_key=True,verbose_name="Codigo")	  # Field name made lowercase.
    le_codigo_txt = models.CharField(db_column='LE_CODIGO_TXT', max_length=4,verbose_name="Codigo txt")	  # Field name made lowercase.
    le_tipo_estacion = models.ForeignKey(TiposEstaciones,db_column='LE_TIPO_ESTACION', max_length=2,verbose_name="Tipo de Estacion",on_delete=models.DO_NOTHING)	  # Field name made lowercase.
    le_bloquear = models.BooleanField(db_column='LE_BLOQUEAR', blank=True, verbose_name="Bloquear traspasos")	  # Field name made lowercase.    
    le_zona = models.ForeignKey(ListaZonas,on_delete=models.DO_NOTHING,db_column="LE_ZONA",verbose_name="Zona")	
    le_nombre = models.CharField(db_column='LE_NOMBRE', max_length=30,verbose_name="Nombre")	  # Field name made lowercase.
    le_nombre_corto = models.CharField(db_column='LE_NOMBRE_CORTO', max_length=18,verbose_name="Nombre corto")	  # Field name made lowercase.    
    #LOCALIZACION
    le_comu_auto = models.ForeignKey(Comunidades, on_delete=models.DO_NOTHING, db_column="LE_COMU_AUTO",verbose_name="Comunidad autonoma")	    
    le_provincia = models.ForeignKey(Provincias, on_delete=models.DO_NOTHING, db_column="LE_PROVINCIA",verbose_name="Provincia")	    
    le_municipio = models.ForeignKey(Poblaciones, on_delete=models.DO_NOTHING, db_column="LE_MUNICIPIO",verbose_name="Municipio")	    
    le_rio = models.ForeignKey(Rios, on_delete=models.DO_NOTHING, db_column="LE_RIO",verbose_name="Rio")	
    le_recid = models.IntegerField(db_column='LE_RECID', blank=True, null=True,verbose_name="Recid")	  # Field name made lowercase.
    le_utm_huso = models.IntegerField(db_column='LE_UTM_HUSO', blank=True, null=True,verbose_name="Huso")	  # Field name made lowercase.
    le_utm_x = models.DecimalField(db_column='LE_UTM_X', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Utm x")	  # Field name made lowercase.
    le_utm_y = models.DecimalField(db_column='LE_UTM_Y', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Utm y")	  # Field name made lowercase.
    le_utm_z = models.DecimalField(db_column='LE_UTM_Z', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Utm z")	  # Field name made lowercase.
    le_h29_x = models.DecimalField(db_column='LE_H29_X', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_h29_y = models.DecimalField(db_column='LE_H29_Y', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    le_h29_z = models.DecimalField(db_column='LE_H29_Z', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    
    #CONFIGURACION
    le_infoplus = models.BooleanField(db_column='LE_INFOPLUS', blank=True, verbose_name="Crear en SCADA")	  # Field name made lowercase.
    le_ver_web = models.BooleanField(db_column='LE_VER_WEB', blank=True, verbose_name="Ver web")	  # Field name made lowercase.
    le_ver_intranet = models.BooleanField(db_column='LE_VER_INTRANET', blank=True, verbose_name="Ver intranet")	  # Field name made lowercase.
    le_ver_pda = models.BooleanField(db_column='LE_VER_PDA', blank=True,verbose_name="Ver PDA")  # Field name made lowercase.
    le_datos_manuales = models.BooleanField(db_column='LE_DATOS_MANUALES', blank=True, verbose_name="Datos manuales")	  # Field name made lowercase.
    le_datos_automaticos = models.BooleanField(db_column='LE_DATOS_AUTOMATICOS', blank=True, verbose_name="Datos automaticos")	  # Field name made lowercase.
    le_codigo_ant = models.CharField(db_column='LE_CODIGO_ANT', max_length=6, blank=True, null=True,verbose_name="codigo ant")	  # Field name made lowercase.
    le_provee_info = models.CharField(db_column='LE_PROVEE_INFO', max_length=50, blank=True, null=True,verbose_name="provee info")	  # Field name made lowercase.
    le_tipo_dato = models.SmallIntegerField(db_column='LE_TIPO_DATO', blank=True, null=True,verbose_name="tipo dato")	  # Field name made lowercase.
    le_datos_8h = models.SmallIntegerField(db_column='LE_DATOS_8H', blank=True, null=True)  # Field name made lowercase.
    le_datos_dm = models.SmallIntegerField(db_column='LE_DATOS_DM', blank=True, null=True,verbose_name="datos dm")	  # Field name made lowercase.
    le_posicion = models.SmallIntegerField(db_column='LE_POSICION', blank=True, null=True,verbose_name="posicion")	  # Field name made lowercase.    
    le_tipologia = models.CharField(db_column='LE_TIPOLOGIA', max_length=20, blank=True, null=True,verbose_name="Tipologia",choices=tipologias)	  # Field name made lowercase.
    le_tipo_sensor = models.CharField(db_column='LE_TIPO_SENSOR', max_length=20, blank=True, null=True,verbose_name="Tipo de sensor",choices=tipos_sensores)	  # Field name made lowercase.
    le_superficie = models.DecimalField(db_column='LE_SUPERFICIE', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Superficie")	  # Field name made lowercase.
    le_fuera_servicio = models.BooleanField(db_column='LE_FUERA_SERVICIO', blank=True, verbose_name="Fuera de servicio")	  # Field name made lowercase.
    le_ver_estadisticas = models.BooleanField(db_column='LE_VER_ESTADISTICAS', blank=True, verbose_name="Ver estadisticas")	  # Field name made lowercase.
    le_ver_codigo_roea = models.BooleanField(db_column='LE_VER_CODIGO_ROEA', blank=True,verbose_name="Mostrar codigo ROEA")  # Field name made lowercase.
    le_codigo_saica = models.CharField(db_column='LE_CODIGO_SAICA', max_length=4, blank=True, null=True,verbose_name="Codigo SAICA")	  # Field name made lowercase.
    
    #FECHA DE MODIFICACION
    le_falta = models.DateTimeField(db_column='LE_FALTA', blank=True, null=True,editable=False,verbose_name="falta")	  # Field name made lowercase.
    le_fmodif = models.DateTimeField(db_column='LE_FMODIF', blank=True, null=True,editable=False,verbose_name="fmodif")	  # Field name made lowercase.
    le_fbaja = models.DateTimeField(db_column='LE_FBAJA', blank=True, null=True,editable=False,verbose_name="fbaja")	  # Field name made lowercase.
    
    #RANGOS
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
    
    #DATOS ESTACION (Que no se usan creo)
    le_expediente = models.CharField(db_column='LE_EXPEDIENTE', max_length=30, blank=True, null=True,verbose_name="expediente")	  # Field name made lowercase.
    le_titular_concesion = models.IntegerField(db_column='LE_TITULAR_CONCESION', blank=True, null=True,verbose_name="titular concesion")	  # Field name made lowercase.
    le_fecha_concesion = models.DateTimeField(db_column='LE_FECHA_CONCESION', blank=True, null=True,verbose_name="fecha concesion")	  # Field name made lowercase.
    le_ffin_obras = models.DateTimeField(db_column='LE_FFIN_OBRAS', blank=True, null=True,verbose_name="ffin obras")	  # Field name made lowercase.
    le_arrendatario = models.DecimalField(db_column='LE_ARRENDATARIO', max_digits=6, decimal_places=0, blank=True, null=True,verbose_name="arrendatario")	  # Field name made lowercase.
    le_registroseg = models.CharField(db_column='LE_REGISTROSEG', max_length=30, blank=True, null=True,verbose_name="registroseg")	  # Field name made lowercase.
    le_riesgopotencial = models.CharField(db_column='LE_RIESGOPOTENCIAL', max_length=30, blank=True, null=True,verbose_name="riesgopotencial")	  # Field name made lowercase.
    le_fnormasexp = models.DateTimeField(db_column='LE_FNORMASEXP', blank=True, null=True,verbose_name="fnormasexp")	  # Field name made lowercase.
    le_fclasificacion = models.DateTimeField(db_column='LE_FCLASIFICACION', blank=True, null=True,verbose_name="fclasificacion")	  # Field name made lowercase.
    le_faprobacion_pe = models.DateTimeField(db_column='LE_FAPROBACION_PE', blank=True, null=True,verbose_name="faprobacion pe")	  # Field name made lowercase.
    le_fimplantacion_pe = models.DateTimeField(db_column='LE_FIMPLANTACION_PE', blank=True, null=True,verbose_name="fimplantacion pe")	  # Field name made lowercase.
    le_puntosaviso = models.DecimalField(db_column='LE_PUNTOSAVISO', max_digits=4, decimal_places=0, blank=True, null=True,verbose_name="puntosaviso")	  # Field name made lowercase.
    le_director_pe = models.CharField(db_column='LE_DIRECTOR_PE', max_length=30, blank=True, null=True,verbose_name="director pe")	  # Field name made lowercase.
    le_represante_pe = models.CharField(db_column='LE_REPRESANTE_PE', max_length=30, blank=True, null=True,verbose_name="represante pe")	  # Field name made lowercase.
    le_direccion_cc = models.CharField(db_column='LE_DIRECCION_CC', max_length=50, blank=True, null=True,verbose_name="direccion cc")	  # Field name made lowercase.
    le_telefono_cc = models.CharField(db_column='LE_TELEFONO_CC', max_length=30, blank=True, null=True,verbose_name="telefono cc")	  # Field name made lowercase.
    le_fax_cc = models.CharField(db_column='LE_FAX_CC', max_length=30, blank=True, null=True,verbose_name="fax cc")	  # Field name made lowercase.
    le_correo_cc = models.CharField(db_column='LE_CORREO_CC', max_length=30, blank=True, null=True,verbose_name="correo cc")	  # Field name made lowercase.
    #MASA DE AGUA
    le_masa_codigo = models.CharField(db_column='LE_MASA_CODIGO', max_length=30, blank=True, null=True,verbose_name="Codigo masa")	  # Field name made lowercase.
    le_masa_nombre = models.CharField(db_column='LE_MASA_NOMBRE', max_length=70, blank=True, null=True,verbose_name="Nombre masa")	  # Field name made lowercase.
    le_masa_categoria = models.CharField(db_column='LE_MASA_CATEGORIA', max_length=30, blank=True, null=True,verbose_name="Categoría masa")	  # Field name made lowercase.
    le_masa_naturaleza = models.CharField(db_column='LE_MASA_NATURALEZA', max_length=30, blank=True, null=True,verbose_name="Naturaleza masa")	  # Field name made lowercase.
    le_masa_est_eco = models.CharField(db_column='LE_MASA_EST_ECO', max_length=30, blank=True, null=True,verbose_name="Estado ecológico masa")  # Field name made lowercase.
    le_masa_est_quim = models.CharField(db_column='LE_MASA_EST_QUIM', max_length=30, blank=True, null=True, verbose_name="Estado químico masa")   # Field name made lowercase.
    le_masa_est_glob = models.CharField(db_column='LE_MASA_EST_GLOB', max_length=30, blank=True, null=True,verbose_name="Estado global masa")  # Field name made lowercase.
    le_masa_tipo = models.CharField(db_column='LE_MASA_TIPO', max_length=70, blank=True, null=True,verbose_name="masa tipo")	  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_ESTACIONES'
        ordering=['le_codigo_txt']
        verbose_name="Estacion"
        verbose_name_plural="Estaciones"

    def save(self,*args,force_insert=False, force_update=False, using=None, update_fields=None):
        ultimo_id =  ListaEstaciones.objects.aggregate(Max('le_codigo'))['le_codigo__max']
        ultimo_recid_hist = models_hist.ListaEstaciones_H.objects.aggregate(Max('le_codigo'))['le_codigo__max']                
        ultimo_recid_gest = ListaEstaciones.objects.aggregate(Max('le_codigo'))['le_codigo__max']                
        pp(self.__dict__)
        if not self.le_codigo :
            self.le_codigo=ultimo_id+1        
            self.le_recid=max(ultimo_recid_hist,ultimo_recid_gest) +1
        super().save(force_insert,force_update,using,update_fields)    


    def __str__(self):
        return str(self.le_codigo_txt) + " : " + str(self.le_nombre)

'''
# ESTA NO ESTá EN EL GESTOR PERO SE PODRíA METER, EN EL GESTOR ORIGINAL SI ESTÁ, SIRVE PARA HACER LAS GRAFICAS PREDETERMINADAS DE CADA ESTACIÓN
class ListaEstacionesAreas(models.Model):
    lea_codigo = models.OneToOneField(ListaEstaciones,on_delete=models.DO_NOTHING,db_column='LEA_CODIGO', primary_key=True,verbose_name="Codigo estación")  # Field name made lowercase. The composite primary key (LEA_CODIGO, LEA_AREA, LEA_NUMORDEN) found, that is not supported. The first column is selected.
    lea_area = models.CharField(db_column='LEA_AREA', max_length=3,verbose_name="area")  # Field name made lowercase.
    lea_numorden = models.SmallIntegerField(db_column='LEA_NUMORDEN')  # Field name made lowercase.
    lea_tag = models.IntegerField(db_column='LEA_TAG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_ESTACIONES_AREAS'
        unique_together = (('lea_codigo', 'lea_area', 'lea_numorden'),)

    def __str__(self):
        return str(self.lea_codigo.le_codigo_txt) + " : " + str(self.lea_codigo.le_nombre)    
'''
class ListaRemotas(models.Model):
    lr_codigo = models.SmallIntegerField(db_column='LR_CODIGO', primary_key=True,verbose_name="Codigo",null=False)	  # Field name made lowercase.    
    lr_tipo_estacion = models.ForeignKey(TiposEstaciones,db_column="LR_TIPO_ESTACION", on_delete=models.DO_NOTHING,verbose_name="Tipo de estacion")	
    lr_nombre = models.CharField(db_column='LR_NOMBRE', max_length=30, blank=True, null=True,verbose_name="Nombre")	  # Field name made lowercase.
    lr_nombre_corto = models.CharField(db_column='LR_NOMBRE_CORTO', max_length=18, blank=True, null=True,verbose_name="Nombre corto")	  # Field name made lowercase.
    lr_estacion = models.ForeignKey(ListaEstaciones,db_column='LR_ESTACION',on_delete=models.CASCADE,verbose_name="Estacion")	  # Field name made lowercase.
    lr_codigo_txt = models.CharField(db_column='LR_CODIGO_TXT', max_length=5, blank=True, null=True,verbose_name="Codigo txt")	  # Field name made lowercase.
    lr_zona = models.ForeignKey(ListaZonas,on_delete=models.DO_NOTHING,db_column="LR_ZONA",verbose_name="Zona")	   
    lr_recid = models.IntegerField(db_column='LR_RECID',verbose_name="Recid",unique=True)	  # Field name made lowercase.
    lr_infoplus = models.BooleanField(db_column='LR_INFOPLUS', blank=True, verbose_name="Crear en SCADA")	  # Field name made lowercase.
    lr_remota_fisica = models.IntegerField(db_column='LR_REMOTA_FISICA', blank=True, null=True,verbose_name="Remota fisica")	  # Field name made lowercase.
    lr_tag_comunica = models.IntegerField(db_column='LR_TAG_COMUNICA', blank=True, null=True,verbose_name="Tag de comunicacióm")	  # Field name made lowercase.
    lr_saih_saica = models.BooleanField(db_column='LR_SAIH_SAICA', blank=True,verbose_name="Remota conjunta SAIH - SAICA")	  # Field name made lowercase.
    lr_conf_remota = models.BooleanField(db_column='LR_CONF_REMOTA', blank=True,verbose_name="Configurar remota")	  # Field name made lowercase.
    lr_remota_principal = models.BooleanField(db_column='LR_REMOTA_PRINCIPAL', blank=True, verbose_name="Es remota principal")	  # Field name made lowercase.
    lr_tiene_pluv = models.BooleanField(db_column='LR_TIENE_PLUV', blank=True, verbose_name="Tiene pluviometro")	  # Field name made lowercase.
    lr_equipo_mant = models.IntegerField(db_column='LR_EQUIPO_MANT', blank=True, null=True,verbose_name="Equipo mantenimiento")	  # Field name made lowercase.
    lr_num_orden = models.IntegerField(db_column='LR_NUM_ORDEN', blank=True, null=True,verbose_name="Numero de orden")	  # Field name made lowercase.    
    lr_rio = models.ForeignKey(Rios, on_delete=models.DO_NOTHING, db_column="LR_RIO",verbose_name="Rio",blank=True,null=True)	
   
    lr_empresa_suminis = models.IntegerField(db_column='LR_EMPRESA_SUMINIS', blank=True, null=True,verbose_name="Empresa suministradora")	  # Field name made lowercase.
    lr_num_poliza = models.CharField(db_column='LR_NUM_POLIZA', max_length=20, blank=True, null=True,verbose_name="Numero de poliza")	  # Field name made lowercase.
    lr_tipo_acceso = models.CharField(db_column='LR_TIPO_ACCESO', max_length=1, blank=True, null=True,verbose_name="Tipo de acceso")	  # Field name made lowercase.
    lr_desc_tipo_acceso = models.CharField(db_column='LR_DESC_TIPO_ACCESO', max_length=50, blank=True, null=True,verbose_name="Descripcion tipo acceso")	  # Field name made lowercase.
    lr_persona_contacto = models.IntegerField(db_column='LR_PERSONA_CONTACTO', blank=True, null=True,verbose_name="persona contacto")	  # Field name made lowercase.
    lr_observaciones = models.CharField(db_column='LR_OBSERVACIONES', max_length=400, blank=True, null=True,verbose_name="observaciones")	  # Field name made lowercase.
    lr_utm_huso = models.IntegerField(db_column='LR_UTM_HUSO', blank=True, null=True,verbose_name="Huso ")	  # Field name made lowercase.
    lr_utm_x = models.DecimalField(db_column='LR_UTM_X', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Utm x")	  # Field name made lowercase.
    lr_utm_y = models.DecimalField(db_column='LR_UTM_Y', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Utm y")	  # Field name made lowercase.
    lr_utm_z = models.DecimalField(db_column='LR_UTM_Z', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Utm z")	  # Field name made lowercase.
    lr_superficie = models.DecimalField(db_column='LR_SUPERFICIE', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Superficie")	  # Field name made lowercase.
    lr_longitud = models.DecimalField(db_column='LR_LONGITUD', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Longitud")	  # Field name made lowercase.
    lr_cota_estacion = models.DecimalField(db_column='LR_COTA_ESTACION', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Cota estacion")	  # Field name made lowercase.
    lr_cota_max = models.DecimalField(db_column='LR_COTA_MAX', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Cota máxima")	  # Field name made lowercase.
    lr_vol_max = models.DecimalField(db_column='LR_VOL_MAX', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Volumen máximo")	  # Field name made lowercase.
    lr_cota_men = models.DecimalField(db_column='LR_COTA_MEN', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Cota MEN del embalse")	  # Field name made lowercase.
    lr_cota_lecho = models.DecimalField(db_column='LR_COTA_LECHO', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Cota lecho del río")	  # Field name made lowercase.
    lr_cota_toma = models.DecimalField(db_column='LR_COTA_TOMA', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Cota toma del embalse")	  # Field name made lowercase.
    lr_tiempo_concentracion = models.DecimalField(db_column='LR_TIEMPO_CONCENTRACION', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Tiempo de concentracion")	  # Field name made lowercase.
    lr_cota_des_izq = models.DecimalField(db_column='LR_COTA_DES_IZQ', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="cota des izq")	  # Field name made lowercase.
    lr_cota_des_der = models.DecimalField(db_column='LR_COTA_DES_DER', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="cota des der")	  # Field name made lowercase.
    lr_cota_caseta = models.DecimalField(db_column='LR_COTA_CASETA', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="cota caseta")	  # Field name made lowercase.
    lr_caudal_diseno = models.DecimalField(db_column='LR_CAUDAL_DISENO', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="caudal diseno")	  # Field name made lowercase.
    lr_qmedio_emplaz = models.DecimalField(db_column='LR_QMEDIO_EMPLAZ', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="qmedio emplaz")	  # Field name made lowercase.
    lr_caudal_q2 = models.DecimalField(db_column='LR_CAUDAL_Q2', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="caudal q2")	  # Field name made lowercase.
    lr_caudal_q5 = models.DecimalField(db_column='LR_CAUDAL_Q5', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="caudal q5")	  # Field name made lowercase.
    lr_caudal_q10 = models.DecimalField(db_column='LR_CAUDAL_Q10', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="caudal q10")	  # Field name made lowercase.
    lr_caudal_q25 = models.DecimalField(db_column='LR_CAUDAL_Q25', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="caudal q25")	  # Field name made lowercase.
    lr_caudal_q100 = models.DecimalField(db_column='LR_CAUDAL_Q100', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="caudal q100")	  # Field name made lowercase.
    lr_caudal_q500 = models.DecimalField(db_column='LR_CAUDAL_Q500', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="caudal q500")	  # Field name made lowercase.
    lr_cota_cauce = models.DecimalField(db_column='LR_COTA_CAUCE', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="cota cauce")	  # Field name made lowercase.
    lr_cota_aliviadero = models.DecimalField(db_column='LR_COTA_ALIVIADERO', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="cota aliviadero")	  # Field name made lowercase.
    lr_cota_coronacion = models.DecimalField(db_column='LR_COTA_CORONACION', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="cota coronacion")	  # Field name made lowercase.
    lr_altura_cauce = models.DecimalField(db_column='LR_ALTURA_CAUCE', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="altura cauce")	  # Field name made lowercase.
    lr_altura_cimientos = models.DecimalField(db_column='LR_ALTURA_CIMIENTOS', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="altura cimientos")	  # Field name made lowercase.
    lr_cota_min_epl = models.DecimalField(db_column='LR_COTA_MIN_EPL', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="cota_min epl")	  # Field name made lowercase.
    lr_vol_min_epl = models.DecimalField(db_column='LR_VOL_MIN_EPL', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="vol_min epl")	  # Field name made lowercase.
    lr_cota_nmn = models.DecimalField(db_column='LR_COTA_NMN', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="cota nmn")	  # Field name made lowercase.
    lr_vol_nmn = models.DecimalField(db_column='LR_VOL_NMN', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="vol nmn")	  # Field name made lowercase.
    lr_cota_nap = models.DecimalField(db_column='LR_COTA_NAP', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="cota nap")	  # Field name made lowercase.
    lr_vol_nap = models.DecimalField(db_column='LR_VOL_NAP', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="vol nap")	  # Field name made lowercase.
    lr_caudal_nap = models.DecimalField(db_column='LR_CAUDAL_NAP', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="caudal nap")	  # Field name made lowercase.
    lr_period_nap = models.DecimalField(db_column='LR_PERIOD_NAP', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="period nap")	  # Field name made lowercase.
    lr_cota_nae = models.DecimalField(db_column='LR_COTA_NAE', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="cota nae")	  # Field name made lowercase.
    lr_vol_nae = models.DecimalField(db_column='LR_VOL_NAE', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="vol nae")	  # Field name made lowercase.
    lr_caudal_nae = models.DecimalField(db_column='LR_CAUDAL_NAE', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="caudal nae")	  # Field name made lowercase.
    lr_period_nae = models.DecimalField(db_column='LR_PERIOD_NAE', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="period nae")	  # Field name made lowercase.
    lr_escala_max = models.DecimalField(db_column='LR_ESCALA_MAX', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="escala max")	  # Field name made lowercase.
    lr_capacidad_max = models.DecimalField(db_column='LR_CAPACIDAD_MAX', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="capacidad max")	  # Field name made lowercase.
    lr_vol_util = models.DecimalField(db_column='LR_VOL_UTIL', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="vol util")	  # Field name made lowercase.
    lr_p24h_r2 = models.DecimalField(db_column='LR_P24H_R2', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="p24h r2")	  # Field name made lowercase.
    lr_p24h_r5 = models.DecimalField(db_column='LR_P24H_R5', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="p24h r5")	  # Field name made lowercase.
    lr_p24h_r10 = models.DecimalField(db_column='LR_P24H_R10', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="p24h r10")	  # Field name made lowercase.
    lr_p24h_r25 = models.DecimalField(db_column='LR_P24H_R25', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="p24h r25")	  # Field name made lowercase.
    lr_p24h_r100 = models.DecimalField(db_column='LR_P24H_R100', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="p24h r100")	  # Field name made lowercase.
    lr_p24h_r500 = models.DecimalField(db_column='LR_P24H_R500', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="p24h r500")	  # Field name made lowercase.
    lr_falta = models.DateTimeField(db_column='LR_FALTA', blank=True, null=True,verbose_name="Fecha de alta")	  # Field name made lowercase.
    lr_fmodif = models.DateTimeField(db_column='LR_FMODIF', blank=True, null=True,verbose_name="Fecha de modificacion")	  # Field name made lowercase.
    lr_fbaja = models.DateTimeField(db_column='LR_FBAJA', blank=True, null=True,verbose_name="Fecha de baja")	  # Field name made lowercase.
    lr_vol_min_util = models.DecimalField(db_column='LR_VOL_MIN_UTIL', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="vol_min util")	  # Field name made lowercase.
    lr_coef_erep = models.DecimalField(db_column='LR_COEF_EREP', max_digits=12, decimal_places=4, blank=True, null=True,verbose_name="coef erep")	  # Field name made lowercase.
    lr_caudal_punta = models.DecimalField(db_column='LR_CAUDAL_PUNTA', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="caudal punta")	  # Field name made lowercase.
    lr_fcaudal_punta = models.DateTimeField(db_column='LR_FCAUDAL_PUNTA', blank=True, null=True,verbose_name="fcaudal punta")	  # Field name made lowercase.
    lr_resguardo_nmn = models.DecimalField(db_column='LR_RESGUARDO_NMN', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="resguardo nmn")	  # Field name made lowercase.
    lr_superficie_nmn = models.DecimalField(db_column='LR_SUPERFICIE_NMN', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="superficie nmn")	  # Field name made lowercase.
    lr_longitud_emb = models.DecimalField(db_column='LR_LONGITUD_EMB', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="longitud emb")	  # Field name made lowercase.
    lr_longitud_coronacion = models.DecimalField(db_column='LR_LONGITUD_CORONACION', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="longitud coronacion")	  # Field name made lowercase.
    lr_hipotesis_qnap = models.CharField(db_column='LR_HIPOTESIS_QNAP', max_length=20, blank=True, null=True,verbose_name="hipotesis qnap")	  # Field name made lowercase.
    lr_hipotesis_qnae = models.CharField(db_column='LR_HIPOTESIS_QNAE', max_length=20, blank=True, null=True,verbose_name="hipotesis qnae")	  # Field name made lowercase.
    lr_caudal_ecologico = models.DecimalField(db_column='LR_CAUDAL_ECOLOGICO', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Caudal ecologico")	  # Field name made lowercase.
    lr_concesion = models.DecimalField(db_column='LR_CONCESION', max_digits=12, decimal_places=2, blank=True, null=True,verbose_name="Concesion")	  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_REMOTAS'
        ordering=["lr_estacion"]
        verbose_name="Remota"
        verbose_name_plural="Remotas"

    def __str__(self):
        return str(self.lr_codigo_txt) + " : " + str(self.lr_nombre)

    def save(self,*args,force_insert=False, force_update=False, using=None, update_fields=None):
        ultimo_id =  ListaRemotas.objects.aggregate(Max('lr_codigo'))['lr_codigo__max']
        ultimo_recid_hist = models_hist.ListaRemotas_H.objects.aggregate(Max('lr_codigo'))['lr_codigo__max']                
        ultimo_recid_gest = ListaRemotas.objects.aggregate(Max('lr_recid'))['lr_recid__max']                
        pp(self.__dict__)
        if not self.lr_codigo :
            pp("INSERT")
            self.lr_codigo=ultimo_id+1        
            self.lr_recid=max(ultimo_recid_gest,ultimo_recid_hist) +1
        self.lr_codigo_txt=self.lr_estacion.le_codigo_txt+"_"
        self.lr_tipo_estacion=self.lr_estacion.le_tipo_estacion
        self.lr_zona=self.lr_estacion.le_zona
        self.lr_rio=self.lr_estacion.le_rio
        super().save(force_insert,force_update,using,update_fields)


class ListaRemotasConf(models.Model):
    lrc_codigo = models.OneToOneField(ListaRemotas,db_column='LRC_CODIGO',on_delete=models.DO_NOTHING, primary_key=True,verbose_name="Codigo")	  # Field name made lowercase.
    lrc_num_remota = models.IntegerField(db_column='LRC_NUM_REMOTA', blank=True, null=True,verbose_name="Numero remota")	  # Field name made lowercase.
    lrc_zona_com = models.IntegerField(db_column='LRC_ZONA_COM', blank=True, null=True,verbose_name="Zona de comunicaciones")	  # Field name made lowercase.
    lrc_direccion_ip = models.CharField(db_column='LRC_DIRECCION_IP', max_length=20, blank=True, null=True,verbose_name="Direccion IP")	  # Field name made lowercase.
    lrc_modelo = models.CharField(db_column='LRC_MODELO', max_length=5, blank=True, null=True,verbose_name="Modelo")	  # Field name made lowercase.
    lrc_max_tarjetas = models.IntegerField(db_column='LRC_MAX_TARJETAS', blank=True, null=True,verbose_name="Max tarjetas")	  # Field name made lowercase.
    lrc_max_factores = models.IntegerField(db_column='LRC_MAX_FACTORES', blank=True, null=True,verbose_name="Max factores")	  # Field name made lowercase.
    lrc_max_tags = models.IntegerField(db_column='LRC_MAX_TAGS', blank=True, null=True,verbose_name="Max tags")	  # Field name made lowercase.
    lrc_max_ent_digital = models.IntegerField(db_column='LRC_MAX_ENT_DIGITAL', blank=True, null=True,verbose_name="Max ent digital")	  # Field name made lowercase.
    lrc_max_ent_analog = models.IntegerField(db_column='LRC_MAX_ENT_ANALOG', blank=True, null=True,verbose_name="Max ent analog")	  # Field name made lowercase.
    lrc_max_sal_analog = models.IntegerField(db_column='LRC_MAX_SAL_ANALOG', blank=True, null=True,verbose_name="Max sal analog")	  # Field name made lowercase.
    lrc_max_sal_digital = models.IntegerField(db_column='LRC_MAX_SAL_DIGITAL', blank=True, null=True,verbose_name="Max sal digital")	  # Field name made lowercase.
    lrc_max_ent_binarias = models.IntegerField(db_column='LRC_MAX_ENT_BINARIAS', blank=True, null=True,verbose_name="Max ent binarias")	  # Field name made lowercase.
    lrc_max_ent_grays = models.IntegerField(db_column='LRC_MAX_ENT_GRAYS', blank=True, null=True,verbose_name="Max ent grays")	  # Field name made lowercase.
    lrc_max_ent_bnc = models.IntegerField(db_column='LRC_MAX_ENT_BNC', blank=True, null=True,verbose_name="Max ent bnc")	  # Field name made lowercase.
    lrc_max_ent_digdobles = models.IntegerField(db_column='LRC_MAX_ENT_DIGDOBLES', blank=True, null=True,verbose_name="Max ent digdobles")	  # Field name made lowercase.
    lrc_max_contadores = models.IntegerField(db_column='LRC_MAX_CONTADORES', blank=True, null=True,verbose_name="Max contadores")	  # Field name made lowercase.
    lrc_max_db = models.IntegerField(db_column='LRC_MAX_DB', blank=True, null=True,verbose_name="Max db")	  # Field name made lowercase.
    lrc_max_sizedb = models.IntegerField(db_column='LRC_MAX_SIZEDB', blank=True, null=True,verbose_name="Max sizedb")	  # Field name made lowercase.
    lrc_max_tomamuestras = models.IntegerField(db_column='LRC_MAX_TOMAMUESTRAS', blank=True, null=True,verbose_name="Max tomamuestras")	  # Field name made lowercase.
    lrc_max_enclavamientos = models.IntegerField(db_column='LRC_MAX_ENCLAVAMIENTOS', blank=True, null=True,verbose_name="Max enclavamientos")	  # Field name made lowercase.
    lrc_max_rebotes = models.IntegerField(db_column='LRC_MAX_REBOTES', blank=True, null=True,verbose_name="Max rebotes")	  # Field name made lowercase.
    lrc_temp_inhibicion = models.IntegerField(db_column='LRC_TEMP_INHIBICION', blank=True, null=True,verbose_name="Tiempo inhibicion")	  # Field name made lowercase.
    lrc_observaciones = models.CharField(db_column='LRC_OBSERVACIONES', max_length=200, blank=True, null=True,verbose_name="Observaciones")	  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_REMOTAS_CONF'
        verbose_name="Configuración remota"
        verbose_name_plural="Configuraciones remota"

    def __str__(self):
        return str(self.lrc_codigo.lr_codigo_txt) + " : " + str(self.lrc_codigo.lr_nombre) 




class ListaRemotasTarjetas(models.Model):
    pk = models.CompositePrimaryKey('lrt_codigo', 'lrt_nombre')
    lrt_codigo = models.ForeignKey(ListaRemotas,db_column='LRT_CODIGO', on_delete=models.DO_NOTHING,verbose_name="Codigo de la remota")  # Field name made lowercase. The composite primary key (LRT_CODIGO, LRT_NOMBRE,found, that is not supported. The first column is selected.
    lrt_nombre = models.CharField(db_column='LRT_NOMBRE', max_length=6,verbose_name="Nombre", blank='True')  # Field name made lowercase.
    lrt_modelo = models.CharField(db_column='LRT_MODELO', max_length=20, blank=True, null=True,verbose_name="Modelo")  # Field name made lowercase.
    lrt_tipo = models.ForeignKey(TiposTarjetas,on_delete=models.DO_NOTHING,db_column='LRT_TIPO', blank=True, null=True,verbose_name="Tipo")  # Field name made lowercase.
    lr_dir_control = models.CharField(db_column='LRT_DIR_CONTROL', max_length=4, blank=True, null=True,verbose_name="Dirección de control")	  # Field name made lowercase.
    lr_dir_datos = models.CharField(db_column='LRT_DIR_DATOS', max_length=4, blank=True, null=True,verbose_name="Dirección de datos")	  # Field name made lowercase.
    lrt_numdatos = models.IntegerField(db_column='LRT_NUMDATOS', blank=True, null=True,verbose_name="Numero de datos")  # Field name made lowercase.
    lrt_signo = models.SmallIntegerField(db_column='LRT_SIGNO', blank=True, null=True,verbose_name="Signo",choices={0:"+",1:"-"})  # Field name made lowercase.
    lr_dir_ip = models.CharField(db_column='LRT_DIR_IP', max_length=20, blank=True, null=True,verbose_name="Dirección IP")	  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_REMOTAS_TARJETAS'
        unique_together = (('lrt_codigo', 'lrt_nombre'),)
        verbose_name="Tarjeta"
        verbose_name_plural="Tarjetas"

    
    def __str__(self):
        return str(self.lrt_nombre)   

    def _do_update(self, base_qs, using, pk_val, values, update_fields, forced_update):
        filtered = base_qs.filter(lrt_codigo=pk_val[0],lrt_nombre=pk_val[1])
        if not values:
            return update_fields is not None or filtered.exists()
        if self._meta.select_on_save and not forced_update:
            return (
                filtered.exists() and (filtered._update(values) > 0 or filtered.exists())
            )
        return filtered._update(values) > 0

    def delete(self, using=None, keep_parents=False):
        if not self._is_pk_set():
            raise ValueError(
                "%s object can't be deleted because its %s attribute is set "
                "to None." % (self._meta.object_name, self._meta.pk.attname)
            )
        using = using or router.db_for_write(self.__class__, instance=self)
        collector = CompositeCollector(using=using, origin=self)
        collector.collect([self], keep_parents=keep_parents)
        return collector.delete()
     
        
class ListaSenales(models.Model):
    ls_tag = models.IntegerField(db_column='LS_TAG', primary_key=True,editable=False,verbose_name="Id",null=False)  # Field name made lowercase.
    ls_descripcion = models.CharField(db_column='LS_DESCRIPCION', max_length=50, blank=True, null=True,verbose_name="Descripcion")   # Field name made lowercase.
    ls_tag_txt = models.CharField(db_column='LS_TAG_TXT', max_length=16,verbose_name="Codigo",unique=True)   # Field name made lowercase.
    ls_remota = models.ForeignKey(ListaRemotas, on_delete=models.DO_NOTHING,db_column="ls_remota",verbose_name="Remota",null=True) 
    ls_num_senal = models.IntegerField(db_column='LS_NUM_SENAL', blank=True, null=True,verbose_name="Nmero de señal")   # Field name made lowercase.
    ls_clase_senal = models.CharField(db_column='LS_CLASE_SENAL', max_length=5, blank=True, null=True,choices={"CONT":"Continua","COMUN":"Comun","DIGIS":"Digital"},verbose_name="Clase de señal")   # Field name made lowercase.
    ls_tipo_senal = models.ForeignKey(TiposSenales, db_column='LS_TIPO_SENAL', on_delete=models.DO_NOTHING,verbose_name="Tipo de señal",null=True)   # Field name made lowercase.
    ls_tipo_alarma = models.ForeignKey('TiposAlarmas', db_column='LS_TIPO_ALARMA', on_delete=models.DO_NOTHING,verbose_name="Tipo de alarma")   # Field name made lowercase.
    ls_naturaleza = models.ForeignKey('NaturalezaSenales', db_column='LS_NATURALEZA', on_delete=models.DO_NOTHING,verbose_name="Naturaleza")   # Field name made lowercase.
    ls_recid = models.IntegerField(db_column='LS_RECID', blank=True, null=True,verbose_name="Id historica", unique=True)   # Field name made lowercase.
    ls_recid_ch = models.IntegerField(db_column='LS_RECID_CH', blank=True, null=True,verbose_name="recid_ch")   # Field name made lowercase.
    ls_origen = models.CharField(db_column='LS_ORIGEN', max_length=10,choices=origenes,verbose_name="Origen")   # Field name made lowercase.
    ls_marca_cons = models.BooleanField (db_column='LS_MARCA_CONS', blank=True,verbose_name="Marca consolidacion")   # Field name made lowercase.
    ls_tipo_consolidacion = models.ForeignKey(TiposConsolidacion, db_column='LS_TIPO_CONSOLIDACION', on_delete=models.DO_NOTHING,verbose_name="Tipo consolidacion")   # Field name made lowercase.
    ls_tag_cons_1 = models.IntegerField(db_column='LS_TAG_CONS_1', blank=True, null=True,verbose_name="tag_cons_1")   # Field name made lowercase.
    ls_tag_cons_2 = models.IntegerField(db_column='LS_TAG_CONS_2', blank=True, null=True,verbose_name="tag_cons_2")   # Field name made lowercase.
    ls_hora_cons = models.TimeField(db_column='LS_HORA_CONS', max_length=5, blank=True, null=True, editable=False,verbose_name="Hora consolidacion")  #CHARFIELD # Field name made lowercase.
    ls_curvaref = models.SmallIntegerField(db_column='LS_CURVAREF', blank=True,verbose_name="curvaref")   # Field name made lowercase.
    ls_conf_remota = models.BooleanField(db_column='LS_CONF_REMOTA', blank=True,verbose_name="conf_remota")   # Field name made lowercase.
    ls_conf_scada = models.BooleanField(db_column='LS_CONF_SCADA', blank=True,verbose_name="conf_scada")   # Field name made lowercase.
    ls_conf_historia = models.BooleanField(db_column='LS_CONF_HISTORIA', blank=True,verbose_name="conf_historia")   # Field name made lowercase.
    ls_min_grafico = models.FloatField(db_column='LS_MIN_GRAFICO', blank=True, null=True,verbose_name="Min_grafico")   # Field name made lowercase.
    ls_max_grafico = models.FloatField(db_column='LS_MAX_GRAFICO', blank=True, null=True,verbose_name="Max_grafico")   # Field name made lowercase.
    ls_tiempo_grafico = models.CharField(db_column='LS_TIEMPO_GRAFICO', max_length=15, blank=True, null=True,verbose_name="tiempo_grafico")   # Field name made lowercase.
    ls_fuente = models.CharField(db_column='LS_FUENTE', max_length=5, blank=True, null=True,choices=
        {"ROEAM":"ROEAM","SAIH":"SAIH","DME-E":"DME-E","INM":"Meteorologia","DME":"DME","PLUVM":"Pluviometro"}
        ,verbose_name="Fuente")  # Field name made lowercase.
    ls_factor_manual = models.FloatField(db_column='LS_FACTOR_MANUAL', blank=True, null=True,verbose_name="Factor manual")   # Field name made lowercase.
    ls_columna = models.IntegerField(db_column='LS_COLUMNA', blank=True, null=True,verbose_name="columna")   # Field name made lowercase.
    ls_orden = models.IntegerField(db_column='LS_ORDEN', blank=True, null=True,verbose_name="orden")   # Field name made lowercase.
    ls_falta = models.DateTimeField(db_column='LS_FALTA', blank=True, null=True, editable=False,verbose_name="falta")   # Field name made lowercase.
    ls_fmodif = models.DateTimeField(db_column='LS_FMODIF', blank=True, null=True,editable=False,verbose_name="fmodif")   # Field name made lowercase.
    ls_fbaja = models.DateTimeField(db_column='LS_FBAJA', blank=True, null=True,editable=False,verbose_name="fbaja")   # Field name made lowercase.
    ls_ver_web = models.BooleanField(db_column='LS_VER_WEB', blank=True,verbose_name="ver_web")   # Field name made lowercase.
    ls_ver_intranet = models.BooleanField(db_column='LS_VER_INTRANET', blank=True,verbose_name="ver_intranet")   # Field name made lowercase.
    ls_ver_pda = models.BooleanField(db_column='LS_VER_PDA', blank=True,verbose_name="ver_pda")   # Field name made lowercase.
    ls_fews = models.BooleanField(db_column='LS_FEWS', blank=True,verbose_name="Fews")   # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_SENALES'
        ordering=["ls_remota__lr_estacion","ls_tipo_senal__ts_orden"]
        verbose_name="Señal"
        verbose_name_plural="Señales"

    def __str__(self):
        return str(self.ls_tag_txt) + " : " + str(self.ls_descripcion)


class ListaSenalesAnalogicas(models.Model):
    lsa_tag = models.OneToOneField(ListaSenales,db_column='LSA_TAG',on_delete=models.DO_NOTHING,primary_key=True,verbose_name="Codigo")  # Field name made lowercase.
    lsa_unid_ing = models.ForeignKey(UnidadesIngenieria, on_delete=models.DO_NOTHING,db_column='LSA_UNID_ING', max_length=10, blank=True, null=True,verbose_name="Unidad")  # Field name made lowercase.
    lsa_digitos_enteros = models.SmallIntegerField(db_column='LSA_DIGITOS_ENTEROS', blank=True, null=True,verbose_name="Digitos enteros")  # Field name made lowercase.
    lsa_digitos_decimales = models.SmallIntegerField(db_column='LSA_DIGITOS_DECIMALES', blank=True, null=True,verbose_name="Digitos decimales")  # Field name made lowercase.
    lsa_factor_scada = models.CharField(db_column='LSA_FACTOR_SCADA', max_length=20, blank=True, null=True,verbose_name="Factor scada")  # Field name made lowercase.
    lsa_tipo_almacenamiento = models.ForeignKey(TiposAlmacenamiento,db_column='LSA_TIPO_ALMACENAMIENTO', max_length=5, blank=True, null=True, on_delete=models.DO_NOTHING,verbose_name="Tipo almacenamiento")  # Field name made lowercase.
    lsa_minimo = models.FloatField(db_column='LSA_MINIMO', blank=True, null=True,verbose_name="Valor minimo")  # Field name made lowercase.
    lsa_maximo = models.FloatField(db_column='LSA_MAXIMO', blank=True, null=True,verbose_name="Valor maximo")  # Field name made lowercase.
    lsa_lim_alto_alto_alto = models.FloatField(db_column='LSA_LIM_ALTO_ALTO_ALTO', blank=True, null=True,verbose_name="Limite alerta")  # Field name made lowercase.
    lsa_lim_alto_alto = models.FloatField(db_column='LSA_LIM_ALTO_ALTO', blank=True, null=True,verbose_name="Limite prealerta")  # Field name made lowercase.
    lsa_lim_alto = models.FloatField(db_column='LSA_LIM_ALTO', blank=True, null=True,verbose_name="Limite activacion")  # Field name made lowercase.
    lsa_lim_bajo = models.FloatField(db_column='LSA_LIM_BAJO', blank=True, null=True,verbose_name="Limite bajo")  # Field name made lowercase.
    lsa_lim_bajo_bajo = models.FloatField(db_column='LSA_LIM_BAJO_BAJO', blank=True, null=True,verbose_name="Limite muy bajo")  # Field name made lowercase.
    lsa_valor_histeresis = models.FloatField(db_column='LSA_VALOR_HISTERESIS', blank=True, null=True,verbose_name="Histeresis")  # Field name made lowercase.
    lsa_lim_neg_rampa = models.FloatField(db_column='LSA_LIM_NEG_RAMPA', blank=True, null=True,verbose_name="Valor rampa negativa")  # Field name made lowercase.
    lsa_lim_pos_rampa = models.FloatField(db_column='LSA_LIM_POS_RAMPA', blank=True, null=True,verbose_name="Valor rampa positiva")  # Field name made lowercase.
    lsa_lim_rampa_histeresis = models.FloatField(db_column='LSA_LIM_RAMPA_HISTERESIS', blank=True, null=True,verbose_name="Valor histeresis negativa")  # Field name made lowercase.
    lsa_gravedad_aaa = models.CharField(db_column='LSA_GRAVEDAD_AAA', max_length=5, blank=True, null=True,choices=gravedades,verbose_name="Gravedad alerta")  # Field name made lowercase.
    lsa_gravedad_aa = models.CharField(db_column='LSA_GRAVEDAD_AA', max_length=5, blank=True, null=True,choices=gravedades,verbose_name="Gravedad prealerta")  # Field name made lowercase.
    lsa_gravedad_a = models.CharField(db_column='LSA_GRAVEDAD_A', max_length=5, blank=True, null=True,choices=gravedades,verbose_name="Gravedad activacion")  # Field name made lowercase.
    lsa_gravedad_b = models.CharField(db_column='LSA_GRAVEDAD_B', max_length=5, blank=True, null=True,choices=gravedades,verbose_name="Gravedad alarma bajo")  # Field name made lowercase.
    lsa_gravedad_bb = models.CharField(db_column='LSA_GRAVEDAD_BB', max_length=5, blank=True, null=True,choices=gravedades,verbose_name="Gravedad alarma muy bajo")  # Field name made lowercase.
    lsa_gravedad_rn = models.CharField(db_column='LSA_GRAVEDAD_RN', max_length=5, blank=True, null=True,choices=gravedades,verbose_name="Gravedad alarma rampa negativa")  # Field name made lowercase.
    lsa_gravedad_rp = models.CharField(db_column='LSA_GRAVEDAD_RP', max_length=5, blank=True, null=True,choices=gravedades,verbose_name="Gravedad alarma rampa positiva")  # Field name made lowercase.
    lsa_ver_web_a = models.BooleanField(db_column='LSA_VER_WEB_A',verbose_name="Ver activacion en la web")  # Field name made lowercase.
    lsa_ver_web_aa = models.BooleanField(db_column='LSA_VER_WEB_AA',verbose_name="Ver prealerta en la web")  # Field name made lowercase.
    lsa_ver_web_aaa = models.BooleanField(db_column='LSA_VER_WEB_AAA',verbose_name="Ver alerta en la web")  # Field name made lowercase.
    lsa_ver_intranet_a = models.BooleanField(db_column='LSA_VER_INTRANET_A',verbose_name="Ver activacion en la intranet")  # Field name made lowercase.
    lsa_ver_intranet_aa = models.BooleanField(db_column='LSA_VER_INTRANET_AA',verbose_name="Ver prealerta en la intranet")  # Field name made lowercase.
    lsa_ver_intranet_aaa = models.BooleanField(db_column='LSA_VER_INTRANET_AAA',verbose_name="Ver alerta en la intranet")  # Field name made lowercase.
    lsa_ver_pda_a = models.BooleanField(db_column='LSA_VER_PDA_A',verbose_name="Ver activacion en PDA")  # Field name made lowercase.
    lsa_ver_pda_aa = models.BooleanField(db_column='LSA_VER_PDA_AA',verbose_name="Ver prealerta en PDA")  # Field name made lowercase.
    lsa_ver_pda_aaa = models.BooleanField(db_column='LSA_VER_PDA_AAA',verbose_name="Ver alerta en PDA")  # Field name made lowercase.
    lsa_lim_tv = models.SmallIntegerField(db_column='LSA_LIM_TV', blank=True, null=True,verbose_name="Limites temporalmente variables")  # Field name made lowercase.
    lsa_criterio_tv = models.CharField(db_column='LSA_CRITERIO_TV', max_length=10, blank=True, null=True,verbose_name="Criterio temporalmente variable")  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'LISTA_SENALES_ANALOGICAS'
        verbose_name="Señal analógica"
        verbose_name_plural="Señales analógicas"

    def __str__(self):
        return str(self.lsa_tag.ls_tag_txt) + " : " + str(self.lsa_tag.ls_descripcion)


class ListaSenalesDigdobles(models.Model):
    ldd_tag = models.OneToOneField(ListaSenales,on_delete=models.PROTECT,db_column='LDD_TAG', primary_key=True,verbose_name="Codigo señal")  # Field name made lowercase.
    ldd_texto_valor_0 = models.CharField(db_column='LDD_TEXTO_VALOR_0', max_length=24, blank=True, null=True,verbose_name="Texto valor 0",choices=estado_digital_0)  # Field name made lowercase.
    ldd_texto_valor_1 = models.CharField(db_column='LDD_TEXTO_VALOR_1', max_length=24, blank=True, null=True,verbose_name="Texto valor 1",choices=estado_digital_0)  # Field name made lowercase.
    ldd_texto_valor_2 = models.CharField(db_column='LDD_TEXTO_VALOR_2', max_length=24, blank=True, null=True,verbose_name="Texto valor 2",choices=estado_digital_0)  # Field name made lowercase.
    ldd_texto_valor_3 = models.CharField(db_column='LDD_TEXTO_VALOR_3', max_length=24, blank=True, null=True,verbose_name="Texto valor 3",choices=estado_digital_0)  # Field name made lowercase.
    ldd_es_alarma = models.BooleanField(db_column='LDD_ES_ALARMA', blank=True, verbose_name="Es alarma")  # Field name made lowercase.
    ldd_valor_alarma = models.SmallIntegerField(db_column='LDD_VALOR_ALARMA', blank=True, null=True,verbose_name="Valor alarma")  # Field name made lowercase.
    ldd_gravedad = models.CharField(db_column='LDD_GRAVEDAD', max_length=5, blank=True, null=True,verbose_name="Gravedad")  # Field name made lowercase.
    ldd_digital1 = models.IntegerField(db_column='LDD_DIGITAL1', blank=True, null=True)  # Field name made lowercase.
    ldd_digital2 = models.IntegerField(db_column='LDD_DIGITAL2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_SENALES_DIGDOBLES'
        verbose_name='Señal digital doble'
        verbose_name_plural='Señales digitales dobles'

    def __str__(self):
        return str(self.ldd_tag)    

class ListaSenalesDigitales(models.Model):
    lsd_tag = models.OneToOneField(ListaSenales,on_delete=models.PROTECT,db_column='LSD_TAG', primary_key=True,verbose_name="Codigo señal")  # Field name made lowercase.
    lsd_texto_valor_0 = models.CharField(db_column='LSD_TEXTO_VALOR_0', max_length=24, blank=True, null=True,verbose_name="Texto valor 0",choices=estado_digital_0)  # Field name made lowercase.
    lsd_texto_valor_1 = models.CharField(db_column='LSD_TEXTO_VALOR_1', max_length=24, blank=True, null=True,verbose_name="Texto valor 1",choices=estado_digital_1)  # Field name made lowercase.
    lsd_es_alarma = models.BooleanField(db_column='LSD_ES_ALARMA', blank=True, verbose_name="Es alarma")  # Field name made lowercase.
    lsd_valor_activacion = models.SmallIntegerField(db_column='LSD_VALOR_ACTIVACION', blank=True, null=True,verbose_name="Valor de activación")  # Field name made lowercase.
    lsd_gravedad = models.CharField(db_column='LSD_GRAVEDAD', max_length=5, blank=True, null=True,verbose_name="Gravedad")  # Field name made lowercase.
    lsd_logica_negativa = models.BooleanField(db_column='LSD_LOGICA_NEGATIVA', blank=True,verbose_name="Logica Negativa")  # Field name made lowercase.
    lsd_tmp_proceso = models.CharField(db_column='LSD_TMP_PROCESO', max_length=12, blank=True, null=True,verbose_name="Tiempo de proceso")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_SENALES_DIGITALES'
        verbose_name='Señal digital'
        verbose_name_plural='Señales digitales'

    def __str__(self):
        return str(self.lsd_tag)    

class ListaSenalesCalculadas(models.Model):
    pk=models.CompositePrimaryKey('lsc_tag','lsc_fecha_inicio')
    lsc_tag = models.ForeignKey(ListaSenales,on_delete=models.DO_NOTHING,db_column='LSC_TAG',verbose_name='Id')  # Field name made lowercase. The composite primary key (LSC_TAG, LSC_FECHA_INICIO) found, that is not supported. The first column is selected.
    lsc_fecha_inicio = models.DateTimeField(db_column='LSC_FECHA_INICIO',verbose_name="Fecha de inicio")  # Field name made lowercase.
    lsc_fecha_fin = models.DateTimeField(db_column='LSC_FECHA_FIN', blank=True, null=True,verbose_name="Fecha de finalización")  # Field name made lowercase.
    lsc_version = models.CharField(db_column='LSC_VERSION', max_length=50, blank=True, null=True,verbose_name="Versión")  # Field name made lowercase.
    lsc_fichero = models.CharField(db_column='LSC_FICHERO', max_length=25, blank=True, null=True,verbose_name="Fichero")  # Field name made lowercase.
    lsc_tipo_calculo = models.SmallIntegerField(db_column='LSC_TIPO_CALCULO', blank=True, null=True,verbose_name="Tipo de cálculo") #CHOICES???? NO SE DONDE ESTÁN # Field name made lowercase.
    lsc_tag_campo = models.ForeignKey(ListaSenales,on_delete=models.DO_NOTHING,db_column='LSC_TAG_CAMPO',related_name="campo1")#, blank=True, null=True)  # Field name made lowercase.
    lsc_tag_campo_2 = models.ForeignKey(ListaSenales,on_delete=models.DO_NOTHING,db_column='LSC_TAG_CAMPO_2', blank=True, null=True,related_name="campo2")  # Field name made lowercase.
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
        verbose_name="Cálculo señal"
        verbose_name_plural="Cálculos señal"

    def __str__(self):
        return f"{self.lsc_tag}, desde el {self.lsc_fecha_inicio}"

    
class ListaSenalesLimitevariables(models.Model):    
    pk = models.CompositePrimaryKey('lsl_tag', 'lsl_alarma','lsl_mes')
    lsl_tag = models.ForeignKey(ListaSenales,on_delete=models.DO_NOTHING,db_column='LSL_TAG',verbose_name='Id')  # Field name made lowercase. The composite primary key (LSL_TAG, LSL_ALARMA, LSL_DIA, LSL_MES) found, that is not supported. The first column is selected.
    lsl_alarma = models.CharField(db_column='LSL_ALARMA', max_length=4,choices=niveles_alarmas,verbose_name='Alarma')  # Field name made lowercase.
    lsl_dia = models.SmallIntegerField(db_column='LSL_DIA',default=1,verbose_name='Dia')  # Field name made lowercase.
    lsl_mes = models.SmallIntegerField(db_column='LSL_MES',verbose_name='Mes')  # Field name made lowercase.
    lsl_valor = models.FloatField(db_column='LSL_VALOR', blank=True, null=True,verbose_name='Valor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_SENALES_LIMITEVARIABLES'
        unique_together = (('lsl_tag', 'lsl_alarma', 'lsl_dia', 'lsl_mes'),)    
        verbose_name='Limite variable'
        verbose_name_plural='Limites variables'
    
    def _do_update(self, base_qs, using, pk_val, values, update_fields, forced_update):
        filtered = base_qs.filter(lsl_tag=pk_val[0],lsl_alarma=pk_val[1],lsl_mes=pk_val[2])
        if not values:
            return update_fields is not None or filtered.exists()
        if self._meta.select_on_save and not forced_update:
            return (
                filtered.exists() and (filtered._update(values) > 0 or filtered.exists())
            )
        return filtered._update(values) > 0

    def delete(self, using=None, keep_parents=False):
        if not self._is_pk_set():
            raise ValueError(
                "%s object can't be deleted because its %s attribute is set "
                "to None." % (self._meta.object_name, self._meta.pk.attname)
            )
        using = using or router.db_for_write(self.__class__, instance=self)
        collector = CompositeCollector(using=using, origin=self)
        collector.collect([self], keep_parents=keep_parents)
        return collector.delete()

'''Órdenes
    No están ni en la históric ani en la intranet
    Solo se pasan al scada
    Se ponen por si se quieren hacer cambios en el SCADA (gravándolos a través del antiguo gestor)
'''
class ListaOrdenes(models.Model):
    lo_tag = models.IntegerField(db_column='LO_TAG', primary_key=True,verbose_name="Id")  # Field name made lowercase.
    lo_descripcion = models.CharField(db_column='LO_DESCRIPCION', max_length=50, blank=True, null=True,verbose_name="Descripcion")  # Field name made lowercase.
    lo_tag_txt = models.CharField(db_column='LO_TAG_TXT', max_length=16,verbose_name="Codigo")  # Field name made lowercase.
    lo_remota = models.ForeignKey(ListaRemotas,on_delete=models.DO_NOTHING,db_column='LO_REMOTA',verbose_name="Remota")  # Field name made lowercase.
    lo_num_senal = models.IntegerField(db_column='LO_NUM_SENAL', blank=True, null=True,verbose_name="Numero de señal")  # Field name made lowercase.
    lo_tipo_orden = models.CharField(db_column='LO_TIPO_ORDEN', max_length=10, blank=True, null=True,verbose_name="Tipo de orden")  # Field name made lowercase.
    lo_naturaleza = models.SmallIntegerField(db_column='LO_NATURALEZA', blank=True, null=True,verbose_name="Naturaleza")  # Field name made lowercase.
    lo_conf_remota = models.SmallIntegerField(db_column='LO_CONF_REMOTA', blank=True,verbose_name="Configurar en remota")  # Field name made lowercase.
    lo_conf_scada = models.SmallIntegerField(db_column='LO_CONF_SCADA', blank=True, verbose_name="Configurar en Scada")  # Field name made lowercase.
    lo_conf_historia = models.SmallIntegerField(db_column='LO_CONF_HISTORIA', blank=True, verbose_name="Configurar en histórica")  # Field name made lowercase.
    lo_texto_valor_0 = models.CharField(db_column='LO_TEXTO_VALOR_0', max_length=24, blank=True, null=True,verbose_name="Texto estado 0",choices=estado_digital_0)  # Field name made lowercase.
    lo_texto_valor_1 = models.CharField(db_column='LO_TEXTO_VALOR_1', max_length=24, blank=True, null=True,verbose_name="Texto estado 1",choices=estado_digital_1)  # Field name made lowercase.
    lo_tarjeta = models.CharField(db_column='LO_TARJETA', max_length=6, blank=True, null=True, verbose_name="Tarjeta")  # Field name made lowercase.ES MEDIO FOREIGN KEY PERO NO SE PUEDE CNOFIGURAR COMO TAL; SI COMO CHOICE
    lo_entrada = models.SmallIntegerField(db_column='LO_ENTRADA', blank=True, null=True,verbose_name="Entrada")  # Field name made lowercase.
    lo_modo = models.SmallIntegerField(db_column='LO_MODO', blank=True, null=True,verbose_name="Modo",choices=modos_ordenes)  # Field name made lowercase.
    lo_tipo_contacto = models.SmallIntegerField(db_column='LO_TIPO_CONTACTO', blank=True, null=True,verbose_name="Inversion(Tipo de contacto)",choices={"0":"Normalmente Aberto","1":"Normalmente cerrado"})  # Field name made lowercase.
    lo_tiempo = models.SmallIntegerField(db_column='LO_TIEMPO', blank=True, null=True,verbose_name="Impulso minimo (ms)")  # Field name made lowercase.
    lo_descripcion1 = models.CharField(db_column='LO_DESCRIPCION1', max_length=20, blank=True, null=True,verbose_name="Descripcion 1")  # Field name made lowercase.
    lo_descripcion2 = models.CharField(db_column='LO_DESCRIPCION2', max_length=20, blank=True, null=True,verbose_name="Descripcion 2")  # Field name made lowercase.
    lo_falta = models.DateTimeField(db_column='LO_FALTA', blank=True, null=True,verbose_name="Fecha de Alta")  # Field name made lowercase.
    lo_fmodif = models.DateTimeField(db_column='LO_FMODIF', blank=True, null=True,verbose_name="Fecha de Baja")  # Field name made lowercase.
    lo_fbaja = models.DateTimeField(db_column='LO_FBAJA', blank=True, null=True,verbose_name="Fecha de Modificacion")  # Field name made lowercase.
    lo_recid = models.IntegerField(db_column='LO_RECID', blank=True, null=True, verbose_name="RecID")  # Field name made lowercase.
    lo_origen = models.CharField(db_column='LO_ORIGEN', max_length=10, blank=True, null=True,verbose_name="Origen",choices=origenes)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_ORDENES'
        verbose_name='Orden'
        verbose_name_plural='Ordenes'

    def __str__(self):
        return str(self.lo_descripcion)    


#CASOS ESPECIALITOS
#Tipos Alarmas no está en la intranet
class TiposAlarmas(models.Model):
    ta_codigo = models.SmallIntegerField(db_column='TA_CODIGO', primary_key=True)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ta_falta = models.DateTimeField(db_column='TA_FALTA', blank=True, null=True)  # Field name made lowercase.
    ta_fmodif = models.DateTimeField(db_column='TA_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_ALARMAS'

    def __str__(self):
        return str(self.ta_codigo) + ' : ' + str(self.ta_descripcion)        

#Naturaleza senales en la intranet está en blanco (provis)
class NaturalezaSenales(models.Model):
    ns_codigo = models.SmallIntegerField(db_column='NS_CODIGO', primary_key=True)  # Field name made lowercase.
    ns_nombre = models.CharField(db_column='NS_NOMBRE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ns_falta = models.DateTimeField(db_column='NS_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    ns_fmodif = models.DateTimeField(db_column='NS_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NATURALEZA_SENALES'

    def __str__(self):
        return str(self.ns_nombre)   

'''

class ListaZonas(models.Model):
    lz_codigo = models.SmallIntegerField(db_column='LZ_CODIGO', primary_key=True)  # Field name made lowercase.
    lz_descripcion = models.CharField(db_column='LZ_DESCRIPCION', max_length=16, blank=True, null=True)  # Field name made lowercase.
    lz_superficie = models.DecimalField(db_column='LZ_SUPERFICIE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lz_confederacion = models.SmallIntegerField(db_column='LZ_CONFEDERACION', blank=True, null=True)  # Field name made lowercase.
    lz_cod_ser = models.CharField(db_column='LZ_COD_SER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lz_falta = models.DateTimeField(db_column='LZ_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    lz_fmodif = models.DateTimeField(db_column='LZ_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_ZONAS'

    def __str__(self):
        return str(self.lz_codigo) + ":" + str(self.lz_descripcion)


########################################################################################################################
########################################  TIPOS  #######################################################################
########################################################################################################################
############################### ( CONFIGURACUION WEB) ##################################################################
########################################################################################################################
class FactoresConversionRemota(models.Model):
    fc_codigo = models.CharField(db_column='FC_CODIGO', primary_key=True, max_length=10,verbose_name="Código")	  # Field name made lowercase.
    fc_descripcion = models.CharField(db_column='FC_DESCRIPCION', max_length=50, blank=True, null=True,verbose_name="Descripción")	  # Field name made lowercase.
    fc_x1 = models.FloatField(db_column='FC_X1', blank=True, null=True,verbose_name="x1")	  # Field name made lowercase.
    fc_x2 = models.FloatField(db_column='FC_X2', blank=True, null=True,verbose_name="x2")	  # Field name made lowercase.
    fc_x3 = models.FloatField(db_column='FC_X3', blank=True, null=True,verbose_name="x3")	  # Field name made lowercase.
    fc_x4 = models.FloatField(db_column='FC_X4', blank=True, null=True,verbose_name="x4")	  # Field name made lowercase.
    fc_ui_rango_bajo = models.FloatField(db_column='FC_UI_RANGO_BAJO', blank=True, null=True,verbose_name="Ui rango bajo")  # Field name made lowercase.
    fc_ui_rango_alto = models.FloatField(db_column='FC_UI_RANGO_ALTO', blank=True, null=True,verbose_name="Ui rango alto")  # Field name made lowercase.
    fc_decimal = models.SmallIntegerField(db_column='FC_DECIMAL', blank=True, null=True,verbose_name="Decimales")	  # Field name made lowercase.
    fc_falta = models.DateTimeField(db_column='FC_FALTA', blank=True, null=True,verbose_name="falta")	  # Field name made lowercase.
    fc_fmodif = models.DateTimeField(db_column='FC_FMODIF', blank=True, null=True,verbose_name="fmodif")	  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FACTORES_CONVERSION_REMOTA'




'''

'''

class TiposAlmacenamiento(models.Model):
    ta_codigo = models.CharField(db_column='TA_CODIGO', max_length=5,primary_key=True)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ta_periodo = models.IntegerField(db_column='TA_PERIODO', blank=True, null=True)  # Field name made lowercase.
    ta_almacen = models.IntegerField(db_column='TA_ALMACEN', blank=True, null=True)  # Field name made lowercase.
    ta_falta = models.DateTimeField(db_column='TA_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    ta_fmodif = models.DateTimeField(db_column='TA_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_ALMACENAMIENTO'

    def __str__(self):
        return str(self.ta_descripcion)    


class TiposAreas(models.Model):
    ta_codigo = models.CharField(db_column='TA_CODIGO', max_length=3)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ta_falta = models.DateTimeField(db_column='TA_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    ta_fmodif = models.DateTimeField(db_column='TA_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_AREAS'

class TiposAvisos(models.Model):
    ta_codigo = models.SmallIntegerField(db_column='TA_CODIGO', primary_key=True)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ta_falta = models.DateTimeField(db_column='TA_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    ta_fmodif = models.DateTimeField(db_column='TA_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_AVISOS'

class TiposCalidades(models.Model):
    tca_codigo = models.SmallIntegerField(db_column='TCA_CODIGO', primary_key=True)  # Field name made lowercase.
    tca_descripcion = models.CharField(db_column='TCA_DESCRIPCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tca_porcen_ini = models.SmallIntegerField(db_column='TCA_PORCEN_INI', blank=True, null=True)  # Field name made lowercase.
    tca_porcen_fin = models.SmallIntegerField(db_column='TCA_PORCEN_FIN', blank=True, null=True)  # Field name made lowercase.
    tca_falta = models.DateTimeField(db_column='TCA_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    tca_fmodif = models.DateTimeField(db_column='TCA_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.
    tca_tipo = models.CharField(db_column='TCA_TIPO', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_CALIDADES'


class TiposConsolidacion(models.Model):
    tc_codigo = models.SmallIntegerField(db_column='TC_CODIGO', primary_key=True)  # Field name made lowercase.
    tc_descripcion = models.CharField(db_column='TC_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tc_falta = models.DateTimeField(db_column='TC_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    tc_fmodif = models.DateTimeField(db_column='TC_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_CONSOLIDACION'

    def __str__(self):
        return str(self.tc_codigo) + " : " + str(self.tc_descripcion)


class TiposEquipos(models.Model):
    te_codigo = models.IntegerField(db_column='TE_CODIGO', primary_key=True)  # Field name made lowercase.
    te_descripcion = models.CharField(db_column='TE_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    te_fmodif = models.DateTimeField(db_column='TE_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.
    te_falta = models.DateTimeField(db_column='TE_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_EQUIPOS'


class TiposEstaciones(models.Model):
    te_codigo = models.CharField(db_column='TE_CODIGO', primary_key=True, max_length=2)  # Field name made lowercase.
    te_descripcion = models.CharField(db_column='TE_DESCRIPCION', max_length=32, blank=True, null=True)  # Field name made lowercase.
    te_falta = models.DateTimeField(db_column='TE_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    te_fmodif = models.DateTimeField(db_column='TE_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_ESTACIONES'

    def __str__(self):
        return str(self.te_descripcion)


class TiposFuentes(models.Model):
    tf_codigo = models.CharField(db_column='TF_CODIGO', primary_key=True, max_length=5)  # Field name made lowercase.
    tf_descripcion = models.CharField(db_column='TF_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tf_fmodif = models.DateTimeField(db_column='TF_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.
    tf_falta = models.DateTimeField(db_column='TF_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_FUENTES'

'''

'''
class GruposTiposSenales(models.Model):
    gs_codigo = models.CharField(db_column='GS_CODIGO', primary_key=True, max_length=5)  # Field name made lowercase.
    gs_descripcion = models.CharField(db_column='GS_DESCRIPCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gs_orden = models.SmallIntegerField(db_column='GS_ORDEN', blank=True, null=True)  # Field name made lowercase.
    gs_falta = models.DateTimeField(db_column='GS_FALTA', blank=True, null=True)  # Field name made lowercase.
    gs_fmodif = models.DateTimeField(db_column='GS_FMODIF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GRUPOS_TIPOS_SENALES'

    def __str__(self):
        return str(self.gs_descripcion)          




class TiposTarjetas(models.Model):
    tt_codigo = models.SmallIntegerField(db_column='TT_CODIGO', primary_key=True, verbose_name="Código")
    tt_nombre = models.CharField(db_column='TT_NOMBRE', max_length=20,verbose_name="Nombre")        
    tt_descripcion = models.CharField(db_column='TT_DESCRIPCION', max_length=200,verbose_name="Descripcion")
    tt_falta = models.DateTimeField(db_column='TT_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    tt_fmodif = models.DateTimeField(db_column='TT_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_TARJETAS'
        verbose_name="Tipo de tarjeta"
        verbose_name_plural="Tipos de tarjeta"

    def __str__(self):
        return str(self.tt_nombre)    


class ModalidadesAlarmas(models.Model):
    ma_alarma = models.CharField(db_column='MA_ALARMA', primary_key=True, max_length=1)  # Field name made lowercase.
    ma_txt_alarma = models.CharField(db_column='MA_TXT_ALARMA', max_length=8)  # Field name made lowercase.
    ma_falta = models.DateTimeField(db_column='MA_FALTA', blank=True, null=True, editable=False)  # Field name made lowercase.
    ma_fmodif = models.DateTimeField(db_column='MA_FMODIF', blank=True, null=True, editable=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MODALIDADES_ALARMAS'
'''

'''
'''
'''

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
'''


'''



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

'''
'''
class ListaEstacionesCaudales(models.Model):
    lq_codigo = models.ForeignKey(ListaEstaciones,on_delete=models.DO_NOTHING,db_column='LQ_CODIGO', primary_key=True)  # Field name made lowercase.
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

    def __str__(self):
        return str(self.lq_codigo.le_codigo_txt) + " : " + str(self.lq_codigo.le_nombre)      


class ListaEstacionesDerivaciones(models.Model):
    led_codigo = models.ForeignKey(ListaEstaciones,on_delete=models.DO_NOTHING,db_column='LED_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (LED_CODIGO, LED_TIPO_DERIVACION, LED_NOMBRE) found, that is not supported. The first column is selected.
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

    def __str__(self):
        return str(self.led_codigo.le_codigo_txt) + " : " + str(self.led_codigo.le_nombre)  


class ListaEstacionesPresas(models.Model):
    lep_codigo = models.ForeignKey(ListaEstaciones,on_delete=models.DO_NOTHING,db_column='LEP_CODIGO', primary_key=True)  # Field name made lowercase.
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

    def __str__(self):
        return str(self.lep_codigo.le_codigo_txt) + " : " + str(self.lep_codigo.le_nombre)      


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
'''


'''
########################################################################################################################
##############################################     WEB       ##############################################################
########################################################################################################################

class CajetinesUnifilares(models.Model):
    pk = models.CompositePrimaryKey("cu_codigo_mapa", "cu_estacion_txt")
    cu_codigo_mapa = models.CharField(db_column='CU_CODIGO_MAPA',  max_length=3)  # Field name made lowercase. The composite primary key (CU_CODIGO_MAPA, CU_ESTACION_TXT) found, that is not supported. The first column is selected.
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
    cw_codigo_mapa = models.CharField(db_column='CW_CODIGO_MAPA', max_length=3)  # Field name made lowercase.
    cw_estacion_txt = models.CharField(db_column='CW_ESTACION_TXT', max_length=4)  # Field name made lowercase.
    cw_tipo_cajetin = models.SmallIntegerField(db_column='CW_TIPO_CAJETIN', blank=True, null=True)  # Field name made lowercase.
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
    cwt_codigo_mapa = models.CharField(db_column='CWT_CODIGO_MAPA', max_length=3)  # Field name made lowercase.
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

'''

'''
naturalezas={1:"Analogica",2:"Digital",3:"Doble Digital"}
tarjetas_ordenes={'DIL001':'DIL001','DOF001':'DOF001','DO7260':'DO7260'}

modos={"ACTIVA":"Activa","NO ACTIVA":"No activa"}
estado_digital_0={"-":"-","ABIERTA":"ABIERTA","APAGADO":"APAGADO","APAGAR":"APAGAR","ARMADO":"ARMADO","ARMAR":"ARMAR","ARRANCADO":"ARRANCADO","CERRADA":"CERRADA","CLAPETA":"CLAPETA",
"COMUNICA":"COMUNICA","DESACTIVA":"DESACTIVA","DESARMADA":"DESARMADA","DESCONECTAR":"DESCONECTAR","ENCENDIDO":"ENCENDIDO","FALLO":"FALLO","INACTIVA":"INACTIVA","MANIOBRA":"MANIOBRA",
"NO":"NO","NORMAL":"NORMAL","PARADO":"PARADO","PARAR":"PARAR","SALIENTE":"SALIENTE"}# Create your models here.
estado_digital_1={"ARMAR/DESARMAR":"ARMAR/DESARMAR","IN/DESINHIBIR":"IN/DESINHIBIR","RESETEAR":"RESETEAR","CERRADA":"CERRADA","ENCENDIDO":"ENCENDIDO","ENCENDER":"ENCENDER",
"DESARMADO":"DESARMADO","DESARMAR":"DESARMAR","PARADO":"PARADO","ABIERTA":"ABIERTA","COMPUERTA":"COMPUERTA","NO COMUNICA":"NO COMUNICA","ACTIVA":"ACTIVA","ARMADA":"ARMADA",
"CONECTAR":"CONECTAR","APAGADO":"APAGADO","NORMAL":"NORMAL","ABIERTO":"ABIERTO","SI":"SI","FALLO":"FALLO","PARAR":"PARAR","ARRANCADO":"ARRANCADO",
"ARRANCAR":"ARRANCAR","ENTRANTE":"ENTRANTE"}
tipos_ordenes={"TELEMANDO":"TELEMANDO","EMERGENCIA":"EMERGENCIA","CONTROL":"CONTROL"}

'''