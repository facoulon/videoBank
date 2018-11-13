# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from autoslug import AutoSlugField
# Create your models here.
from django.contrib.auth.models import User
# from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from django.core.urlresolvers import reverse

class MovieGenre(models.Model):
    label = models.CharField(max_length=10, blank=True, null=True)
    slug = AutoSlugField(populate_from="label")

    def __unicode__(self):
        return self.label
    class Meta:
        """docstring for Meta."""
        verbose_name = "genre film"

class Movie(TranslatableModel):

    translations = TranslatedFields(
    title = models.CharField(verbose_name=_("titre"),max_length=100, blank=True, null=True),
    country = models.CharField(verbose_name=_("pays"),max_length=25, blank=True, null=True),
    synopsis = models.TextField(blank=True, null=True),
    slug = AutoSlugField(populate_from="title", always_update=True, unique_with=['title']),
    )


    actors = models.CharField(verbose_name=_("acteur"),max_length=200, blank=True, null=True)
    director = models.CharField(verbose_name=_("directeur"),max_length=25, blank=True, null=True)   
    length = models.TimeField(verbose_name=_("durée"),auto_now=False, auto_now_add=False,blank=True, null=True)
    picture = models.ImageField(verbose_name=_("image"),upload_to="Movie",blank=True, null=True)
    release_date = models.DateField(verbose_name=_("date de sortie"),auto_now=False, auto_now_add=False,blank=True, null=True)
    rented = models.BooleanField(verbose_name=_("loué"),)
    trailer_url = models.URLField(verbose_name=_("bande annonce"),max_length=200,blank=True, null=True)
    genre = models.ForeignKey('MovieGenre',blank=True, null=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('movie-detail', args=[self.slug])

    class Meta:
        """docstring for Meta."""
        verbose_name = "film"
            

class Customer(UserenaBaseProfile):
    """Model definition for Customer."""
    user = models.OneToOneField(User,verbose_name=_("utilisateur"), unique=True)

    def __unicode__(self):
        return self.user.username

    class Meta:
        """docstring for Meta."""
        verbose_name = "client"

class MovieRent(models.Model):
    # checkout_date = models.DateTimeField(verbose_name=_("date de location"),auto_now=False, auto_now_add=True)
    checkout_date = models.DateTimeField(verbose_name=_("date de location"),auto_now=False, auto_now_add=False)
    return_date = models.DateTimeField(verbose_name=_("date de retour"),auto_now=False, auto_now_add=False,blank=True, null=True)
    customer = models.ForeignKey('Customer',verbose_name=_("client"),blank=True, null=True, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie',verbose_name=_("film"),blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        """docstring for Meta."""
        verbose_name = "film loué"