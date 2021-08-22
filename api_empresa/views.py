from django.shortcuts import render
from rest_framework import generics, viewsets, SearchFilter
from core.models import Vaga,Empresa,Requisito
from serializers import VagaSerializer, EmpresaSerializer, RequisitoSerializer

class VagaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
class ListarVagasAPIView(generics.ListCreateAPIView):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo']
class EmpresaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
class ListarEmpresasAPIView(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome_fantasia']

class RequisitoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Requisito.objects.all()
    serializer_class = RequisitoSerializer
class ListarRequisitosAPIView(generics.ListCreateAPIView):
    queryset = Requisito.objects.all()
    serializer_class = RequisitoSerializer




