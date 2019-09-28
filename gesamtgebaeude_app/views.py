from django.shortcuts import render
from.models import Gesamtgebaeude
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from gesamt_pdf_app.models import GesamtPdf
from django.forms.models import model_to_dict
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
class GesamtgebaeudeCreateView(LoginRequiredMixin, CreateView):
    model = Gesamtgebaeude
    form_class = flachdaecherForm


    def form_valid(self, form):

        form.instance.user = self.request.user



        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FlachdachCreateView, self).get_context_data(**kwargs)

        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')
        return context
