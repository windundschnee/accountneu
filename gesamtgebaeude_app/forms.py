
from django import forms
from .models import Gesamtgebaeude
from django.utils.safestring import mark_safe
from django.urls import reverse

DACHART = (
        ('Flachdach', 'Flachdach'),
        ('Satteldach', 'Satteldach'),
        ('Pultdach', 'Pultdach'),
        ('Trogdach', 'Trogdach'),
        )

class GesamtgebauedeForm(forms.ModelForm):
    dach_wahl = forms.ChoiceField(
        label='Dachart:',
        choices = DACHART,
        widget=forms.Select(attrs={'class': 'form-control'})

    )

    class Meta:

        model = Gesamtgebaeude
        fields  = ['dach_wahl']
