# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoRental', '0005_auto_20181105_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierent',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
