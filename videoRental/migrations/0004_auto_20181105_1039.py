# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoRental', '0003_auto_20181105_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierent',
            name='checkout_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
