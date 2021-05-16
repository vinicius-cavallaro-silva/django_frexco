from rest_framework import serializers
from .models import *

class OrganizacoesSerializer(serializers.Serializer):
    class Meta:
        model = Organizacoes
        fields = '__all__'

    def create(self, validated_data):
        return Organizacoes.objects.create(**validated_data)

class NegociosSerializer(serializers.Serializer):
    class Meta:
        model = Negocios
        fields = '__all__'

class AtividadesSerializer(serializers.Serializer):
    class Meta:
        model = Atividades
        fields = '__all__'
    def create(self, validated_data):
        return Atividades.objects.create(**validated_data)