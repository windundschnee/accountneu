from django.urls import path
from .views import (SatteldachSchneeCreateView,
                    SatteldachSchneeUpdateView, SatteldachSchneeDetailView,PdfCreateRedirectViewSatteldachSchnee)

app_name = 'satteldach_schnee_app'

urlpatterns = [

    path('<slug:slug>/<int:my>/SatteldachSchnee/<int:pk>/new',
         SatteldachSchneeCreateView.as_view(), name='satteldach_schnee_create'),
    path('<slug:slug>/<int:my>/SatteldachSchnee/<int:pk>/update/',
         SatteldachSchneeUpdateView.as_view(), name='satteldach_schnee_update'),
    path('<slug:slug>/<int:my>/SatteldachSchnee/<int:pk>',
         SatteldachSchneeDetailView.as_view(), name='satteldach_schnee_detail'),
    path('<slug:slug>/<int:my>/SatteldachSchnee/<int:pk>/pdferzeugen',
         PdfCreateRedirectViewSatteldachSchnee.as_view(), name='satteldach_schnee_redirect'),

]
