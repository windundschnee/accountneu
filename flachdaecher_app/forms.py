import json
from django import forms
from .models import *
from django.utils.safestring import mark_safe
arten_traufbereich = (
    ('scharfkantiger Traufbereich', 'scharfkantiger Traufbereich'),
    ('mit Attika', 'mit Attika'),
    ('abgerundeter Traufbereich', 'abgerundeter Traufbereich'),
    ('mansardenartig abgeschrägter Traufbereich',
     'mansardenartig abgeschrägter Traufbereich'),
)
anzahl_streifen_wahl = (

    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),



)
CHOICES = (

    # First one is the value of select option and second is the displayed value in option
    ('Vereinfachtes Verfahren gemäß ÖNORM B 1991-1-4, Abschnitt 9.2.3.1',
     'Vereinfachtes Verfahren gemäß ÖNORM B 1991-1-4, Abschnitt 9.2.3.1'),
    ('Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.3',
     ' Verfahren gemäß ÖNORM EN 1991-1-4, Abschnitt 7.2.3'),

)
CHOICES2 = (

    # First one is the value of select option and second is the displayed value in option
    ('Innendruckbeiwerte mittels dominanter Fläche nach Abschnitt 7.2.9',
     'Innendruckbeiwerte gemäß ÖNORM EN 1991-1-4 Abschnitt 7.2.9'),

    ('Innendruckbeiwerte mittels empfohlener Werte nach Abschnitt 9.2.10',
     'Innendruckbeiwerte mittels empfohlener Werte gemäß ÖNORM B 1991-1-4 Abschnitt 9.2.10'),

)




