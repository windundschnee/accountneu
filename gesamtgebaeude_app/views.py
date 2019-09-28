from django.shortcuts import render
from.models import Gesamtgebaeude
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from gesamt_pdf_app.models import GesamtPdf
from django.forms.models import model_to_dict
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import GesamtgebauedeForm
from .models import Gesamtgebaeude
from django.utils import timezone
from core.models import allgEingaben, Bauteil
from gesamt_pdf_app.models import GesamtPdf
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
import os.path as path
from pathlib import Path
import os
from django.urls import reverse_lazy # new
# Create your views here.
class GesamtgebaeudeCreateView(LoginRequiredMixin, CreateView):
    model = Gesamtgebaeude
    form_class = GesamtgebauedeForm


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

            return reverse_lazy('flachdaecher_app:flachdach_create', args=(self.object.projekt.slug, self.object.projekt.id, self.object.bautteil_name.id))
        else:
            print('Errrrrööööööööööööööööööööööööööööööööööööööööööööööööööör')
            return reverse_lazy('core:allgEingaben_list')
