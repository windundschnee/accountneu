# Generated by Django 2.2 on 2019-09-19 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kehldach_schnee_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kehldachschneemodel',
            name='abrutschen_verhindert',
        ),
    ]
