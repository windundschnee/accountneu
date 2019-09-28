from django.urls import path
from . import views

app_name = 'base_app'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('getpro/', views.GetProView, name='getpro'),
]
