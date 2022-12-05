from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def detailmovie(request, id):
    obj = get_object_or_404(Movies, pk=id)
    return render(request, 'detailmovie.html', {'object': obj})

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
    obj.length_in_minutes = request.POST['duur']
    obj.country_of_origin = request.POST['country']
    obj.summary = request.POST['summary']
    obj.youtube_trailer_id = request.POST['trailerid']
    obj.save()
    return HttpResponseRedirect("/")

