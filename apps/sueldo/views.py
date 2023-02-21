from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SueldoSerializer
from .models import Sueldo
# Create your views here.

class SueldoView(viewsets.ModelViewSet):
    serializer_class = SueldoSerializer
    queryset = Sueldo.objects.all()