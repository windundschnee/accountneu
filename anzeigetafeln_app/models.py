from django.db import models
from account_app.models import User

from django.utils import timezone
from core.models import allgEingaben, Bauteil
from django.urls import reverse
from django.template.defaultfilters import slugify
import uuid
# Create your models here.
class AnzeigetafelnModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    projekt = models.ForeignKey(
        allgEingaben,
        on_delete=models.CASCADE,)


    bautteil_name = models.ForeignKey(
        Bauteil,
        on_delete=models.CASCADE,)



    hoehe = models.DecimalField(decimal_places=2, max_digits=5, blank=False, null=True)
    breite = models.DecimalField(decimal_places=2, max_digits=5, blank=False, null=True)
    abstand_zum_grund = models.DecimalField(decimal_places=2, max_digits=5, blank=False, null=True)

    date_posted = models.DateTimeField(default=timezone.now)
    anzeigetafeln_eingegeben = models.BooleanField(blank=False)
    edited_date = models.DateTimeField(blank=True, null=True)






    def __str__(self):
        return self.bautteil_name.bautteil_name

    def get_absolute_url(self):
        return reverse('anzeigetafeln_app:anzeigetafeln_redirect', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})

    def get_absolute_url2(self):
        return reverse('anzeigetafeln_app:anzeigetafeln_update', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})

    def get_absolute_url3(self):
        return reverse('anzeigetafeln_app:anzeigetafeln_detail', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})
