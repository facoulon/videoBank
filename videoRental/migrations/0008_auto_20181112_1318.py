# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 13:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videoRental', '0007_auto_20181108_1258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'client'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'film'},
        ),
        migrations.AlterModelOptions(
            name='moviegenre',
            options={'verbose_name': 'genre film'},
        ),
        migrations.AlterModelOptions(
            name='movierent',
            options={'verbose_name': 'film lou\xe9'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='utilisateur'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='auteur'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='pays'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='directeur'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='length',
            field=models.TimeField(blank=True, null=True, verbose_name='dur\xe9e'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='Movie', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(blank=True, null=True, verbose_name='date de sortie'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rented',
            field=models.BooleanField(verbose_name='lou\xe9'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='titre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='trailer_url',
            field=models.URLField(blank=True, null=True, verbose_name='bande annonce'),
        ),
        migrations.AlterField(
            model_name='movierent',
            name='checkout_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date de location'),
        ),
        migrations.AlterField(
            model_name='movierent',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='videoRental.Customer', verbose_name='client'),
        ),
        migrations.AlterField(
            model_name='movierent',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='videoRental.Movie', verbose_name='film'),
        ),
        migrations.AlterField(
            model_name='movierent',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date de retour'),
        ),
    ]
