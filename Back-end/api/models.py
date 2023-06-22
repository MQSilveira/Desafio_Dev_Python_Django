from django.db import models


class Proposta(models.Model):
    nomeCompleto = models.CharField(max_length=100, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    endereco = models.CharField(max_length=200)
    valorEmprestimoPretendido = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor do Emprestimo Pretendido")
    situacao = models.CharField(max_length=10, default='Em Analise', verbose_name="Situação")


    def __str__(self):
        return self.nomeCompleto.title()
    
    class Meta:
        db_table = 'tabela_proposta'
    

    def statusProposta(self):
        return f"Valor: {self.valor} | {self.situacao}"

    