from django.db import models

# Create your models here.


class Sueldo(models.Model):
    nombre = models.CharField(max_length=240)
    importe = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)
    resolucion = models.CharField(max_length=240)