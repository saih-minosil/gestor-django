from django.contrib import admin
from gestor.models import Poblaciones,Rios,TiposSenales, UnidadesIngenieria
from gestor.admin import PoblacionesAdmin,TiposSenalesAdmin,UnidadesIngenieriaAdmin



#Otros
#####INTRANET + HISTORICA
admin.site.register(Poblaciones,PoblacionesAdmin)
admin.site.register(Rios)
admin.site.register(TiposSenales,TiposSenalesAdmin)
#Solo Intranet
admin.site.register(UnidadesIngenieria,UnidadesIngenieriaAdmin)


#### INFOPLUS
#gestor_admin_site.register(ListaOrdenes,ListaOrdenesAdmin)
#gestor_admin_site.register(FactoresConversionRemota,FactoresConversionRemotaAdmin)
#gestor_admin_site.register(FormatosDigitales,FormatosDigitalesAdmin)