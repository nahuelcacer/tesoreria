from rest_framework import viewsets
from apps.periodo.serializers import PeriodoSerializer
from apps.periodo.models import Periodo


class PeriodoViews(viewsets.ModelViewSet):
    serializer_class = PeriodoSerializer
    queryset = Periodo.objects.all()


