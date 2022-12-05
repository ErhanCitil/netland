from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def detailserie(request, id):
    obj = get_object_or_404(Series, pk=id)
    return render(request, 'detailserie.html', {'object': obj})

def index(request):
    movies = Movies.objects.all()
    series = Series.objects.all()
    context = {
        'movies': movies,
        'series': series
    }
    return render(request, 'index.html', context)

def updateserie(request, id):
    obj = get_object_or_404(Series, pk=id)
    return render(request, 'updateserie.html', {'object': obj})

def updateseriedetails(request, id):
    obj = get_object_or_404(Series, pk=id)
    obj.title = request.POST['title']
    obj.rating = request.POST['rating']
    obj.summary = request.POST['summary']
    obj.has_won_awards = request.POST['has_won_awards']
    obj.seasons = request.POST['seasons']
    obj.country = request.POST['country']
    obj.spoken_in_language = request.POST['spoken_in_language']
    obj.save()
    return HttpResponseRedirect("/")

def deleteserie(request, id):
    seriedelete = Series.objects.get(id=id)
    seriedelete.delete()
    return HttpResponseRedirect("/")