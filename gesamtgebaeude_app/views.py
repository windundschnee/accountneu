from django.shortcuts import render
from.models import Gesamtgebaeude
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from gesamt_pdf_app.models import GesamtPdf
from django.forms.models import model_to_dict
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import GesamtgebauedeForm,SpecialForm
from .models import Gesamtgebaeude
from django.utils import timezone
from core.models import allgEingaben, Bauteil
from gesamt_pdf_app.models import GesamtPdf
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
import os.path as path
from pathlib import Path
import os
from django.urls import reverse_lazy
# Create your views here.
class GesamtgebaeudeCreateView(LoginRequiredMixin, CreateView):
    model = Gesamtgebaeude
    form_class = SpecialForm


    def form_valid(self, form):

        form.instance.user = self.request.user


        form.instance.edited_date = timezone.now()
        meinProjekt_pk = self.kwargs.get('my')
        #setze ForeignKey projekt auf meinProjekt_pk
        form.instance.projekt_id = meinProjekt_pk
        form.instance.bautteil_name_id = self.kwargs.get('pk')


        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(GesamtgebaeudeCreateView, self).get_context_data(**kwargs)

        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')
        return context

    def get_success_url(self):
        if self.object.dach_wahl ==  'Flachdach':
            return reverse_lazy('flachdaecher_app:flachdach_create', args=(self.kwargs.get('slug'), self.kwargs.get('pk'), self.object.id))
        elif self.object.dach_wahl ==  'Satteldach':
            return reverse_lazy('flachdaecher_app:flachdach_create', args=(self.kwargs.get('slug'), self.kwargs.get('pk'), self.object.id))
        elif self.object.dach_wahl ==  'Pultdach':
            return reverse_lazy('flachdaecher_app:flachdach_create', args=(self.kwargs.get('slug'), self.kwargs.get('pk'), self.object.id))

        else:
            print('Errrrrööööööööööööööööööööööööööööööööööööööööööööööööööör')
            return reverse_lazy('core:allgEingaben_list')

class GesamtgebaeudeDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Gesamtgebaeude

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

        pk_gesamtgebaeude = self.kwargs.get('pk')

        #context['pdf_bearbeitet'] ist für Entscheidung ob updateView oder createView
        context['pdf_bearbeitet'] = pdf_bearbeitet_ja

        #wenn das Pdf mit demselben pk bereits einmal erzeugt wurde
        #soll im freistehendewaende_detail.html der downloadButton und der Pfad
        #angezeigt werden
        user_id = str(self.request.user.id)
        filename_pdf_anzeigen = '/media/gesamtgebaeude/'+user_id+'/Ausdruckprotokoll_Gesamtgebaeude'+str(pk_gesamtgebaeude)+'.pdf'
        my_file = Path(filename_pdf_anzeigen)
        BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
        my_path = BASE_DIR +'/media/gesamtgebaeude/' + user_id +'/Ausdruckprotokoll_Gesamtgebaeude'+str(pk_gesamtgebaeude)+'.pdf'

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


class GesamtgebaeudeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Gesamtgebaeude
    form_class = SpecialForm


    def form_valid(self, form):
        form.instance.gesamtgebaeude_eingegeben = True
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
        context = super(GesamtgebaeudeUpdateView, self).get_context_data(**kwargs)

        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')
        return context
