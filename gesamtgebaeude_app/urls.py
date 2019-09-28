from django.urls import path
from views import GesamtgebaeudeCreateView


app_name = 'gesamtgebaeude_app'

urlpatterns = [

    path('<slug:slug>/<int:my>/gesamtgebauede/<int:pk>/new',GesamtgebaeudeCreateView.as_view(), name='gesamtgebauede_create'),

]
