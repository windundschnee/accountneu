from django.urls import path
from .views_schichten_all import *
from .views_bauteil import *

from .views_schichten import *


app_name = 'lastaufstellung_app'


urlpatterns = [

    path('HomogeneSchicht/new', HomogeneSchichtCreateView.as_view(), name='homogene_schicht_create'),
    path('Bauteil/new', BauteilCreateView.as_view(), name='bauteil_create'),
    path('Bauteil/<int:pk>/', BauteilDetailView.as_view(), name='bauteil_detail'),
    path('<slug:slug>/<int:pk>/Schicht/list/', HomogeneSchichtUserListView.as_view(), name='homogene_schicht_list'),
    path('Bauteil/list/', BauteilListView.as_view(), name='bauteil_list'),
    path('<slug:slug>/<int:pk>/delete', BauteilDeleteView.as_view(), name='bauteil_delete'),
    path('<slug:slug>/<int:pk>/bauteil/', BauteilUpdateView.as_view(), name='bauteil_update'),
    path('<slug:slug>/<int:pk2>/Schicht/<int:pk>/delete', HomogeneSchichtDeleteView.as_view(), name='homogene_schicht_delete'),
    path('<slug:slug>/<int:pk2>/bauteil/<int:pk>/', HomogeneSchichtUpdateView.as_view(), name='homogene_schicht_update'),
    path('Datenbank/list/', HomogeneSchichtAllListView.as_view(), name='datenbank_list'),
    path('Datenbank/new', HomogeneSchichtAllCreateView.as_view(), name='datenbank_create'),
    path('Datenbank/<int:pk>/delete/', HomogeneSchichtAllDeleteView.as_view(), name='datenbank_delete'),
    path('Datenbank/<int:pk>/', HomogeneSchichtAllUpdateView.as_view(), name='datenbank_update'),
]
