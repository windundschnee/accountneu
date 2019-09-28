from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import DatenbankMaterial
from .forms_all import DatenbankMaterialForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.
class HomogeneSchichtAllCreateView(LoginRequiredMixin,CreateView): # new
    model = DatenbankMaterial
    form_class = DatenbankMaterialForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class HomogeneSchichtAllListView(LoginRequiredMixin, ListView):
    model = DatenbankMaterial


    def get_queryset(self):
        result = super(HomogeneSchichtAllListView, self).get_queryset()
        if self.request.user.is_authenticated:
            querylist = DatenbankMaterial.objects.all()
        else:
            querylist = DatenbankMaterial.objects.none()

        return querylist


class HomogeneSchichtAllDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DatenbankMaterial

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
    def get_success_url(self):
        return reverse_lazy('lastaufstellung_app:datenbank_list')

class HomogeneSchichtAllUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DatenbankMaterial
    form_class = DatenbankMaterialForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    #macht das nur der User der den Post erstellt hat, ihn auch bearbeiten kann!
    def test_func(self):
        allgEingaben = self.get_object()
        if self.request.user == allgEingaben.user:
            return True
        return False
    def get_context_data(self, **kwargs):
        context = super(HomogeneSchichtAllUpdateView, self).get_context_data(**kwargs)
        return context
    # success_url mittel {{NExt}}
    def get_success_url(self):
        return reverse_lazy('lastaufstellung_app:datenbank_list')
