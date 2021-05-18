from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class OrganizacoesView(APIView):
    serializer_class = OrganizacoesSerializer
    def get(self, request):
        allOrganizations = Organizacoes.objects.all().values()
        return Response({
            "Message": "List of Organizations",
            "Organizations List": allOrganizations
        })

    def post(self, request):
        dados = Organizacoes()
        dados.id = request.data["id"]
        dados.nome = request.data["nome"]
        dados.etiqueta = request.data["etiqueta"]
        dados.org_endereco = request.data["org_endereco"]
        dados.org_pessoas = request.data["org_pessoas"]
        dados.negocios_fechados = request.data["negocios_fechados"]
        dados.negocios_em_aberto = request.data["negocios_em_aberto"]
        dados.proxima_atividade = request.data["proxima_atividade"]
        dados.proprietario = request.data["proprietario"]
        dados.org_tempo_funcionando = request.data["org_tempo_funcionando"]
        dados.atividades_concluidas = request.data["atividades_concluidas"]
        dados.atividades_fazer = request.data["atividades_fazer"]
        dados.cnpj = request.data["cnpj"]
        dados.data_atualizada = request.data["data_atualizada"]
        dados.data_ultima_atividade = request.data["data_ultima_atividade"]
        dados.org_comprava_de = request.data["org_comprava_de"]
        dados.org_dias_pedido_semanais = request.data["org_dias_pedido_semanais"]
        dados.endereco_mesmo_da_loja = request.data["endereco_mesmo_da_loja"]
        dados.org_horario_recebe_min = request.data["org_horario_recebe_min"]
        dados.fuso_horario_min = request.data["fuso_horario_min"]
        dados.org_horario_recebe_max = request.data["org_horario_recebe_max"]
        dados.fuso_horario_max = request.data["fuso_horario_max"]
        dados.inscricao_estadual = request.data["inscricao_estadual"]
        dados.negocios_ganhos = request.data["negocios_ganhos"]
        dados.negocios_perdidos = request.data["negocios_perdidos"]
        dados.numero_mensagens_email = request.data["numero_mensagens_email"]
        dados.organizacao_criada = request.data["organizacao_criada"]
        dados.prazo_pagamento = request.data["prazo_pagamento"]
        dados.org_item_mais_pedido1 = request.data["org_item_mais_pedido1"]
        dados.org_item_mais_pedido2 = request.data["org_item_mais_pedido2"]
        dados.org_item_mais_pedido3 = request.data["org_item_mais_pedido3"]
        dados.org_atendimento_tipo = request.data["org_atendimento_tipo"]
        dados.ticket_medio_pessoa = request.data["ticket_medio_pessoa"]
        dados.org_tipo_cozinha = request.data["org_tipo_cozinha"]
        dados.pratos_servidos_diariamente = request.data["pratos_servidos_diariamente"]
        dados.razao_social = request.data["razao_social"]
        dados.caso_contrario_completar = request.data["caso_contrario_completar"]
        dados.org_tem_delivery = request.data["org_tem_delivery"]
        dados.total_atividades = request.data["total_atividades"]
        dados.valor_gasto_mensal = request.data["valor_gasto_mensal"]
        dados.moeda = request.data["moeda"]
        dados.visivel_para = request.data["visivel_para"]
        dados.org_area = request.data["org_area"]
        dados.cidade = request.data["cidade"]
        dados.estado_municipio = request.data["estado_municipio"]
        dados.regiao = request.data["regiao"]
        dados.pais = request.data["pais"]
        dados.cep = request.data["cep"]
        dados.endereco_completo = request.data["endereco_completo"]
        dados.apartamento_suite = request.data["apartamento_suite"]
        dados.numero_casa = request.data["numero_casa"]
        dados.logradouro = request.data["logradouro"]
        dados.distrito_sublocalidade = request.data["distrito_sublocalidade"]
        dados.save()

        return Response(AtividadesSerializer(dados).data)
