from django.db import models
from account_app.models import User
from stdimage import StdImageField
from core.models import allgEingaben
from django.urls import reverse

from flachdaecher_app.models import FlachdachModel
from anzeigetafeln_app.models import AnzeigetafelnModel
from freistehende_waende_app.models import FreistehendeWaende
from freistehendeDaecher_app.models import FreistehendeDaecherModel
from pultdaecher_app.models import PultdachModel
from pultdach_schnee_app.models import PultdachSchneeModel
from kehldach_schnee_app.models import KehldachSchneeModel

class GesamtPdf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    projekt = models.ForeignKey(allgEingaben, on_delete=models.CASCADE,)
    logo_kopfzeile = StdImageField(upload_to='bilder/', blank=True, variations={'small': (160, 124),})
    pdf_bearbeitet = models.BooleanField(default=False)
    next = models.CharField(max_length=80, blank=True)
    kurz_lang_version = models.CharField(max_length=80, default="text", blank=False)
    kopfzeilen_art_wahl = models.CharField(max_length=80, default="text", blank=False)
    flachdach_app_wahl = models.ManyToManyField(FlachdachModel)
    anzeigetafeln_app_wahl = models.ManyToManyField(AnzeigetafelnModel)
    freistehendewaende_app_wahl = models.ManyToManyField(FreistehendeWaende)
    freistehendedaecher_app_wahl = models.ManyToManyField(FreistehendeDaecherModel)
    pultdach_app_wahl = models.ManyToManyField(PultdachModel)
    pultdach_schnee_app_wahl = models.ManyToManyField(PultdachSchneeModel)
    kehldach_schnee_app_wahl = models.ManyToManyField(KehldachSchneeModel)
    def __str__(self):
        return self.kurz_lang_version

    def get_absolute_url(self):
        return reverse('gesamt_pdf_app:gesamt_pdf_redirect', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})
    def get_absolute_url2(self):
        return reverse('gesamt_pdf_app:gesamt_pdf_update', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})
