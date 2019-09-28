# accounts/urls.py
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views
from django.urls import path, re_path
app_name = 'account_app'
urlpatterns = [
    url(r'^signup/$', views.Signup_view, name='signup'),
    url(r'^profile/$', views.Profile_view, name='profile'),
    url(r'^profile/edit$', views.Edit_Profile_view, name='edit_profile'),
    url(r'^change-password$', views.change_password_view, name='change_password'),
    url(r'^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    url(r'^reset/$',
    auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt'
    ),
    name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
    name='password_reset_confirm'),

    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^charge/$', views.charge, name='charge'),



]
