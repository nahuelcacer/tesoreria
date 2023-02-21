from django.db import models

# Create your models here.

class Banco(models.Model):
    nombre =  models.CharField(max_length=240)
    codigo = models.CharField(max_length=10)

