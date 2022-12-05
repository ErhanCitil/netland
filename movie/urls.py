from django.urls import path
from .models import *
from . import views

urlpatterns = [
        path('deletemovie/<int:id>', views.deletemovie, name='deletemovie'),
        path('updatemovie/<int:id>', views.updatemovie, name='updatemovie'),
        path('updatemovie/updatemoviedetails/<int:id>', views.updatemoviedetails, name='updatemoviedetails'),
        path('movie/<int:id>', views.detailmovie, name='detailmovie'),
]