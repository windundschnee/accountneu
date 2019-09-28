from django.shortcuts import render
from .models import FreistehendeDaecherModel
from .forms import FreistehendeDaecherForm
from core.models import allgEingaben, Bauteil
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from gesamt_pdf_app.models import GesamtPdf
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone

from django.forms.models import model_to_dict
import os.path as path
import os, sys
from pathlib import Path
import json
from .berechnung_gesamt import freistehende_daecher_berechnung


class FreistehendeDaecherUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = FreistehendeDaecherModel
    form_class = FreistehendeDaecherForm



    def form_valid(self, form):
        form.instance.freistehendedaecher_eingegeben = True
        form.instance.edited_date = timezone.now()
        form.instance.user = self.request.user
        berechnen_latex_erzeugen(self)
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(FreistehendeDaecherUpdateView, self).get_context_data(**kwargs)

        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')
        return context
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class FreistehendeDaecherCreateView(LoginRequiredMixin, CreateView):
    model = FreistehendeDaecherModel
    form_class = FreistehendeDaecherForm

    def form_valid(self, form):
        form.instance.freistehendedaecher_eingegeben = True
        form.instance.edited_date = timezone.now()
        meinProjekt_pk = self.kwargs.get('my')

        #setze ForeignKey projekt auf meinProjekt_pk
        form.instance.projekt_id = meinProjekt_pk

        form.instance.user = self.request.user
        #setze ForeignKey bauteil auf mein Bauteil pk
        form.instance.bautteil_name_id = self.kwargs.get('pk')
        berechnen_latex_erzeugen(self)
        print('ende')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FreistehendeDaecherCreateView, self).get_context_data(**kwargs)

        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')
        return context

class FreistehendeDaecherDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = FreistehendeDaecherModel

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

        pk_freistehendedaecher = self.kwargs.get('pk')

        #context['pdf_bearbeitet'] ist für Entscheidung ob updateView oder createView
        context['pdf_bearbeitet'] = pdf_bearbeitet

        #wenn das Pdf mit demselben pk bereits einmal erzeugt wurde
        #soll im freistehendedaecher_detail.html der downloadButton und der Pfad
        #angezeigt werden
        user_id = str(self.request.user.id)
        filename_pdf_anzeigen = '/media/freistehende_daecher/'+user_id+'/Ausdruckprotokoll_Freistehende_Daecher'+str(pk_freistehendedaecher)+'.pdf'
        my_file = Path(filename_pdf_anzeigen)
        BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
        my_path = BASE_DIR +'/media/freistehende_daecher/' + user_id +'/Ausdruckprotokoll_Freistehende_Daecher'+str(pk_freistehendedaecher)+'.pdf'

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



    def get(self, request, *args, **kwargs):
        allgeingaben = allgEingaben.objects.filter(user=self.request.user).values('projekt_name')


        return super(FreistehendeDaecherDetailView, self).get(request, *args, **kwargs)


    #Pdf erzeugen!!
    #pdferzeugen = freistehende_waende_pdferzeugen(self, args_latex)
class PdfCreateRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'freistehendeDaecher_app:freistehende_daecher_detail'

    def get_redirect_url(self, *args, **kwargs):
        self.freistehende_daecher = get_object_or_404(FreistehendeDaecherModel, pk=self.kwargs['pk'])
        allgeingaben = allgEingaben.objects.filter(user=self.request.user, id=self.kwargs['my']).update(allgEingaben_eingegeben=False)
        meineigenes = FreistehendeDaecherModel.objects.filter(user=self.request.user, id=self.kwargs['pk']).update(freistehendedaecher_eingegeben=False)




        #Berechnung
        ergebnisse_freistehende_daecher = freistehende_daecher_berechnung(self)


        #Argumente fürs Lates (Wasserzeichen)
        user_id = str(self.request.user.id)
        user_has_free_account = self.request.user.is_free
        #Ordner erstellen für das zuküftige Pdf
        BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
        media_path = BASE_DIR +'/media/freistehende_daecher/' + user_id
        if not os.path.exists(media_path):
            os.makedirs(media_path)

        pk_freistehendedaecher = pk=self.kwargs['pk']

        foldername =  media_path +'/Ausdruckprotokoll_Freistehende_Daecher'+str(pk_freistehendedaecher)

        #Wenn bereits Objekte im GesamtPdf Model je Projekt existiert
        test = GesamtPdf.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()

        #Dann soll Dict 'eingaben_GesamtPdf' Liste gefüllt werden, sonst bleibt sie leer
        if test == True:
            eingaben_pdfbearbeiten = model_to_dict(get_object_or_404(GesamtPdf, projekt_id=self.kwargs['my']))

        else:
            eingaben_pdfbearbeiten = {}



        #Wenn bereits Objekte im pdfBearbeitenTitel Model je Bauteil/FreistehendeWand existiert



        args_latex = {'user_has_free_account': user_has_free_account,
                    'foldername':foldername,
                    'ergebnisse_freistehende_daecher':ergebnisse_freistehende_daecher,
                    'eingaben_pdfbearbeiten':eingaben_pdfbearbeiten,

                    }

        print(ergebnisse_freistehende_daecher)
        #Pdf erzeugen!!
        #pdferzeugen = freistehende_waende_pdferzeugen(self, args_latex)



        return super().get_redirect_url(*args, **kwargs)
