from django.urls import path
from .views import (
FreistehendeDaecherCreateView,
FreistehendeDaecherDetailView,
FreistehendeDaecherUpdateView,
PdfCreateRedirectView,



)

app_name = 'freistehendeDaecher_app'

urlpatterns = [

    path('<slug:slug>/<int:my>/freistehende_daecher/<int:pk>/new', FreistehendeDaecherCreateView.as_view(), name='freistehende_daecher_create'),
    path('<slug:slug>/<int:my>/freistehende_daecher/<int:pk>', FreistehendeDaecherDetailView.as_view(), name='freistehende_daecher_detail'),
    path('<slug:slug>/<int:my>/freistehende_daecher/<int:pk>/update/', FreistehendeDaecherUpdateView.as_view(), name='freistehende_daecher_update'),
    path('<slug:slug>/<int:my>/freistehende_daecher/<int:pk>/pdferzeugen', PdfCreateRedirectView.as_view(), name='freistehende_daecher_redirect'),



]
