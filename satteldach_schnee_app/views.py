from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from core.models import Bauteil, allgEingaben
from gesamt_pdf_app.models import GesamtPdf
import os.path as path
from django.views.generic.base import RedirectView
from django.forms.models import model_to_dict
from .berechnung_satteldach_schnee import berechnung_satteldach_schnee
from .latex_ablauf_satteldach_schnee import satteldach_schnee_pdferzeugen
#Classbased views
from django.utils import timezone
from django.urls import reverse_lazy
from .models import SatteldachSchneeModel
from .forms import SatteldachSchneeForm
from pathlib import Path
import os, sys
# Create your views here.
class SatteldachSchneeCreateView(LoginRequiredMixin, CreateView):
    model = SatteldachSchneeModel
    form_class = SatteldachSchneeForm



    def form_valid(self, form):
        form.instance.satteldach_schnee_eingegeben = True
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
        context = super(SatteldachSchneeCreateView, self).get_context_data(**kwargs)

        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')
        return context

class SatteldachSchneeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SatteldachSchneeModel
    form_class = SatteldachSchneeForm


    def form_valid(self, form):
        form.instance.satteldach_schnee_eingegeben = True
        form.instance.edited_date = timezone.now()
        form.instance.user = self.request.user

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SatteldachSchneeUpdateView, self).get_context_data(**kwargs)

        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')
        return context

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class SatteldachSchneeDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = SatteldachSchneeModel

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

        pk_satteldach_schnee = self.kwargs.get('pk')

        #context['pdf_bearbeitet'] ist für Entscheidung ob updateView oder createView
        context['pdf_bearbeitet'] = pdf_bearbeitet_ja

        #wenn das Pdf mit demselben pk bereits einmal erzeugt wurde
        #soll im freistehendewaende_detail.html der downloadButton und der Pfad
        #angezeigt werden
        user_id = str(self.request.user.id)
        filename_pdf_anzeigen = '/media/satteldach_schnee/'+user_id+'/Ausdruckprotokoll_satteldach_schnee'+str(pk_satteldach_schnee)+'.pdf'
        my_file = Path(filename_pdf_anzeigen)
        BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
        my_path = BASE_DIR +'/media/satteldach_schnee/' + user_id +'/Ausdruckprotokoll_satteldach_schnee'+str(pk_satteldach_schnee)+'.pdf'

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

class PdfCreateRedirectViewSatteldachSchnee(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'satteldach_schnee_app:satteldach_schnee_detail'

    def get_redirect_url(self, *args, **kwargs):
        self.satteldach_schnee = get_object_or_404(SatteldachSchneeModel, pk=kwargs['pk'])
        allgeingaben = allgEingaben.objects.filter(user=self.request.user, id=self.kwargs['my']).update(allgEingaben_eingegeben=False)
        meineigenes = SatteldachSchneeModel.objects.filter(user=self.request.user, id=self.kwargs['pk']).update(satteldach_schnee_eingegeben=False)

        meineigenes_pdf = GesamtPdf.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).update(pdf_bearbeitet=False)




        #Berechnung
        ergebnisse_satteldach_schnee = berechnung_satteldach_schnee(self)
        #Argumente fürs Lates (Wasserzeichen)
        user_id = str(self.request.user.id)
        user_has_free_account = self.request.user.is_free
        #Ordner erstellen für das zuküftige Pdf
        BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
        media_path = BASE_DIR +'/media/satteldach_schnee/' + user_id
        if not os.path.exists(media_path):
            os.makedirs(media_path)

        pk_satteldach_schnee = pk=self.kwargs['pk']

        foldername =  media_path +'/Ausdruckprotokoll_satteldach_schnee'+str(pk_satteldach_schnee)

        #Wenn bereits Objekte im GesamtPdf Model je Projekt existiert
        test = GesamtPdf.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()

        #Dann soll Dict 'eingaben_GesamtPdf' Liste gefüllt werden, sonst bleibt sie leer
        if test == True:
            eingaben_pdfbearbeiten = model_to_dict(get_object_or_404(GesamtPdf, projekt_id=self.kwargs['my']))

        else:
            eingaben_pdfbearbeiten = {}

        allgeingaben = allgEingaben.objects.filter(user=self.request.user, id=self.kwargs['my']).values()


        arg_latex_list = [user_has_free_account,foldername,ergebnisse_satteldach_schnee,allgeingaben]

        args_latex = {'user_has_free_account': user_has_free_account,
                    'foldername':foldername,
                    'ergebnisse_schnee':ergebnisse_satteldach_schnee,


                    }

        #Pdf erzeugen!!
        pdferzeugen = satteldach_schnee_pdferzeugen(self, args_latex)



        return super().get_redirect_url(*args, **kwargs)
