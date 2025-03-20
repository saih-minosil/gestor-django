import django
from django.db.models import Model
from django.db.models.options import Options


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
        if model._meta.app_label in self.default_app_labels:
            return "default"
        elif model._meta.app_label in self.vsad_app_labels:
            return"vsad"
        elif model._meta.app_label in self.manager_app_labels:
            if str(model._meta)=="admin.logentry":
                return "default"
            else:
                return "gestor"
        elif model._meta.app_label in self.intranet_app_labels:
            if model._meta.db_table in self.tablas_datos_historicos or model._meta.db_table.startswith("DATOS_T") or model._meta.db_table.startswith("DATOS_V"):
                return "historica"
            else:
                return "intranet"

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.default_app_labels:
            return "default"
        elif model._meta.app_label in self.manager_app_labels:
            return "default"
        elif model._meta.app_label in self.intranet_app_labels:
            return "default"
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