class NegociosView(APIView):
    serializer_class = NegociosSerializer

    def get(self, request):
        allNegocios = Negocios.objects.all().values()
        return Response({
            "Message": "List of Deals",
            "Deals List": allNegocios
        })

    def post(self, request):
        dados = Negocios()
        dados.id = request.data["id"]
        dados.id_organizacao_id = request.data["id_organizacao"]
        dados.funil = request.data["funil"]
        dados.titulo = request.data["titulo"]
        dados.horario_recebe_min = request.data["horario_recebe_min"]
        dados.horario_recebe_max = request.data["horario_recebe_max"]
        dados.area = request.data["area"]
        dados.pessoa_contato = request.data["pessoa_contato"]
        dados.proprietario = request.data["proprietario"]
        dados.valor = request.data["valor"]
        dados.tempo_funcionando = request.data["tempo_funcionando"]
        dados.comprava_de = request.data["comprava_de"]
        dados.dias_pedido_semanais = request.data["dias_pedido_semanais"]
        dados.pessoas = request.data["pessoas"]
        dados.item_mais_pedido1 = request.data["item_mais_pedido1"]
        dados.item_mais_pedido2 = request.data["item_mais_pedido2"]
        dados.item_mais_pedido3 = request.data["item_mais_pedido3"]
        dados.atendimento_tipo = request.data["atendimento_tipo"]
        dados.tipo_cozinha = request.data["tipo_cozinha"]
        dados.tem_delivery = request.data["tem_delivery"]
        dados.valor_produtos = request.data["valor_produtos"]
        dados.endereco = request.data["endereco"]
        dados.ganho_em = request.data["ganho_em"]
        dados.atividades_concluidas = request.data["atividades_concluidas"]
        dados.atividades_a_fazer = request.data["atividades_a_fazer"]
        dados.como_conheceu = request.data["como_conheceu"]
        dados.criador = request.data["criador"]
        dados.data_atualizada = request.data["data_atualizada"]
        dados.data_proxima_atividade = request.data["data_proxima_atividade"]
        dados.data_ultima_atividade = request.data["data_ultima_atividade"]
        dados.data_fechamento_esperada = request.data["data_fechamento_esperada"]
        dados.etapa = request.data["etapa"]
        dados.data_perda = request.data["data_perda"]
        dados.etiqueta = request.data["etiqueta"]
        dados.motivo_perda = request.data["motivo_perda"]
        dados.negocio_criado_em = request.data["negocio_criado_em"]
        dados.negocio_fechado_em = request.data["negocio_fechado_em"]
        dados.num_mensagens_email = request.data["num_mensagens_email"]
        dados.organizacao = request.data["organizacao"]
        dados.pq_parou = request.data["pq_parou"]
        dados.probabilidade = request.data["probabilidade"]
        dados.qtd_produtos = request.data["qtd_produtos"]
        dados.status = request.data["status"]
        dados.total_atividades = request.data["total_atividades"]
        dados.valor_ponderado = request.data["valor_ponderado"]
        dados.visivel_para = request.data["visivel_para"]
        dados.moeda = request.data["moeda"]
        dados.ultima_alteracao_etapa = request.data["ultima_alteracao_etapa"]
        dados.ultimo_email_enviado = request.data["ultimo_email_enviado"]
        dados.ultimo_email_recebido = request.data["ultimo_email_recebido"]
        dados.save()

        return Response(AtividadesSerializer(dados).data)

class AtividadesView(APIView):
    serializer_class = AtividadesSerializer
    def get(self, request):
        allActivities = Atividades.objects.all().values()
        return Response({
            "Message": "List of Activities",
            "Activities List": allActivities
        })

    def post(self, request):
        dados = Atividades()
        dados.id = request.data["id"]
        dados.id_negocios_id = request.data["id_negocios"]
        dados.concluido = request.data["concluido"]
        dados.assunto = request.data["assunto"]
        dados.negocio_nome = request.data["negocio_nome"]
        dados.pessoa_contato = request.data["pessoa_contato"]
        dados.email = request.data["email"]
        dados.telefone = request.data["telefone"]
        dados.organizacao = request.data["organizacao"]
        dados.data_vencimento = request.data["data_vencimento"]
        dados.duracao = request.data["duracao"]
        dados.atribuido_a_usuario = request.data["atribuido_a_usuario"]
        dados.criador = request.data["criador"]
        dados.data_adicionada = request.data["data_adicionada"]
        dados.data_atualizada = request.data["data_atualizada"]
        dados.descricao_publica = request.data["descricao_publica"]
        dados.hora_ultima_notificacao = request.data["hora_ultima_notificacao"]
        dados.lead = request.data["lead"]
        dados.livre_ocupado = request.data["livre_ocupado"]
        dados.localizacao = request.data["localizacao"]
        dados.marcado_como_feito = request.data["marcado_como_feito"]
        dados.nota = request.data["nota"]
        dados.tipo = request.data["tipo"]
        dados.save()

        return Response(AtividadesSerializer(dados).data)

        #
        # print('Request data is : ', request.data)
        # serializer_obj = AtividadesSerializer(data=request.data)
        # if (serializer_obj.is_valid()):
        #     Atividades.objects.create(id=serializer_obj.data.get("id"),
        #                                    concluido=serializer_obj.data.get("concluido")
        #                                    )
        # atividade = Atividades.objects.all().filter(id=request.data["id"]).values()
        # return Response({
        #     "Message": "New Activity Added!",
        #     "Atividade": atividade
        # })