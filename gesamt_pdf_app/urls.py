from django.urls import path

from .views import pdfBearbeitenListView, CreateGesamtPdfView, UpdateGesamtPdfView, PdfCreateRedirectView


app_name = 'gesamt_pdf_app'




urlpatterns = [
    path('list/', pdfBearbeitenListView.as_view(), name='gesamt_pdf_list'),
    path('<slug:slug>/<int:my>/PdfBearbeiten/<int:pk>/PdfErzeugen', PdfCreateRedirectView.as_view(), name='gesamt_pdf_redirect'),
    path('<slug:slug>/<int:my>/PdfBearbeiten/new', CreateGesamtPdfView.as_view(), name='gesamt_pdf_create'),
    path('<slug:slug>/<int:my>/PdfBearbeiten/<int:pk>/update', UpdateGesamtPdfView.as_view(), name='gesamt_pdf_update'),
]
