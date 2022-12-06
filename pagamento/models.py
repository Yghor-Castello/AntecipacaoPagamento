from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


LISTA_STATUS = (
    ('PENDENTE', 'Pendente'),
    ('APROVADO', 'Aprovado'),
    ('NEGADO', 'Negado')
)

class Fornecedor(models.Model):
    razao_social = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=13)

    def __str__(self):
        return self.razao_social


class Pagamento(models.Model):
    fornecedor = models.ForeignKey('Fornecedor', related_name='pagamento', on_delete=models.CASCADE)
    descricao = models.CharField(max_length=90)
    data_emissao = models.DateField()
    data_vencimento = models.DateField()
    valor_original = models.FloatField(default=0)


    def __str__(self):
        return self.descricao


class Operador(models.Model): pass


class SolicitacaoAntecipacao(models.Model):
    pagamento = models.ForeignKey('Pagamento', related_name='solicitacaoantecipacao', on_delete=models.PROTECT)
    status = models.CharField(max_length=10, choices=LISTA_STATUS, default='Pendente')
    data_pagamento = models.DateField(blank=True, default='')
    novo_valor = models.FloatField(blank=True, default=0)

    def __str__(self):
        return str(self.pagamento)

@receiver(pre_save, sender=SolicitacaoAntecipacao)
def save_solicitacao_antecipacao(sender, instance, *args, **kwargs):
    pagamento = Pagamento.objects.get(id=instance.pagamento.id)
    instance.novo_valor = float(pagamento.valor_original - (pagamento.valor_original * ((0.03 / 30) * abs(pagamento.data_vencimento - instance.data_pagamento).days)))














