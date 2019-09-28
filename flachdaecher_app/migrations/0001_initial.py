# Generated by Django 2.2 on 2019-09-18 22:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0008_auto_20190917_1217'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FlachdachModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_traufenbereich', models.CharField(default='', max_length=80)),
                ('hoehe_attika', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('alpha', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('radius', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('hoehe', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('breite_x', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('breite_y', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('innendruck', models.BooleanField(blank=True, default=True, null=True)),
                ('innendruck_empfohlen', models.BooleanField(blank=True, default=True, null=True)),
                ('some_field', models.CharField(max_length=80)),
                ('some_field_radio2', models.CharField(blank=True, default=1, max_length=80, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('flachdach_eingegeben', models.BooleanField()),
                ('edited_date', models.DateTimeField(blank=True, null=True)),
                ('waende_beruecksichtigen', models.BooleanField(blank=True, default=False, null=True)),
                ('oeffnungen_beruecksichtigen', models.BooleanField(blank=True, default=False, null=True)),
                ('oeffnung_nord_flaeche', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(200)])),
                ('oeffnung_ost_flaeche', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(200)])),
                ('oeffnung_sued_flaeche', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(200)])),
                ('oeffnung_west_flaeche', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, validators=[django.core.validators.MaxValueValidator(200)])),
                ('reibung_beruecksichtigen', models.BooleanField(blank=True, default=False, null=True)),
                ('reibbeiwert_dach', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('reibbeiwert_waende', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('anzahl_streifen', models.CharField(blank=True, default=2, max_length=80, null=True)),
                ('fehlende_korrelation_beruecksichtigen', models.BooleanField(blank=True, default=False, null=True)),
                ('bautteil_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Bauteil')),
                ('projekt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.allgEingaben')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
