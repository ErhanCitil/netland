from django.urls import path
from .models import *
from .views import *

urlpatterns = [
        path('', Index.as_view(), name='index'),
        path('serie/<int:pk>', DetailSerie.as_view(), name='detailserie'),
        path('updateserie/<int:pk>', UpdateSerie.as_view(), name='updateserie'),
        path('deleteserie/<int:id>', DeleteSerie.as_view(), name='deleteserie'),
]