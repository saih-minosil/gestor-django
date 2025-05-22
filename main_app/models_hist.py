from django.db import models
from .models_comun import TiposEstaciones,ListaZonas,Provincias,Comunidades,Poblaciones,Rios,TiposConsolidacion,NaturalezaSenales,copy_object

#CALIDADES PARA CONSOLIDADAS NO PARA DATOS VALID NI TREAL
class TiposCalidades(models.Model):
    tca_codigo = models.SmallIntegerField(db_column='TCA_CODIGO', primary_key=True)  # Field name made lowercase.
    tca_descripcion = models.CharField(db_column='TCA_DESCRIPCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tca_porcen_ini = models.SmallIntegerField(db_column='TCA_PORCEN_INI', blank=True, null=True)  # Field name made lowercase.
    tca_porcen_fin = models.SmallIntegerField(db_column='TCA_PORCEN_FIN', blank=True, null=True)  # Field name made lowercase.
    tca_tipo = models.CharField(db_column='TCA_TIPO', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_CALIDADES'     

####################################################### VALORES ################################################################

class DatosTreal(models.Model):
    pk = models.CompositePrimaryKey('cc_idsenal', 'cc_fecha')
    cc_idsenal = models.ForeignKey('ListaSenales_H',on_delete=models.PROTECT,db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_TREAL'
        unique_together = (('cc_idsenal', 'cc_fecha'),)

def createTablaDatosTreal(nombre_tabla):
    class nuevaTablaDatosTreal(models.Model):
        pk = models.CompositePrimaryKey('cc_idsenal', 'cc_fecha')
        cc_idsenal = models.ForeignKey('ListaSenales_H',on_delete=models.PROTECT,db_column='CC_IDSENAL')  # Field name made lowercase.
        cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
        cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
        cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
        class Meta:
            managed = False
            db_table = nombre_tabla  
            unique_together = (('cc_idsenal', 'cc_fecha'),)      
    return nuevaTablaDatosTreal        

class DatosValid(models.Model):
    pk = models.CompositePrimaryKey('cc_idsenal', 'cc_fecha')
    cc_idsenal = models.ForeignKey('ListaSenales_H',on_delete=models.PROTECT,db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DATOS_VALID'
        unique_together = (('cc_idsenal', 'cc_fecha'),)

def createTablaDatosValid(nombre_tabla):
    class nuevaTablaDatosValid(models.Model):
        pk = models.CompositePrimaryKey('cc_idsenal', 'cc_fecha')
        cc_idsenal = models.ForeignKey('ListaSenales_H',on_delete=models.PROTECT,db_column='CC_IDSENAL')  # Field name made lowercase.
        cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
        cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
        cc_calidad = models.SmallIntegerField(db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
        cc_validado = models.SmallIntegerField(db_column='CC_VALIDADO', blank=True, null=True)  # Field name made lowercase.
    
        class Meta:
            managed = False
            db_table = nombre_tabla   
            unique_together = (('cc_idsenal', 'cc_fecha'),)    


        def _do_update(self, base_qs, using, pk_val, values, update_fields, forced_update):
            filtered = base_qs.filter(cc_idsenal=pk_val[0],cc_fecha=pk_val[1])
            if not values:
                return update_fields is not None or filtered.exists()
            if self._meta.select_on_save and not forced_update:
                return (
                    filtered.exists() and (filtered._update(values) > 0 or filtered.exists())
                )
            return filtered._update(values) > 0

    return nuevaTablaDatosValid          

##################### DIA Y MES SE LEEN DE LA INTRANET, PERO PARA FUTURA APLICACION QUE MODIFIQUE LA BBDD

class ConsDia_H(models.Model):
    pk = models.CompositePrimaryKey('cc_idsenal', 'cc_fecha')
    cc_idsenal = models.ForeignKey('ListaSenales_H',on_delete=models.PROTECT,db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor_min = models.FloatField(db_column='CC_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
    cc_f_valor_min = models.DateTimeField(db_column='CC_F_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_max = models.FloatField(db_column='CC_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
    cc_f_valor_max = models.DateTimeField(db_column='CC_F_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
    cc_valor_ultimo = models.FloatField(db_column='CC_VALOR_ULTIMO', blank=True, null=True)  # Field name made lowercase.
    cc_valor_gradiente = models.FloatField(db_column='CC_VALOR_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.ForeignKey(TiposCalidades, models.DO_NOTHING, db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_porcen = models.FloatField(db_column='CC_PORCEN', blank=True, null=True)  # Field name made lowercase.
    cc_f_gradiente = models.DateTimeField(db_column='CC_F_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
    cc_volumen = models.FloatField(db_column='CC_VOLUMEN', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'CONS_DIA'
        unique_together = (('cc_idsenal', 'cc_fecha'),)
    def __str__(self):
        return str(self.cc_idsenal) + "." + str(self.cc_fecha)


class ConsMes_H(models.Model):
    pk = models.CompositePrimaryKey('cc_idsenal', 'cc_fecha')
    cc_idsenal = models.ForeignKey('ListaSenales_H',on_delete=models.PROTECT,db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor_min = models.FloatField(db_column='CC_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
    cc_f_valor_min = models.DateTimeField(db_column='CC_F_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_max = models.FloatField(db_column='CC_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
    cc_f_valor_max = models.DateTimeField(db_column='CC_F_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
    cc_valor_ultimo = models.FloatField(db_column='CC_VALOR_ULTIMO', blank=True, null=True)  # Field name made lowercase.
    cc_valor_gradiente = models.FloatField(db_column='CC_VALOR_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.ForeignKey(TiposCalidades, models.DO_NOTHING, db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_porcen = models.FloatField(db_column='CC_PORCEN', blank=True, null=True)  # Field name made lowercase.
    cc_f_gradiente = models.DateTimeField(db_column='CC_F_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
    cc_volumen = models.FloatField(db_column='CC_VOLUMEN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONS_MES'
        unique_together = (('cc_idsenal', 'cc_fecha'),)



class ConsAnoH(models.Model):
    pk = models.CompositePrimaryKey('cc_idsenal', 'cc_fecha')
    cc_idsenal = models.ForeignKey('ListaSenales_H', models.PROTECT, db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor_min = models.FloatField(db_column='CC_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
    cc_f_valor_min = models.DateTimeField(db_column='CC_F_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_max = models.FloatField(db_column='CC_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
    cc_f_valor_max = models.DateTimeField(db_column='CC_F_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
    cc_valor_ultimo = models.FloatField(db_column='CC_VALOR_ULTIMO', blank=True, null=True)  # Field name made lowercase.
    cc_valor_gradiente = models.FloatField(db_column='CC_VALOR_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.ForeignKey(TiposCalidades, models.DO_NOTHING, db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_porcen = models.FloatField(db_column='CC_PORCEN', blank=True, null=True)  # Field name made lowercase.
    cc_f_gradiente = models.DateTimeField(db_column='CC_F_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
    cc_volumen = models.FloatField(db_column='CC_VOLUMEN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONS_ANO_H'
        unique_together = (('cc_idsenal', 'cc_fecha'),)


class ConsAnoN(models.Model):
    pk = models.CompositePrimaryKey('cc_idsenal', 'cc_fecha')
    cc_idsenal = models.ForeignKey('ListaSenales_H', models.PROTECT, db_column='CC_IDSENAL')  # Field name made lowercase.
    cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
    cc_valor_min = models.FloatField(db_column='CC_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
    cc_f_valor_min = models.DateTimeField(db_column='CC_F_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
    cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
    cc_valor_max = models.FloatField(db_column='CC_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
    cc_f_valor_max = models.DateTimeField(db_column='CC_F_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
    cc_valor_ultimo = models.FloatField(db_column='CC_VALOR_ULTIMO', blank=True, null=True)  # Field name made lowercase.
    cc_valor_gradiente = models.FloatField(db_column='CC_VALOR_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
    cc_calidad = models.ForeignKey(TiposCalidades, models.DO_NOTHING, db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
    cc_porcen = models.FloatField(db_column='CC_PORCEN', blank=True, null=True)  # Field name made lowercase.
    cc_f_gradiente = models.DateTimeField(db_column='CC_F_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
    cc_volumen = models.FloatField(db_column='CC_VOLUMEN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONS_ANO_N'
        unique_together = (('cc_idsenal', 'cc_fecha'),)

################################## LISTAS BUENAS (ESTACIONES, SEÑALES Y REMOTAS ) ###################################################################
'''

'''

class ListaEstaciones_H(models.Model):
    le_codigo = models.IntegerField(db_column='LE_CODIGO', primary_key=True)  # Field name made lowercase.
    le_codigo_txt = models.CharField(db_column='LE_CODIGO_TXT', max_length=4)  # Field name made lowercase.
    le_tipo_estacion = models.ForeignKey(TiposEstaciones,db_column='LE_TIPO_ESTACION', max_length=2,verbose_name="Tipo de Estacion",on_delete=models.DO_NOTHING)	  # Field name made lowercase.
    le_zona = models.ForeignKey(ListaZonas, models.DO_NOTHING, db_column='LE_ZONA')  # Field name made lowercase.
    le_nombre = models.CharField(db_column='LE_NOMBRE', max_length=30)  # Field name made lowercase.
    le_nombre_corto = models.CharField(db_column='LE_NOMBRE_CORTO', max_length=18)  # Field name made lowercase.
    le_comu_auto = models.ForeignKey(Comunidades, on_delete=models.DO_NOTHING, db_column="LE_COMU_AUTO",verbose_name="Comunidad autonoma")	    
    le_provincia = models.ForeignKey(Provincias, on_delete=models.DO_NOTHING, db_column="LE_PROVINCIA",verbose_name="Provincia")	    
    le_municipio = models.ForeignKey(Poblaciones, on_delete=models.DO_NOTHING, db_column="LE_MUNICIPIO",verbose_name="Municipio")	    
    le_rio = models.ForeignKey(Rios, on_delete=models.DO_NOTHING, db_column="LE_RIO",verbose_name="Rio")	
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

    def __str__(self):
        return f"{self.le_codigo_txt} : {self.le_nombre}"   

    def from_gestor(self,obj):
        copy_object(orig=obj,dest=self)    
        self.le_codigo=obj.le_recid


class ListaRemotas_H(models.Model):
    lr_codigo = models.IntegerField(db_column='LR_CODIGO', primary_key=True)  # Field name made lowercase.
    lr_tipo_estacion = models.ForeignKey(TiposEstaciones,db_column="LR_TIPO_ESTACION", on_delete=models.DO_NOTHING,verbose_name="Tipo de estacion")	
    lr_nombre = models.CharField(db_column='LR_NOMBRE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lr_nombre_corto = models.CharField(db_column='LR_NOMBRE_CORTO', max_length=18, blank=True, null=True)  # Field name made lowercase.
    lr_estacion = models.ForeignKey(ListaEstaciones_H, models.DO_NOTHING, db_column='LR_ESTACION')  # Field name made lowercase.
    lr_zona = models.ForeignKey(ListaZonas, models.DO_NOTHING, db_column='LR_ZONA')  # Field name made lowercase.
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
    lr_rio = models.ForeignKey(Rios, on_delete=models.DO_NOTHING, db_column="LR_RIO",verbose_name="Rio",blank=True,null=True)	
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

    def __str__(self):
        return f"{self.lr_codigo_txt} : {self.lr_nombre}"   

    def from_gestor(self,obj):
        copy_object(orig=obj,dest=self)    
        self.lr_codigo=obj.lr_recid   
        self.lr_estacion_id=obj.lr_estacion.le_recid  



class ListaSenales_H(models.Model):
    ls_tag = models.IntegerField(db_column='LS_TAG', primary_key=True)  # Field name made lowercase.
    ls_descripcion = models.CharField(db_column='LS_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ls_tag_txt = models.CharField(db_column='LS_TAG_TXT', max_length=16)  # Field name made lowercase.
    ls_remota = models.ForeignKey(ListaRemotas_H, models.DO_NOTHING, db_column='LS_REMOTA')  # Field name made lowercase.
    ls_estacion = models.ForeignKey(ListaEstaciones_H, models.DO_NOTHING, db_column='LS_ESTACION', blank=True, null=True)  # Field name made lowercase.
    ls_tipo_senal = models.CharField(db_column='LS_TIPO_SENAL', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_tipo_alarma = models.ForeignKey('TiposAlarmas', models.DO_NOTHING, db_column='LS_TIPO_ALARMA', blank=True, null=True)  # Field name made lowercase.
    ls_marca_cons = models.SmallIntegerField(db_column='LS_MARCA_CONS', blank=True, null=True)  # Field name made lowercase.
    ls_tipo_almacenamiento = models.CharField(db_column='LS_TIPO_ALMACENAMIENTO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_tipo_consolidacion = models.ForeignKey(TiposConsolidacion, models.DO_NOTHING, db_column='LS_TIPO_CONSOLIDACION', blank=True, null=True)  # Field name made lowercase.
    ls_tag_cons_1 = models.SmallIntegerField(db_column='LS_TAG_CONS_1', blank=True, null=True)  # Field name made lowercase.
    ls_tag_cons_2 = models.SmallIntegerField(db_column='LS_TAG_CONS_2', blank=True, null=True)  # Field name made lowercase.
    ls_hora_cons = models.CharField(db_column='LS_HORA_CONS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ls_curvaref = models.SmallIntegerField(db_column='LS_CURVAREF', blank=True, null=True)  # Field name made lowercase.
    ls_naturaleza = models.ForeignKey(NaturalezaSenales, models.DO_NOTHING, db_column='LS_NATURALEZA', blank=True, null=True)  # Field name made lowercase.
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

    def __str__(self):
        return f"{self.ls_tag_txt}"     

    def from_gestor(self,obj):
        copy_object(orig=obj,dest=self)    
        self.ls_tag=obj.ls_recid      
        self.ls_remota_id=obj.ls_remota.lr_recid
        self.ls_estacion_id=obj.ls_remota.lr_estacion.le_recid

    
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

    def from_gestor(self,obj):
        copy_object(orig=obj,dest=self)    
        self.lsc_tag=obj.lsc_tag.ls_recid          


class ListaSenalesLimitevariables(models.Model):
    pk = models.CompositePrimaryKey('lsl_tag', 'lsl_alarma', 'lsl_mes')
    lsl_tag = models.IntegerField(db_column='LSL_TAG')  # Field name made lowercase.
    lsl_alarma = models.CharField(db_column='LSL_ALARMA', max_length=4)  # Field name made lowercase.
    lsl_dia = models.SmallIntegerField(db_column='LSL_DIA')  # Field name made lowercase.
    lsl_mes = models.SmallIntegerField(db_column='LSL_MES')  # Field name made lowercase.
    lsl_valor = models.FloatField(db_column='LSL_VALOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_SENALES_LIMITEVARIABLES'
        unique_together = (('lsl_tag', 'lsl_alarma', 'lsl_mes'),)

    def from_gestor(self,obj):
        copy_object(orig=obj,dest=self)    
        self.lsl_tag=obj.lsl_tag.ls_recid         
    
''' NO SONCOMUNES: '''
class TiposAlarmas(models.Model):
    ta_codigo = models.SmallIntegerField(db_column='TA_CODIGO', primary_key=True)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_ALARMAS'

    def __str__(self):
        return str(self.ta_codigo) + ' : ' + str(self.ta_descripcion)   



################################################# LISTAS SENCILLAS DE DATOS #############################################################################################
''' (SON COMUNES; QUE LES DEN, NO?)
class Comunidades(models.Model):
    ca_codigo = models.SmallIntegerField(db_column='CA_CODIGO', primary_key=True, db_comment='Codigo de la comunidad autonom')  # Field name made lowercase.
    ca_descripcion = models.CharField(db_column='CA_DESCRIPCION', max_length=50, blank=True, null=True, db_comment='Nombre de la comunidad autonom')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMUNIDADES'


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
    pr_comunidad = models.ForeignKey('Comunidades', models.DO_NOTHING, db_column='PR_COMUNIDAD', blank=True, null=True, db_comment='Codigo de la comunidad autonom')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROVINCIAS'

class Rios(models.Model):
    ri_codigo = models.IntegerField(db_column='RI_CODIGO', primary_key=True)  # Field name made lowercase.
    ri_descripcion = models.CharField(db_column='RI_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIOS'
'''