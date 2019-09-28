"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [


    path('accounts/', include('account_app.urls')),
    path('', include('base_app.urls')),
    path('', include('core.urls')),
    path('kontakt/', include('contact_app.urls')),
    path('', include('freistehende_waende_app.urls')),
    path('', include('flachdaecher_app.urls')),
    path('', include('anzeigetafeln_app.urls')),
    path('', include('freistehendeDaecher_app.urls')),
    path('', include('pultdaecher_app.urls')),
    path('lastannahmen/', include('lastaufstellung_app.urls')),
    path('', include('waende_app.urls')),
    path('', include('pultdach_schnee_app.urls')),
    path('', include('satteldach_schnee_app.urls')),
    path('', include('kehldach_schnee_app.urls')),


    path('', include('allg_berechnungen_app.urls')),
    path('', include('gesamt_pdf_app.urls')),
    path('', include('gesamtgebaeude_app.urls')),



    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
