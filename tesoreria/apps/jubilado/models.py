from django.db import models
from apps.sueldo.models import Sueldo
from apps.cuenta.models import Banco
from apps.periodo.models import Periodo
# Create your models here.
class Jubilado(models.Model):
    SEXO_CHOICE =[ ('FEMENINO', 'FEMENINO'), ('MASCULINO', 'MASCULINO')]
    TIPO_CUENTA =[ ('01', 'CC'), ('02', 'CA')]

    nombre = models.CharField(max_length=240)
    numero = models.CharField(max_length=240)
    sexo = models.CharField(choices=SEXO_CHOICE, max_length=20)
    sueldo = models.ForeignKey(Sueldo, on_delete=models.CASCADE)
    cuenta = models.CharField(max_length=240)
    tipo_cuenta = models.CharField(choices=TIPO_CUENTA, max_length=9, null=True)
    cbu =  models.CharField(max_length=240, null=True)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE, null=True)
    aplicacion_sueldo = models.IntegerField()
    tipo_jubilacion = models.CharField(max_length=240, null=True)



class Liquidacion(models.Model):
    jubilado = models.ForeignKey(Jubilado, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    descuento = models.CharField(max_length=240, null=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    total = models.CharField(max_length=240, null=True)

    