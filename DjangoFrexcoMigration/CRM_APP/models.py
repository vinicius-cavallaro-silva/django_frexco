from django.db import models
from datetime import datetime

# Create your models here.
class DateMixing:
    created = models.DateTimeField(default=datetime.utcnow)
    updated = models.DateTimeField(default=datetime.utcnow)

class Organizacoes(DateMixing, models.Model):
    __tablename__ = 'organizacoes'
    __table_args__ = {'schema': 'pipedrive'}

    id = models.IntegerField(primary_key=True, blank=False)
    nome = models.CharField(max_length=200, blank=True)
    etiqueta = models.CharField(max_length=200, blank = True)
    org_endereco = models.CharField(max_length=200, blank=True)
    org_pessoas = models.IntegerField(blank=True)
    negocios_fechados = models.IntegerField(blank=True)
    negocios_em_aberto = models.IntegerField(blank=True)
    proxima_atividade = models.CharField(max_length=200, blank=True)
    proprietario = models.CharField(max_length=200, blank=True)
    org_tempo_funcionando = models.CharField(max_length=200, blank=True)
    atividades_concluidas = models.CharField(max_length=200, blank=True)
    atividades_fazer = models.CharField(max_length=200, blank=True)
    cnpj = models.CharField(max_length=200, blank=True)
    data_atualizada = models.DateTimeField(blank=True)
    data_ultima_atividade = models.DateField(blank=True)
    org_comprava_de = models.CharField(max_length=200, blank=True)
    org_dias_pedido_semanais = models.CharField(max_length=200, blank=True)
    endereco_mesmo_da_loja = models.CharField(max_length=200 ,blank=True)
    org_horario_recebe_min = models.TimeField(blank=True)
    fuso_horario_min = models.CharField(max_length=200 ,blank=True)
    org_horario_recebe_max = models.TimeField(blank=True)
    fuso_horario_max = models.CharField(max_length=200, blank=True)
    inscricao_estadual = models.CharField(max_length=200, blank=True)
    negocios_ganhos = models.IntegerField(blank=True)
    negocios_perdidos = models.IntegerField(blank=True)
    numero_mensagens_email = models.IntegerField(blank=True)
    organizacao_criada = models.CharField(max_length=200, blank=True)
    prazo_pagamento = models.CharField(max_length=200, blank = True)
    org_item_mais_pedido1 = models.CharField(max_length=200, blank = True)
    org_item_mais_pedido2 = models.CharField(max_length=200, blank = True)
    org_item_mais_pedido3 = models.CharField(max_length=200, blank = True)
    org_atendimento_tipo = models.CharField(max_length=200, blank = True)
    ticket_medio_pessoa = models.CharField(max_length=200, blank = True)
    org_tipo_cozinha = models.CharField(max_length=200, blank = True)
    pratos_servidos_diariamente = models.CharField(max_length=200, blank = True)
    razao_social = models.CharField(max_length=200, blank = True)
    caso_contrario_completar = models.CharField(max_length=200, blank = True)
    org_tem_delivery = models.CharField(max_length=200, blank = True)
    total_atividades = models.IntegerField(blank=True)
    valor_gasto_mensal = models.FloatField(max_length=200, blank=True)
    moeda = models.CharField(max_length=200, blank = True)
    visivel_para = models.CharField(max_length=200, blank = True)
    org_area = models.CharField(max_length=200, blank = True)
    cidade = models.CharField(max_length=200, blank = True)
    estado_municipio = models.CharField(max_length=200, blank = True)
    regiao = models.CharField(max_length=200, blank = True)
    pais = models.CharField(max_length=200, blank = True)
    cep = models.CharField(max_length=200, blank = True)
    endereco_completo = models.CharField(max_length=200, blank = True)
    apartamento_suite = models.CharField(max_length=200, blank = True)
    numero_casa = models.CharField(max_length=200, blank = True)
    logradouro = models.CharField(max_length=200, blank = True)
    distrito_sublocalidade = models.CharField(max_length=200, blank = True)



