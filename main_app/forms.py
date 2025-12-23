# forms.py
from django import forms
from .models_intranet import ListaEstaciones_I

SOURCE_CHOICES = [
    ("historica", "Historica"),
    ("intranet", "Intranet"),
    ("web_quince", "Web (Quinceminutales)"),
    ("web_horarios", "Web (Horarios)"),
]


class FormTraspaso(forms.Form):
    start_date = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "datetime-local"})
    )
    end_date = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "datetime-local"})
    )
    station = forms.ModelChoiceField(
        queryset=ListaEstaciones_I.objects.all()
    )
    source_1 = forms.ChoiceField(choices=SOURCE_CHOICES)
    source_2 = forms.ChoiceField(choices=SOURCE_CHOICES)