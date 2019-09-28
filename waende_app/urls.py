from django.urls import path

from .views import RecipeCreateView



app_name = 'waende_app'




urlpatterns = [

    path('rezept/create/', RecipeCreateView.as_view(), name='add_recipe') # new
]
