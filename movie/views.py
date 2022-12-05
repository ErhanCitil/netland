from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
class DetailMovie(ListView):
    model = Movies
    template_name = 'detailmovie.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Movies.objects.get(id=self.kwargs['id'])
        return context

def updatemoviedetails(request, id):
    obj = get_object_or_404(Movies, pk=id)
    obj.title = request.POST['title']
    obj.length_in_minutes = request.POST['duur']
    obj.released_at = request.POST['released_at']
    obj.country_of_origin = request.POST['country']
    obj.summary = request.POST['summary']
    obj.youtube_trailer_id = request.POST['youtube_trailer_id']
    obj.save()
    return HttpResponseRedirect("/")

class UpdateMovie(ListView):
    model = Movies
    template_name = 'updatemovie.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Movies.objects.get(id=self.kwargs['id'])
        return context

class DeleteMovie(DeleteView):
    model = Movies
    template_name = 'deletemovie.html'
    success_url = reverse_lazy('index')