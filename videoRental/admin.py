# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from videoRental.models import Movie,MovieGenre,Customer,MovieRent
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title","director","release_date")
admin.site.register(Movie, MovieAdmin)

class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ('label',)
admin.site.register(MovieGenre, MovieGenreAdmin)

class MovieRentAdmin(admin.ModelAdmin):
    list_display = ('customer','movie','checkout_date','return_date')

admin.site.register(MovieRent, MovieRentAdmin)
