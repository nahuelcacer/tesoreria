from rest_framework import serializers
from apps.jubilado.models import Jubilado, Liquidacion
from apps.sueldo.serializers import SueldoSerializer
from apps.cuenta.serializers import BancoSerializer
from apps.periodo.serializers import PeriodoSerializer
from apps.sueldo.models import Sueldo
from apps.periodo.models import Periodo
from apps.cuenta.models import Banco 
class JubiladoSerializer(serializers.ModelSerializer):
    sueldo = SueldoSerializer()
    banco = BancoSerializer()
    class Meta:
        model = Jubilado
        fields = '__all__'


    def create(self, validated_data):
        sueldo_data = validated_data.pop('sueldo')
        banco_data = validated_data.pop('banco')
        print('s')
        sueldo = Sueldo.objects.get(**sueldo_data)
        banco = Banco.objects.get(**banco_data)
        jubilado = Jubilado.objects.create(sueldo=sueldo,banco=banco,**validated_data)
        print(jubilado)
        jubilado.save()
        return jubilado


class LiquidacionSerializer(serializers.ModelSerializer):
    jubilado = JubiladoSerializer()
    periodo = PeriodoSerializer()
    class Meta:
        model = Liquidacion
        fields = '__all__'

    def create(self,validated_data):
        jubilado_data = validated_data.pop('jubilado')
        periodo_data = validated_data.pop('periodo')
    
        sueldo_data = jubilado_data.pop('sueldo')    
        sueldo = Sueldo.objects.get(**sueldo_data)
        banco_data = jubilado_data.pop('banco')    
        banco = Banco.objects.get(**banco_data)
        jubilado = Jubilado.objects.get(**jubilado_data)

        periodo = Periodo.objects.get(**periodo_data)

   
        liquidacion = Liquidacion.objects.create(
            jubilado=jubilado, 
            # jubilado__banco=banco,
            # jubilado__sueldo=sueldo, 
            periodo=periodo, 
            **validated_data)
        
        liquidacion.save()
        return liquidacion
        