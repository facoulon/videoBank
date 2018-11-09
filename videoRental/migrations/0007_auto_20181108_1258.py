# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-08 12:58
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videoRental', '0006_auto_20181106_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', unique_with=['title']),
        ),
    ]