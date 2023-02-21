from rest_framework import serializers
from apps.periodo.models import Periodo



class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'