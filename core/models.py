from django.db import models
from django.contrib.auth.models import User

TIPO_CONTRATO_CHOICES = (
    ('PJ', 'Pessoa Jurídica'),
    ('CLT', 'Consolidação das Leis do Trabalho')
)

class Empresa(models.Model):
    nome_fantasia = models.CharField('nome_empresa', null=False, max_length=50)
    cnpj = models.CharField('cnpj', null=False, max_length=14)
    email = models.EmailField('email', null=False)
    
    def __str__(self):
        return str(self.nome_fantasia)

class Vaga(models.Model):
    titulo = models.CharField('titulo', max_length=30, null=False)
    descricao = models.TextField('descricao', null=False)
    salario = models.FloatField('salario', null=False)
    tipo_contrato = models.CharField('tipo_contrato', choices=TIPO_CONTRATO_CHOICES, null=False, max_length=50)
    status = models.BooleanField('status', null=False, default=1)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='empresa_vaga', verbose_name='Empresa')

    def __str__(self):
        return str(self.id)

class Requisito(models.Model):
    descricao = models.TextField('descricao', null=False)
    vaga = models.ForeignKey(Vaga,on_delete=models.CASCADE, related_name='requisitos_vaga', verbose_name='Vaga')
    
    def __str__(self):
        return str(self.descricao)

# Create your models here.
