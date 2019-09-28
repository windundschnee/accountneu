from django.urls import path

from .views import (
FlachdachCreateView,
FlachdachDetailView,
FlachdachUpdateView,
PdfCreateRedirectView,



)


app_name = 'flachdaecher_app'

urlpatterns = [


    path('<slug:slug>/<int:my>/Flachdaecher/<int:pk>/new', FlachdachCreateView.as_view(), name='flachdach_create'),
    path('<slug:slug>/<int:my>/Flachdaecher/<int:pk>', FlachdachDetailView.as_view(), name='flachdach_detail'),
    path('<slug:slug>/<int:my>/Flachdaecher/<int:pk>/Update/', FlachdachUpdateView.as_view(), name='flachdach_update'),
    path('<slug:slug>/<int:my>/Flachdaecher/<int:pk>/PdfErzeugen', PdfCreateRedirectView.as_view(), name='flachdach_redirect'),





]
