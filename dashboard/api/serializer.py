from rest_framework import serializers
from dashboard.models import PaisData, CovidData


class PaisDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaisData
        fields = '__all__'
        
class CovidDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidData
        fields = '__all__'
    

