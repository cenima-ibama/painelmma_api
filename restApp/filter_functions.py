# -*- coding: utf-8 -*-

from django.db.models import Sum
from django.db.models.expressions import RawSQL

from .utils import get_month
from datetime import *


def filter_daily_total(queryset, context, qualif=False):
    if 'ano' in context and context['ano']:
        queryset = queryset.filter(
            ano=int(context['ano'])
        )

    if 'mes' in context and context['mes'] and not qualif:
        queryset = queryset.filter(
            mes=get_month(int(context['mes']))
        )
    elif 'mes' in context and context['mes'] and qualif:
        queryset = queryset.filter(
            mes=int(context['mes'])
        )

    if 'estagio' in context and context['estagio'] and context['tipo'] == 'AWIFS':
        queryset = queryset.filter(
            estagio=context['estagio']
        )

    if 'uf' in context and context['uf'] and not qualif:
        queryset = queryset.filter(
            estado=context['uf']
        )

    if not qualif:
        return queryset.values('data_imagem')\
            .annotate(
                total=Sum('area_km2'),
            ).annotate(
                dia=RawSQL("EXTRACT(day FROM data_imagem)", ())
            ).order_by('dia')
    # else:
    #     if context['estagio'] == 'degradacao':
    #         return queryset.values('mes_ano')\
    #             .annotate(
    #                 total=Sum('degradacao_deter'),
    #             )
    #     elif context['estagio'] == 'corte':
    #         return queryset.values('mes_ano')\
    #             .annotate(
    #                 total=Sum('corte_raso_deter'),
    #             )
    #     elif context['estagio'] == 'cicatriz':
    #         return queryset.values('mes_ano')\
    #             .annotate(
    #                 total=Sum('cicatriz_fogo'),
    #             )


def filter_montly_total(queryset, context, qualif=False):
    if 'estagio' in context and context['estagio'] and not qualif:
        queryset = queryset.filter(
            estagio=context['estagio']
        )

    if 'uf' in context and context['uf'] and not qualif:
        queryset = queryset.filter(
            estado=context['uf']
        )

    if not qualif:
        return queryset.extra(select={'mes_id': 'select EXTRACT(month from data_imagem)'}).values('mes_id')\
            .annotate(
                total=Sum('area_km2'),
            )\
            .order_by('mes_id')
    elif 'estagio' in context and context['estagio']:
        if context['estagio'] == 'Degradação':
            return queryset.extra(select={'mes_id': 'mes'}).values('mes_id')\
                .annotate(
                    total=Sum('degradacao_deter'),
                )
        elif context['estagio'] == 'Corte Raso':
            return queryset.extra(select={'mes_id': 'mes'}).values('mes_id')\
                .annotate(
                    total=Sum('corte_raso_deter'),
                )
        elif context['estagio'] == 'Cicatriz de Queimada':
            return queryset.extra(select={'mes_id': 'mes'}).values('mes_id')\
                .annotate(
                    total=Sum('cicatriz_fogo'),
                )


def filter_indice_total(queryset, context, hasStage=True):
    if 'uf' in context and context['uf']:
        queryset = queryset.filter(
            estado=context['uf']
        )
    if 'estagio' in context and context['estagio'] and hasStage:
        queryset = queryset.filter(
            estagio=context['estagio']
        )


    mes_parc = (int(context['mes']) - 7) if (int(context['mes']) > 7) else (int(context['mes']) + 5)

    return queryset.values('periodo_prodes').filter(mesid__in=['{:02d}'.format(i) for i in range(int(mes_parc) + 1,13)])



def filter_indice_parcial(queryset, context, hasStage=True):
    if 'uf' in context and context['uf']:
        queryset = queryset.filter(
            estado=context['uf']
        )
    if 'estagio' in context and context['estagio'] and hasStage:
        queryset = queryset.filter(
            estagio=context['estagio']
        )

    mes_parc = (int(context['mes']) - 7) if (int(context['mes']) > 7) else (int(context['mes']) + 5)

    return queryset.values('periodo_prodes').filter(mesid__in=['{:02d}'.format(i) for i in range(1, int(mes_parc) + 1)])




