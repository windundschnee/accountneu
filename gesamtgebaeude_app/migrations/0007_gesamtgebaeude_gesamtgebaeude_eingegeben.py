# Generated by Django 2.2.4 on 2019-10-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gesamtgebaeude_app', '0006_auto_20191018_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='gesamtgebaeude',
            name='gesamtgebaeude_eingegeben',
            field=models.BooleanField(default=False),
        ),
    ]
