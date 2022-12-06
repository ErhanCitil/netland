from .models import *
from django.views import generic
from django.urls import reverse_lazy
from .forms import *
# Create your views here.

class DetailMovie(generic.DetailView):
    model = Movies
    template_name = 'detailmovie.html'

class UpdateMovie(generic.UpdateView):
    model = Movies
    template_name = 'updatemovie.html'
    form_class = MovieForm
    success_url = reverse_lazy('index')

class DeleteMovie(generic.DeleteView):
    model = Movies
    template_name = 'deletemovie.html'
    success_url = reverse_lazy('index')

class CreateMovie(generic.CreateView):
    model = Movies
    template_name = 'createmovie.html'
    form_class = MovieForm
    success_url = reverse_lazy('index')
    