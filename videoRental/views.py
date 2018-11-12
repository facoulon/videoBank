# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Movie, MovieRent, Customer
from django.contrib.auth.mixins import PermissionRequiredMixin
import datetime
from datetime import timedelta, datetime

class MovieListView(ListView):
    model = Movie
    
class MovieDetailView(DetailView):
    model = Movie

class MovieCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'videoRent.add_Movie'
    model = Movie
    template_name = "videoRental/movie_form.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse('movie-detail', args=[self.object.slug] )

class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'videoRent.change_Movie'
    model = Movie
    template_name = "videoRental/movie_form.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse('movie-detail', args=[self.object.slug])

class MovieDeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = 'videoRent.delete_Movie'
    model = Movie

    def get_success_url(self):
        return reverse('movie-list')

class MovieRentListView(ListView):
    model = MovieRent

    def get_queryset(self):

        if self.request.user == "admin":
            return MovieRent.objects.all().order_by('-checkout_date')
        else:
            query = self.request.user
            user = User.objects.get(username=query)
            customer = Customer.objects.get(user=user)
            return MovieRent.objects.filter(customer=customer).order_by('-checkout_date')


class MovieRentView(View):

    def post(self, request, *args, **kwargs):
        movie = Movie.objects.get(pk=request.POST["movie-pk"])
        user = User.objects.get(username=request.user.username)
        customer = Customer.objects.get(user=user.pk)
        # return_date = datetime.now() + timedelta(days=7)

        if movie.rented == True:
            return HttpResponse('Ce film est déja loué')
        else:
            setattr(movie, 'rented', "True")
            movie.save()
            b = MovieRent(  customer=customer, 
                            movie=movie,   
                            # return_date=return_date
                            )
            b.save()
            return HttpResponseRedirect(reverse('movie-list'))

class MovieReturnView(View):
    
    def post(self, request, *args, **kwargs):
        movie = Movie.objects.get(pk=request.POST["movie-pk"])
        movieRent = MovieRent.objects.get(movie=movie, return_date=None)
        date = datetime.now()

        setattr(movie, 'rented', "False")
        movie.save()
        setattr(movieRent, 'return_date', date)
        movieRent.save()
        return HttpResponseRedirect(reverse('movie-rent-list'))