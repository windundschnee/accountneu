from django.urls import path
from .views import (
PultdachCreateView,
PultdachDetailView,
PultdachUpdateView,




)


app_name = 'pultdaecher_app'

urlpatterns = [
    path('<slug:slug>/<int:my>/Pultdaecher/<int:pk>/new', PultdachCreateView.as_view(), name='pultdach_create'),
    path('<slug:slug>/<int:my>/Pultdaecher/<int:pk>', PultdachDetailView.as_view(), name='pultdach_detail'),
    path('<slug:slug>/<int:my>/Pultdaecher/<int:pk>/Update/', PultdachUpdateView.as_view(), name='pultdach_update'),




]
