from audioop import reverse
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


def deletemovie(request, id):
    moviedelete = Movies.objects.get(id=id)
    moviedelete.delete()
    return HttpResponseRedirect("/")

def updatemovie(request, id):
    obj = get_object_or_404(Movies, pk=id)
    return render(request, 'updatemovie.html', {'object': obj})


def updatemoviedetails(request, id):
    obj = get_object_or_404(Movies, pk=id)
    obj.title = request.POST['title']
    obj.length_in_minutes = request.POST['length_in_minutes']
    obj.released_at = request.POST['released_at']
    obj.country_of_origin = request.POST['country_of_origin']
    obj.summary = request.POST['summary']
    obj.youtube_trailer_id = request.POST['youtube_trailer_id']
    obj.save()
    return HttpResponseRedirect("/")
