
from .models import FlachdachModel
from .forms import *
from core.models import allgEingaben
from django.shortcuts import render, redirect

from pathlib import Path
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from gesamt_pdf_app.models import GesamtPdf
from .flachdachBerechnung import flachdach_berechnung_ablauf
from gesamtgebaeude_app.models import Gesamtgebaeude


from django.forms.models import model_to_dict
from django.utils import timezone
import os, sys
import os.path as path
from django.shortcuts import get_object_or_404
from .latex_ablauf import flachdach_pdferzeugen
from django.core import serializers
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
import json


class FlachdachUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = FlachdachModel
    form_class = flachdaecherForm


    def form_valid(self, form):
        form.instance.flachdach_eingegeben = True
        #checkbox, dass der user ein flachdach Model Objekt eingegeben hat
        form.instance.edited_date = timezone.now()
        #die entsprechende Zeit hinzufügen zum Objekt
        form.instance.user = self.request.user
        #Den entsprechenden User speichern

        return super().form_valid(form)

    def test_func(self):
        #Diese Funktion dient zur überprüfun, ob der registrierte User auch er ist
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
    def get_context_data(self, **kwargs):
        context = super(FlachdachUpdateView, self).get_context_data(**kwargs)

        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')

        gesamtgebaeude= None
        if Gesamtgebaeude.objects.filter(user=self.request.user, projekt_id=self.kwargs.get('my'),bautteil_name_id=self.object.bautteil_name.id).exists():
            gesamtgebaeude = Gesamtgebaeude.objects.filter(user=self.request.user, projekt_id=self.kwargs.get('my'),bautteil_name_id=self.object.bautteil_name.id)
        context['gesamtgebaeude'] = gesamtgebaeude
        return context
class FlachdachCreateView(LoginRequiredMixin, CreateView):
    model = FlachdachModel
    form_class = flachdaecherForm


    def form_valid(self, form):
        form.instance.flachdach_eingegeben = True
        form.instance.edited_date = timezone.now()
        meinProjekt_pk = self.kwargs.get('my')
        #setze ForeignKey projekt auf meinProjekt_pk
        form.instance.projekt_id = meinProjekt_pk
        form.instance.user = self.request.user
        #setze ForeignKey bauteil auf mein Bauteil pk
        form.instance.bautteil_name_id = self.kwargs.get('pk')


        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FlachdachCreateView, self).get_context_data(**kwargs)

        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')

        gesamtgebaeude= None
        if Gesamtgebaeude.objects.filter(user=self.request.user, projekt_id=self.kwargs.get('my'),bautteil_name_id=self.kwargs.get('pk')).exists():
            gesamtgebaeude = Gesamtgebaeude.objects.filter(user=self.request.user, projekt_id=self.kwargs.get('my'),bautteil_name_id=self.kwargs.get('pk'))
        context['gesamtgebaeude'] = gesamtgebaeude
        return context

class FlachdachDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = FlachdachModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #pk vom allgEingaben (Projekts) Model um pk´s anzuzeigen
        allgEingaben2 = allgEingaben.objects.filter(user=self.request.user).values('projekt_name')
        gesamtgebaeude= None
        if Gesamtgebaeude.objects.filter(user=self.request.user, projekt_id=self.kwargs.get('my'),bautteil_name_id=self.object.bautteil_name.id).exists():
            gesamtgebaeude = Gesamtgebaeude.objects.filter(user=self.request.user, projekt_id=self.kwargs.get('my'),bautteil_name_id=self.object.bautteil_name.id)
        context['gesamtgebaeude'] = gesamtgebaeude
        #pk vom allgEingaben (Projekts) Model um pk´s anzuzeigen
        if allgEingaben2.exists() == True:
            context['allgEingaben_bearbeitet'] = get_object_or_404(allgEingaben,user=self.request.user, id=self.kwargs['my'])
        #pk vom Windbemessung (Bauteil) Model um pk´s anzuzeigen
        context['windbemessung'] = Bauteil.objects.filter(user=self.request.user).values('bautteil_name')
        meinProjekt_pk = self.kwargs.get('my')
        pdf_bearbeitet = GesamtPdf.objects.filter(user=self.request.user, projekt_id=meinProjekt_pk).exists()
        context['pdf_bearbeitet'] = pdf_bearbeitet
        print(self.kwargs['my'])
        pdfbearbeiten = GesamtPdf.objects.filter(user=self.request.user,projekt_id=self.kwargs['my'])
        if pdfbearbeiten.exists() == True:
            pdf_bearbeiten_object = get_object_or_404(GesamtPdf,user=self.request.user, projekt_id=self.kwargs['my'])
            print(pdf_bearbeiten_object)
            context['pdf_bearbeiten_object'] = pdf_bearbeiten_object
        #pk von flachdach model
        pk_flachdach = self.kwargs.get('pk')
        user_id = str(self.request.user.id)
        filename_pdf_anzeigen = '/media/flachdach/'+user_id+'/Ausdruckprotokoll_Flachdach'+str(pk_flachdach)+'.pdf'
        BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
        my_path = BASE_DIR +'/media/flachdach/' + user_id +'/Ausdruckprotokoll_Flachdach'+str(pk_flachdach)+'.pdf'

        if os.path.exists(my_path):
            context['filename_pdf_anzeigen'] = filename_pdf_anzeigen
            context['existiert_pdf'] = True
        else:
            context['filename_pdf_anzeigen'] = ''
            context['existiert_pdf'] = False

        return context

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class PdfCreateRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'flachdaecher_app:flachdach_detail'

    def get_redirect_url(self, *args, **kwargs):
        print('dobini zerscht im redirect')
        self.flachdach = get_object_or_404(FlachdachModel, pk=self.kwargs['pk'])
        allgeingaben = allgEingaben.objects.filter(user=self.request.user, id=self.kwargs['my']).update(allgEingaben_eingegeben=False)
        meineigenes = FlachdachModel.objects.filter(user=self.request.user, id=self.kwargs['pk']).update(flachdach_eingegeben=False)
        meineigenes_pdf = GesamtPdf.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).update(pdf_bearbeitet=False)

        #alles wird hir berechnet
        ergebnisse_berechnung = flachdach_berechnung_ablauf(self)






        pk_projekt_name = self.kwargs.get('my')
        #Wenn bereits ein Objekt in pdfBearbeiten erstellt wurde
        pdf_bearbeitet = GesamtPdf.objects.filter(user=self.request.user, projekt_id=pk_projekt_name).exists()

        args_latex = {
                    #'output_margin_ergebnisse':output_margin_ergebnisse,
                    'ergebnisse_berechnung':ergebnisse_berechnung,
                    'pdf_bearbeitet':pdf_bearbeitet,
                    }
        #Pdf erzeugen!!
        pdferzeugen = flachdach_pdferzeugen(self, args_latex)
        return super().get_redirect_url(*args, **kwargs)