class Negocios(DateMixing, models.Model):
    __tablename__ = 'negocios'
    __table_args__ = {'schema': 'pipedrive'}

    id = models.IntegerField(primary_key=True, blank=False)
    id_organizacao = models.ForeignKey("Organizacoes", on_delete=models.SET_NULL, null=True)
    funil = models.CharField(max_length=200, blank=True)
    titulo = models.CharField(max_length=200, blank=False)
    horario_recebe_min = models.TimeField(blank = True)
    horario_recebe_max = models.TimeField(blank = True)
    area = models.CharField(max_length=200, blank=True)
    pessoa_contato = models.CharField(max_length=200, blank=True)
    proprietario = models.CharField(max_length=200, blank=True)
    valor = models.FloatField(blank=True)
    tempo_funcionando = models.CharField(max_length=200, blank=True)
    comprava_de = models.CharField(max_length=200, blank=True)
    dias_pedido_semanais = models.CharField(max_length=200, blank=True)
    pessoas = models.CharField(max_length=200, blank=True)
    item_mais_pedido1 = models.CharField(max_length=200, blank=True)
    item_mais_pedido2 = models.CharField(max_length=200, blank=True)
    item_mais_pedido3 = models.CharField(max_length=200, blank=True)
    atendimento_tipo = models.CharField(max_length=200, blank=True)
    tipo_cozinha = models.CharField(max_length=200, blank=True)
    tem_delivery = models.CharField(max_length=200, blank=True)
    valor_produtos = models.CharField(max_length=200, blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    ganho_em = models.DateTimeField(blank=True)
    atividades_concluidas = models.CharField(max_length=200, blank=True)
    atividades_a_fazer = models.CharField(max_length=200, blank=True)
    como_conheceu = models.CharField(max_length=200, blank=True)
    criador = models.CharField(max_length=200, blank=True)
    data_atualizada = models.DateTimeField(blank=True)
    data_proxima_atividade = models.DateTimeField(blank = True)
    data_ultima_atividade = models.DateField(blank = True)
    data_fechamento_esperada = models.DateField(blank = True)
    etapa = models.CharField(max_length=200, blank=True)
    data_perda = models.DateTimeField(blank=True)
    etiqueta = models.CharField(max_length=200, blank=True)
    motivo_perda = models.CharField(max_length=200, blank=True)
    negocio_criado_em = models.DateTimeField(blank=True)
    negocio_fechado_em = models.DateTimeField(blank=True)
    num_mensagens_email = models.CharField(max_length=200, blank=True)
    organizacao = models.CharField(max_length=200, blank=True)
    pq_parou = models.CharField(max_length=200, blank=True)
    probabilidade = models.CharField(max_length=200, blank=True)
    qtd_produtos = models.IntegerField(blank = True)
    status = models.CharField(max_length=200, blank=True)
    total_atividades = models.IntegerField(blank = True)
    valor_ponderado = models.FloatField(blank = True)
    visivel_para = models.CharField(max_length=200, blank=True)
    moeda = models.CharField(max_length=200, blank=True)
    ultima_alteracao_etapa = models.DateTimeField(blank=True)
    ultimo_email_enviado = models.DateTimeField(blank=True)
    ultimo_email_recebido = models.DateTimeField(blank=True)


class Atividades(DateMixing, models.Model):
    __tablename__ = 'atividades'
    __table_args__ = {'schema': 'pipedrive'}

    id = models.IntegerField(primary_key=True, blank=False)
    id_negocios = models.ForeignKey("Negocios", on_delete=models.SET_NULL, null=True)
    concluido = models.CharField(max_length=200, blank=True)
    assunto = models.CharField(max_length=200, blank=True)
    negocio_nome = models.CharField(max_length=200, blank=True)
    pessoa_contato = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    telefone = models.CharField(max_length=200, blank=True)
    organizacao = models.CharField(max_length=200, blank=True)
    data_vencimento = models.DateTimeField(blank=True)
    duracao = models.CharField(max_length=200, blank=True)
    atribuido_a_usuario = models.CharField(max_length=200, blank=True)
    criador = models.CharField(max_length=200, blank=True)
    data_adicionada = models.DateTimeField(blank=True)
    data_atualizada = models.DateTimeField(blank=True)
    descricao_publica = models.CharField(max_length=200, blank=True)
    hora_ultima_notificacao = models.CharField(max_length=200, blank=True)
    lead = models.CharField(max_length=200, blank=True)
    livre_ocupado = models.CharField(max_length=200, blank=True)
    localizacao = models.CharField(max_length=200, blank=True)
    marcado_como_feito = models.CharField(max_length=200, blank=True)
    nota = models.CharField(max_length=200, blank=True)
    tipo = models.CharField(max_length=200, blank=True)

























