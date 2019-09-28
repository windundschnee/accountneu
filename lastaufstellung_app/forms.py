from django import forms
from .models import *
from django.forms.models import inlineformset_factory
from django.utils.safestring import mark_safe
class HomogeneSchichtForm(forms.ModelForm):
    class Meta:
        model = HomogeneSchicht
        exclude = ['user','slug', 'bauteil']
        labels = {

            'schichtname': 'Schichtname',
            'dicke': 'Dicke [cm]',
            'wichte': 'Material',
            'last': 'Flächenlast [kN/m²]',

        }

        widgets = {


            'schichtname': forms.TextInput(attrs={'placeholder': 'Schichtname', 'class': 'form-control'}),
            'dicke': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.1,
                    'placeholder': 'Dicke in [cm]', 'type': 'number',}),

            'last': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.1,
                    'placeholder': 'Flächenlast in [kN/m²]', 'type': 'number',}),


        }

class BauteilForm(forms.ModelForm):


    class Meta:
        model = Bauteil_Last
        exclude = ['user', 'slug']
        labels = {

            'name': 'Bauteilname',

        }

        widgets = {


            'name': forms.TextInput(attrs={'placeholder': 'Mein Bauteil', 'class': 'form-control'}),

        }

SchichtenFormSet = inlineformset_factory(
    Bauteil_Last,HomogeneSchicht, form=HomogeneSchichtForm,
    fields=['schichtname','wichte','last', 'dicke',], extra=2, can_delete=True
    )
