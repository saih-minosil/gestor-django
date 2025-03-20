from django.contrib import admin
from .models import ListaSenales,ListaEstaciones,ListaRemotas,CajetinesWeb,CajetinesUnifilares, Rios, Poblaciones
# Register your models here.
admin.site.register(ListaEstaciones)
admin.site.register(ListaSenales)
admin.site.register(ListaRemotas)
admin.site.register(Rios)
admin.site.register(Poblaciones)