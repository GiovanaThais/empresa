from django.contrib import admin
from .models import Empresa
from .models import Vaga
from .models import Requisito

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nome_fantasia','cnpj','email']

@admin.register(Requisito)
class VagaAdmin(admin.ModelAdmin):
    list_display = ['titulo','descricao','salario','status','tipo_contrato','empresa']

@admin.register(Vaga)
class RequisitoAdmin(admin.ModelAdmin):
    list_display = ['vaga','descricao']
# Register your models here.
