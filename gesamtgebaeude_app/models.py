from django.db import models
from account_app.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from core.models import allgEingaben
from django.template.defaultfilters import slugify
from django.urls import reverse
import uuid
from flachdaecher_app.models import FlachdachModel


SAMPLE_CHOICES2=(
( 'Freistehende Wände','Freistehende Wände'),
('Flachdach','Flachdach'),
('Anzeigetafeln','Anzeigetafeln'),
('Satteldach','Satteldach'),

)





class Gesamtgebaeude(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dach_wahl = models.CharField(max_length=100, null=False, default="Dachwahl")

    projekt = models.ForeignKey(allgEingaben, on_delete=models.CASCADE, null=True)
    app_wahl = models.CharField(max_length=100, null=False)
    edited_date = models.DateTimeField(blank=True, null=True)



    def save(self, *args, **kwargs):
        self.app_wahl = slugify(self.dach_wahl)
        super(Gesamtgebaeude, self).save(*args, **kwargs)

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('gesamtgebaeude_app:gesamtgebaeude_detail', kwargs={'slug': self.projekt.slug,'my': self.projekt.pk,'pk': self.pk})
