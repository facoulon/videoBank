# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie
# Create your views here.

class MovieListView(ListView):
    model = Movie

class MovieDetailView(DetailView):
    model = Movie


class MovieCreateView(CreateView):
    model = Movie
    template_name = "videoRental/movie_form.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse('movie-detail', args=[self.object.slug] )

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = "videoRental/movie_form.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse('movie-detail', args=[self.object.slug] )


class MovieDeleteView(DeleteView):
    model = Movie

    def get_success_url(self):
        return reverse('movie-list')

