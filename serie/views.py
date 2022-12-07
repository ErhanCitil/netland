from .models import *
from django.views import generic
from django.urls import reverse_lazy
from movie.models import *
from .forms import *

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

class DetailSerie(LoginRequiredMixin, generic.DetailView):
    model = Series
    template_name = 'detailserie.html'

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