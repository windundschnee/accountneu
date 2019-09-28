
from django import forms
from .models import *
from django.utils.safestring import mark_safe
from django.urls import reverse



class SatteldachSchneeForm(forms.ModelForm):

    class Meta:

        model = SatteldachSchneeModel
        fields  = ['neigung_alpha1','neigung_alpha2','abrutschen_verhindert']

        labels = {




            "neigung_alpha1": mark_safe('Dachneigung &alpha;<sub>1</sub> [°]'),
            "neigung_alpha2": mark_safe('Dachneigung &alpha;<sub>2</sub> [°]'),
            "abrutschen_verhindert": 'Das Abrutschen des Schnees wird verhindert',




        }

        widgets = {



            'neigung_alpha1': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': mark_safe('&alpha;1 in [°]'), 'type': 'number',}),
            'neigung_alpha2': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder':mark_safe('&alpha;2 [°]'), 'type': 'number',}),







        }
