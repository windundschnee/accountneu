
from django import forms
from .models import *
from django.utils.safestring import mark_safe
from django.urls import reverse



class KehldachSchneeForm(forms.ModelForm):

    class Meta:

        model = KehldachSchneeModel
        fields  = ['neigung_alpha1','neigung_alpha2']

        labels = {




            "neigung_alpha1": mark_safe('Dachneigung &alpha;<sub>1</sub> [°]'),
            "neigung_alpha2": mark_safe('Dachneigung &alpha;<sub>2</sub> [°]'),




        }

        widgets = {



            'neigung_alpha1': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': mark_safe('&alpha;1 in [°]'), 'type': 'number',}),
            'neigung_alpha2': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': mark_safe('&alpha;2 in [°]'), 'type': 'number',}),







        }
