# Generated by Django 2.2.4 on 2019-10-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190917_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='bauteil',
            name='gesamtgebaeude_dachart',
            field=models.CharField(blank=True, default='', max_length=185, null=True),
        ),
        migrations.AlterField(
            model_name='bauteil',
            name='bemessungsart_wind_schnee',
            field=models.CharField(blank=True, default='', max_length=185, null=True),
        ),
    ]