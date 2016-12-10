# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-10 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonapi', '0008_newsitem_preamble'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='image_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beer',
            name='untappd_url',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
