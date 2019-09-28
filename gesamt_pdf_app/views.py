from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.forms.models import model_to_dict
from .models import GesamtPdf
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new
from .latex_ablauf_gesamtpdf import gesamt_pdf_erzeugen
from .forms import pdfBearbeitenForm # new
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from flachdaecher_app.models import FlachdachModel
from anzeigetafeln_app.models import AnzeigetafelnModel
from freistehende_waende_app.models import FreistehendeWaende
from freistehendeDaecher_app.models import FreistehendeDaecherModel
from pultdaecher_app.models import PultdachModel
from pultdach_schnee_app.models import PultdachSchneeModel
from satteldach_schnee_app.models import SatteldachSchneeModel
from kehldach_schnee_app.models import KehldachSchneeModel
from account_app.models import User


class UpdateGesamtPdfView(UpdateView): # new
    form_class = pdfBearbeitenForm
    model = GesamtPdf


    def form_valid(self, form):
        form.instance.user = self.request.user


        meinProjekt_pk = self.kwargs.get('my')
        form.instance.projekt_id = meinProjekt_pk
        if self.request.GET.get('next'):
            form.instance.next = self.request.GET.get('next')
        form.instance.pdf_bearbeitet = True

        return super().form_valid(form)
    def get_form_kwargs(self):
        kwargs = super(UpdateGesamtPdfView, self).get_form_kwargs()

        kwargs['meinProjekt_pk'] = self.kwargs.get('my')
        kwargs['user'] = self.request.user
        kwargs['next'] = self.request.GET.get('next')



        return kwargs
    def get_context_data(self, **kwargs):
        context=super(UpdateGesamtPdfView, self).get_context_data(**kwargs)

        user_id = str(self.request.user.id)
        filename_pdf_anzeigen = '/media/pdf_bearbeiten/'+user_id+'/FullPDF_'+str(self.object.id)+'.pdf'
        context['filename_pdf_anzeigen'] = filename_pdf_anzeigen
        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')

        flachdach_app_wahl = FlachdachModel.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()
        context['flachdach_app_wahl_exists'] = flachdach_app_wahl
        anzeigetafeln_app_wahl = AnzeigetafelnModel.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()
        context['anzeigetafeln_app_wahl_exists'] = anzeigetafeln_app_wahl
        freistehendedaecher_app_wahl = FreistehendeDaecherModel.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()
        context['freistehendedaecher_app_wahl_exists'] = freistehendedaecher_app_wahl
        freistehendewaende_app_wahl = FreistehendeWaende.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()
        context['freistehendewaende_app_wahl_exists'] = freistehendewaende_app_wahl
        pultdach_schnee_app_wahl = PultdachSchneeModel.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()

        context['pultdach_schnee_app_wahl_exists'] = pultdach_schnee_app_wahl
        satteldach_schnee_app_wahl = SatteldachSchneeModel.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()
        context['satteldach_schnee_app_wahl_exists'] = satteldach_schnee_app_wahl

        kehldach_schnee_app_wahl = KehldachSchneeModel.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()
        context['kehldach_schnee_app_wahl_exists'] = kehldach_schnee_app_wahl

        pultdach_app_wahl = PultdachModel.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()
        context['pultdach_app_wahl_exists'] = pultdach_app_wahl
        context['next'] = self.object.next
        context['next_url'] = self.request.GET.get('next')

        return context

class pdfBearbeitenListView(ListView):
    model = GesamtPdf
    template_name = 'gesamt_pdf_app/list.html'


class CreateGesamtPdfView(CreateView): # new
    model = GesamtPdf
    form_class = pdfBearbeitenForm
    template_name = 'gesamt_pdf_app/gesamtpdf_form.html'
    def get_form_kwargs(self):
        kwargs = super(CreateGesamtPdfView, self).get_form_kwargs()

        kwargs['meinProjekt_pk'] = self.kwargs.get('my')
        kwargs['user'] = self.request.user
        kwargs['next'] = self.request.GET.get('next')

        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user

        meinProjekt_pk = self.kwargs.get('my')
        form.instance.projekt_id = meinProjekt_pk
        form.instance.next = self.request.GET.get('next')



        form.instance.pdf_bearbeitet = True


        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context=super(CreateGesamtPdfView, self).get_context_data(**kwargs)
        flachdach_app_wahl = FlachdachModel.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()
        context['flachdach_app_wahl_exists'] = flachdach_app_wahl
        anzeigetafeln_app_wahl = AnzeigetafelnModel.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()
        context['anzeigetafeln_app_wahl_exists'] = anzeigetafeln_app_wahl
        freistehendedaecher_app_wahl = FreistehendeDaecherModel.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()
        context['freistehendedaecher_app_wahl_exists'] = freistehendedaecher_app_wahl
        freistehendewaende_app_wahl = FreistehendeWaende.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()
        context['freistehendewaende_app_wahl_exists'] = freistehendewaende_app_wahl
        pultdach_app_wahl = PultdachModel.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()
        context['pultdach_app_wahl_exists'] = pultdach_app_wahl
        pultdach_schnee_app_wahl = PultdachSchneeModel.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()
        context['pultdach_schnee_app_wahl_exists'] = pultdach_schnee_app_wahl
        satteldach_schnee_app_wahl = SatteldachSchneeModel.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()
        context['satteldach_schnee_app_wahl_exists'] = satteldach_schnee_app_wahl

        kehldach_schnee_app_wahl = KehldachSchneeModel.objects.filter(user=self.request.user, projekt_id=self.kwargs['my']).exists()
        context['kehldach_schnee_app_wahl_exists'] = kehldach_schnee_app_wahl

        context['pk'] = self.kwargs.get('my')
        context['slug'] = self.kwargs.get('slug')
        next_url = self.request.GET.get('next')
        context['next'] = self.request.GET.get('next')
        context['next_url'] = self.request.GET.get('next')


        return context
class PdfCreateRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'gesamt_pdf_app:gesamt_pdf_update'

    def get_redirect_url(self, *args, **kwargs):
        print('dobini zerscht im redirect')

        pk=self.kwargs['pk']
        user_has_free_account = self.request.user.is_free
        arg_latex = {'user_has_free_account': user_has_free_account,


                    }

        #hier könnte die funktion für das gesamtpdf gestartet werden
        pdf_erzeugen = gesamt_pdf_erzeugen(self, arg_latex)




        return super().get_redirect_url(*args, **kwargs)
