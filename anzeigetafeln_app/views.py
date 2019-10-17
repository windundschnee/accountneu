
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from core.models import allgEingaben, Bauteil
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import os.path as path
from django.views.generic.base import RedirectView
from gesamt_pdf_app.models import GesamtPdf
from .berechnung_anzeigetafeln import berechnung_anzeigetafel

from django.forms.models import model_to_dict
from .latex_ablauf import anzeigetafeln_pdferzeugen
import os, sys
from pathlib import Path
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#Classbased views
from django.utils import timezone
from django.urls import reverse_lazy
import json





class AnzeigetafelnUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AnzeigetafelnModel
    form_class = anzeigetafelnForm


    def form_valid(self, form):
        form.instance.anzeigetafeln_eingegeben = True
        form.instance.edited_date = timezone.now()
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AnzeigetafelnUpdateView, self).get_context_data(**kwargs)

        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')
        return context

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False



class AnzeigetafelnCreateView(LoginRequiredMixin, CreateView):
    model = AnzeigetafelnModel
    form_class = anzeigetafelnForm



    def form_valid(self, form):
        form.instance.anzeigetafeln_eingegeben = True
        form.instance.edited_date = timezone.now()
        meinProjekt_pk = self.kwargs.get('my')
        #setze ForeignKey projekt auf meinProjekt_pk
        form.instance.projekt_id = meinProjekt_pk
        form.instance.user = self.request.user
        #setze ForeignKey bauteil auf mein Bauteil pk
        form.instance.bautteil_name_id = self.kwargs.get('pk')

        print('ende')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AnzeigetafelnCreateView, self).get_context_data(**kwargs)

        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')
        return context


class AnzeigetafelnDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = AnzeigetafelnModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        #print(aktueller_projekt_name.gelaendekategorie)
        bauteile_je_projekt = allgEingaben.objects.filter(user=self.request.user).values('projekt_name')
        allgEingaben2 = allgEingaben.objects.filter(user=self.request.user).values('projekt_name')
        #pk vom allgEingaben (Projekts) Model um pk´s anzuzeigen
        if allgEingaben2.exists() == True:
            context['allgEingaben_bearbeitet'] = get_object_or_404(allgEingaben,user=self.request.user, id=self.kwargs['my'])
        #pk vom Windbemessung (Bauteil) Model um pk´s anzuzeigen
        context['windbemessung'] = Bauteil.objects.filter(user=self.request.user).values('bautteil_name')
        #pk vom Projekt
        pk_projekt_name = self.kwargs.get('my')
        #Wenn bereits ein Objekt in GesamtPdf erstellt wurde
        pdf_bearbeitet_ja = GesamtPdf.objects.filter(user=self.request.user, projekt_id=pk_projekt_name).exists()
        #Dann soll dieses mittels context['pdf'] bereit Freistehende
        #Damit ich die id auslesen kann um GesamtPdf_update zu erreichen
        if pdf_bearbeitet_ja == True:
            context['pdf'] = get_object_or_404(GesamtPdf,user=self.request.user, projekt_id=self.kwargs['my'])

        pk_anzeigetafeln = self.kwargs.get('pk')

        #context['pdf_bearbeitet'] ist für Entscheidung ob updateView oder createView
        context['pdf_bearbeitet'] = pdf_bearbeitet_ja

        #wenn das Pdf mit demselben pk bereits einmal erzeugt wurde
        #soll im freistehendewaende_detail.html der downloadButton und der Pfad
        #angezeigt werden
        user_id = str(self.request.user.id)
        filename_pdf_anzeigen = '/media/anzeigetafeln/'+user_id+'/Ausdruckprotokoll_Anzeigetafeln'+str(pk_anzeigetafeln)+'.pdf'
        my_file = Path(filename_pdf_anzeigen)
        BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
        my_path = BASE_DIR +'/media/anzeigetafeln/' + user_id +'/Ausdruckprotokoll_Anzeigetafeln'+str(pk_anzeigetafeln)+'.pdf'

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

class PdfCreateRedirectViewAnzeigetafeln(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'anzeigetafeln_app:anzeigetafeln_detail'

    def get_redirect_url(self, *args, **kwargs):
        self.anzeigetafeln = get_object_or_404(AnzeigetafelnModel, pk=kwargs['pk'])
        allgeingaben = allgEingaben.objects.filter(user=self.request.user, id=self.kwargs['my']).update(allgEingaben_eingegeben=False)
        meineigenes = AnzeigetafelnModel.objects.filter(user=self.request.user, id=self.kwargs['pk']).update(anzeigetafeln_eingegeben=False)

        meineigenes_pdf = GesamtPdf.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).update(pdf_bearbeitet=False)




        #Berechnung
        ergebnisse_anzeigetafeln = berechnung_anzeigetafel(self)
        #Argumente fürs Lates (Wasserzeichen)
        user_id = str(self.request.user.id)
        user_has_free_account = self.request.user.is_free
        #Ordner erstellen für das zuküftige Pdf
        BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
        media_path = BASE_DIR +'/media/anzeigetafeln/' + user_id
        if not os.path.exists(media_path):
            os.makedirs(media_path)

        pk_anzeigetafeln = pk=self.kwargs['pk']

        foldername =  media_path +'/Ausdruckprotokoll_Anzeigetafeln'+str(pk_anzeigetafeln)

        #Wenn bereits Objekte im GesamtPdf Model je Projekt existiert
        test = GesamtPdf.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()

        #Dann soll Dict 'eingaben_GesamtPdf' Liste gefüllt werden, sonst bleibt sie leer
        if test == True:
            eingaben_pdfbearbeiten = model_to_dict(get_object_or_404(GesamtPdf, projekt_id=self.kwargs['my']))

        else:
            eingaben_pdfbearbeiten = {}


        user = User.objects.filter(email=self.request.user)




        args_latex = {'user_has_free_account': user_has_free_account,
                    'foldername':foldername,
                    'ergebnisse_anzeigetafeln':ergebnisse_anzeigetafeln,
                    'eingaben_pdfbearbeiten':eingaben_pdfbearbeiten,
                    'user':user,


                    }


        #Pdf erzeugen!!
        pdferzeugen = anzeigetafeln_pdferzeugen(self, args_latex)



        return super().get_redirect_url(*args, **kwargs)
