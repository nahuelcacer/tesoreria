from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BancoSerializer
from .models import Banco
# Create your views here.

class BancoView(viewsets.ModelViewSet):
    serializer_class = BancoSerializer
    queryset = Banco.objects.all()





