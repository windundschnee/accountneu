from django.db import models
from account_app.models import User
from django.core.validators import MinValueValidator
from core.models import allgEingaben, Bauteil
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class FreistehendeWaende(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    projekt = models.ForeignKey(
        allgEingaben,
        on_delete=models.CASCADE,)


    bautteil_name = models.ForeignKey(
        Bauteil,
        on_delete=models.CASCADE,)

    hoehe_ueber_GOK = models.DecimalField(validators=[MinValueValidator(0)], decimal_places=2, max_digits=5, blank=False, null=True)
    wandhoehe = models.DecimalField(validators=[MinValueValidator(1)], decimal_places=2, max_digits=5, blank=False, null=True)
    wandlaenge = models.DecimalField(validators=[MinValueValidator(1)],decimal_places=2, max_digits=5, blank=False, null=True)
    wandverlauf = models.CharField(max_length=30, default='')
    schenkellaenge = models.DecimalField(validators=[MinValueValidator(0)], decimal_places=2, max_digits=5, blank=True, null=True)
    voelligkeitsgrad = models.CharField(max_length=30, default='')
    abschattung = models.CharField(max_length=30, default='')
    abstand_abschattendewand = models.DecimalField(validators=[MinValueValidator(0)], decimal_places=2, max_digits=5, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    freistehendewaende_eingegeben = models.BooleanField(blank=False)
    edited_date = models.DateTimeField(blank=True, null=True)
    hoehe_abschattende_wand = models.DecimalField(validators=[MinValueValidator(0)], decimal_places=2, max_digits=5, blank=True, null=True)



    def __str__(self):
        return  self.bautteil_name.bautteil_name

    def get_absolute_url(self):
        return reverse('freistehende_waende_app:freistehende_waende_redirect', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})

    def get_absolute_url2(self):
        return reverse('freistehende_waende_app:freistehende_waende_update', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})

    def get_absolute_url3(self):
        return reverse('freistehende_waende_app:freistehende_waende_detail', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})
