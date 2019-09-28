
from django import forms
from .models import Gesamtgebaeude
from django.utils.safestring import mark_safe
from django.urls import reverse



class GesamtgebauedeForm(forms.ModelForm):

    class Meta:

        model = Gesamtgebaeude
        fields  = ['flachdach_app_wahl', 'app_wahl']
