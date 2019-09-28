from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from stdimage import StdImageField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager):
    #"""Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        #"""Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        #"""Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        #"""Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    #"""User model."""
    username = None
    email = models.EmailField(_('email address'), unique=True, blank=False)
    company = models.CharField(max_length=30, blank=False)
    #allg Eingaben
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email_confirmed = models.BooleanField(default=False)
    is_pro = models.BooleanField('Pro User', default=False)
    is_pro_date = models.DateTimeField(blank=True, null=True)
    is_pro_exired_date = models.DateTimeField(blank=True, null=True)
    is_free_date = models.DateTimeField(blank=True, null=True)
    allgEingaben_eingegeben = models.BooleanField(default=False)
    verlaengerung_notwendig = models.BooleanField(default=False)
    is_free = models.BooleanField('Free User', default=False)
    logo_kopfzeile = StdImageField(upload_to='bilder/', blank=True, variations={'small': (160, 124),})
    objects = UserManager()


class Profile(models.Model):
    email_confirmed = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.email

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:

        Profile.objects.create(user=instance)
        instance.profile.save()
