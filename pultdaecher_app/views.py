from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import PultdachModel
from .forms import pultdaecherForm
from django.utils import timezone
from core.models import allgEingaben, Bauteil
from django.shortcuts import get_object_or_404
from gesamt_pdf_app.models import GesamtPdf
import os, sys
import os.path as path
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import json
from django.urls import reverse_lazy
from .berechnung_gesamt import pultdach_berechnung
from django.forms.models import model_to_dict
from .latex_ablauf import pultdach_pdferzeugen
# Create your views here.

class PultdachUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PultdachModel
    form_class = pultdaecherForm

    def form_valid(self, form):
        form.instance.pultdach_eingegeben = True
        form.instance.edited_date = timezone.now()
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PultdachUpdateView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')
        return context

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PultdachCreateView(LoginRequiredMixin, CreateView):
    model = PultdachModel
    form_class = pultdaecherForm

    def form_valid(self, form):
        form.instance.pultdach_eingegeben = True
        form.instance.edited_date = timezone.now()
        meinProjekt_pk = self.kwargs.get('my')
        #setze ForeignKey projekt auf meinProjekt_pk
        form.instance.projekt_id = meinProjekt_pk
        form.instance.user = self.request.user
        #setze ForeignKey bauteil auf mein Bauteil pk
        form.instance.bautteil_name_id = self.kwargs.get('pk')

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PultdachCreateView, self).get_context_data(**kwargs)

        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')
        return context



class PultdachDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = PultdachModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #pk vom allgEingaben (Projekts) Model um pk´s anzuzeigen
        allgEingaben2 = allgEingaben.objects.filter(user=self.request.user).values('projekt_name')
        #pk vom allgEingaben (Projekts) Model um pk´s anzuzeigen
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

        pk_pultdach = self.kwargs.get('pk')

        #context['pdf_bearbeitet'] ist für Entscheidung ob updateView oder createView
        context['pdf_bearbeitet'] = pdf_bearbeitet

        #wenn das Pdf mit demselben pk bereits einmal erzeugt wurde
        #soll im freistehendewaende_detail.html der downloadButton und der Pfad
        #angezeigt werden
        user_id = str(self.request.user.id)
        filename_pdf_anzeigen = '/media/Pultdach/'+user_id+'/Ausdruckprotokoll_Pultdach'+str(pk_pultdach)+'.pdf'

        BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
        my_path = BASE_DIR +'/media/Pultdach/' + user_id +'/Ausdruckprotokoll_Pultdach'+str(pk_pultdach)+'.pdf'

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
