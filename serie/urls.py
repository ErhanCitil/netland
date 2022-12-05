from django.urls import path
from .models import *
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('serie/<int:id>', views.detailserie, name='detailserie'),
        path('updateserie/<int:id>', views.updateserie, name='updateserie'),
        path('updateserie/updateseriedetails/<int:id>', views.updateseriedetails, name='updateseriedetails'),
        path('deleteserie/<int:id>', views.deleteserie, name='deleteserie'),
]
