from django.shortcuts import render
from .models import Pagamento
from django.views.generic import TemplateView, ListView, DetailView


class Homepage(TemplateView):
    template_name = 'homepage.html'


class HomePagamento(ListView):
    template_name = 'homepagamento.html'
    model = Pagamento


# class DescontoPagamento(DetailView):
#     template_name = 'descontopagamento.html'
#     model = Pagamento
#
#     def get(self, request, *args, **kwargs):
#         #descobrir qual pagamento ele ta acessando
#         pagamento = self.get_object()
#         #contabilizar o desconto
#         novo_valor = pagamento - (pagamento * ((0.03*100 / 30) * (data_vencimento - data_pagamento)))
#         novo_valor.save() #registrar no BD
#         return super().get(request, *args, **kwargs) #redireciona o usuario para a url final
#
#     def get_context_data(self, **kwargs):
#         context = super(Detalhesfilme, self).get_context_data(**kwargs)
#         #filtrar a minha tabela de filmes pegando os filmes cuja categoria é igual à categoriado filme da página (object)
#         #self.object()
#         filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:8]
#         context['filmes_relacionados'] = filmes_relacionados
#         return context
#
#
# class Pesquisafilme(ListView):
#     template_name = 'pesquisa.html'
#     model = Filme
#
#     def get_queryset(self):
#         termo_pesquisa = self.request.GET.get('query')
#         if termo_pesquisa:
#             object_list = Filme.objects.filter(titulo__icontains=termo_pesquisa)
#             return object_list
#         else:
#             return None


