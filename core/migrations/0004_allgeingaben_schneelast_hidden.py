# Generated by Django 2.2 on 2019-09-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190915_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='allgeingaben',
            name='schneelast_hidden',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
