from rest_framework import viewsets
from dashboard.models import PaisData, CovidData
from .serializer import PaisDataSerializer, CovidDataSerializer


class PaisDataViewSet(viewsets.ModelViewSet):
    queryset = PaisData.objects.all()
    serializer_class = PaisDataSerializer
    
    
class CovidDataViewSet(viewsets.ModelViewSet):
    queryset = CovidData.objects.all()
    serializer_class = CovidDataSerializer