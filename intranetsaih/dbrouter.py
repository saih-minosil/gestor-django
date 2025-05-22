import django
from django.db.models import Model
from django.db.models.options import Options
from pprint import pp


class DbRouter:
    """
    A router to control all database operations on models depending on the application that uses them
    """

    default_app_labels = {"auth", "contenttypes","sessions","messages"}
    manager_app_labels = {"admin", "gestor"}
    intranet_app_labels={"main_app"}
    historica_app_labels={"historica"}
    vsad_app_labels={"vsad"}
    tablas_datos_historicos=["CONS_ANO_N","CONS_ANO_H"] #,"DATOS_TREAL","DATOS_VALID" se compruebamn por startswith para incluir las mensuales ya nuales (consulta rapida)

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.default_app_labels: #MAIN BBDD(Users, messages, etc)
            return "default"
        elif model._meta.app_label in self.vsad_app_labels: #VSAD APP
            return"vsad"
        elif model._meta.app_label in self.manager_app_labels:  #ADMIN
            if str(model._meta)=="admin.logentry":
                return "default"                            #USERS
            else:
                return "gestor"                                 #GESTOR
        elif model._meta.app_label in self.intranet_app_labels:
            #print(model._meta.db_table)
            #pp(model.__dict__)
            #pp(model._meta.__dict__)
            #pp(model.__class__)
           
            if model.__module__ == "main_app.models_hist":
            #if model._meta.db_table in self.tablas_datos_historicos or model._meta.db_table.startswith("DATOS_T") or model._meta.db_table.startswith("DATOS_V") or model._meta.db_table.endswith("_H"):
                print("Leyendo BBDD historica")
                return "historica"
            else:
                print("Leyendo BBDD intranet")
                return "intranet"

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.default_app_labels: #USERS,MESSAGES,ETC (SYSTEM)
            return "default"
        elif model._meta.app_label in self.manager_app_labels: 
            if str(model._meta)=="admin.logentry":  #USERS ADMIN
                return "default"
            else:                                   #GESTOR BB.DD                
                return "gestor"
        elif model._meta.app_label in self.intranet_app_labels:  #NO SE ESCRIBEN DATOS!!!!SOLO CONFIGURACIÓN (POR AHORA)
            #if  model._meta.db_table in self.tablas_datos_historicos or model._meta.db_table.startswith("DATOS_T") or model._meta.db_table.startswith("DATOS_V") or
            if model.__module__ == "main_app.models_hist":    #GESTOR ESCRIBIENDO EN HISTORICA
                return "historica"
            elif model.__module__ == "main_app.models_web":  #GESTOR ESCRIBIENDO EN WEB
                return "web"
            else:                                        #GESTOR ESCRIBIENDO EN INTRANET
                return "intranet"                      
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        #if (
        #    obj1._meta.app_label in self.default_app_labels
        #    or obj2._meta.app_label in self.default_app_labels
        #):
        return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        print("Trying to migrate : " + app_label)
        if app_label in self.default_app_labels:
            return db == "default"
        return None