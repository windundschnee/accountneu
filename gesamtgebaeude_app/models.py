from django.db import models
from account_app.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from core.models import allgEingaben
from django.template.defaultfilters import slugify
from django.urls import reverse
import uuid
from flachdaecher_app.models import FlachdachModel
from core.models import Bauteil

SAMPLE_CHOICES2=(
( 'Freistehende Wände','Freistehende Wände'),
('Flachdach','Flachdach'),
('Anzeigetafeln','Anzeigetafeln'),
('Satteldach','Satteldach'),

)



DEFAULT_EXAM_ID = 1


class Gesamtgebaeude(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dach_wahl = models.CharField(max_length=100, null=False, default="Dachwahl")



    
    bautteil_name = models.ForeignKey(
        Bauteil,
        on_delete=models.CASCADE, default=1)
    projekt = models.ForeignKey(allgEingaben, on_delete=models.CASCADE)
    app_wahl = models.CharField(max_length=100, null=False)
    edited_date = models.DateTimeField(blank=True, null=True)
    gesamtgebaeude_eingegeben = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        self.app_wahl = slugify(self.dach_wahl)
        super(Gesamtgebaeude, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


    def get_absolute_url2(self):
        return reverse('gesamtgebaeude_app:gesamtgebaeude_update', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})

    def get_absolute_url3(self):
        return reverse('gesamtgebaeude_app:gesamtgebaeude_detail', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})