def filter_uf_total(queryset, context, qualif=False):
    if 'estagio' in context and context['estagio'] and context['tipo'] == 'AWIFS':
        queryset = queryset.filter(
            estagio=context['estagio']
        )

    if 'uf' in context and context['uf'] and not qualif:
        queryset = queryset.filter(
            estado=context['uf']
        )


    if not qualif:
        return queryset.values('estado','estagio')\
            .annotate(
                total=Sum('area_km2'),
            ).order_by('estado')
    # elif 'estagio' in context and context['estagio']:
    #     if context['estagio'] == 'Degradação':
    #         return queryset.extra(select={'mes_id': 'mes'}).values('periodo_prodes','mes_id')\
    #             .annotate(
    #                 total=Sum('degradacao_deter'),
    #             )
    #     elif context['estagio'] == 'Corte Raso':
    #         return queryset.extra(select={'mes_id': 'mes'}).values('periodo_prodes','mes_id')\
    #             .annotate(
    #                 total=Sum('corte_raso_deter'),
    #             )
    #     elif context['estagio'] == 'Cicatriz de Queimada':
    #         return queryset.extra(select={'mes_id': 'mes'}).values('periodo_prodes','mes_id')\
    #             .annotate(
    #                 total=Sum('cicatriz_fogo'),
    #             )


def filter_acumulado_uf(queryset, context, hasStage=False):
    if 'uf' in context and context['uf']:
        queryset = queryset.filter(
            estado=context['uf']
        )

    return queryset


def filter_uf_comparativo(queryset, context):
    if 'uf' in context and context['uf']:
        queryset = queryset.filter(
            estado=context['uf']
        )

    return queryset


def filter_uf_nuvem(queryset, context):
    if 'uf' in context and context['uf']:
        queryset = queryset.filter(
            uf=context['uf']
        )

    return queryset


def filter_uf_periodo_mensal(queryset, context, periodo):


    if 'tipo' in context and context['tipo']:

        tipo = context['tipo']

        # if 'uf' in context and context['uf']:
        #     queryset = queryset.filter(
        #         estado=context['uf']
        # )

        # if tipo == 'DETER_QUALIF' or  tipo == 'AWIFS' or tipo == 'DETER':
        # queryset = queryset.filter(
        #     periodo_prodes=periodo
        # )

        if 'ano' in context and context['ano']:
            queryset = queryset.filter(
                ano=context['ano']
            )

        if 'mes' in context and context['mes']:
            # if tipo == 'DETER' or tipo == 'AWIFS':
            queryset = queryset.filter(
                mes=get_month(int(context['mes']))
            )
            # elif tipo == 'DETER_QUALIF':
            #     queryset = queryset.filter(
            #         mes=int(context['mes'])
            #     )

        # if 'estagio' in context and context['estagio'] and tipo=='AWIFS':
        #     queryset = queryset.filter(
        #         estagio=context['estagio']
        #     )

    return queryset

def filter_comparativo(queryset, context, ano, qualif=False):
    # queryset = DailyAlertaAwifs.objects.all().filter(ano=obj, mes=get_month(int(mes)), estado=uf, estagio=estagio)
    if 'ano':
        queryset = queryset.filter(
            ano=ano
        )
    if 'mes' in context and context['mes'] and not qualif:
        queryset = queryset.filter(
            mes=get_month(int(context['mes']))
        )
    if 'mes' in context and context['mes'] and qualif:
        queryset = queryset.filter(
            mes=int(context['mes'])
        )
    if 'uf' in context and context['uf'] and not qualif:
        queryset = queryset.filter(
            estado=context['uf']
        )

    return queryset

def filter_comparativo_prodes(queryset, context, ano, qualif=False):
    # queryset = DailyAlertaAwifs.objects.all().filter(ano=obj, mes=get_month(int(mes)), estado=uf, estagio=estagio)

    #mes = int(context['mes'])
    #prodes = ""

    mes = int(context['mes']) + 5 if int(context['mes']) < 8 else int(context['mes']) - 7
    prodes = (str(ano - 1) + "-" + str(ano)) if int(context['mes']) < 8 else (str(ano) + "-" + str(ano + 1))

    if 'ano':
        queryset = queryset.filter(
            periodo_prodes=prodes
        )
    if 'mes' in context and context['mes']:
        queryset = queryset.filter(
            mesid__in=['{:02d}'.format(i) for i in range(1, int(mes) + 1)]
        )
    if 'uf' in context and context['uf'] and not qualif:
        queryset = queryset.filter(
            estado=context['uf']
        )

    return queryset

