# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-30 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonapi', '0045_auto_20171030_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mashsessionentry',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='amount of malt in kg'),
        ),
    ]
