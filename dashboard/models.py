from django.db import models


class PaisData(models.Model):
    pais = models.CharField(max_length=100)
    poblacion = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Datos De Poblacion'

    def __str__(self):
        return f'{self.pais}-{self.poblacion}'
    
    
class CovidData(models.Model):
    pais = models.ForeignKey(PaisData, on_delete=models.CASCADE)
    contagios = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Contagios De Poblacion'

    def __str__(self):
        return f'{self.pais} M/habitantes - contagios: {self.contagios} M/'
