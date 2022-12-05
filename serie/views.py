from django.shortcuts import get_object_or_404
from .models import *
from django.http import HttpResponseRedirect

from django.views.generic.list import ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from movie.models import Movies
# Create your views here.
class Index(ListView):
    model = Series
    template_name = 'index.html'
    context_object_name = 'series'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movies.objects.all()
        return context

class DetailSeries(ListView):
    model = Series
    template_name = 'detailserie.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Series.objects.get(id=self.kwargs['id'])
        return context

class UpdateSerie(ListView):
    model = Series
    template_name = 'updateserie.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Series.objects.get(id=self.kwargs['id'])
        return context

def updateseriedetails(request, id):
    obj = get_object_or_404(Series, pk=id)
    obj.title = request.POST['title']
    obj.rating = request.POST['rating']
    obj.summary = request.POST['summary']
    obj.has_won_awards = request.POST['has_won_awards']
    obj.seasons = request.POST['seasons']
    obj.country = request.POST['country']
    obj.save()
    return HttpResponseRedirect("/")

class DeleteSerie(DeleteView):
    model = Series
    template_name = 'deleteserie.html'
    success_url = reverse_lazy('index')
