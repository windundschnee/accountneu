import stripe # new
from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import render # new

from django.conf import settings



stripe.api_key = settings.STRIPE_SECRET_KEY # new


def charge(request): # new
    if request.method == 'POST':
        token = request.POST['stripeToken']
        charge = stripe.Charge.create(
            amount=5000, #500 = 5,00 Eur
            currency='eur',
            description='A Django charge',
            source=token
        )

        return redirect('student_signup')
