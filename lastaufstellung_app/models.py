from django.db import models
from account_app.models import User
from stdimage import StdImageField

from django.urls import reverse
from django.core.validators import MinValueValidator
from django.template.defaultfilters import slugify

class DatenbankMaterial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, blank=False)
    wichte = models.DecimalField(validators=[MinValueValidator(1)],decimal_places=2, max_digits=5, blank=True, null=True)
    def __str__(self):
        return "%s; Wichte: %s kN/m³" % (self.name, self.wichte)
    def get_absolute_url(self):
        return reverse('lastaufstellung_app:datenbank_list')
class Bauteil_Last(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, blank=False)

    slug = models.SlugField(max_length=40, default='slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Bauteil, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lastaufstellung_app:homogene_schicht_create')

class HomogeneSchicht(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bauteil = models.ForeignKey(Bauteil_Last, on_delete=models.CASCADE)
    schichtname = models.CharField(max_length=80, blank=False)
    dicke = models.DecimalField(validators=[MinValueValidator(1)],decimal_places=2, max_digits=5, blank=True, null=True)
    wichte = models.ForeignKey(DatenbankMaterial, on_delete=models.CASCADE)
    last = models.DecimalField(validators=[MinValueValidator(1)],decimal_places=2, max_digits=5, blank=True, null=True)
    slug = models.SlugField(max_length=40, default='slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.schichtname)
        super(HomogeneSchicht, self).save(*args, **kwargs)

    def __str__(self):
        return self.schichtname

    def get_absolute_url(self):
        return reverse('lastaufstellung_app:homogene_schicht_create')
