# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-19 20:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jsonapi', '0034_auto_20170119_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='target_pitch_rate',
            new_name='pitch_type',
        ),
    ]
