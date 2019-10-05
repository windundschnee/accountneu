from django.shortcuts import render, redirect, get_object_or_404
from account_app.models import User
from .forms import *
from decimal import *
from .models import *
import random
from django.forms.models import model_to_dict
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
import math
from django.http import HttpResponseRedirect
from anzeigetafeln_app.models import AnzeigetafelnModel
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.utils import timezone
from datetime import datetime, timedelta
import os
import os.path as path
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.forms.models import model_to_dict
from django.views.generic.base import TemplateView
from itertools import chain
from operator import attrgetter
from django.db.models import Count
from freistehende_waende_app.models import FreistehendeWaende
from freistehendeDaecher_app.models import FreistehendeDaecherModel
from flachdaecher_app.models import FlachdachModel
from pultdaecher_app.models import PultdachModel
from pultdach_schnee_app.models import PultdachSchneeModel
from satteldach_schnee_app.models import SatteldachSchneeModel
from kehldach_schnee_app.models import KehldachSchneeModel
from django.core.mail import send_mail
from gesamtgebaeude_app.models import Gesamtgebaeude
#Liste aller Projekte
class AllgemeineAngabenListView(LoginRequiredMixin, ListView):
    model = allgEingaben
    context_object_name = 'allgEingaben'
    template_name = 'core/allgeingaben_list.html'
    paginate_by = 8


    def get_queryset(self):
        if self.request.user.is_authenticated:

            #hier soll geprüft werden ob user bald expired date erreicht hat
            if self.request.user.is_pro:
                is_pro_exired_date = self.request.user.is_pro_exired_date
                is_pro_exired_date_two_weeks_before = is_pro_exired_date-timedelta(14)
                datetime_now = datetime.now(tz=timezone.utc)
                if is_pro_exired_date_two_weeks_before <= datetime_now:
                    self.request.user.verlaengerung_notwendig = True
                    self.request.user.save()

                else:
                    self.request.user.verlaengerung_notwendig = False
                    self.request.user.save()


            list_date_sorted = allgEingaben.objects.filter(user=self.request.user).order_by('-edited_date')

            return list_date_sorted
        else:
            return allgEingaben.objects.none()

