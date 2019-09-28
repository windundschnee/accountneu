from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (

    AnzeigetafelnCreateView,
    AnzeigetafelnUpdateView,
    AnzeigetafelnDetailView,
    PdfCreateRedirectViewAnzeigetafeln,



)
app_name = 'anzeigetafeln_app'

urlpatterns = [


    path('<slug:slug>/<int:my>/anzeigetafeln/<int:pk>/update/', AnzeigetafelnUpdateView.as_view(), name='anzeigetafeln_update'),
    path('<slug:slug>/<int:my>/anzeigetafeln/<int:pk>/new', AnzeigetafelnCreateView.as_view(), name='anzeigetafeln_create'),

    path('<slug:slug>/<int:my>/anzeigetafeln/<int:pk>', AnzeigetafelnDetailView.as_view(), name='anzeigetafeln_detail'),
    path('<slug:slug>/<int:my>/anzeigetafeln/<int:pk>/pdferzeugen', PdfCreateRedirectViewAnzeigetafeln.as_view(), name='anzeigetafeln_redirect'),





]
