from rest_framework import serializers
from .models import *
from rest_framework.response import Response

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

    def create(self, validated_data):
        return Negocios.objects.create(**validated_data)

class AtividadesSerializer(serializers.Serializer):
    class Meta:
        model = Atividades
        fields = '__all__'

    def create(self, validated_data):
        return Atividades.objects.create(**validated_data)