from django.db import models
from account_app.models import User
from core.models import allgEingaben, Bauteil
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse




class PultdachModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    projekt = models.ForeignKey(
        allgEingaben,
        on_delete=models.CASCADE,)


    bautteil_name = models.ForeignKey(
        Bauteil,
        on_delete=models.CASCADE,)


    dachneigung = models.DecimalField(validators=[MaxValueValidator(75),MinValueValidator(5)],decimal_places=2, max_digits=5, blank=True, null=True)
    hoehe = models.DecimalField(decimal_places=2, max_digits=5, blank=False, null=True)
    breite_x = models.DecimalField(decimal_places=2, max_digits=5, blank=False, null=True)
    breite_y = models.DecimalField(decimal_places=2, max_digits=5, blank=False, null=True)
    innendruck = models.BooleanField(blank=True, null=True, default=True)
    innendruck_cpi = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    flaechenparameter_mue = models.DecimalField(validators=[MaxValueValidator(1),MinValueValidator(0.33)], decimal_places=2, max_digits=5, blank=True, null=True)
    innendruck_empfohlen = models.BooleanField(default=True, blank=True, null=True)

    verfahren_wahl = models.CharField(max_length=80, blank=False)
    innendruck_verfahren_wahl = models.CharField(max_length=80, blank=True, null=True, default=1)
    date_posted = models.DateTimeField(default=timezone.now)
    pultdach_eingegeben = models.BooleanField(blank=False)
    edited_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return  self.bautteil_name.bautteil_name



    def get_absolute_url2(self):
        return reverse('pultdaecher_app:pultdach_update', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})

    def get_absolute_url(self):
        return reverse('pultdaecher_app:pultdach_detail', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})
    def get_absolute_url3(self):
        return reverse('pultdaecher_app:pultdach_detail', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})
