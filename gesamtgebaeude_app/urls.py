from django.urls import path
from .views import GesamtgebaeudeCreateView, GesamtgebaeudeDetailView,GesamtgebaeudeUpdateView


app_name = 'gesamtgebaeude_app'

urlpatterns = [

    path('<slug:slug>/<int:my>/Gesamtgebaeude/<int:pk>/new',GesamtgebaeudeCreateView.as_view(), name='gesamtgebaeude_create'),
    path('<slug:slug>/<int:my>/Gesamtgebaeude/<int:pk>', GesamtgebaeudeDetailView.as_view(), name='gesamtgebaeude_detail'),
    path('<slug:slug>/<int:my>/Gesamtgebaeude/<int:pk>/Update/', GesamtgebaeudeUpdateView.as_view(), name='gesamtgebaeude_update'),
]
