from django import forms

class TarjetaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=5)
    modelo = forms.CharField(label="Modelo", max_length=20)
    tipo = forms.IntegerField(label="Tipo")    
    lr_dir_control = forms.CharField(label="Dirección de control", max_length=4)	  # Field name made lowercase.
    lr_dir_datos = forms.CharField(label="Dirección de datos", max_length=4)	  # Field name made lowercase.
    lrt_numdatos = forms.IntegerField(label="Numero de datos")  # Field name made lowercase.
    lrt_signo = forms.IntegerField(label="Signo")  # Field name made lowercase.
    lr_dir_ip = forms.CharField(max_length=20)	  # Field name made lowercase.
