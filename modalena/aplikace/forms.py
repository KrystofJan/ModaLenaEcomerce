from django import forms
from .models import Adresa,Zakaznik,ZakazikAccount,Produkt

class ZakaznikForm(forms.ModelForm):
    class Meta:
        model = Zakaznik
        exclude = ['adresa']

class AdresaForm(forms.ModelForm):
    class Meta:
        model = Adresa
        exclude = []
class LogInForm(forms.ModelForm):
    class Meta:
        model = ZakazikAccount
        exclude = []

class ProduktForm(forms.ModelForm):
    class Meta:
        model = Produkt
        exclude = []
"""    form_jmeno = forms.CharField(label = "Jméno")
    form_prijmei = form.CharField(label = "Příjmení")
    form_email = form.CharField(label = "e-mail")
    form_telefoni_cislo = form.CharField(label="Telefonní číslo")
"""

