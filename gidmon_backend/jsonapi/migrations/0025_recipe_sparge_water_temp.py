# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-04 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonapi', '0024_auto_20170104_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='sparge_water_temp',
            field=models.IntegerField(default=0, verbose_name='sparge water temperature'),
        ),
    ]