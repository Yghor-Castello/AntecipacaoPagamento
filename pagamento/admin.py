from django.contrib import admin
from .models import Fornecedor, Pagamento, SolicitacaoAntecipacao, Operador

admin.site.register(Fornecedor)
admin.site.register(Pagamento)
admin.site.register(SolicitacaoAntecipacao)
admin.site.register(Operador)

