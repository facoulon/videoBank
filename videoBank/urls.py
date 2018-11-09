"""videoBank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from userena import views as userena_views

from videoRental.views import MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView, MovieDeleteView, MovieRentListView, MovieRentView, MovieReturnView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('userena.urls')),
    
    url(r"^$", MovieListView.as_view(), name="movie-list"),
    url(r"^(?:/(?P<username>[-\w]+))/rent-log$", MovieRentListView.as_view(), name="movie-rent-customer-log"),
    url(r"^rent$", MovieRentListView.as_view(), name="movie-rent-list"),

    url(r"^(?P<slug>[-\w]+)/$", MovieDetailView.as_view(), name="movie-detail"),
    url(r"^movie/create$", MovieCreateView.as_view(), name="movie-create"),
    url(r"^movie/(?P<slug>[-\w]+)/update$", MovieUpdateView.as_view(), name="movie-update"),
    url(r"^movie/(?P<slug>[-\w]+)/delete$", MovieDeleteView.as_view(), name="movie-delete"),
    
    url(r"^movie/rent$", MovieRentView.as_view(), name="movieRentAdd"),
    url(r"^movie/return$", MovieReturnView.as_view(), name="movieReturn"),
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
