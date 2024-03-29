from django.db import models
from account_app.models import User
from core.models import allgEingaben, Bauteil
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class FreistehendeDaecherModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    projekt = models.ForeignKey(allgEingaben, on_delete=models.CASCADE)


    bautteil_name = models.ForeignKey(Bauteil, on_delete=models.CASCADE)

    hoehe = models.DecimalField(decimal_places=2, max_digits=5, blank=False, null=True)
    breite_d = models.DecimalField(decimal_places=2, max_digits=5, blank=False, null=True)
    breite_b = models.DecimalField(decimal_places=2, max_digits=5, blank=False, null=True)
    alpha = models.DecimalField(decimal_places=2, max_digits=5, blank=False, null=True)
    phi = models.DecimalField(decimal_places=2, max_digits=5, blank=False, null=True)
    hoehe_GOK = models.DecimalField(decimal_places=2, max_digits=5, blank=False, null=True)
    some_field_radio = models.CharField(max_length=80, blank=False, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    freistehendedaecher_eingegeben = models.BooleanField(blank=False)
    edited_date = models.DateTimeField(blank=True, null=True)



    def __str__(self):
        return  self.bautteil_name.bautteil_name

    def get_absolute_url(self):
        return reverse('freistehendeDaecher_app:freistehende_daecher_redirect', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})

    def get_absolute_url2(self):
        return reverse('freistehendeDaecher_app:freistehende_daecher_update', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})

    def get_absolute_url3(self):
        return reverse('freistehendeDaecher_app:freistehende_daecher_detail', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})
