import json
from django import forms
from .models import *
from django.utils.safestring import mark_safe


CHOICES = (

                ('Vereinfachtes Verfahren gemäß ÖNORM B 1991-1-4, Abschnitt 9.2.4.1', 'Vereinfachtes Verfahren gemäß ÖNORM B 1991-1-4, Abschnitt 9.2.4.1'), #First one is the value of select option and second is the displayed value in option
                ('Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.4', 'Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.4'),

                )
CHOICES2 = (

                ('Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9', 'Innendruckbeiwerte mittels dominanter Fläche gemäß ÖNORM EN 1991-1-4 Abschnitt 7.2.9 (5)'), #First one is the value of select option and second is the displayed value in option
                ('Innendruckbeiwerte mittels Flächenparameter nach Abschnitt 7.2.9', 'Innendruckbeiwerte mittels Flächenparameter gemäß ÖNORM EN 1991-1-4 Abschnitt 7.2.9 (6)'),
                ('Innendruckbeiwerte mittels empfohlener Werte nach Abschnitt 9.2.10', 'Innendruckbeiwerte mittels empfohlener Werte gemäß ÖNORM B 1991-1-4 Abschnitt 9.2.10'),

                )





class pultdaecherForm(forms.ModelForm):




    class Meta:

        model = PultdachModel
        exclude = ['user', 'projekt', 'bautteil_name', 'date_posted',
         'pultdach_eingegeben', 'edited_date']

        labels = {

            "dachneigung": mark_safe('Neigungswinkel &alpha; [°]'),

            "hoehe": "Höhe h [m]:",
            "breite_x": "Breite x [m]:",
            "breite_y": "Breite y [m]:",
            "verfahren_wahl": "Berechnungsverfahren:",
            "innendruck_verfahren_wahl": "Berechnungsverfahren",

            "innendruck_cpi": mark_safe('Innendruckbeiwert c<sub>pi</sub> [-]:'),
            "flaechenparameter_mue": 'Flächenparameter [-]:',




        }

        widgets = {

            'dachneigung': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': mark_safe('&alpha; in [°]'), 'type': 'number',}),

            'hoehe': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'h in [m]', 'type': 'number',}),

            'breite_x': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'bx in [m]', 'type': 'number',}),

            'breite_y': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'by in [m]', 'type': 'number',}),

            'innendruck_cpi': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'cpi in [-]', 'type': 'number',

                    }),

            'flaechenparameter_mue': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'Flächenparameter in [-]', 'type': 'number',

                    }),


            'innendruck': forms.CheckboxInput(attrs={'class': 'custom-control-input',


            }),

            'verfahren_wahl': forms.RadioSelect(choices=CHOICES,attrs={'class': 'form-control-input'


            }),
            'innendruck_verfahren_wahl': forms.RadioSelect(choices=CHOICES2,attrs={'class': 'form-control-input',




            }),





        }
