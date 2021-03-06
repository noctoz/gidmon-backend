# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-11-05 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonapi', '0049_recipecreator_sessionbrewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewingsession',
            name='final_volume',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='scale adjusted final volume'),
        ),
        migrations.AddField(
            model_name='brewingsession',
            name='measured_final_volume',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='measured final volume'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='final_volume',
            field=models.DecimalField(decimal_places=2, default=12, max_digits=4, verbose_name='volume left after fermentation'),
        ),
    ]