#Hier kann ein Projekt erstellt werden
class ProjektCreateView(LoginRequiredMixin, CreateView):
    model = allgEingaben
    form_class = RegCarForm

    template_name = 'core/allgeingaben_form.html'


    def get_context_data(self, **kwargs):
        context = super(ProjektCreateView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.allgEingaben_eingegeben = True
        form.instance.edited_date = timezone.now()

        user_id = str(self.request.user.id)

        #Ordner erstellen für das zuküftige Pdf
        BASE_DIR = os.path.dirname(os.path.abspath(path.join(__file__ ,"../")))
        media_path = BASE_DIR +'/media/pdf_bearbeiten/' + user_id
        if not os.path.exists(media_path):
            os.makedirs(media_path)
        return super(ProjektCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('core:windbemessung_create', args=(self.object.slug, self.object.id))


 # Hier kann ein Bauteil erstellt Werden (Windbemessung Model)
class WindbemessungCreateView(LoginRequiredMixin, CreateView):
    model = Bauteil
    form_class = WindbemessungForm
    def get_context_data(self, **kwargs):
        context = super(WindbemessungCreateView, self).get_context_data(**kwargs)
        context['bin_im_updateview'] = False
        context['pk_neu'] = self.kwargs.get('pk')
        context['slug_neu'] = self.kwargs.get('slug')
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.projekt_id = self.kwargs.get('pk')
        print(form.cleaned_data['bemessungsart_wind_schnee'])
        print(form.cleaned_data['bemessungsart_wind_schnee'])
        print(form.cleaned_data['bemessungsart_wind_schnee'][:4])
        if form.cleaned_data['bemessungsart_wind_schnee'][:4] == 'Wind':
            form.instance.wind = True
        elif form.cleaned_data['bemessungsart_wind_schnee'][:4] == 'Schn':
            form.instance.schnee = True



        return super().form_valid(form)
    #geh zum createView je nach RadioButtonWahl
    def get_success_url(self):
        if self.object.bemessungsart_wind_schnee ==  'Windlasten Freistehende Wände':
            return reverse_lazy('freistehende_waende_app:freistehende_waende_create', args=(self.kwargs.get('slug'), self.kwargs.get('pk'), self.object.id))
        elif self.object.bemessungsart_wind_schnee ==  'Windlasten Freistehende Dächer':
            return reverse_lazy('freistehendeDaecher_app:freistehende_daecher_create', args=(self.kwargs.get('slug'), self.kwargs.get('pk'), self.object.id))
        elif self.object.bemessungsart_wind_schnee ==  'Windlasten Anzeigetafeln':
            return reverse_lazy('anzeigetafeln_app:anzeigetafeln_create', args=(self.kwargs.get('slug'), self.kwargs.get('pk'), self.object.id))
        elif self.object.bemessungsart_wind_schnee ==  'Windlasten Flachdächer':
            return reverse_lazy('flachdaecher_app:flachdach_create', args=(self.kwargs.get('slug'), self.kwargs.get('pk'), self.object.id))
        elif self.object.bemessungsart_wind_schnee ==  'Windlasten Pultdächer':
            return reverse_lazy('pultdaecher_app:pultdach_create', args=(self.kwargs.get('slug'), self.kwargs.get('pk'), self.object.id))
        elif self.object.bemessungsart_wind_schnee ==  'Schneelasten Pultdächer':
            return reverse_lazy('pultdach_schnee_app:pultdach_schnee_create', args=(self.kwargs.get('slug'), self.kwargs.get('pk'), self.object.id))
        elif self.object.bemessungsart_wind_schnee ==  'Schneelasten Kehldächer':
            return reverse_lazy('kehldach_schnee_app:kehldach_schnee_create', args=(self.kwargs.get('slug'), self.kwargs.get('pk'), self.object.id))
        elif self.object.bemessungsart_wind_schnee ==  'Schneelasten Kehldächer':
            return reverse_lazy('kehldach_schnee_app:kehldach_schnee_create', args=(self.kwargs.get('slug'), self.kwargs.get('pk'), self.object.id))
        elif self.object.bemessungsart_wind_schnee ==  'Windlasten Gesamtgebäude':
            return reverse_lazy('gesamtgebaeude_app:gesamtgebaeude_create', args=(self.kwargs.get('slug'), self.kwargs.get('pk'), self.object.id))
        elif self.object.bemessungsart_wind_schnee ==  'Schneelasten Satteldächer':
            print('jhkjhjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
            return reverse_lazy('satteldach_schnee_app:satteldach_schnee_create', args=(self.kwargs.get('slug'), self.kwargs.get('pk'), self.object.id))
        else:
            print('Errrrrööööööööööööööööööööööööööööööööööööööööööööööööööör')
            return reverse_lazy('core:allgEingaben_list')




class WindbemessungUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bauteil
    form_class = WindbemessungForm




    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(WindbemessungUpdateView, self).get_context_data(**kwargs)
        aktuelles_projekt = allgEingaben.objects.get(pk=self.kwargs['pk2'])
        projekt_name = aktuelles_projekt.projekt_name
        context['projekt_name'] = projekt_name
        context['bauteil_name'] = self.object.bautteil_name
        context['bin_im_updateview'] = True
        context['pk_neu'] = self.kwargs.get('pk2')
        context['slug_neu'] = self.kwargs.get('slug')
        return context

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('core:windbemessung_list', args=(self.kwargs.get('slug'), self.kwargs.get('pk2'),))


class WindbemessungListView(LoginRequiredMixin, ListView):
    model = Bauteil
    template_name = 'core/bauteil_list.html'
    paginate_by = 8
    context_object_name = 'character_series_list'


    def get_context_data(self, **kwargs):
        context = super(WindbemessungListView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        context['slug_mein'] = self.kwargs['slug']
        aktuelles_projekt = allgEingaben.objects.get(pk=self.kwargs['pk'])
        pk = self.kwargs['pk']
        #aus jedem App hole ich die Objekte je Projekt um deren pk zu benutzen für UpdateViews

        context['projekt_name'] = aktuelles_projekt.projekt_name
        return context


    def get_queryset(self):
        result = super(WindbemessungListView, self).get_queryset()
        if self.request.user.is_authenticated:

            pk = self.kwargs['pk']
            #aus jedem App hole ich die Objekte je Projekt um sie
            #in der Bauteilliste anzuzeigen und hole die jeweiligen pk´s
            anzeigetafeln_je_projekt = AnzeigetafelnModel.objects.filter(user=self.request.user, projekt_id=pk)
            freistehende_waende_je_projekt = FreistehendeWaende.objects.filter(user=self.request.user, projekt_id=pk)
            freistehende_daecher_je_projekt = FreistehendeDaecherModel.objects.filter(user=self.request.user, projekt_id=pk)
            flachdaecher_je_projekt = FlachdachModel.objects.filter(user=self.request.user, projekt_id=pk)
            pultdaecher_je_projekt = PultdachModel.objects.filter(user=self.request.user, projekt_id=pk)
            #Schnee
            pultdaecher_schnee_je_projekt = PultdachSchneeModel.objects.filter(user=self.request.user, projekt_id=pk)
            satteldaecher_schnee_je_projekt = SatteldachSchneeModel.objects.filter(user=self.request.user, projekt_id=pk)
            kehldaecher_schnee_je_projekt = KehldachSchneeModel.objects.filter(user=self.request.user, projekt_id=pk)
            gesamtgebauede_je_projekt = Gesamtgebaeude.objects.filter(user=self.request.user, projekt_id=pk)
            #hier darf gechained werden!!!jedes model
            querylist = list(sorted(chain(anzeigetafeln_je_projekt,freistehende_waende_je_projekt,
            freistehende_daecher_je_projekt,flachdaecher_je_projekt,pultdaecher_je_projekt,pultdaecher_schnee_je_projekt,satteldaecher_schnee_je_projekt,
            kehldaecher_schnee_je_projekt), key=attrgetter('edited_date'), reverse=True))




        else:
            querylist = Bauteil.objects.none()

        return querylist





class WindbemessungDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bauteil

    def get_context_data(self, **kwargs):
        context = super(WindbemessungDeleteView, self).get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk2']
        context['slug_mein'] = self.kwargs['slug']
        return context

#macht das nur der User der den Post erstellt hat, ihn auch bearbeiten kann!
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


    def get_success_url(self):
        return reverse_lazy('core:windbemessung_list', args=(self.kwargs.get('slug'),self.kwargs.get('pk2'),))





class ProjektUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = allgEingaben
    form_class = RegCarForm
    template_name = 'core/allgeingaben_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.allgEingaben_eingegeben = True
        #timezone.now()YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]
        form.instance.edited_date = timezone.now()

        return super().form_valid(form)
    #macht das nur der User der den Post erstellt hat, ihn auch bearbeiten kann!
    def test_func(self):
        allgEingaben = self.get_object()
        if self.request.user == allgEingaben.user:
            return True
        return False
    def get_context_data(self, **kwargs):
        context = super(ProjektUpdateView, self).get_context_data(**kwargs)
        aktuelles_projekt = allgEingaben.objects.get(pk=self.kwargs['pk'])
        projekt_name = aktuelles_projekt.projekt_name
        context['projekt_name'] = projekt_name
        context['bin_im_updateview'] = True

        return context
    # success_url mittel {{NExt}}
    def get_success_url(self):
        next_url = self.request.GET.get('next')

        if next_url:
            return (next_url)
        else :
            print('lkhlkjlkjlkjljljlj')
            return reverse_lazy('core:allgEingaben_list')




class AllgemeineAngabenDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = allgEingaben
    success_url = reverse_lazy('core:allgEingaben_list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
