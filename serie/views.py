from .models import *
from django.views import generic
from django.urls import reverse_lazy
from movie.models import *
from .forms import *

import csv
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class Index(LoginRequiredMixin, generic.ListView):
    model = Series
    template_name = 'index.html'
    context_object_name = 'series'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movies.objects.all()
        return context

def export_to_csv(request, queryset, fields):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'
    writer = csv.writer(response)
    writer.writerow(fields)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in fields])
    return response

class DetailSerie(LoginRequiredMixin, generic.DetailView):
    model = Series
    template_name = 'detailserie.html'
    queryset = Series.objects.all()
    
    export_to_csv(template_name, queryset, ['title', 'rating', 'summary', 'has_won_awards', 'seasons', 'country', 'spoken_in_language'])
class UpdateSerie(LoginRequiredMixin, generic.UpdateView):
    model = Series
    template_name = 'updateserie.html'
    form_class = SerieForm
    success_url = reverse_lazy('index')

class DeleteSerie(LoginRequiredMixin, generic.DeleteView):
    model = Series
    success_url = reverse_lazy('index')

class CreateSerie(LoginRequiredMixin, generic.CreateView):
    model = Movies
    template_name = 'createmovie.html'
    form_class = SerieForm
    success_url = reverse_lazy('index')