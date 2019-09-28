from django.contrib import admin
from .models import allgEingaben, Bauteil

# Register your models here.

class allgEingabenAdmin(admin.ModelAdmin):
    list_display = ['projekt_name','user',]


admin.site.register(allgEingaben, allgEingabenAdmin)


class BauteilAdmin(admin.ModelAdmin):
    list_display = ['bautteil_name', 'projekt','user','bemessungsart_wind_schnee','wind','schnee']





admin.site.register(Bauteil, BauteilAdmin)
