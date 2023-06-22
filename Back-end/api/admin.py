from django import forms
from django.contrib import admin
from .models import Proposta


"""
Estrutura da Proposta
O administrador do sistema poderá cadastrar os campos que devem constar na proposta através do django-admin. 
Nome Completo | CPF |Endereço | Valor do Empréstimo Pretendido
"""

# Faz a validação dos dados inseridos pelo administrador
class PropostaForm(forms.ModelForm):
    class Meta:
        model = Proposta
        fields = '__all__'

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if len(cpf) != 11:
            raise forms.ValidationError("O CPF deve ter 11 caracteres.")
        return cpf


class PropostaAdmin(admin.ModelAdmin):
    form = PropostaForm
    list_display = ('nomeCompleto', 'valorEmprestimoPretendido', 'situacao')
    list_per_page = 20  # Define o número de itens por página

    # Define os campos exibidos na página de cadastro do django-admin.
    add_fieldsets = (
        (None, {
            'fields': ('nomeCompleto', 'cpf', 'endereco', 'valorEmprestimoPretendido'),
        }),
    )


    def has_delete_permission(self, request, obj=None):
        return False    # Remove excluir 
    
    def has_change_permission(self, request, obj=None):
        return False    # Remove salvar alterações 
    
    def get_exclude(self, request, obj=None):
        if obj:         # Remove "situacao" página de cadastro
            return []
        return ['situacao']

    
admin.site.register(Proposta, PropostaAdmin)
