from django.urls import path
from .views import (KehldachSchneeCreateView,
                    KehldachSchneeUpdateView, KehldachSchneeDetailView,PdfCreateRedirectViewKehldachSchnee)

app_name = 'kehldach_schnee_app'

urlpatterns = [

    path('<slug:slug>/<int:my>/KehldaecherSchnee/<int:pk>/new',
         KehldachSchneeCreateView.as_view(), name='kehldach_schnee_create'),
    path('<slug:slug>/<int:my>/KehldaecherSchnee/<int:pk>/update/',
         KehldachSchneeUpdateView.as_view(), name='kehldach_schnee_update'),
    path('<slug:slug>/<int:my>/KehldaecherSchnee/<int:pk>',
         KehldachSchneeDetailView.as_view(), name='kehldach_schnee_detail'),
    path('<slug:slug>/<int:my>/kehldach_schnee/<int:pk>/pdferzeugen',
         PdfCreateRedirectViewKehldachSchnee.as_view(), name='kehldach_schnee_redirect'),

]
