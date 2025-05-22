from django.db import models


def copy_object(orig, dest):
    attributes=orig.__dict__.keys()
    for at in attributes:
        if at in dest.__dict__:
            setattr(dest,at,getattr(orig,at))

def copy_from_different_object(orig,dest,orig_prefix,dest_prefix):
    attributes=orig.__dict__.keys()
    for at in attributes:
        dest_at=at.replace(orig_prefix,dest_prefix)
        if dest_at in dest.__dict__:
            setattr(dest,dest_at,getattr(orig,at))

########################################################################################################################
########################################  DATOS  #######################################################################
########################################################################################################################


class Comunidades(models.Model):
    ca_codigo = models.SmallIntegerField(db_column='CA_CODIGO', primary_key=True, db_comment='Codigo de la comunidad autonoma')  # Field name made lowercase.
    ca_descripcion = models.CharField(db_column='CA_DESCRIPCION', max_length=50, blank=True, null=True, db_comment='Nombre de la comunidad autonom')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMUNIDADES'

    def __str__(self):
        return str(self.ca_descripcion)


class Rios(models.Model):
    ri_codigo = models.IntegerField(db_column='RI_CODIGO', primary_key=True)  # Field name made lowercase.
    ri_descripcion = models.CharField(db_column='RI_DESCRIPCION', max_length=50, blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIOS'

    def __str__(self):
        return str(self.ri_descripcion)


class Provincias(models.Model):
    pr_codigo = models.SmallIntegerField(db_column='PR_CODIGO', primary_key=True)  # Field name made lowercase.
    pr_descripcion = models.CharField(db_column='PR_DESCRIPCION', max_length=50, blank=False,  null=False)
    pr_comunidad = models.SmallIntegerField(db_column='PR_COMUNIDAD', blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'PROVINCIAS'

    def __str__(self):
        return str(self.pr_descripcion)        

class Poblaciones(models.Model):
    po_codigo = models.IntegerField(db_column='PO_CODIGO', primary_key=True)  # Field name made lowercase.
#    po_provincia = models.SmallIntegerField(db_column='PO_PROVINCIA', blank=True,
#                                            null=True)  # Field name made lowercase.
    po_provincia  = models.ForeignKey(Provincias, db_column="PO_PROVINCIA", on_delete=models.DO_NOTHING)
    po_descripcion = models.CharField(db_column='PO_DESCRIPCION', max_length=50, blank=True,
                                     null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'POBLACIONES'

    def __str__(self):
        return str(self.po_descripcion)  

    #def from_gestor(self,obj):            
    #    copy_object(orig=obj,dest=self)
        

class ListaZonas(models.Model):
    lz_codigo = models.SmallIntegerField(db_column='LZ_CODIGO', primary_key=True,verbose_name="Código")  # Field name made lowercase.
    lz_descripcion = models.CharField(db_column='LZ_DESCRIPCION', max_length=16,verbose_name="Descripción")  # Field name made lowercase.
    lz_confederacion = models.SmallIntegerField(db_column='LZ_CONFEDERACION', blank=True, null=True,verbose_name="Confederación")  # Field name made lowercase.
    #lz_superficie = models.DecimalField(db_column='LZ_SUPERFICIE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_ZONAS'

    def __str__(self):
        return str(self.lz_descripcion)   

class TiposEstaciones(models.Model):
    te_codigo = models.CharField(db_column='TE_CODIGO', primary_key=True, max_length=2)  # Field name made lowercase.
    te_descripcion = models.CharField(db_column='TE_DESCRIPCION', max_length=32, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TIPOS_ESTACIONES'   

    def __str__(self):
        return str(self.te_descripcion)   
    


class TiposConsolidacion(models.Model):
    tc_codigo = models.SmallIntegerField(db_column='TC_CODIGO', primary_key=True)  # Field name made lowercase.
    tc_descripcion = models.CharField(db_column='TC_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TIPOS_CONSOLIDACION'

    def __str__(self):
        return str(self.tc_codigo) + " : " + str(self.tc_descripcion)          

class NaturalezaSenales(models.Model):
    ns_codigo = models.SmallIntegerField(db_column='NS_CODIGO', primary_key=True)  # Field name made lowercase.
    ns_nombre = models.CharField(db_column='NS_NOMBRE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'NATURALEZA_SENALES'        
   


class TiposAlmacenamiento(models.Model):
    ta_codigo = models.CharField(db_column='TA_CODIGO', max_length=5,primary_key=True)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ta_periodo = models.IntegerField(db_column='TA_PERIODO', blank=True, null=True)  # Field name made lowercase.
    ta_almacen = models.IntegerField(db_column='TA_ALMACEN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_ALMACENAMIENTO'

class GruposTiposSenales(models.Model):
    gs_codigo = models.CharField(db_column='GS_CODIGO', primary_key=True, max_length=5)  # Field name made lowercase.
    gs_descripcion = models.CharField(db_column='GS_DESCRIPCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gs_orden = models.SmallIntegerField(db_column='GS_ORDEN', blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'GRUPOS_TIPOS_SENALES'

    def __str__(self):
        return str(self.gs_descripcion)          








########################################################################################################################
########################################  TIPOS  #######################################################################
########################################################################################################################
'''




class TiposAreas(models.Model):
    ta_codigo = models.CharField(db_column='TA_CODIGO', max_length=3)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_AREAS'


class TiposAvisos(models.Model):
    ta_codigo = models.SmallIntegerField(db_column='TA_CODIGO', primary_key=True)  # Field name made lowercase.
    ta_descripcion = models.CharField(db_column='TA_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_AVISOS'







class TiposEquipos(models.Model):
    te_codigo = models.IntegerField(db_column='TE_CODIGO', primary_key=True)  # Field name made lowercase.
    te_descripcion = models.CharField(db_column='TE_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TIPOS_EQUIPOS'





class TiposFuentes(models.Model):
    tf_codigo = models.CharField(db_column='TF_CODIGO', primary_key=True, max_length=5)  # Field name made lowercase.
    tf_descripcion = models.CharField(db_column='TF_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TIPOS_FUENTES'


class ModalidadesAlarmas(models.Model):
    ma_alarma = models.CharField(db_column='MA_ALARMA', primary_key=True, max_length=1)  # Field name made lowercase.
    ma_txt_alarma = models.CharField(db_column='MA_TXT_ALARMA', max_length=8)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'MODALIDADES_ALARMAS'



class SequiaNiveles(models.Model):
    sn_codigo = models.SmallIntegerField(db_column='SN_CODIGO', primary_key=True)  # Field name made lowercase.
    sn_descripcion = models.CharField(db_column='SN_DESCRIPCION', max_length=30)  # Field name made lowercase.
    sn_valor_ini = models.DecimalField(db_column='SN_VALOR_INI', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sn_valor_fin = models.DecimalField(db_column='SN_VALOR_FIN', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'SEQUIA_NIVELES'

'''
########################################################################################################################
############################################   LISTAS            #########################################################
########################################################################################################################




# class ListaEstacionesAreas(models.Model):
#     lea_codigo = models.IntegerField(db_column='LEA_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (LEA_CODIGO, LEA_AREA, LEA_NUMORDEN) found, that is not supported. The first column is selected.
#     lea_area = models.CharField(db_column='LEA_AREA', max_length=3)  # Field name made lowercase.
#     lea_numorden = models.SmallIntegerField(db_column='LEA_NUMORDEN')  # Field name made lowercase.
#     lea_tag = models.IntegerField(db_column='LEA_TAG', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'LISTA_ESTACIONES_AREAS'
#         unique_together = (('lea_codigo', 'lea_area', 'lea_numorden'),)
#
#
# class ListaEstacionesCaudales(models.Model):
#     lq_codigo = models.IntegerField(db_column='LQ_CODIGO', primary_key=True)  # Field name made lowercase.
#     lq_control_qe = models.CharField(db_column='LQ_CONTROL_QE', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     lq_control_qc = models.CharField(db_column='LQ_CONTROL_QC', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     lq_control_qu = models.CharField(db_column='LQ_CONTROL_QU', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     lq_control_qt = models.CharField(db_column='LQ_CONTROL_QT', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     lq_dispositivos_qe = models.CharField(db_column='LQ_DISPOSITIVOS_QE', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     lq_fe_resolucion_dv = models.DateTimeField(db_column='LQ_FE_RESOLUCION_DV', blank=True, null=True)  # Field name made lowercase.
#     lq_mes1_dv = models.DecimalField(db_column='LQ_MES1_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes2_dv = models.DecimalField(db_column='LQ_MES2_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes3_dv = models.DecimalField(db_column='LQ_MES3_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes4_dv = models.DecimalField(db_column='LQ_MES4_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes5_dv = models.DecimalField(db_column='LQ_MES5_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes6_dv = models.DecimalField(db_column='LQ_MES6_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes7_dv = models.DecimalField(db_column='LQ_MES7_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes8_dv = models.DecimalField(db_column='LQ_MES8_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes9_dv = models.DecimalField(db_column='LQ_MES9_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes10_dv = models.DecimalField(db_column='LQ_MES10_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes11_dv = models.DecimalField(db_column='LQ_MES11_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes12_dv = models.DecimalField(db_column='LQ_MES12_DV', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_porce_dv = models.DecimalField(db_column='LQ_PORCE_DV', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     lq_fe_resolucion_eco = models.DateTimeField(db_column='LQ_FE_RESOLUCION_ECO', blank=True, null=True)  # Field name made lowercase.
#     lq_mes1_eco = models.DecimalField(db_column='LQ_MES1_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes2_eco = models.DecimalField(db_column='LQ_MES2_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes3_eco = models.DecimalField(db_column='LQ_MES3_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes4_eco = models.DecimalField(db_column='LQ_MES4_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes5_eco = models.DecimalField(db_column='LQ_MES5_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes6_eco = models.DecimalField(db_column='LQ_MES6_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes7_eco = models.DecimalField(db_column='LQ_MES7_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes8_eco = models.DecimalField(db_column='LQ_MES8_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes9_eco = models.DecimalField(db_column='LQ_MES9_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes10_eco = models.DecimalField(db_column='LQ_MES10_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes11_eco = models.DecimalField(db_column='LQ_MES11_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_mes12_eco = models.DecimalField(db_column='LQ_MES12_ECO', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_porce_eco = models.DecimalField(db_column='LQ_PORCE_ECO', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     lq_fe_bombeado = models.DateTimeField(db_column='LQ_FE_BOMBEADO', blank=True, null=True)  # Field name made lowercase.
#     lq_qmax_concesion_b = models.DecimalField(db_column='LQ_QMAX_CONCESION_B', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_fe_escalapeces = models.DateTimeField(db_column='LQ_FE_ESCALAPECES', blank=True, null=True)  # Field name made lowercase.
#     lq_qmax_ep = models.DecimalField(db_column='LQ_QMAX_EP', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_qmin_eq = models.DecimalField(db_column='LQ_QMIN_EQ', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_fe_trasvasado = models.DateTimeField(db_column='LQ_FE_TRASVASADO', blank=True, null=True)  # Field name made lowercase.
#     lq_qmax_concesion_t = models.DecimalField(db_column='LQ_QMAX_CONCESION_T', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lq_observ_eco = models.CharField(db_column='LQ_OBSERV_ECO', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     lq_observ_dv = models.CharField(db_column='LQ_OBSERV_DV', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     lq_observ_b = models.CharField(db_column='LQ_OBSERV_B', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     lq_observ_t = models.CharField(db_column='LQ_OBSERV_T', max_length=200, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'LISTA_ESTACIONES_CAUDALES'
#
#
# class ListaEstacionesDerivaciones(models.Model):
#     led_codigo = models.IntegerField(db_column='LED_CODIGO', primary_key=True)  # Field name made lowercase. The composite primary key (LED_CODIGO, LED_TIPO_DERIVACION, LED_NOMBRE) found, that is not supported. The first column is selected.
#     led_tipo_derivacion = models.CharField(db_column='LED_TIPO_DERIVACION', max_length=20)  # Field name made lowercase.
#     led_nombre = models.CharField(db_column='LED_NOMBRE', max_length=20)  # Field name made lowercase.
#     led_descripcion = models.CharField(db_column='LED_DESCRIPCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     led_tipo_turbina = models.CharField(db_column='LED_TIPO_TURBINA', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     led_qmax = models.DecimalField(db_column='LED_QMAX', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_qmin = models.DecimalField(db_column='LED_QMIN', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_potencia_nominal = models.DecimalField(db_column='LED_POTENCIA_NOMINAL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_qmax_entrada = models.DecimalField(db_column='LED_QMAX_ENTRADA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_potencia_total = models.DecimalField(db_column='LED_POTENCIA_TOTAL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_salto_bruto = models.DecimalField(db_column='LED_SALTO_BRUTO', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_produccion_media = models.DecimalField(db_column='LED_PRODUCCION_MEDIA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_h29_x_central = models.DecimalField(db_column='LED_H29_X_CENTRAL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_h29_y_central = models.DecimalField(db_column='LED_H29_Y_CENTRAL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_h29_z_central = models.DecimalField(db_column='LED_H29_Z_CENTRAL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_toma_tipo = models.CharField(db_column='LED_TOMA_TIPO', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     led_toma_capacidad = models.DecimalField(db_column='LED_TOMA_CAPACIDAD', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_toma_cota = models.DecimalField(db_column='LED_TOMA_COTA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_toma_seccion = models.CharField(db_column='LED_TOMA_SECCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     led_toma_lon_canal = models.DecimalField(db_column='LED_TOMA_LON_CANAL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_toma_lon_tuberia = models.DecimalField(db_column='LED_TOMA_LON_TUBERIA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_toma_chimenea = models.CharField(db_column='LED_TOMA_CHIMENEA', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     led_toma_corriente = models.CharField(db_column='LED_TOMA_CORRIENTE', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     led_toma_provincia = models.CharField(db_column='LED_TOMA_PROVINCIA', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     led_toma_municipio = models.CharField(db_column='LED_TOMA_MUNICIPIO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     led_toma_h29_x = models.DecimalField(db_column='LED_TOMA_H29_X', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_toma_h29_y = models.DecimalField(db_column='LED_TOMA_H29_Y', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_toma_h29_z = models.DecimalField(db_column='LED_TOMA_H29_Z', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_rest_corriente = models.CharField(db_column='LED_REST_CORRIENTE', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     led_rest_provincia = models.CharField(db_column='LED_REST_PROVINCIA', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     led_rest_municipio = models.CharField(db_column='LED_REST_MUNICIPIO', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     led_rest_h29_x = models.DecimalField(db_column='LED_REST_H29_X', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_rest_h29_y = models.DecimalField(db_column='LED_REST_H29_Y', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_rest_h29_z = models.DecimalField(db_column='LED_REST_H29_Z', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_tipo_conduccion = models.CharField(db_column='LED_TIPO_CONDUCCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     led_seccion = models.CharField(db_column='LED_SECCION', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     led_lon_trasvase = models.DecimalField(db_column='LED_LON_TRASVASE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_capacidad = models.DecimalField(db_column='LED_CAPACIDAD', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_superficie = models.DecimalField(db_column='LED_SUPERFICIE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     led_poblaciones_ab = models.CharField(db_column='LED_POBLACIONES_AB', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     led_habitantes_ab = models.CharField(db_column='LED_HABITANTES_AB', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     led_toma_secciontoma = models.CharField(db_column='LED_TOMA_SECCIONTOMA', max_length=20, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'LISTA_ESTACIONES_DERIVACIONES'
#         unique_together = (('led_codigo', 'led_tipo_derivacion', 'led_nombre'),)
#
#
# class ListaEstacionesPresas(models.Model):
#     lep_codigo = models.IntegerField(db_column='LEP_CODIGO', primary_key=True)  # Field name made lowercase.
#     lep_tipo_explotacion = models.CharField(db_column='LEP_TIPO_EXPLOTACION', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     lep_tipo_presa = models.CharField(db_column='LEP_TIPO_PRESA', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     lep_granpresa = models.SmallIntegerField(db_column='LEP_GRANPRESA', blank=True, null=True)  # Field name made lowercase.
#     lep_tipo_gestor = models.CharField(db_column='LEP_TIPO_GESTOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     lep_registroseg = models.CharField(db_column='LEP_REGISTROSEG', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     lep_riesgopotencial = models.CharField(db_column='LEP_RIESGOPOTENCIAL', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     lep_dispositivo_qeco = models.CharField(db_column='LEP_DISPOSITIVO_QECO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     lep_ffin_obras = models.DateTimeField(db_column='LEP_FFIN_OBRAS', blank=True, null=True)  # Field name made lowercase.
#     lep_fclasificacion = models.DateTimeField(db_column='LEP_FCLASIFICACION', blank=True, null=True)  # Field name made lowercase.
#     lep_fnormasexp = models.DateTimeField(db_column='LEP_FNORMASEXP', blank=True, null=True)  # Field name made lowercase.
#     lep_tipo_compuerta_1 = models.CharField(db_column='LEP_TIPO_COMPUERTA_1', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     lep_cap_aliv_1 = models.DecimalField(db_column='LEP_CAP_ALIV_1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lep_cota_aliv_1 = models.DecimalField(db_column='LEP_COTA_ALIV_1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lep_nvanos_aliv_1 = models.IntegerField(db_column='LEP_NVANOS_ALIV_1', blank=True, null=True)  # Field name made lowercase.
#     lep_tipo_compuerta_2 = models.CharField(db_column='LEP_TIPO_COMPUERTA_2', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     lep_cap_aliv_2 = models.DecimalField(db_column='LEP_CAP_ALIV_2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lep_cota_aliv_2 = models.DecimalField(db_column='LEP_COTA_ALIV_2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lep_nvanos_aliv_2 = models.IntegerField(db_column='LEP_NVANOS_ALIV_2', blank=True, null=True)  # Field name made lowercase.
#     lep_tipo_compuerta_3 = models.CharField(db_column='LEP_TIPO_COMPUERTA_3', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     lep_cap_aliv_3 = models.DecimalField(db_column='LEP_CAP_ALIV_3', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lep_cota_aliv_3 = models.DecimalField(db_column='LEP_COTA_ALIV_3', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lep_nvanos_aliv_3 = models.IntegerField(db_column='LEP_NVANOS_ALIV_3', blank=True, null=True)  # Field name made lowercase.
#     lep_tipo_desague_1 = models.CharField(db_column='LEP_TIPO_DESAGUE_1', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     lep_tipo_valvula_1 = models.CharField(db_column='LEP_TIPO_VALVULA_1', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     lep_cap_desague_1 = models.DecimalField(db_column='LEP_CAP_DESAGUE_1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lep_cota_eje_1 = models.DecimalField(db_column='LEP_COTA_EJE_1', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lep_ncon_des_1 = models.IntegerField(db_column='LEP_NCON_DES_1', blank=True, null=True)  # Field name made lowercase.
#     lep_tipo_desague_2 = models.CharField(db_column='LEP_TIPO_DESAGUE_2', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     lep_tipo_valvula_2 = models.CharField(db_column='LEP_TIPO_VALVULA_2', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     lep_cap_desague_2 = models.DecimalField(db_column='LEP_CAP_DESAGUE_2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lep_cota_eje_2 = models.DecimalField(db_column='LEP_COTA_EJE_2', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lep_ncon_des_2 = models.IntegerField(db_column='LEP_NCON_DES_2', blank=True, null=True)  # Field name made lowercase.
#     lep_tipo_toma = models.CharField(db_column='LEP_TIPO_TOMA', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     lep_seccion_toma = models.CharField(db_column='LEP_SECCION_TOMA', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     lep_cap_toma = models.DecimalField(db_column='LEP_CAP_TOMA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lep_cota_toma = models.DecimalField(db_column='LEP_COTA_TOMA', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lep_tipo_escalapeces = models.CharField(db_column='LEP_TIPO_ESCALAPECES', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     lep_cota_escalapeces = models.DecimalField(db_column='LEP_COTA_ESCALAPECES', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
#     lep_observaciones = models.CharField(db_column='LEP_OBSERVACIONES', max_length=200, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = True
#         db_table = 'LISTA_ESTACIONES_PRESAS'

'''
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
        '''
'''
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
'''


'''
class ListaRemotas(models.Model):
    lr_codigo = models.IntegerField(db_column='LR_CODIGO', primary_key=True)  # Field name made lowercase.
    #lr_tipo_estacion = models.CharField(db_column='LR_TIPO_ESTACION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lr_tipo_estacion=models.ForeignKey(TiposEstaciones,db_column="LR_TIPO_ESTACION", on_delete=models.DO_NOTHING)
    lr_nombre = models.CharField(db_column='LR_NOMBRE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lr_nombre_corto = models.CharField(db_column='LR_NOMBRE_CORTO', max_length=18, blank=True, null=True)  # Field name made lowercase.
    lr_estacion = models.ForeignKey(ListaEstaciones,db_column='LR_ESTACION',on_delete=models.CASCADE)  # Field name made lowercase.
    lr_codigo_txt = models.CharField(db_column='LR_CODIGO_TXT', max_length=5, blank=True, null=True)  # Field name made lowercase.
    lr_zona = models.ForeignKey(ListaZonas,on_delete=models.DO_NOTHING,db_column="LR_ZONA")
   # lr_zona = models.SmallIntegerField(db_column='LR_ZONA')  # Field name made lowercase.
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
    #lr_rio = models.IntegerField(db_column='LR_RIO', blank=True, null=True)  # Field name made lowercase.
    lr_rio = models.ForeignKey(Rios, on_delete=models.DO_NOTHING, db_column="LR_RIO")
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

    def __str__(self):
        return str(self.lr_codigo_txt) + " : " + str(self.lr_nombre)
'''
'''
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
'''


'''
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



'''





####________________________ DE LA HISTORICA (5 MINUTALES , CONSOLIDADOS (DIA,MES,AÑO ,AÑO HIDROLOGICO _____________####
#Los valores para consolidados diarios y menusales se pueden sacar tanto de la intranet como de la hisotrica
#Ahora mismo se sacan de la intranet
#esto se decide en el archivo intranetsaih/dbrouter.py



#
# class ConsDia(models.Model):
#     pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
#     cc_idsenal = models.ForeignKey('ListaSenales', models.DO_NOTHING, db_column='CC_IDSENAL')  # Field name made lowercase.
#     cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
#     cc_valor_min = models.FloatField(db_column='CC_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
#     cc_f_valor_min = models.DateTimeField(db_column='CC_F_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
#     cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
#     cc_valor_max = models.FloatField(db_column='CC_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
#     cc_f_valor_max = models.DateTimeField(db_column='CC_F_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
#     cc_valor_ultimo = models.FloatField(db_column='CC_VALOR_ULTIMO', blank=True, null=True)  # Field name made lowercase.
#     cc_valor_gradiente = models.FloatField(db_column='CC_VALOR_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
#     cc_calidad = models.ForeignKey('TiposCalidades', models.DO_NOTHING, db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
#     cc_porcen = models.FloatField(db_column='CC_PORCEN', blank=True, null=True)  # Field name made lowercase.
#     cc_f_gradiente = models.DateTimeField(db_column='CC_F_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
#     cc_volumen = models.FloatField(db_column='CC_VOLUMEN', blank=True, null=True)  # Field name made lowercase.
#     cc_traspaso_web = models.SmallIntegerField(db_column='CC_TRASPASO_WEB', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CONS_DIA'
#         unique_together = (('cc_idsenal', 'cc_fecha'),)
#
#
# class ConsMes(models.Model):
#     pk = models.CompositePrimaryKey('CC_IDSENAL', 'CC_FECHA')
#     cc_idsenal = models.ForeignKey('ListaSenales', models.DO_NOTHING, db_column='CC_IDSENAL')  # Field name made lowercase.
#     cc_fecha = models.DateTimeField(db_column='CC_FECHA')  # Field name made lowercase.
#     cc_valor_min = models.FloatField(db_column='CC_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
#     cc_f_valor_min = models.DateTimeField(db_column='CC_F_VALOR_MIN', blank=True, null=True)  # Field name made lowercase.
#     cc_valor = models.FloatField(db_column='CC_VALOR', blank=True, null=True)  # Field name made lowercase.
#     cc_valor_max = models.FloatField(db_column='CC_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
#     cc_f_valor_max = models.DateTimeField(db_column='CC_F_VALOR_MAX', blank=True, null=True)  # Field name made lowercase.
#     cc_valor_ultimo = models.FloatField(db_column='CC_VALOR_ULTIMO', blank=True, null=True)  # Field name made lowercase.
#     cc_valor_gradiente = models.FloatField(db_column='CC_VALOR_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
#     cc_calidad = models.ForeignKey('TiposCalidades', models.DO_NOTHING, db_column='CC_CALIDAD', blank=True, null=True)  # Field name made lowercase.
#     cc_porcen = models.FloatField(db_column='CC_PORCEN', blank=True, null=True)  # Field name made lowercase.
#     cc_f_gradiente = models.DateTimeField(db_column='CC_F_GRADIENTE', blank=True, null=True)  # Field name made lowercase.
#     cc_volumen = models.FloatField(db_column='CC_VOLUMEN', blank=True, null=True)  # Field name made lowercase.
#     cc_traspaso_web = models.SmallIntegerField(db_column='CC_TRASPASO_WEB', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'CONS_MES'
#         unique_together = (('cc_idsenal', 'cc_fecha'),)
#


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