# Generated by Django 2.2.4 on 2019-09-28 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gesamt_pdf_app', '0003_gesamtpdf_kehldach_schnee_app_wahl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gesamtpdf',
            name='logo_kopfzeile',
        ),
    ]
