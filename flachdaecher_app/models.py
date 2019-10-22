from django.db import models
from account_app.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import allgEingaben, Bauteil
from django.urls import reverse
from django.utils import timezone
from django.core.validators import DecimalValidator

# Create your models here.
class FlachdachModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    projekt = models.ForeignKey(
        allgEingaben,
        on_delete=models.CASCADE,)


    bautteil_name = models.ForeignKey(
        Bauteil,
        on_delete=models.CASCADE,)
    art_traufenbereich = models.CharField(max_length=80, default='')
    hoehe_attika = models.DecimalField(decimal_places=1, max_digits=7, blank=True, null=True)
    alpha = models.DecimalField(decimal_places=2, max_digits=7, blank=True, null=True)
    radius = models.DecimalField(decimal_places=1, max_digits=7, blank=True, null=True)



    hoehe = models.DecimalField(decimal_places=1, max_digits=7, blank=False, null=True)
    breite_x = models.DecimalField(decimal_places=1, max_digits=7, blank=False, null=True)
    breite_y = models.DecimalField(decimal_places=1, max_digits=7, blank=False, null=True)
    innendruck = models.BooleanField(blank=True, null=True, default=True)


    innendruck_empfohlen = models.BooleanField(default=True, blank=True, null=True)

    some_field = models.CharField(max_length=80, blank=False)
    some_field_radio2 = models.CharField(max_length=80, blank=True, null=True, default=1)
    cpe_wahl = models.CharField(max_length=80, blank=True, null=True, default=1)
    cpe_1_einflussflaeche = models.CharField(max_length=80, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    flachdach_eingegeben = models.BooleanField(blank=False)
    edited_date = models.DateTimeField(blank=True, null=True)
    waende_beruecksichtigen = models.BooleanField(blank=True, null=True, default=False)
    oeffnungen_beruecksichtigen = models.BooleanField(blank=True, null=True, default=False)
    oeffnung_nord_flaeche = models.DecimalField(decimal_places=1, max_digits=7, blank=True, null=False, default=0)
    oeffnung_ost_flaeche = models.DecimalField(decimal_places=1, max_digits=7, blank=True, null=False, default=0)
    oeffnung_sued_flaeche = models.DecimalField(decimal_places=1, max_digits=7, blank=True, null=False, default=0)
    oeffnung_west_flaeche = models.DecimalField(decimal_places=1, max_digits=7, blank=True, null=False, default=0)
    reibung_beruecksichtigen = models.BooleanField(blank=True, null=True, default=False)
    reibbeiwert_dach = models.DecimalField(decimal_places=2,default=0, max_digits=7, blank=True, null=True)
    reibbeiwert_dach_benutzerdef = models.BooleanField(blank=True, null=True, default=True)
    reibbeiwerte_dach_wahl = models.CharField(max_length=80, blank=False, default='test')
    reibbeiwert_waende_benutzerdef = models.BooleanField(blank=True, null=True, default=True)
    reibbeiwert_waende = models.DecimalField(decimal_places=2,default=0, max_digits=7, blank=True, null=True)
    reibbeiwerte_waende_wahl = models.CharField(max_length=80, blank=False, default='test')
    anzahl_streifen = models.CharField(max_length=80, blank=True, null=True, default=2)
    fehlende_korrelation_beruecksichtigen = models.BooleanField(blank=True, null=True, default=False)



    def __str__(self):
        return  self.bautteil_name.bautteil_name
    def get_absolute_url(self):
        return reverse('flachdaecher_app:flachdach_redirect', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})

    def get_absolute_url2(self):
        return reverse('flachdaecher_app:flachdach_update', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})

    def get_absolute_url3(self):
        return reverse('flachdaecher_app:flachdach_detail', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})
