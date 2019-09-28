from .models import FreistehendeWaende
from .forms import FreistehendeWaendeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import *
import os, sys
from django.forms.models import model_to_dict
from . freistehendeWaendeBerechnung import freistehende_waende_berechnung
from core.models import allgEingaben

from .latex_ablauf import freistehende_waende_pdferzeugen
import os.path as path
from django.utils import timezone


from pathlib import Path
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from gesamt_pdf_app.models import GesamtPdf
from django.shortcuts import get_object_or_404
import json
class FreistehendeWaendeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = FreistehendeWaende
    form_class = FreistehendeWaendeForm

    def form_valid(self, form):
        form.instance.freistehendewaende_eingegeben = True
        form.instance.edited_date = timezone.now()
        form.instance.user = self.request.user

        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(FreistehendeWaendeUpdateView, self).get_context_data(**kwargs)

        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')
        return context
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class FreistehendeWaendeCreateView(LoginRequiredMixin, CreateView):
    model = FreistehendeWaende
    form_class = FreistehendeWaendeForm

    def form_valid(self, form):
        form.instance.freistehendewaende_eingegeben = True
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
        context = super(FreistehendeWaendeCreateView, self).get_context_data(**kwargs)

        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')
        return context


class FreistehendeWaendeDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = FreistehendeWaende

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #pk vom allgEingaben (Projekts) Model um pk´s anzuzeigen
        allgEingaben2 = allgEingaben.objects.filter(user=self.request.user).values('projekt_name')
        if allgEingaben2.exists() == True:
            context['allgEingaben_bearbeitet'] = get_object_or_404(allgEingaben,user=self.request.user, id=self.kwargs['my'])

        #pk vom Windbemessung (Bauteil) Model um pk´s anzuzeigen
        context['windbemessung'] = Bauteil.objects.filter(user=self.request.user).values('bautteil_name')
        #pk vom Projekt
        pk_projekt_name = self.kwargs.get('my')
        #Wenn bereits ein Objekt in GesamtPdf erstellt wurde
        pdf_bearbeitet = GesamtPdf.objects.filter(user=self.request.user, projekt_id=pk_projekt_name).exists()
        #Dann soll dieses mittels context['pdf'] bereit Freistehende
        #Damit ich die id auslesen kann um GesamtPdf_update zu erreichen
        if pdf_bearbeitet == True:
            context['pdf'] = get_object_or_404(GesamtPdf,user=self.request.user, projekt_id=self.kwargs['my'])

        pk_freistehendewaende = self.kwargs.get('pk')

        #context['pdf_bearbeitet'] ist für Entscheidung ob updateView oder createView
        context['pdf_bearbeitet'] = pdf_bearbeitet

        #wenn das Pdf mit demselben pk bereits einmal erzeugt wurde
        #soll im freistehendewaende_detail.html der downloadButton und der Pfad
        #angezeigt werden
        user_id = str(self.request.user.id)
        filename_pdf_anzeigen = '/media/freistehende_waende/'+user_id+'/Ausdruckprotokoll_Freistehende_Waende'+str(pk_freistehendewaende)+'.pdf'
        my_file = Path(filename_pdf_anzeigen)
        BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
        my_path = BASE_DIR +'/media/freistehende_waende/' + user_id +'/Ausdruckprotokoll_Freistehende_Waende'+str(pk_freistehendewaende)+'.pdf'

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
    pattern_name = 'freistehende_waende_app:freistehende_waende_detail'

    def get_redirect_url(self, *args, **kwargs):
        self.freistehende_waende = get_object_or_404(FreistehendeWaende, pk=self.kwargs['pk'])
        allgeingaben = allgEingaben.objects.filter(user=self.request.user, id=self.kwargs['my']).update(allgEingaben_eingegeben=False)
        meineigenes = FreistehendeWaende.objects.filter(user=self.request.user, id=self.kwargs['pk']).update(freistehendewaende_eingegeben=False)

        meineigenes_pdf = GesamtPdf.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).update(pdf_bearbeitet=False)


        #Berechnung
        ergebnisse_freistehende_waende = freistehende_waende_berechnung(self)
        #Argumente fürs Lates (Wasserzeichen)
        user_id = str(self.request.user.id)
        user_has_free_account = self.request.user.is_free
        #Ordner erstellen für das zuküftige Pdf
        BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
        media_path = BASE_DIR +'/media/freistehende_waende/' + user_id
        if not os.path.exists(media_path):
            os.makedirs(media_path)

        pk_freistehendewaende =self.kwargs['pk']

        foldername =  media_path +'/Ausdruckprotokoll_Freistehende_Waende'+str(pk_freistehendewaende)

        #Wenn bereits Objekte im GesamtPdf Model je Projekt existiert
        test = GesamtPdf.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()

        #Dann soll Dict 'eingaben_GesamtPdf' Liste gefüllt werden, sonst bleibt sie leer
        if test == True:
            eingaben_pdfbearbeiten = model_to_dict(get_object_or_404(GesamtPdf, projekt_id=self.kwargs['my']))

        else:
            eingaben_pdfbearbeiten = {}




        pk_projekt_name = self.kwargs.get('my')
        pdf_bearbeitet = GesamtPdf.objects.filter(user=self.request.user, projekt_id=pk_projekt_name).exists()
        user = User.objects.filter(email=self.request.user)
        args_latex = {'user_has_free_account': user_has_free_account,
                    'foldername':foldername,
                    'ergebnisse_freistehende_waende':ergebnisse_freistehende_waende,
                    'eingaben_pdfbearbeiten':eingaben_pdfbearbeiten,
                    'pdf_bearbeitet':pdf_bearbeitet,
                    'user':user,
                    }


        pdferzeugen = freistehende_waende_pdferzeugen(self, args_latex)



        return super().get_redirect_url(*args, **kwargs)
#wenn pdf aktualisieren Button gedrückt wurde komme ich zum RedirectView
#darin erstelle ich ein Pdf