class flachdaecherForm(forms.ModelForm):

    art_traufenbereich = forms.ChoiceField(required=False, choices=(
        arten_traufbereich), label='Art des Traufenbereichs:', widget=forms.Select(attrs={'class': 'form-control', 'onclick': 'bildLaden()'}))
    anzahl_streifen = forms.ChoiceField(required=False, choices=(
        anzahl_streifen_wahl), label='Anzahl der Streifen', widget=forms.Select(attrs={'class': 'form-control', }))

    class Meta:

        model = FlachdachModel
        exclude = ['user', 'projekt', 'bautteil_name', 'date_posted',
                   'flachdach_eingegeben', 'edited_date']

        labels = {
            "hoehe_attika": mark_safe('Höhe Attika h<sub>p</sub> [m]'),
            "alpha": mark_safe('Winkel &alpha; [°]'),
            "radius": "Radius r [m]:",
            "hoehe": "Höhe h [m]:",
            "breite_x":  mark_safe('Länge l<sub>Westen</sub> [m]'),
            "breite_y":  mark_safe('Länge l<sub>Süd</sub> [m]'),

            "some_field": "Berechnungsverfahren:",
            "some_field_radio2": "Berechnungsverfahren",

            "innendruck_cpi": mark_safe('Innendruckbeiwert c<sub>pi</sub> [-]:'),
            "flaechenparameter_mue": 'Flächenparameter [-]:',
            "oeffnung_nord_prozent": 'Nordwand:',
            "oeffnung_ost_prozent": 'Ostwand:',
            "oeffnung_sued_prozent": 'Südwand:',
            "oeffnung_west_prozent": 'Westwand:',
            "oeffnung_nord_flaeche": 'Nordwand:',
            "oeffnung_ost_flaeche": 'Ostwand:',
            "oeffnung_sued_flaeche": 'Südwand:',
            "oeffnung_west_flaeche": 'Westwand:',
            "oeffnungen_beruecksichtigen": 'oeffnungen_beruecksichtigen',
            "reibbeiwert_dach":mark_safe('Reibbeiwert Dach c<sub>fr</sub> [-]:'),
            "reibbeiwert_waende":mark_safe('Reibbeiwert Wände c<sub>fr</sub> [-]:'),

        }

        widgets = {



            'hoehe_attika': forms.NumberInput(attrs={'class': 'form-control',
                                                     'step': 0.01,
                                                     'placeholder': 'hp in [m]', 'type': 'number', }),
            'alpha': forms.NumberInput(attrs={'class': 'form-control',
                                              'step': 0.01,
                                              'placeholder': mark_safe('&alpha; in [°]'), 'type': 'number', }),
            'radius': forms.NumberInput(attrs={'class': 'form-control',
                                               'step': 0.01,
                                               'placeholder': 'r in [m]', 'type': 'number', }),
            'hoehe': forms.NumberInput(attrs={'class': 'form-control',
                                              'step': 0.01,
                                              'placeholder': 'h in [m]', 'type': 'number', }),

            'breite_x': forms.NumberInput(attrs={'class': 'form-control',
                                                 'step': 0.01,
                                                 'placeholder': 'lwest in [m]', 'type': 'number', }),

            'breite_y': forms.NumberInput(attrs={'class': 'form-control',
                                                 'step': 0.01,
                                                 'placeholder': 'lsüd in [m]', 'type': 'number', }),

            'innendruck_cpi': forms.NumberInput(attrs={'class': 'form-control',
                                                       'step': 0.01,
                                                       'placeholder': 'cpi in [-]', 'type': 'number',

                                                       }),

            'flaechenparameter_mue': forms.NumberInput(attrs={'class': 'form-control',
                                                              'step': 0.01,
                                                              'placeholder': 'Flächenparameter in [-]', 'type': 'number',

                                                              }),


            'innendruck': forms.CheckboxInput(attrs={'class': 'onoffswitch-checkbox',


                                                     }),

            'some_field': forms.RadioSelect(choices=CHOICES, attrs={'class': 'form-control-input'


                                                                    }),
            'some_field_radio2': forms.RadioSelect(choices=CHOICES2, attrs={'class': 'form-control-input',




                                                                            }),
            'oeffnungen_beruecksichtigen': forms.CheckboxInput(attrs={'class': 'onoffswitch-checkbox',


                                                                      }),
            'oeffnung_nord_prozent': forms.NumberInput(attrs={'class': 'form-control',
                                                              'step': 0.01,
                                                              'type': 'number', }),
            'oeffnung_ost_prozent': forms.NumberInput(attrs={'class': 'form-control',
                                                             'step': 0.01,
                                                             'type': 'number', }),
            'oeffnung_sued_prozent': forms.NumberInput(attrs={'class': 'form-control',
                                                              'step': 0.01,
                                                              'type': 'number', }),
            'oeffnung_west_prozent': forms.NumberInput(attrs={'class': 'form-control',
                                                              'step': 0.01,
                                                              'type': 'number', }),
            'oeffnung_nord_flaeche': forms.NumberInput(attrs={'class': 'form-control',
                                                              'step': 0.01,
                                                              'type': 'number', }),
            'oeffnung_ost_flaeche': forms.NumberInput(attrs={'class': 'form-control',
                                                             'step': 0.01,
                                                             'type': 'number', }),
            'oeffnung_sued_flaeche': forms.NumberInput(attrs={'class': 'form-control',
                                                              'step': 0.01,
                                                              'type': 'number', }),
            'oeffnung_west_flaeche': forms.NumberInput(attrs={'class': 'form-control',
                                                              'step': 0.01,
                                                              'type': 'number', }),

            'reibung_beruecksichtigen': forms.CheckboxInput(attrs={'class': 'onoffswitch-checkbox',


                                                                   }),
            'waende_beruecksichtigen': forms.CheckboxInput(attrs={'class': 'onoffswitch-checkbox',


                                                                  }),
            'fehlende_korrelation_beruecksichtigen': forms.CheckboxInput(attrs={'class': 'form-check-input',


                                                                                }),
            'reibbeiwert_dach': forms.NumberInput(attrs={'class': 'form-control',
                                                              'step': 0.01,
                                                              'type': 'number', }),


            'reibbeiwert_waende': forms.NumberInput(attrs={'class': 'form-control',
                                                              'step': 0.01,
                                                              'type': 'number', }),



        }

    def clean(self):


        super(flachdaecherForm, self).clean()
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        print(cleaned_data)
        print(cleaned_data)
        print(cleaned_data)
        print(cleaned_data)
        hoehe = self.cleaned_data.get("hoehe")
        hoehe_attika = self.cleaned_data.get("hoehe_attika")
        alpha = self.cleaned_data.get("alpha")
        radius = self.cleaned_data.get("radius")
        breite_x = self.cleaned_data.get("breite_x")
        breite_y = self.cleaned_data.get("breite_y")
        art_traufenbereich = self.cleaned_data.get("art_traufenbereich")
        oeffnungen_beruecksichtigen = self.cleaned_data.get(
            "oeffnungen_beruecksichtigen")
        oeffnung_nord_flaeche = self.cleaned_data.get("oeffnung_nord_flaeche")
        oeffnung_ost_flaeche = self.cleaned_data.get("oeffnung_ost_flaeche")
        oeffnung_sued_flaeche = self.cleaned_data.get("oeffnung_sued_flaeche")
        oeffnung_west_flaeche = self.cleaned_data.get("oeffnung_west_flaeche")
        if art_traufenbereich == 'mit Attika':
            if hoehe_attika is not None:

                hoehe_attika_req = 0.025 * float(hoehe)
                if hoehe_attika < hoehe_attika_req:
                    msg = "Die Attikahöhe sollte größer als 0,025 * Höhe sein!"
                    self.add_error('hoehe_attika', msg)


        if art_traufenbereich == 'abgerundeter Traufbereich':
            if radius is not None:
                radius_req = 0.05 * float(hoehe)
                if float(radius) < radius_req:
                    msg = "Der Radius sollte größer als 0,05 * Höhe sein!"
                    self.add_error('radius', msg)


        if art_traufenbereich == 'mansardenartig abgeschrägter Traufbereich':
            if alpha is not None:
                if float(alpha) < 30:
                    msg = mark_safe(
                        'Der Winkel &alpha; sollte mindestens 30° sein!')
                    self.add_error('alpha', msg)


        if oeffnungen_beruecksichtigen == True:
            if oeffnung_nord_flaeche is not None:
                if oeffnung_nord_flaeche > breite_y * hoehe:
                    msg = mark_safe(
                        'Die Öffnungen sind größer als die entsprechende Wandseite!')
                    self.add_error('oeffnung_nord_flaeche', msg)
            if oeffnung_ost_flaeche is not None:
                if oeffnung_ost_flaeche > float(breite_x) * float(hoehe):
                    msg = mark_safe(
                        'Die Öffnungen sind größer als die entsprechende Wandseite!')
                    self.add_error('oeffnung_ost_flaeche', msg)
            if oeffnung_sued_flaeche is not None:
                if oeffnung_sued_flaeche > float(breite_y) * float(hoehe):
                    msg = mark_safe(
                        'Die Öffnungen sind größer als die entsprechende Wandseite!')
                    self.add_error('oeffnung_sued_flaeche', msg)
            if oeffnung_west_flaeche is not None:
                if oeffnung_west_flaeche > float(breite_x) * float(hoehe):
                    msg = mark_safe(
                        'Die Öffnungen sind größer als die entsprechende Wandseite!')
                    self.add_error('oeffnung_west_flaeche', msg)

        return self.cleaned_data
