from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import SetPasswordForm

class PasswordChangeForm(SetPasswordForm):

    error_messages = {
        **SetPasswordForm.error_messages,
        'password_incorrect': ("Your old password was entered incorrectly. Please enter it again."),
    }
    old_password = forms.CharField(
        label=("Altes Passwort"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True, 'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        label=("Neues Passwort"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True, 'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label=("Neues Passwort bestätigen"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True, 'class': 'form-control'}),
    )
    field_order = ['old_password', 'new_password1', 'new_password2']

    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password



class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label=("Passwort"),
    widget=forms.PasswordInput(attrs={'class': 'form-control',
                    'placeholder': 'Passwort eingeben',
                                      'required': 'true',

    })
)
    password2 = forms.CharField(label=("Passwort bestätigen"),
    widget=forms.PasswordInput(attrs={'class': 'form-control',
    'placeholder': 'Passwort bestätigen',
                                      'required': 'true',

    })
)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
                'email',
                'company',


                 )
        labels = {
            "email": "E-Mail:",
            "company": "Firma:",



        }
        widgets = {

            'company': forms.TextInput( attrs={ 'class': 'form-control',
                    'placeholder': 'Firmenname eingeben', 'required': True, } ),
            'email': forms.EmailInput( attrs={ 'class': 'form-control',
                    'placeholder': 'Bitte gültige E-Mail Adresse eingeben', 'required': True, } ),





        }


    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']


        if commit:
            user.save()

        return user


class EditProfileForm(UserChangeForm):

    password = ReadOnlyPasswordHashField(label= ("Passwort:"),
            help_text= ("Passwort wird verschlüsselt angezeigt. "
                        "Sie können Ihr Passwort jederzeit unter Profil ändern. "))

    class Meta:
        model = User
        fields = (
                'email',
                'company',

                )

        labels = {
                    "company": "Firma:",
        "email": "E-Mail:",
                }
        widgets = {

            'company': forms.TextInput( attrs={ 'class': 'form-control',
                    'placeholder': 'Firmenname eingeben', 'required': True, } ),
            'email': forms.EmailInput( attrs={ 'class': 'form-control',
                    'placeholder': 'Bitte gültige E-Mail Adresse eingeben', 'required': True, } ),





        }
