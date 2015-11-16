# -*- coding: utf-8 -*-

from django.db.models import Sum
from django.db.models.expressions import RawSQL

from .utils import get_month


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
            )
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