from django import forms
from .models import *
from django.utils.safestring import mark_safe
class DatenbankMaterialForm(forms.ModelForm):


    class Meta:
        model = DatenbankMaterial
        exclude = ['user', ]
        labels = {

            'name': 'Schichtname',

            'wichte': mark_safe('Wichte &#947; [kN/m³]:'),


        }

        widgets = {


            'name': forms.TextInput(attrs={'placeholder': 'Schichtname', 'class': 'form-control'}),

            'wichte': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.1,
                    'placeholder': 'Wichte in [kN/m³]', 'type': 'number',}),



        }
