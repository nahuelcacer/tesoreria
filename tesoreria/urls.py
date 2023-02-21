"""tesoreria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from apps.jubilado import views
from django.views.generic import TemplateView
from apps.sueldo.views import SueldoView
from apps.cuenta.views import BancoView
from apps.periodo.views import PeriodoViews
router = routers.DefaultRouter()

router.register(r'jubilado', views.JubiladoView , 'jubilado')
router.register(r'sueldo', SueldoView , 'sueldo')
router.register(r'banco', BancoView , 'banco')
router.register(r'liquidacion', views.LiquidacionView , 'liquidacion')
router.register(r'periodo', PeriodoViews , 'periodo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), 
    path('', TemplateView.as_view(template_name="index.html")),
        re_path(r'^jubilados/agregar$', TemplateView.as_view(template_name="index.html"))
]
