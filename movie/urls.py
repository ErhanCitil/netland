from django.urls import path
from .models import *
from . import views
from .views import *
urlpatterns = [
        path('deletemovie/<int:id>', DeleteMovie.as_view(), name='deletemovie'),
        path('updatemovie/<int:id>', UpdateMovie.as_view(), name='updatemovie'),
        path('updatemovie/updatemoviedetails/<int:id>', views.updatemoviedetails, name='updatemoviedetails'),
        path('movie/<int:id>', DetailMovie.as_view(), name='detailmovie'),
]