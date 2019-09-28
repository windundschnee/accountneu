from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import HomogeneSchicht, Bauteil_Last
from .forms import HomogeneSchichtForm, BauteilForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.

class BauteilCreateView(LoginRequiredMixin,CreateView): # new
    model = Bauteil_Last
    form_class = BauteilForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BauteilDetailView(DetailView):

    model = Bauteil_Last

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class BauteilListView(LoginRequiredMixin, ListView):
    model = Bauteil_Last

    def get_context_data(self, **kwargs):
        context = super(BauteilListView, self).get_context_data(**kwargs)


        return context


    def get_queryset(self):
        result = super(BauteilListView, self).get_queryset()
        if self.request.user.is_authenticated:
            querylist = Bauteil_Last.objects.all()
        else:
            querylist = Bauteil_Last.objects.none()

        return querylist

class BauteilDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Bauteil_Last
    success_url = reverse_lazy('lastaufstellung_app:bauteil_list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class BauteilUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bauteil_Last
    form_class = BauteilForm

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
        context = super(BauteilUpdateView, self).get_context_data(**kwargs)
        return context
    # success_url mittel {{NExt}}
    def get_success_url(self):
        return reverse_lazy('lastaufstellung_app:bauteil_list')
