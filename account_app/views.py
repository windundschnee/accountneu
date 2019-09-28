
from django.shortcuts import render, redirect
from django.contrib.auth import login
#from django.contrib.auth.forms import PasswordChangeForm
from .forms import (
    SignUpForm,
    EditProfileForm,
    PasswordChangeForm,
        )
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.conf import settings
from django.core.mail import send_mail

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


import stripe # new

import os, sys

from .models import User
from django.utils import timezone
from datetime import timedelta
@login_required
def Profile_view(request):
    args = {'user':request.user }
    return render(request, 'registration/profile.html', args)

@login_required
def Edit_Profile_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('account_app:profile')
    else:
        form = EditProfileForm(instance = request.user)
        args = {'form':form }
        return render(request, 'registration/profile_edit.html', args)

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('account_app:profile')
        else:
            messages.error(request,'Das eingegebene Passwort existiert nicht und/oder die Passwörter stimmen nicht überrein!.')
            messages.error(request,'Passwort Anforderungen beachten:.')
            return redirect('account_app:change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        print(form)
        args = {'form':form }
        return render(request, 'registration/change_password.html', args)






stripe.api_key = settings.STRIPE_SECRET_KEY # new


@login_required
def charge(request): # new
    if request.method == 'POST':
        user = User.objects.get(email = request.user)
        if user.is_pro == True:

            user.is_pro_exired_date = user.is_pro_exired_date+ timedelta(365)
        else:
            user.is_pro = True
            user.is_pro_exired_date = timezone.now()+ timedelta(365)


        user.is_pro_date = timezone.now()

        user.is_free = False
        user.save()

        token = request.POST['stripeToken']
        charge = stripe.Charge.create(
            amount=5000, #500 = 5,00 Eur
            currency='eur',
            description='A Django charge',
            source=token
        )

        return redirect('base_app:home')


def Signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.is_free  = True
            user.is_free_date = timezone.now()
            form.save()
            current_site = get_current_site(request)
            subject = 'Aktiviere deinen Account!'
            message = render_to_string('registration/account_activation_email.html', {
                'user':user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),        
                'token': account_activation_token.make_token(user),
            })

            from_email = settings.DEFAULT_FROM_EMAIL
            to_list = [user.email, settings.EMAIL_HOST_USER ]


            send_mail(subject, message, from_email, to_list)

            #hier erstelle ich einen ordner mit usernam




            return redirect('account_app:account_activation_sent')

    else:
        form = SignUpForm()


    return render(request, 'registration/signup.html', {'form': form})



def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('base_app:home')
    else:
        return render(request, 'registration/account_activation_invalid.html')
