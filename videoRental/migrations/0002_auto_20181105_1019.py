# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 10:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videoRental', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='videoRental.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='videoRental.MovieGenre'),
        ),
        migrations.AddField(
            model_name='movierent',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='videoRental.Movie'),
        ),
    ]