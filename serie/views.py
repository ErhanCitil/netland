from django.shortcuts import render, get_object_or_404
from .models import *
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic.list import ListView
# Create your views here.
def detailserie(request, id):
    obj = get_object_or_404(Series, pk=id)
    return render(request, 'detailserie.html', {'object': obj})

class Index(ListView):
    model = Series
    template_name = 'index.html'
    context_object_name = 'series'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movies.objects.all()
        return context

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