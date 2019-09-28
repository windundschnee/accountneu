# Generated by Django 2.2 on 2019-09-18 22:36

from django.conf import settings
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
            name='FreistehendeDaecherModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoehe', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('breite_d', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('breite_b', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('alpha', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('phi', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('hoehe_GOK', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('some_field_radio', models.CharField(max_length=80, null=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('freistehendedaecher_eingegeben', models.BooleanField()),
                ('edited_date', models.DateTimeField(blank=True, null=True)),
                ('bautteil_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Bauteil')),
                ('projekt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.allgEingaben')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
