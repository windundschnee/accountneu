
from django.views.generic.base import TemplateView
from account_app.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime, timedelta

class HomePageView(TemplateView):
    template_name = 'base_app/home.html'

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.is_pro:
                is_pro_exired_date = self.request.user.is_pro_exired_date
                is_pro_exired_date_two_weeks_before = is_pro_exired_date-timedelta(14)
                datetime_now = datetime.now(tz=timezone.utc)
                if is_pro_exired_date <= datetime_now:
                    print('ibinididididididididididididididididiid')
                    self.request.user.verlaengerung_notwendig = True
                    self.request.user.is_free = True
                    self.request.user.is_pro = False
                    self.request.user.save()

                elif is_pro_exired_date_two_weeks_before <= datetime_now:
                    self.request.user.verlaengerung_notwendig = True
                    self.request.user.save()

                else:
                    self.request.user.verlaengerung_notwendig = False
                    self.request.user.save()


        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['verlaengerung_notwendig'] = self.request.user.verlaengerung_notwendig

        return context




@login_required
def GetProView(request):
    return render(request, 'base_app/getpro.html')
