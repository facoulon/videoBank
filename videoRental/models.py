# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField
# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class MovieGenre(models.Model):
    label = models.CharField(max_length=10, blank=True, null=True)
    slug = AutoSlugField(populate_from="label")

    def __unicode__(self):
        return self.label

class Movie(models.Model):
    actors = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True) 
    director = models.CharField(max_length=25, blank=True, null=True)   
    length = models.TimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    picture = models.ImageField(upload_to="Movie",blank=True, null=True)
    release_date = models.DateField(auto_now=False, auto_now_add=False,blank=True, null=True)
    rented = models.BooleanField()
    title = models.CharField(max_length=100, blank=True, null=True)
    slug = AutoSlugField(populate_from="title")
    synopsis = models.TextField(blank=True, null=True)
    trailer_url = models.URLField(max_length=200,blank=True, null=True)
    genre = models.ForeignKey('MovieGenre',blank=True, null=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

class Customer(UserenaBaseProfile):
    """Model definition for Customer."""
    user = models.OneToOneField(User, unique=True)

class MovieRent(models.Model):
    checkout_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    return_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    customer = models.ForeignKey('Customer',blank=True, null=True, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie',blank=True, null=True, on_delete=models.CASCADE)