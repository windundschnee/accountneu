
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    #"""Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password' , 'company','is_pro', 'is_pro_date', 'is_pro_exired_date','verlaengerung_notwendig', 'is_free',
        'is_free_date', 'email_confirmed', 'allgEingaben_eingegeben',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'company', 'is_pro', 'is_pro_date', 'is_pro_exired_date', 'verlaengerung_notwendig', 'is_free', 'is_free_date', 'email_confirmed', 'allgEingaben_eingegeben')
    search_fields = ('email', 'company')
    ordering = ('email',)
