from django.urls import path

from .views import (
FreistehendeWaendeCreateView,
FreistehendeWaendeDetailView,
FreistehendeWaendeUpdateView,
PdfCreateRedirectView,




)
app_name = 'freistehende_waende_app'

urlpatterns = [
    path('<slug:slug>/<int:my>/freistehende_waende/<int:pk>/new', FreistehendeWaendeCreateView.as_view(), name='freistehende_waende_create'),
    path('<slug:slug>/<int:my>/freistehende_waende/<int:pk>', FreistehendeWaendeDetailView.as_view(), name='freistehende_waende_detail'),
    path('<slug:slug>/<int:my>/freistehende_waende/<int:pk>/update/', FreistehendeWaendeUpdateView.as_view(), name='freistehende_waende_update'),
    path('<slug:slug>/<int:my>/freistehende_waende/<int:pk>/pdferzeugen', PdfCreateRedirectView.as_view(), name='freistehende_waende_redirect'),






]
