from django.urls import path
from .views import (PultdachSchneeCreateView,
                    PultdachSchneeUpdateView, PultdachSchneeDetailView,PdfCreateRedirectViewPultdachSchnee)

app_name = 'pultdach_schnee_app'

urlpatterns = [

    path('<slug:slug>/<int:my>/PultdaecherSchnee/<int:pk>/new',
         PultdachSchneeCreateView.as_view(), name='pultdach_schnee_create'),
    path('<slug:slug>/<int:my>/PultdaecherSchnee/<int:pk>/update/',
         PultdachSchneeUpdateView.as_view(), name='pultdach_schnee_update'),
    path('<slug:slug>/<int:my>/PultdaecherSchnee/<int:pk>',
         PultdachSchneeDetailView.as_view(), name='pultdach_schnee_detail'),
    path('<slug:slug>/<int:my>/pultdach_schnee/<int:pk>/pdferzeugen',
         PdfCreateRedirectViewPultdachSchnee.as_view(), name='pultdach_schnee_redirect'),

]
