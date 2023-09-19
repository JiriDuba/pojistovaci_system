from django import forms
from .models import Pojisteni, Pojistenec

class PojisteniForm(forms.ModelForm):
    class Meta:
        model = Pojisteni
        fields = ['castka', 'predmet_pojisteni', 'platnost_od', 'platnost_do']
        widgets = {
            'platnost_od': forms.DateInput(attrs={'type':'date'}),
            'platnost_do': forms.DateInput(attrs={'type':'date'})
        }

class PojistenecForm(forms.ModelForm):
    class Meta:
        model = Pojistenec
        fields = ['jmeno', 'prijmeni', 'email', 'telefon', 'ulice_cislo', 'mesto', 'psc']
