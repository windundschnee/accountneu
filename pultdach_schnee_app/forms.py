
from django import forms
from .models import *
from django.utils.safestring import mark_safe
from django.urls import reverse



class PultdachSchneeForm(forms.ModelForm):

    class Meta:

        model = PultdachSchneeModel
        fields  = ['neigung','abrutschen_verhindert']

        labels = {




            "neigung": mark_safe('Dachneigung &alpha; [°]'),
            "abrutschen_verhindert": 'Das Abrutschen des Schnees wird verhindert',




        }

        widgets = {



            'neigung': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': mark_safe('&alpha; in [°]'), 'type': 'number',}),
            'neigung': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': mark_safe('&alpha; in [°]'), 'type': 'number',}),







        }
