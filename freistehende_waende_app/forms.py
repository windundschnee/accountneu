import json
from django import forms
from .models import *
from django.utils.safestring import mark_safe
gk = (
        ('Gerade Wand', 'Gerade Wand'),
        ('Abgewinkelte Wand', 'Abgewinkelte Wand'),
        )
voelligkeitsgrad_liste = (
        ('0,8', '0,8'),
        ('1,0', '1,0'),
        )
ja_nein_liste = (
        ('Nein', 'Nein'),
        ('Ja', 'Ja'),
        )



class FreistehendeWaendeForm(forms.ModelForm):

    wandverlauf = forms.ChoiceField(choices=(gk), widget=forms.Select(attrs={'class':'form-control'}))
    voelligkeitsgrad = forms.ChoiceField(choices=(voelligkeitsgrad_liste),  label='Völligkeitsgrad',  widget=forms.Select(attrs={'class':'form-control'}))
    abschattung = forms.ChoiceField(choices=(ja_nein_liste), label='Abschattung vorhanden?', widget=forms.Select(attrs={'class':'form-control'}))


    def clean_wandlaenge(self):

        wandhoehe_passed = self.cleaned_data.get("wandhoehe")
        wandlaenge_passed = self.cleaned_data.get("wandlaenge")




        wandlaenge_req = 0.3* float(wandhoehe_passed)
        if wandlaenge_passed <= wandlaenge_req:
            raise forms.ValidationError("Die Wandlänge sollte größer als 0,3 * Wandhöhe sein!")
        return wandlaenge_passed

    class Meta:

        model = FreistehendeWaende
        exclude = ['user','bautteil_name', 'projekt', 'date_posted',
         'freistehendewaende_eingegeben', 'edited_date']

        labels = {
            "hoehe": "Höhe [m]:",
            "hoehe_ueber_GOK": "Höhe über Geländeoberkante z [m]:",
            "wandhoehe": "Wandhöhe h [m]:",
            "wandlaenge": "Wandlänge L [m]:",
            "abstand_abschattendewand": "Abstand zur abschattenden Wand [m]:",

            "schenkellaenge": mark_safe('Schenkellänge L<sub>s</sub> [m]'),
            "hoehe_abschattende_wand": mark_safe('Höhe der abschattenden Wand h<sub>s</sub> [m]'),


        }
        widgets = {

            'hoehe': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'h in [m]', 'type': 'number',}),
            'hoehe_ueber_GOK': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'Z in [m]', 'type': 'number',}),

            'wandhoehe': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'h in [m]', 'type': 'number',}),
            'wandlaenge': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'L in [m]', 'type': 'number',}),
            'schenkellaenge': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'Ls in [m]', 'type': 'number',}),
            'abstand_abschattendewand': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'Abstand in [m]', 'type': 'number',}),
            'hoehe_abschattende_wand': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'Höhe in [m]', 'type': 'number',}),



        }
