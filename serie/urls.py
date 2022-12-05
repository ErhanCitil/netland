from django.urls import path
from .models import *
from .views import *
from . import views

urlpatterns = [
        path('', Index.as_view(), name='index'),
        path('serie/<int:id>', DetailSeries.as_view(), name='detailserie'),
        path('updateserie/<int:id>', UpdateSerie.as_view(), name='updateserie'),
        path('updateserie/updateseriedetails/<int:id>', views.updateseriedetails, name='updateseriedetails'),
        path('deleteserie/<int:id>', DeleteSerie.as_view(), name='deleteserie'),
]
