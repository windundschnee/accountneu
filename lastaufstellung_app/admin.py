from django.contrib import admin
from .models import Bauteil_Last, HomogeneSchicht, DatenbankMaterial

# Register your models here.

admin.site.register(DatenbankMaterial)
admin.site.register(Bauteil_Last)
admin.site.register(HomogeneSchicht)
