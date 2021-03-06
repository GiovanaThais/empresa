"""recrutamento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from api_empresa.views import EmpresaAPIView, ListarEmpresasAPIView, ListarVagasAPIView, VagaAPIView
from django.contrib import admin
from core.views import EmpresaList, EmpresaCreate, EmpresaUpdate, EmpresaDelete
from core.views import VagaList, VagaCreate, VagaDelete, VagaUpdate
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from api_empresa import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('vagas', ListarVagasAPIView, VagaAPIView)
router.register('empresas', ListarEmpresasAPIView, EmpresaAPIView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),

    path('listEmpresa/',EmpresaList.as_view(), name= 'empresa_list'),
    path('createEmpresa/',EmpresaCreate.as_view(), name='empresa_create'),
    path('updateEmpresa/<int:pk>/',EmpresaUpdate.as_view(), name = 'empresa_update'),
    path('deleteEmpresa/<int:pk>/',EmpresaDelete.as_view(), name = 'empresa_delete'),
    path('listVaga/',VagaList.as_view(), name= 'vaga_list'),
    path('createVaga/',VagaCreate.as_view(), name='vaga_create'),
    path('updateVaga/<int:pk>/',VagaUpdate.as_view(), name = 'vaga_update'),
    path('deleteVaga/<int:pk>/',VagaDelete.as_view(), name = 'vaga_delete'),
    #API
    path('vagas/', ListarVagasAPIView.as_view(), name='listar_vagas'),
    path('vagas/<int:pk>/', VagaAPIView.as_view(), name='listar_vagas'),
    path('empresas/', ListarEmpresasAPIView.as_view(), name='listar_empresas'),
    path('empresas/<int:pk>/', EmpresaAPIView.as_view(), name='listar_empresas'),
]
