from .models import *
from django.views import generic
from django.urls import reverse_lazy
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class DetailMovie(LoginRequiredMixin, generic.DetailView):
    model = Movies
    template_name = 'detailmovie.html'

class UpdateMovie(LoginRequiredMixin, generic.UpdateView):
    model = Movies
    template_name = 'updatemovie.html'
    form_class = MovieForm
    success_url = reverse_lazy('index')

class DeleteMovie(LoginRequiredMixin, generic.DeleteView):
    model = Movies
    template_name = 'deletemovie.html'
    success_url = reverse_lazy('index')

class CreateMovie(LoginRequiredMixin, generic.CreateView):
    model = Movies
    template_name = 'createmovie.html'
    form_class = MovieForm()
    success_url = reverse_lazy('index')
    