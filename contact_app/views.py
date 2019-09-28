
# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import CommentForm

import urllib.request
import json
from django.conf import settings
from django.contrib import messages




def emailView(request):
    if request.method == 'GET':
        form = CommentForm()



    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            # Captcha Anfang.
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())


            if result['success']:
                # Wenn Captcha richtig ist...
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['from_email']
                message = form.cleaned_data['message']
                message2 = 'Hallo Dennis! Du hast eine neue Nachricht von: ' + subject + '  E-Mail: ' + from_email +'     Er hat dir folgende Nachricht geschrieben:       ' + message

                send_mail(subject, message2, from_email, ['dennis.am90@gmail.com'] , fail_silently=False)
                return redirect('contact_app:success')



            else:

                messages.error(request, 'Invalid reCAPTCHA. Please try again.')


    return render(request, "contact_app/contacts.html", {'form': form})

def successView(request):
    return render(request, 'contact_app/success.html')