def filter_mapa(queryset, context, qualif=False):
    # queryset = DailyAlertaAwifs.objects.all().filter(ano=obj, mes=get_month(int(mes)), estado=uf, estagio=estagio)
    ano = context['ano']
    mes = context['mes']
    uf = context['uf']

    # queryset = queryset.all()

    if ano:
        queryset = queryset.filter(
            ano=str(ano)
        )
    if mes and not qualif:
        queryset = queryset.filter(
            mes=get_month(int(mes))
        )
    if mes and qualif:
        queryset = queryset.filter(
            mes=int(mes)
        )
    if uf:
        queryset = queryset.filter(
            estado=uf
        )

    # if ano:
    #     queryset = queryset.filter(
    #         ano='2015'
    #     )
    # if mes and not qualif:
    #     queryset = queryset.filter(
    #         mes='10'
    #     )
    # if mes and qualif:
    #     queryset = queryset.filter(
    #         mes='OUTUBRO'
    #     )
    # if uf and not qualif:
    #     queryset = queryset.filter(
    #         estado=''
    #     )

    # return {'ano': ano}
    return queryset

def filter_cruzamento_alerta(queryset, context):

    delta = None

    if 'ano_inicio' in context and 'ano_fim' in context and context['ano_inicio'] and context['ano_fim']:
        fim = context['ano_fim'].split('-')
        inicio = context['ano_inicio'].split('-')

        delta = date(int(fim[0]), int(fim[1]), int(fim[2])) - date(int(inicio[0]), int(inicio[1]), int(inicio[2]))
    
        if delta.days < 60:
            queryset = queryset.extra(select={'label':"to_char(data_imagem,'DD/MM/YY')"}).values('label')
        elif delta.days < 240:
            queryset = queryset.extra(select={'label':"to_char(data_imagem, 'YYYY/MM')"}).values('label')
        else:
            queryset = queryset.extra(select={'label': 'ano'}).values('label')
    else:
        queryset = queryset.extra(select={'label': 'ano'}).values('label')



    if 'ano_inicio' in context and 'ano_fim' in context and context['ano_inicio'] and context['ano_fim']:
        queryset = queryset.filter(
            data_imagem__range=[context['ano_inicio'], context['ano_fim']]
        )

    if 'tipo' in context and context['tipo']:
        queryset = queryset.filter(
            tipo=context['tipo']
        )

    if 'estagio' in context and context['estagio']:
        queryset = queryset.filter(
            estagio=context['estagio']
        )

    if 'estado' in context and context['estado']:
        queryset = queryset.filter(
            estado=context['estado']
        )

    if 'dominio' in context and context['dominio']:
        queryset = queryset.filter(
            dominio=context['dominio']
        )

    if 'area' in context and context['area']:
        area = context['area']
        if area == 'dominio_us':
            queryset = queryset.filter(
                dominio_us__isnull=False
            )
        elif area == 'dominio_ti':
            queryset = queryset.filter(
                dominio_ti__isnull=False
            )
        elif area == 'dominio_pi':
            queryset = queryset.filter(
                dominio_pi__isnull=False
            )
        elif area == 'dominio_as':
            queryset = queryset.filter(
                dominio_as__isnull=False
            )
        elif area == 'areas_livres':
            queryset = queryset.filter(
                dominio_us__isnull=True, dominio_ti__isnull=True, dominio_pi__isnull=True, dominio_as__isnull=True
            )


    return queryset.annotate(total=Sum('area_km2')).order_by('label')

def filter_cruzamento_estadual_federal_padrao(queryset, context):

    if 'ano_inicio' in context and 'ano_fim' in context and context['ano_inicio'] and context['ano_fim']:
        queryset = queryset.filter(
            data_imagem__range=[context['ano_inicio'], context['ano_fim']]
        )

    if 'tipo' in context and context['tipo']:
        queryset = queryset.filter(
            tipo=context['tipo']
        )

    if 'estagio' in context and context['estagio']:
        queryset = queryset.filter(
            estagio=context['estagio']
        )

    if 'estado' in context and context['estado']:
        queryset = queryset.filter(
            estado=context['estado']
        )

    return queryset


def filter_cruzamento_estadual_federal_area(queryset, dominio, area):

    if dominio:
        queryset = queryset.filter(
            dominio=dominio
        )

    if area == 'dominio_us':
        queryset = queryset.filter(
            dominio_us__isnull=False
        )
    elif area == 'dominio_ti':
        queryset = queryset.filter(
            dominio_ti__isnull=False
        )
    elif area == 'dominio_pi':
        queryset = queryset.filter(
            dominio_pi__isnull=False
        )
    elif area == 'dominio_as':
        queryset = queryset.filter(
            dominio_as__isnull=False
        )
    elif area == 'areas_livres':
        queryset = queryset.filter(
            dominio_us__isnull=True, dominio_ti__isnull=True, dominio_pi__isnull=True, dominio_as__isnull=True
        )

    return queryset.aggregate(total=Sum('area_km2'))