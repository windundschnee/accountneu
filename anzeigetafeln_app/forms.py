
from django import forms
from .models import *
from django.utils.safestring import mark_safe
from django.urls import reverse



class anzeigetafelnForm(forms.ModelForm):

    class Meta:

        model = AnzeigetafelnModel
        fields  = ['hoehe', 'breite', 'abstand_zum_grund',
         'anzeigetafeln_eingegeben', 'edited_date']

        labels = {

            "hoehe": "Höhe h [m]:",
            "breite": "Breite b [m]:",


            "abstand_zum_grund": mark_safe('Bodenabstand z<sub>g</sub> [m]:'),




        }

        widgets = {



            'hoehe': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'h in [m]', 'type': 'number',}),
            'breite': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'b in [m]', 'type': 'number',}),
            'abstand_zum_grund': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'zg in [m]', 'type': 'number',}),






        }
