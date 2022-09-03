from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Movies
from .models import Series
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    movies = Movies.objects.all()
    series = Series.objects.all()
    context = {
        'movies': movies,
        'series': series
    }
    return render(request, 'index.html', context)

def detailserie(request, id):
    obj = get_object_or_404(Series, pk=id)
    return render(request, 'detailserie.html', {'object': obj}) 

def detailmovie(request, id):
    obj = get_object_or_404(Movies, pk=id)
    return render(request, 'detailmovie.html', {'object': obj}) 