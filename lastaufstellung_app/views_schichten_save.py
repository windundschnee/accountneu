from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import HomogeneSchicht, Bauteil
from .forms import HomogeneSchichtForm, BauteilForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.
class HomogeneSchichtCreateView(LoginRequiredMixin,CreateView): # new
    model = HomogeneSchicht
    form_class = HomogeneSchichtForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        meinbauteil_pk = self.kwargs.get('pk')
        form.instance.bauteil_id = meinbauteil_pk

        return super().form_valid(form)




class HomogeneSchichtUserListView(LoginRequiredMixin, ListView):
    model = HomogeneSchicht
    template_name = 'lastaufstellung_app/homogeneschicht_user_list.html'

    def get_context_data(self, **kwargs):
        context = super(HomogeneSchichtUserListView, self).get_context_data(**kwargs)
        print(self.kwargs['pk'])
        aktuelles_bauteil = Bauteil.objects.get(id=self.kwargs['pk'])
        bauteil_name = aktuelles_bauteil.name
        context['bauteil_name'] = bauteil_name
        context['pk'] = self.kwargs['pk']
        context['slug'] = self.kwargs['slug']

        return context


    def get_queryset(self):
        result = super(HomogeneSchichtUserListView, self).get_queryset()
        if self.request.user.is_authenticated:
            querylist = HomogeneSchicht.objects.filter(user=self.request.user, bauteil_id=self.kwargs['pk'])
        else:
            querylist = HomogeneSchicht.objects.none()

        return querylist


class HomogeneSchichtDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = HomogeneSchicht

    def get_context_data(self, **kwargs):
        context = super(HomogeneSchichtDeleteView, self).get_context_data(**kwargs)

        context['pk'] = self.kwargs['pk']
        context['pk2'] = self.kwargs['pk2']
        context['slug'] = self.kwargs['slug']

        return context
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
    def get_success_url(self):
        return reverse_lazy('lastaufstellung_app:homogene_schicht_list', args=(self.kwargs.get('slug'),self.kwargs.get('pk2'),))

class HomogeneSchichtUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = HomogeneSchicht
    form_class = HomogeneSchichtForm

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
        context = super(HomogeneSchichtUpdateView, self).get_context_data(**kwargs)
        return context
    # success_url mittel {{NExt}}
    def get_success_url(self):
        return reverse_lazy('lastaufstellung_app:homogene_schicht_list', args=(self.kwargs.get('slug'),self.kwargs.get('pk2'),))
