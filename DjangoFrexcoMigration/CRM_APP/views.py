from .serializers import *
from rest_framework import viewsets


class OrganizacoesViewSet(viewsets.ModelViewSet):
    queryset = Organizacoes.objects.all()
    serializer_class = OrganizacoesSerializer

class NegociosViewSet(viewsets.ModelViewSet):
    queryset = Negocios.objects.all()
    serializer_class = NegociosSerializer

class AtividadesViewSet(viewsets.ModelViewSet):
    queryset = Negocios.objects.all()
    serializer_class = AtividadesSerializer