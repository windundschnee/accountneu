# Generated by Django 2.2 on 2019-09-15 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_allgeingaben_schneelastzone_hidden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allgeingaben',
            name='schneelastzone_hidden',
        ),
    ]
