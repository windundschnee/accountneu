import json
from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from .list_neu import wien_orte, bundesliste
from .alle_orte import alle_orte
gk = (
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
        )

class RegCarForm(forms.ModelForm):
    def clean_basiswinddruck(self):

        if self.data['seehoehe'] != '':
            seehoehe_passed = float(self.data['seehoehe'])
            seehoehe_hidden_passed = float(self.data['seehoehe_hidden'])

            seehoehe_req_diff =abs(seehoehe_hidden_passed-seehoehe_passed)
            basiswinddruck_passed = float(self.cleaned_data['basiswinddruck'])
            basiswinddruck_hidden_passed = float(self.data['basiswinddruck_hidden'])



            if seehoehe_req_diff > 250 and basiswinddruck_passed <= basiswinddruck_hidden_passed:
                raise forms.ValidationError(
                mark_safe('Die benutzerdefinierte Seehöhe ist mehr als 250m über jenem Wert aus ÖNORM NA 1991-1-4 Anhang A <a style="margin-left:8px" id="info_button5" type="button" class="myownclass" name="button"><i id="info_symbol" class="fa fa-info-circle"></i></a>'))

#"Die benutzerdefinierte Seehöhe ist mehr als 250m über jenem Wert aus ÖNORM NA 1991-1-4 Anhang A (siehe Info)"

        return self.cleaned_data['basiswinddruck']

    projekt_name = forms.CharField(
        label='Projektname:',
        widget=forms.TextInput(attrs={'placeholder': 'Mein Projekt', 'class': 'form-control'})
    )
    bundesland = forms.ChoiceField(
        label='Bundesland:',
        choices = bundesliste,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    ort = forms.ChoiceField(
        label='Ort:',
        choices = alle_orte,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    gelaendekategorie = forms.ChoiceField(
        label='Geländekategorie:',
        choices = gk,
        widget=forms.Select(attrs={'class': 'form-control'})

    )
    basiswinddruck = forms.DecimalField(
        label='Basiswinddruck [kN/m²]:',
        widget=forms.NumberInput(attrs={'class': 'form-control'}
                                    )
    )
    winddruck_benutzerdefiniert = forms.BooleanField(
        label='benutzerdefiniert',
        required=False,

    )
    seehoehe = forms.DecimalField(
        label='Seehöhe [m]:',
        widget=forms.NumberInput(attrs={'class': 'form-control'}
                                    )
    )
    seehoehe_benutzerdefiniert = forms.BooleanField(
        label='benutzerdefiniert',
        required=False,

    )
    windgeschwindigkeit = forms.DecimalField(
        label='Windgeschwindigkeit [m/s]:',
        widget=forms.NumberInput(attrs={'class': 'form-control',
                                        'readonly':'readonly'}
                                    )
    )
    schneelast = forms.DecimalField(
        label='Schneeregellast [kN/m²]:',
        widget=forms.NumberInput(attrs={'class': 'form-control'}
                                    )
    )


    abminderungsfaktor = forms.DecimalField(
        label=mark_safe('Abminderungsfaktor f<sub>s</sub> [-]:'),
        initial=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'},

                                    ),

    )
    basiswinddruck_hidden = forms.CharField(

        widget=forms.HiddenInput()
    )
    seehoehe_hidden = forms.CharField(

        widget=forms.HiddenInput()
    )
    schneelast_hidden = forms.CharField(

        widget=forms.HiddenInput()
    )






    class Meta:
        model = allgEingaben


        exclude = ('user', 'date_posted', 'allgEingaben_eingegeben',
                    'slug', 'edited_date')

SAMPLE_CHOICES_WIND=(
( 'Windlasten Freistehende Wände','Freistehende Wände'),
( 'Windlasten Freistehende Dächer','Freistehende Dächer'),
('Windlasten Gesamtgebaeude','Gesamtgebäude (Wände & Dach)'),
('Windlasten Flachdächer','Flachdächer'),
('Windlasten Pultdächer','Pultdächer'),
('Windlasten Anzeigetafeln','Anzeigetafeln'),
( 'Schneelasten Pultdächer',' Pult/Flachdächer'),
( 'Schneelasten Satteldächer','Satteldächer'),
( 'Schneelasten Kehldächer','Kehl/Sheddächer'),
)

class WindbemessungForm(forms.ModelForm):


    bautteil_name = forms.CharField(
        label='Bauteilname:',
        widget=forms.TextInput(attrs={'placeholder': 'Mein Bauteil', 'class': 'form-control'})
    )
    bemessungsart_wind_schnee = forms.ChoiceField(
        label='Windlasten:',
        choices = (SAMPLE_CHOICES_WIND),
        required=True,
        widget = forms.RadioSelect,

)



    class Meta:
        model = Bauteil
        fields = ['bautteil_name', 'bemessungsart_wind_schnee' ,]






class seehoeheForm(forms.ModelForm):


    class Meta:
        model = allgEingaben

        fields = ['seehoehe',]
        labels = {
            "seehoehe": "Seehöhe",
        }
        widgets = {
            'seehoehe': forms.NumberInput(attrs={'class': 'form-control',
                    'placeholder': 'Seehöhe in [m]', 'type': 'number',
                    'step': 0.1}),

        }

class abminderungsfaktorForm(forms.ModelForm):


    class Meta:
        model = allgEingaben

        fields = ['abminderungsfaktor',]
        labels = {
            "abminderungsfaktor": "Abminderungsfaktor:",
        }
        widgets = {
            'abminderungsfaktor': forms.NumberInput(attrs={'class': 'form-control',
                    'placeholder': 'Abminderungsfaktor', 'type': 'number',
                    'step': 0.01}),

        }
