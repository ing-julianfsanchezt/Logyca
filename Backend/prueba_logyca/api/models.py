from django.db import models
from django.db import connection
from .utilidadesDB import getNumerosPrimos

class NumerosPrimos(models.Model):
    numero_n = models.IntegerField()
    resultado_n = models.CharField(max_length=5000)


class NumerosPrimosGemelos(models.Model):
    numero_n = models.IntegerField()
    resultado_n = models.CharField(max_length=5000)


class NumerosPrimosManager(models.Manager):
    
    def getNumerosPrimos(self, n):
        query = "SELECT resultado_n FROM public.api_numerosprimos where numero_n =%s;" %(n)
        return getNumerosPrimos(query)

