from django.urls import path, include
from . import views

from .api.viewset import PaisDataViewSet, CovidDataViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('paises', PaisDataViewSet)
router.register('covid', CovidDataViewSet)


urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('covid/', views.covid, name='covid'),
    path('registro/', views.registro, name='registro'),
    path('api/', include(router.urls)),
]

