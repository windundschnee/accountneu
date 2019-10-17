from django import forms
from .models import *
from anzeigetafeln_app.models import AnzeigetafelnModel
from freistehende_waende_app.models import FreistehendeWaende
from flachdaecher_app.models import FlachdachModel
from anzeigetafeln_app.models import AnzeigetafelnModel
from stdimage import StdImageField
from freistehendeDaecher_app.models import FreistehendeDaecherModel
from pultdaecher_app.models import PultdachModel
from pultdach_schnee_app.models import PultdachSchneeModel
from itertools import chain
from operator import attrgetter
from freistehende_waende_app.models import FreistehendeWaende
from django.utils.safestring import mark_safe
from .models import GesamtPdf
from satteldach_schnee_app.models import SatteldachSchneeModel
from kehldach_schnee_app.models import KehldachSchneeModel
CHOICES = (
        ('kurzversion', 'Kurzversion'),
        ('langversion', 'Langversion'),


        )
CHOICES2 = (
        ('kopfzeile 1', 'Kopfzeile 1'),
        ('kopfzeile 2', 'Kopfzeile 2'),
        ('kopfzeile 3', 'Kopfzeile 3'),


        )
class pdfBearbeitenForm(forms.ModelForm):
    kurz_lang_version = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-control-input'}))
    kopfzeilen_art_wahl = forms.ChoiceField(choices=CHOICES2, widget=forms.RadioSelect(attrs={'class': 'form-control-input'}))
    

    def __init__(self,meinProjekt_pk, next, user, *args, **kwargs):
        super(pdfBearbeitenForm, self).__init__(*args, **kwargs)
        #hier muss ich für jedes app hinzufügen
        self.fields['next'].initial = next
        #aus jedem App hole ich die Objekte je Projekt um sie
        #in der Bauteilliste anzuzeigen und hole die jeweiligen pk´s

        flachdach_bauteile = FlachdachModel.objects.filter(user=user, projekt_id=meinProjekt_pk).all()
        self.fields['flachdach_app_wahl'] = forms.ModelMultipleChoiceField(label='Windlasten Flachdächer',queryset=flachdach_bauteile,required=False,widget = forms.CheckboxSelectMultiple,)
        anzeigetafeln_bauteile = AnzeigetafelnModel.objects.filter(user=user, projekt_id=meinProjekt_pk).all()
        self.fields['anzeigetafeln_app_wahl'] = forms.ModelMultipleChoiceField(label='Windlasten Anzeigetafeln',queryset=anzeigetafeln_bauteile,required=False,widget = forms.CheckboxSelectMultiple,)

        freistehend_waende_bauteile = FreistehendeWaende.objects.filter(user=user, projekt_id=meinProjekt_pk).all()
        self.fields['freistehendewaende_app_wahl'] = forms.ModelMultipleChoiceField(label='Windlasten Freistehende Wände',queryset=freistehend_waende_bauteile,required=False,widget = forms.CheckboxSelectMultiple,)

        freistehend_daecher_bauteile = FreistehendeDaecherModel.objects.filter(user=user, projekt_id=meinProjekt_pk).all()
        self.fields['freistehendedaecher_app_wahl'] = forms.ModelMultipleChoiceField(label='Windlasten Freistehende Dächer',queryset=freistehend_daecher_bauteile,required=False,widget = forms.CheckboxSelectMultiple,)


        pultdach_bauteile = PultdachModel.objects.filter(user=user, projekt_id=meinProjekt_pk).all()
        self.fields['pultdach_app_wahl'] = forms.ModelMultipleChoiceField(label='Windlasten Pultdächer',queryset=pultdach_bauteile,required=False,widget = forms.CheckboxSelectMultiple,)
        pultdach_schnee_bauteile = PultdachSchneeModel.objects.filter(user=user, projekt_id=meinProjekt_pk).all()
        self.fields['pultdach_schnee_app_wahl'] = forms.ModelMultipleChoiceField(label='Schneelasten Pultdächer',queryset=pultdach_schnee_bauteile,required=False,widget = forms.CheckboxSelectMultiple,)
        satteldach_schnee_bauteile = SatteldachSchneeModel.objects.filter(user=user, projekt_id=meinProjekt_pk).all()
        self.fields['satteldach_schnee_app_wahl'] = forms.ModelMultipleChoiceField(label='Schneelasten Satteldächer',queryset=satteldach_schnee_bauteile,required=False,widget = forms.CheckboxSelectMultiple,)
        kehldach_schnee_bauteile = KehldachSchneeModel.objects.filter(user=user, projekt_id=meinProjekt_pk).all()
        self.fields['kehldach_schnee_app_wahl'] = forms.ModelMultipleChoiceField(label='Schneelasten Kehldächer',queryset=kehldach_schnee_bauteile,required=False,widget = forms.CheckboxSelectMultiple,)


    class Meta:
        model = GesamtPdf
        exclude = ['user','projekt', 'pdf_bearbeitet']
