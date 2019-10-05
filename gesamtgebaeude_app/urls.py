from django.urls import path
from .views import GesamtgebaeudeCreateView, GesamtgebaeudeDetailView


app_name = 'gesamtgebaeude_app'

urlpatterns = [

    path('<slug:slug>/<int:my>/gesamtgebaeude/<int:pk>/new',GesamtgebaeudeCreateView.as_view(), name='gesamtgebaeude_create'),
    path('<slug:slug>/<int:my>/gesamtgebaeude/<int:pk>', GesamtgebaeudeDetailView.as_view(), name='gesamtgebaeude_detail'),

]
