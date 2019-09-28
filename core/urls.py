from django.urls import path
from . import views

from .views import (

AllgemeineAngabenListView,
AllgemeineAngabenDeleteView,
WindbemessungCreateView,
WindbemessungListView,
WindbemessungUpdateView,
WindbemessungDeleteView,
WindbemessungListView,
ProjektCreateView,
ProjektUpdateView,


)
app_name = 'core'

urlpatterns = [

    path('meineProjekte/list/', AllgemeineAngabenListView.as_view(), name='allgEingaben_list'),
    path('<slug:slug>/<int:pk>/delete', AllgemeineAngabenDeleteView.as_view(), name='allgEingaben_delete'),
    path('meineProjekte/new/', ProjektCreateView.as_view(), name='projekt_create'),
    path('<slug:slug>/<int:pk>/update/', ProjektUpdateView.as_view(), name='projekt_update'),
    path('<slug:slug>/<int:pk>/meineBauteile/new/', WindbemessungCreateView.as_view(), name='windbemessung_create'),
    path('<slug:slug>/<int:pk2>/meineBauteile/<int:pk>/update/', WindbemessungUpdateView.as_view(), name='windbemessung_update'),
    path('<slug:slug>/<int:pk>/meineBauteile/list/', WindbemessungListView.as_view(), name='windbemessung_list'),
    path('<slug:slug>/<int:pk2>/meineBauteile/<int:pk>/delete/', WindbemessungDeleteView.as_view(), name='windbemessung_delete'),



]
