# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-19 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonapi', '0037_auto_20170119_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beertype',
            name='priming_co2_volume_max',
        ),
        migrations.RemoveField(
            model_name='beertype',
            name='priming_co2_volume_min',
        ),
        migrations.AddField(
            model_name='beertype',
            name='priming_co2_max',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3, verbose_name='max CO2 for priming in g/l'),
        ),
        migrations.AddField(
            model_name='beertype',
            name='priming_co2_min',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3, verbose_name='min CO2 for priming in g/l'),
        ),
    ]