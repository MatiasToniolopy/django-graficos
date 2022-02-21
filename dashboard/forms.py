from django import forms
from .models import PaisData, CovidData
from django.contrib.auth.forms import UserCreationForm


class PaisDataFrom(forms.ModelForm):
    class Meta:
        model = PaisData
        fields = '__all__'
        
class CovidDataFrom(forms.ModelForm):
    class Meta:
        model = CovidData
        fields = '__all__'
        
class CustomUserCreationForm(UserCreationForm):
    pass
