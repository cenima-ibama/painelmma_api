# -*- coding: utf-8 -*-

from django.db.models import Sum
from django.db.models.expressions import RawSQL

# from .utils import get_month
from datetime import *

def filter_total(queryset, context):
    if 'ano' in context and context['ano']:
        queryset = queryset.filter(
            img_data__year=int(context['ano'])
        )

    if 'mes' in context and context['mes']:
        queryset = queryset.filter(
            img_data__month=int(context['mes'])
        )

    if 'estagio' in context and context['estagio']:
        estagio = context['estagio']

        if estagio == 'Corte Raso':
            queryset = queryset.filter(
                estagio__in=['CR','CR+']
            )
        elif estagio == 'Degradação':
            queryset = queryset.filter(
                estagio__in=['DG','DG+']
            )
        elif estagio == 'Degradação + Corte Raso':
            queryset = queryset
        else:
            queryset = queryset.filter(
                estagio=estagio
            )

    return queryset

    # elif 'mes' in context and context['mes'] and qualif:
    #     queryset = queryset.filter(
    #         mes=int(context['mes'])
    #     )

    # if 'estagio' in context and context['estagio']:
    #     queryset = queryset.filter(
    #         estagio=context['estagio']
    #     )

    # if 'uf' in context and context['uf'] and not qualif:
    #     queryset = queryset.filter(
    #         estado=context['uf']
    #     )

    # if not qualif:
    #     return queryset.values('data_imagem')\
    #         .annotate(
    #             total=Sum('area_km2'),
    #         ).annotate(
    #             dia=RawSQL("EXTRACT(day FROM data_imagem)", ())
    #         ).order_by('dia')
