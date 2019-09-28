import json
from django import forms
from .models import *
from django.utils.safestring import mark_safe


CHOICES = (

                ('Freistehendes Flach/Pultdach', 'Freistehendes Flach/Pultdach'), #First one is the value of select option and second is the displayed value in option
                ('Freistehendes Satteldach', 'Freistehendes Satteldach'),
                ('Freistehendes Trogdach', 'Freistehendes Trogdach'),

                )



class FreistehendeDaecherForm(forms.ModelForm):

    def clean(self):
        some_field_radio  = self.cleaned_data.get("some_field_radio")
        alpha = self.cleaned_data.get("alpha")
        phi = self.cleaned_data.get("phi")
        hoehe_GOK = self.cleaned_data.get("hoehe_GOK")
        hoehe = self.cleaned_data.get("hoehe")
        if hoehe < 0:
            msg = "Höhe  sollte mindestens 0 sein!"
            self.add_error('hoehe', msg)



        if some_field_radio == 'Freistehendes Flach/Pultdach':
            if alpha < 0 or alpha > 30:
                msg = mark_safe('Der Winkel &alpha; sollte zwischen 0 und 30° sein!')
                self.add_error('alpha', msg)


        if hoehe_GOK < 0:
            msg = "Höhe über GOK sollte mindestens 0 sein!"
            self.add_error('hoehe_GOK', msg)


        if phi < 0 or phi > 1:
            msg = mark_safe('Der Versperrungsgrad &phi; sollte zwischen 0 und 1 sein!')

            self.add_error('phi', msg)

        return self.cleaned_data




    class Meta:

        model = FreistehendeDaecherModel
        exclude = ['user', 'projekt', 'bautteil_name', 'date_posted',
         'freistehendedaecher_eingegeben', 'edited_date']

        labels = {
            "breite_d": 'Tiefe d [m]:',
            "breite_b": "Breite b [m]:",
            "alpha": mark_safe('Winkel &alpha; [°]'),
            "hoehe":"Höhe h [m]:",
            "phi": mark_safe('Versperrungsgrad &phi; [-]'),
            "hoehe_GOK": "Höhe über GOK z: [m]",
            "some_field_radio":"Dachform:",
        }

        widgets = {


            'hoehe': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'h in [m]', 'type': 'number',}),
            'breite_d': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'd in [m]', 'type': 'number',}),
            'alpha': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': mark_safe('&alpha; in [°]'), 'type': 'number',}),
            'phi': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': mark_safe('&phi; in [-]'), 'type': 'number',}),
            'hoehe_GOK': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'z in [m]', 'type': 'number',}),

            'breite_b': forms.NumberInput(attrs={'class': 'form-control',
                    'step': 0.01,
                    'placeholder': 'b in [m]', 'type': 'number',}),





            'some_field_radio': forms.RadioSelect(choices=CHOICES,attrs={'class': 'form-control-input',}),





        }
