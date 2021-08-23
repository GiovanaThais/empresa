from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView, DeleteView 
from .models import Empresa
from .models import Vaga, Requisito
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
class EmpresaList(ListView):
    model = Empresa
    queryset = Empresa.objects.all()

class EmpresaCreate(CreateView):
    model = Empresa
    queryset = Empresa.objects.all()
    fields = ['nome_fantasia','id','cnpj','email']
    success_url = reverse_lazy('empresa_list')

class EmpresaUpdate(UpdateView):
    model = Empresa
    queryset = Empresa.objects.all()
    fields = ['nome_fantasia','id','cnpj','email']
    success_url = reverse_lazy('empresa_list')

class EmpresaDelete(DeleteView):
    model = Empresa
    queryset = Empresa.objects.all()
    success_url = reverse_lazy('empresa_list')
# Create your views here.
class VagaList(ListView):
    model = Vaga
    queryset = Vaga.objects.all()

class VagaCreate(CreateView):
    model = Vaga
    queryset = Vaga.objects.all()
    fields = ['empresa','titulo','descricao','salario','tipo_contrato','status']
    success_url = reverse_lazy('vaga_list')

class VagaUpdate(UpdateView):
    model = Vaga
    queryset = Vaga.objects.all()
    fields = ['empresa','titulo','descricao','salario','tipo_contrato','status']
    success_url = reverse_lazy('vaga_list')

class VagaDelete(DeleteView):
    model = Vaga
    queryset = Vaga.objects.all()
    success_url = reverse_lazy('vaga_list')