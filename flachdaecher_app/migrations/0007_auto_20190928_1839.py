# Generated by Django 2.2.4 on 2019-09-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flachdaecher_app', '0006_auto_20190924_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flachdachmodel',
            name='breite_x',
            field=models.DecimalField(decimal_places=1, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='flachdachmodel',
            name='breite_y',
            field=models.DecimalField(decimal_places=1, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='flachdachmodel',
            name='hoehe',
            field=models.DecimalField(decimal_places=1, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='flachdachmodel',
            name='hoehe_attika',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='flachdachmodel',
            name='oeffnung_nord_flaeche',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='flachdachmodel',
            name='oeffnung_ost_flaeche',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='flachdachmodel',
            name='oeffnung_sued_flaeche',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='flachdachmodel',
            name='oeffnung_west_flaeche',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='flachdachmodel',
            name='radius',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=7, null=True),
        ),
    ]
