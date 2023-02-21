from django.db import models

# Create your models here.


class Periodo(models.Model):
    mes = models.CharField(max_length=240)
    año = models.CharField(max_length=240)
    inicio = models.DateField()
    fin = models.DateField()


    def __str__(self):
        return self.mes + " " + self.año