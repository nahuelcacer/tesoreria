from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JubiladoSerializer, LiquidacionSerializer
from .models import Jubilado, Liquidacion
from django_filters import rest_framework as filters
from django.db.models import Q
from django_filters import DateFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class JubiladoView(viewsets.ModelViewSet):
    serializer_class = JubiladoSerializer
    queryset = Jubilado.objects.all()

class LiquidacionFilter(filters.FilterSet):
    periodo = filters.CharFilter(method='filter_by_periodo')
    class Meta:
        model = Liquidacion
        fields = ['periodo']

    def filter_by_periodo(self, queryset, name, value):
        if value:
            return queryset.filter(Q(periodo__mes__icontains=value) | Q(periodo__año__icontains=value))
        return queryset


class LiquidacionView(viewsets.ModelViewSet):
    serializer_class = LiquidacionSerializer
    queryset = Liquidacion.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = LiquidacionFilter

