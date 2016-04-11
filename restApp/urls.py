# -*- coding: utf-8 -*-
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import patterns, url

from .views import grafico1, grafico2, grafico3, grafico4, grafico5, grafico6, grafico7, grafico8, grafico9
from .views import gauge1, gauge2
from .views import mapa


urlpatterns = patterns('',
    url(r'^diario/$',
        grafico1.as_view(),
        name="estatisticas-diario"
    ),
    url(r'^mensal/$',
        grafico2.as_view(),
        name="estatisticas-mensal"
    ),
    url(r'^indice/$',
        grafico3.as_view()
    ),
    url(r'^uf/$',
        grafico4.as_view()
    ),
    url(r'^acumulado/$',
        grafico5.as_view()
    ),
    url(r'^uf_comparativo/$',
        grafico6.as_view()
    ),
    url(r'^nuvens/$',
        grafico7.as_view()
    ),
    url(r'^uf_periodo/$',
        grafico8.as_view()
    ),
    url(r'^uf_mes_periodo/$',
        grafico9.as_view()
    ),
    url(r'^comparativo/$',
        gauge1.as_view()
    ),
    url(r'^comparativo_prodes/$',
        gauge2.as_view()
    ),
    url(r'^mapa/$',
        mapa.as_view(),
        name="mapa"
    ),
)

urlpatterns = format_suffix_patterns(urlpatterns)