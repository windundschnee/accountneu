from django.db import models
from account_app.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from core.models import allgEingaben, Bauteil
from django.urls import reverse
from django.template.defaultfilters import slugify
import uuid
# Create your models here.
class PultdachSchneeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    projekt = models.ForeignKey(
        allgEingaben,
        on_delete=models.CASCADE,)


    bautteil_name = models.ForeignKey(
        Bauteil,
        on_delete=models.CASCADE,)



    neigung = models.DecimalField(validators=[MaxValueValidator(90), MinValueValidator(0)],decimal_places=2, max_digits=5, blank=False, null=True)

    abrutschen_verhindert = models.BooleanField(blank=False, default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    pultdach_schnee_eingegeben = models.BooleanField(blank=False)
    edited_date = models.DateTimeField(blank=True, null=True)






    def __str__(self):
        return self.bautteil_name.bautteil_name

    def get_absolute_url(self):
        return reverse('pultdach_schnee_app:pultdach_schnee_redirect', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})

    def get_absolute_url2(self):
        return reverse('pultdach_schnee_app:pultdach_schnee_update', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})

    def get_absolute_url3(self):
        return reverse('pultdach_schnee_app:pultdach_schnee_detail', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})
