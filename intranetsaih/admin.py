from pprint import pp
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.utils.text import capfirst
from django.urls import NoReverseMatch, Resolver404, resolve, reverse, reverse_lazy
from django.apps import apps

'''
class AuthAdminSite(admin.AdminSite):
    def get_app_list(self, request,app_label = "gestor"):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        ordering = {
            "Usuarios": 1,            
        }
        #pp(request.__dict__)
        pp(self.urls)
        print(app_label)
        print(self.name)
        request.app_label=app_label
        app_label="gestor"
        app_dict = self._build_app_dict(request)       
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: ordering[x['name']])

        return app_list

    def _build_app_dict(self, request, label=None):
        """
        Build the app dictionary. The optional `label` parameter filters models
        of a specific app.
        """
        app_dict = {}

        if label:
            models = {
                m: m_a
                for m, m_a in self._registry.items()
                if m._meta.app_label == label
            }
        else:
            models = self._registry

        for model, model_admin in models.items():
            app_label = model._meta.app_label

            has_module_perms = model_admin.has_module_permission(request)
            if not has_module_perms:
                continue

            perms = model_admin.get_model_perms(request)

            # Check whether user has any perm for this module.
            # If so, add the module to the model_list.
            if True not in perms.values():
                continue

            info = (app_label, model._meta.model_name)
            print(info)
            model_dict = {
                "model": model,
                "name": capfirst(model._meta.verbose_name_plural),
                "object_name": model._meta.object_name,
                "perms": perms,
                "admin_url": None,
                "add_url": None,
            }
            if perms.get("change") or perms.get("view"):
                model_dict["view_only"] = not perms.get("change")
                try:
                    model_dict["admin_url"] = reverse(
                        "admin:%s_%s_changelist" % info, current_app=self.name
                    )
                except NoReverseMatch:
                    pass
            if perms.get("add"):
                try:
                    model_dict["add_url"] = reverse(
                        "admin:%s_%s_add" % info, current_app=self.name
                    )
                except NoReverseMatch:
                    pass
            pp(app_dict)            
            if app_label in app_dict:
                app_dict[app_label]["models"].append(model_dict)
            else:
                app_dict[app_label] = {
                    "name": apps.get_app_config(app_label).verbose_name,
                    "app_label": app_label,
                    "app_url":"", 
                    #reverse(
                    #    "admin:app_list",
                    #    kwargs={"app_label": app_label},
                    #    current_app=self.name,
                    #),
                    "has_module_perms": has_module_perms,
                    "models": [model_dict],
                }

        return app_dict    

    def get_urls(self):
        urls= super().get_urls()
        pp(urls)
        dir()
        return urls
    '''

auth_admin_site = admin.AdminSite(name="auth")


#admin_site.get_urls=
#admin_site.request.current_app

auth_admin_site.register(auth_views.UserModel)

