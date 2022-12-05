from django.urls import path, include
from .views import Homepage, HomePagamento


app_name = 'pagamento'


urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('pagamento/', HomePagamento.as_view(), name='homepagamento'),
]