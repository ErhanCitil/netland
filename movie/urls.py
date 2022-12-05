from django.urls import path
from .models import *
from .views import *

urlpatterns = [
        path('deletemovie/<int:id>', DeleteMovie.as_view(), name='deletemovie'),
        path('updatemovie/<int:pk>/', UpdateMovie.as_view(), name='updatemovie'),
        path('movie/<int:pk>/', DetailMovie.as_view(), name='detailmovie'),
]