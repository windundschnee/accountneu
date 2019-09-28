from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'contact_app'

urlpatterns = [

    path('success/', views.successView, name='success'),
    path('', views.emailView, name='contact'),



]
