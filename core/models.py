from django.db import models
from account_app.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.urls import reverse
import uuid

SAMPLE_CHOICES2=(
( 'Freistehende Wände','Freistehende Wände'),
('Flachdach','Flachdach'),
('Anzeigetafeln','Anzeigetafeln'),
('Satteldach','Satteldach'),

)



gk = (
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
        )

class allgEingaben(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    projekt_name = models.CharField(max_length=100, null=False)
    date_posted = models.DateTimeField(default=timezone.now)
    bundesland = models.CharField(max_length=100, default='Wien')
    ort = models.CharField(max_length=100, default='10.Favoriten')
    gelaendekategorie = models.CharField(max_length=25, default='II')
    winddruck_benutzerdefiniert = models.BooleanField(default=False)
    basiswinddruck = models.DecimalField(validators=[MinValueValidator(0)], decimal_places=2, max_digits=5, blank=False, null=True)
    basiswinddruck_hidden = models.CharField(max_length=100, null=True, blank=True)
    allgEingaben_eingegeben = models.BooleanField(blank=False)
    seehoehe_benutzerdefiniert = models.BooleanField(default=False)
    seehoehe = models.DecimalField(validators=[MinValueValidator(0)], decimal_places=1, max_digits=5, blank=False, null=True)
    seehoehe_hidden = models.CharField(max_length=100, blank=True, null=True)
    windgeschwindigkeit = models.DecimalField(validators=[MinValueValidator(0)], decimal_places=2, max_digits=5, blank=False, null=True)
    schneelast_benutzerdefiniert = models.BooleanField(default=False)

    schneelastzone = models.CharField(max_length=10, default='2',blank=True, null=True)

    schneelast = models.DecimalField(validators=[MinValueValidator(0)], default=2, decimal_places=2, max_digits=5, null=False)
    schneelast_hidden = models.CharField(max_length=100, blank=True, null=True)
    abminderungsfaktor = models.DecimalField(validators=[MaxValueValidator(1), MinValueValidator(0)], decimal_places=2, max_digits=5, blank=False, null=True)
    slug = models.SlugField(max_length=40)
    edited_date = models.DateTimeField(blank=True, null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.projekt_name)
        super(allgEingaben, self).save(*args, **kwargs)





    def __str__(self):
        return self.projekt_name

    def get_absolute_url(self):
        return reverse('core:projekt_update', kwargs={'slug': self.slug, 'pk': self.pk})


class Bauteil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    projekt = models.ForeignKey(allgEingaben, on_delete=models.CASCADE)

    bautteil_name = models.CharField(max_length=100,)
    bemessungsart_wind_schnee = models.CharField(max_length=85, default='', null=True, blank=True)

    wind = models.BooleanField(default=False)
    schnee = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.bautteil_name

    def get_absolute_url(self):

        return reverse('core:windbemessung_update', kwargs={'slug': self.projekt.slug, 'pk': self.pk, 'pk2': self.projekt.pk})

    def get_absolute_url_list(self):

        return reverse('core:windbemessung_list', kwargs={'slug': self.projekt.slug, 'pk': self.pk, 'pk2': self.projekt.pk})

    def get_absolute_url_delete(self):

        return reverse('core:windbemessung_delete', kwargs={'slug': self.projekt.slug, 'pk': self.pk, 'pk2': self.projekt.pk})
