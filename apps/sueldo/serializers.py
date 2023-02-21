from rest_framework import serializers
from apps.sueldo.models import Sueldo


class SueldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sueldo
        fields = ('resolucion', 'fecha', 'importe', 'nombre')