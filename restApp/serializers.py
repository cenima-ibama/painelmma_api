# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer, SerializerMethodField, BaseSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from django.db.models import Sum, Count
from decimal import *

from .models import *
from loginApp.models import UserPermited

from .utils import get_reverse_month, belongs_prodes, get_prodes,get_month
from .filter_functions import *



class DailyAlertaAwifsSerializer(ModelSerializer):
    data = SerializerMethodField()

    class Meta:
        model = DailyAlertaAwifs
        fields = ['data']

    def get_data(self, obj):
        queryset = DailyAlertaAwifs.objects.values('data_imagem', 'area_km2')
        queryset = filter_daily_total(
            queryset, self.context['request'].GET
        )
        return queryset


class DailyAlertaDeterSerializer(ModelSerializer):
    data = SerializerMethodField()

    class Meta:
        model = DailyAlertaDeter
        fields = ['data']

    def get_data(self, obj):
        queryset = DailyAlertaDeter.objects.values('data_imagem', 'area_km2')
        queryset = filter_daily_total(
            queryset, self.context['request'].GET
        )
        return queryset


class PublicAlertaDeterSerializer(ModelSerializer):
    data = SerializerMethodField()

    class Meta:
        model = PublicAlertaDeter
        fields = ['data']

    def get_data(self, obj):
        queryset = PublicAlertaDeter.objects.values('data_imagem', 'area_km2')
        queryset = filter_daily_total(
            queryset, self.context['request'].GET
        )
        return queryset


class DailyAlertaDeterQualifSerializer(ModelSerializer):
    data = SerializerMethodField()

    class Meta:
        model = DailyAlertaDeterQualif
        fields = ['data']

    def get_data(self, obj):
        queryset = DailyAlertaDeterQualif.objects.values('mes_ano', 'cicatriz_fogo', 'corte_raso_deter', 'degradacao_deter')
        queryset = filter_daily_total(
            queryset, self.context['request'].GET, True
        )
        return queryset


class MontlySerializer(BaseSerializer):
    def to_representation(self, obj):
        tipo = self.context['request'].GET.get('tipo', None)
        permited = bool(UserPermited.objects.filter(username=self.context['request'].user.username))
        isQualif = False;

        if tipo == 'AWIFS' and self.context['request'].user.is_authenticated() and permited:
            queryset = DailyAlertaAwifs.objects.filter(periodo_prodes=obj)
        elif tipo == 'DETER' and self.context['request'].user.is_authenticated() and permited:
            queryset = DailyAlertaDeter.objects.filter(periodo_prodes=obj)
        elif tipo == 'DETER' and not permited:
            queryset = PublicAlertaDeter.objects.filter(periodo_prodes=obj)
        elif tipo == 'DETER_QUALIF' and self.context['request'].user.is_authenticated() and permited:
            queryset = DailyAlertaDeterQualif.objects.filter(periodo_prodes=obj)
            isQualif = True;
        elif tipo == 'DETER_QUALIF' and not permited:
            queryset = PublicAlertaDeterQualif.objects.filter(periodo_prodes=obj)
            isQualif = True;


        # queryset = DailyAlertaDeterQualif.objects.filter(periodo_prodes=obj)
        queryset = filter_montly_total(
            queryset, self.context['request'].GET, isQualif
        )
        return {
            'periodo': obj,
            'data': queryset,
        }


class IndiceSerializer(BaseSerializer):
    def to_representation(self, obj):
        tipo = self.context['request'].GET.get('tipo', None)
        estagio = self.context['request'].GET.get('estagio', None)
        mes = self.context['request'].GET.get('mes', None)
        ano = self.context['request'].GET.get('ano', None)
        series = 2 + int(self.context['request'].GET.get('frequencia',0)) if self.context['request'].GET.get('frequencia',0) else 2

        hasStage = False;

        seriesRange = list(range(-1 * series, 0))
        seriesRange.reverse()

        periodos = [get_prodes(mes, ano, i + 1) for i in seriesRange]
        permited = bool(UserPermited.objects.filter(username=self.context['request'].user.username))
        # periodos = [str(2015 - i) + '-' + str(2016-i) for i in range(0,series)]
        # periodos = ['2015-2016','2014-2015'];

        data = []

        for per in periodos:
            if tipo == 'AWIFS' and self.context['request'].user.is_authenticated() and permited:
                queryset = DailyAlertaAwifs.objects.filter(periodo_prodes=per)
                hasStage = True;
            elif tipo == 'DETER' and self.context['request'].user.is_authenticated() and permited:
                queryset = DailyAlertaDeter.objects.filter(periodo_prodes=per)
            elif tipo == 'DETER' and not permited:
                queryset = PublicAlertaDeter.objects.filter(periodo_prodes=per)
            elif tipo == 'DETER_QUALIF' and self.context['request'].user.is_authenticated() and permited:
                queryset = DailyAlertaDeterQualif.objects.filter(periodo_prodes=per)
            elif tipo == 'DETER_QUALIF' and not permited:
                queryset = PublicAlertaDeterQualif.objects.filter(periodo_prodes=per)

            if obj == 'Diferença':
                queryset = filter_indice_total(queryset, self.context['request'].GET, hasStage)
            else:
                queryset = filter_indice_parcial(queryset, self.context['request'].GET, hasStage)


            if tipo == 'AWIFS' or tipo == 'DETER':
                indice = queryset.aggregate(total=Sum('area_km2'))
            else:
                if estagio == 'Corte Raso':
                    indice = queryset.aggregate(total=Sum('corte_raso_deter'))
                elif estagio == 'Degradação':
                    indice = queryset.aggregate(total=Sum('degradacao_deter'))
                else:
                    indice = queryset.aggregate(total=Sum('cicatriz_fogo'))

            indice['periodo'] =  per
            data.append(indice)            


        return {
            'tipo': obj,
            'data': data,
        }


class UFSerializer(BaseSerializer):
    def to_representation(self, obj):
        tipo = self.context['request'].GET.get('tipo', None)
        logged = self.context['request'].GET.get('logged', False)
        isQualif = False;
        permited = bool(UserPermited.objects.filter(username=self.context['request'].user.username))

        if tipo == 'AWIFS' and self.context['request'].user.is_authenticated() and permited:
            queryset = DailyAlertaAwifs.objects.filter(periodo_prodes=obj)
        elif (tipo == 'DETER' or 'DETER_QUALIF') and self.context['request'].user.is_authenticated() and permited:
            queryset = DailyAlertaDeter.objects.filter(periodo_prodes=obj)
        elif (tipo == 'DETER' or 'DETER_QUALIF') and not permited:
            queryset = PublicAlertaDeter.objects.filter(periodo_prodes=obj)
        # elif tipo == 'DETER_QUALIF':
        #     queryset = DailyAlertaDeterQualif.objects.filter(periodo_prodes=obj)
        #     isQualif = True;


        # queryset = DailyAlertaDeterQualif.objects.filter(periodo_prodes=obj)
        queryset = filter_uf_total(
            queryset, self.context['request'].GET, isQualif
        )
        return {
            'periodo': obj,
            'data': queryset,
        }


class AcumuladoSerializer(BaseSerializer):
    def to_representation(self, obj):
        uf = self.context['request'].GET.get('uf', None)
        permited = bool(UserPermited.objects.filter(username=self.context['request'].user.username))

        if obj == 'PRODES':
            queryset = TaxaProdes.objects.all().order_by('-ano_prodes')

            if uf != '':
                queryset =  [{'periodo_prodes': i.ano_prodes.replace('/','-'), 'total': getattr(i,uf.lower())} for i in queryset]
            else:
                queryset = [{'periodo_prodes': i.ano_prodes.replace('/','-'), 'total': i.total()} for i in queryset]

            queryset = list(queryset[:13])
            # queryset.reverse()

        elif obj == 'DETER' and self.context['request'].user.is_authenticated() and permited:
            queryset = DailyAlertaDeter.objects
            queryset = filter_acumulado_uf(
                queryset, self.context['request'].GET
            )
            queryset = queryset.values('periodo_prodes').annotate(total=Sum('area_km2')).order_by('-periodo_prodes')

        elif obj == 'DETER' and not permited:
            queryset = PublicAlertaDeter.objects
            queryset = filter_acumulado_uf(
                queryset, self.context['request'].GET
            )
            queryset = queryset.values('periodo_prodes').annotate(total=Sum('area_km2')).order_by('-periodo_prodes')

        elif obj == 'AWIFS' and self.context['request'].user.is_authenticated() and permited:
            queryset = DailyAlertaAwifs.objects
            queryset = filter_acumulado_uf(
                queryset, self.context['request'].GET
            )
            queryset = queryset.filter(estagio='Corte Raso').values('periodo_prodes').annotate(total=Sum('area_km2')).order_by('-periodo_prodes')

        elif obj == 'AWIFS' and not permited:
            queryset = []


        return {
            'taxa': obj,
            'data': queryset,
        }


class UFComparativoSerializer(BaseSerializer):
    def to_representation(self, obj):
        uf = self.context['request'].GET.get('uf', None)
        indice = self.context['request'].GET.get('indice', 0)
        mes = self.context['request'].GET.get('mes', None)
        ano = self.context['request'].GET.get('ano', None)
        
        # if int(mes) > 7:
        #     prodes = str(ano) + '-' + str(int(ano) + 1)
        # else:
        #     prodes = str((int(ano) - 1)) + '-' + str(ano)

        # prodes = '2015-2016'
        # prodes = str(2015 + int(indice)) + '-' + str(2016 + int(indice))
        prodes = get_prodes(mes, ano, indice)
        permited = bool(UserPermited.objects.filter(username=self.context['request'].user.username))


        if obj == 'AWIFS' and self.context['request'].user.is_authenticated() and permited:
            queryset = DailyAlertaAwifs.objects.all().filter(periodo_prodes=prodes,estagio='Corte Raso')
            queryset = filter_uf_comparativo(
                queryset, self.context['request'].GET
            )
            queryset = queryset.values('estado').annotate(total=Sum('area_km2'))

        if obj == 'AWIFS' and not permited:
            queryset = []

        elif obj == 'DETER' and self.context['request'].user.is_authenticated() and permited:
            queryset = DailyAlertaDeter.objects.all().filter(periodo_prodes=prodes)
            queryset = filter_uf_comparativo(
                queryset, self.context['request'].GET
            )
            queryset = queryset.values('estado').annotate(total=Sum('area_km2'))

        elif obj == 'DETER' and not permited:
            queryset = PublicAlertaDeter.objects.all().filter(periodo_prodes=prodes)
            queryset = filter_uf_comparativo(
                queryset, self.context['request'].GET
            )
            queryset = queryset.values('estado').annotate(total=Sum('area_km2'))

        elif obj == 'PRODES':
            queryset = TaxaProdes.objects.all().filter(ano_prodes=prodes.replace('-','/')).order_by('-ano_prodes')

            if len(queryset) > 0:
                if uf != '':
                    queryset = [{'estado': uf, 'total': round(getattr(i,uf.lower()),2)} for i in queryset]
                else:
                    queryset = [[{'total': round(getattr(i,p),2),'estado': p.upper()} for p in i.attributes()] for i in queryset]
                
                queryset = list(queryset[:1])[0]
            else:
                if uf != '':
                    queryset = [{'estado': uf, 'total': 0}]
                else:
                    queryset = [{'estado': 'AC', 'total': 0},
                                {'estado': 'AM', 'total': 0},
                                {'estado': 'AP', 'total': 0},
                                {'estado': 'MA', 'total': 0},
                                {'estado': 'MT', 'total': 0},
                                {'estado': 'PA', 'total': 0},
                                {'estado': 'RO', 'total': 0},
                                {'estado': 'RR', 'total': 0},
                                {'estado': 'TO', 'total': 0}]


        return {
            'taxa': obj,
            'data': queryset,
        }


class NuvemSerializer(BaseSerializer):
    def to_representation(self, obj):
        
        prodes = [int(obj.split('-')[0]), int(obj.split('-')[1])]
        uf = self.context['request'].GET.get('uf', None)
        queryset = None

        if (uf):
            queryset = TaxaNuvens.objects.all()   
        else:
            queryset = TaxaNuvensAml.objects.all()             

        queryset = filter_uf_nuvem(
            queryset, self.context['request'].GET
        )

        if (uf):
            queryset = queryset.values('mes','ano', 'porc_area_km2').filter(uf=uf)
            # queryset = [{'mes': get_reverse_month(qs['mes']),'total': int(qs['porc_area_km2'])} for qs in queryset if belongs_prodes(qs,prodes)]
        else:
            queryset = queryset.values('mes','ano', 'porc_area_km2')
            # queryset = [{'mes': get_reverse_month(qs['mes']),'total': int(qs['porc_area_km2'] * 100)} for qs in queryset if belongs_prodes(qs,prodes)]
        
        queryset = [{'mes': get_reverse_month(qs['mes']),'total': (int(qs['porc_area_km2']) if not qs['porc_area_km2'].is_nan() else 0) } for qs in queryset if belongs_prodes(qs,prodes)]


        # else:
        #     queryset = TaxaNuvensAml.objects.all()        

        #     queryset = filter_uf_nuvem(
        #         queryset, self.context['request'].GET
        #     )

        #     queryset = queryset.values('mes','ano', 'porc_area_km2').filter(uf=uf)

        return {
            'taxa': obj,
            'data': queryset,
        }


class UFPeriodoSerializer(BaseSerializer):
    def to_representation(self, obj):
        tipo = self.context['request'].GET.get('tipo', None)
        permited = bool(UserPermited.objects.filter(username=self.context['request'].user.username))

        if (tipo == 'DETER' or tipo == 'DETER_QUALIF') and self.context['request'].user.is_authenticated() and permited:
            queryset = DailyAlertaDeter.objects.all().filter(periodo_prodes=obj)
            queryset = queryset.values('estado').annotate(total=Sum('area_km2'))
        if (tipo == 'DETER' or tipo == 'DETER_QUALIF') and not permited:
            queryset = PublicAlertaDeter.objects.all().filter(periodo_prodes=obj)
            queryset = queryset.values('estado').annotate(total=Sum('area_km2'))
        elif tipo == 'AWIFS' and self.context['request'].user.is_authenticated() and permited:
            estagio = self.context['request'].GET.get('estagio', None)
            queryset = DailyAlertaAwifs.objects.all().filter(periodo_prodes=obj).filter(estagio=estagio)
            queryset = queryset.values('estado').annotate(total=Sum('area_km2'))

        return {'data': queryset.order_by('total')}


class UFMesPeriodoSerializer(BaseSerializer):
    def to_representation(self, obj):
        tipo = self.context['request'].GET.get('tipo', None)
        permited = bool(UserPermited.objects.filter(username=self.context['request'].user.username))

        if (tipo == 'DETER' or tipo == 'DETER_QUALIF') and self.context['request'].user.is_authenticated() and permited:
            queryset = DailyAlertaDeter.objects.all()
            queryset = filter_uf_periodo_mensal(
                queryset, self.context['request'].GET, obj
            )
            queryset = queryset.values('estado').annotate(total=Sum('area_km2'))
        if (tipo == 'DETER' or tipo == 'DETER_QUALIF') and not permited:
            queryset = PublicAlertaDeter.objects.all()
            queryset = filter_uf_periodo_mensal(
                queryset, self.context['request'].GET, obj
            )
            queryset = queryset.values('estado').annotate(total=Sum('area_km2'))
        elif tipo == 'AWIFS' and self.context['request'].user.is_authenticated() and permited:
            queryset = DailyAlertaAwifs.objects.all()
            queryset = filter_uf_periodo_mensal(
                queryset, self.context['request'].GET, obj
            )
            queryset = queryset.values('estado').annotate(total=Sum('area_km2'))


        return {'data': queryset.order_by('total')}


class ComparativoPeriodosSerializer(BaseSerializer):
    def to_representation(self,obj):

        tipo = self.context['request'].GET.get('tipo', None)
        estagio = self.context['request'].GET.get('estagio', None)
        permited = bool(UserPermited.objects.filter(username=self.context['request'].user.username))

        if tipo == 'AWIFS' and self.context['request'].user.is_authenticated() and permited:
            queryset = DailyAlertaAwifs.objects.all().filter(estagio=estagio)
            queryset = filter_comparativo(
                queryset, self.context['request'].GET, obj
            )
            queryset = queryset.values('ano').annotate(total=Sum('area_km2'))
        
        elif tipo == 'DETER':
            if self.context['request'].user.is_authenticated() and permited:
                queryset = DailyAlertaDeter.objects.all()

            elif not permited:
                queryset = PublicAlertaDeter.objects.all()

            queryset = filter_comparativo(
                queryset, self.context['request'].GET, obj
            )
            queryset = queryset.values('ano').annotate(total=Sum('area_km2'))


        elif tipo == 'DETER_QUALIF':        
            if self.context['request'].user.is_authenticated() and permited:
                queryset = DailyAlertaDeterQualif.objects.all()
        
            elif not permited:
                queryset = PublicAlertaDeterQualif.objects.all()

            queryset = filter_comparativo(
                queryset, self.context['request'].GET, obj, True
            )

            if estagio == 'Corte Raso':
                queryset = queryset.values('ano').annotate(total=Sum('corte_raso_deter'))
            elif estagio == 'Cicatriz de Queimada':
                queryset = queryset.values('ano').annotate(total=Sum('cicatriz_fogo'))
            elif estagio == 'Degradação':
                queryset = queryset.values('ano').annotate(total=Sum('degradacao_deter'))


        if queryset:
            return queryset[0]
        else:
            return {'ano': obj, 'total': 0.0}


class ComparativoProdesPeriodosSerializer(BaseSerializer):
    def to_representation(self,obj):

        tipo = self.context['request'].GET.get('tipo', None)
        estagio = self.context['request'].GET.get('estagio', None)
        permited = bool(UserPermited.objects.filter(username=self.context['request'].user.username))

        if tipo == 'AWIFS' and self.context['request'].user.is_authenticated() and permited:
            queryset = DailyAlertaAwifs.objects.all().filter(estagio=estagio)
            queryset = filter_comparativo_prodes(
                queryset, self.context['request'].GET, obj
            )
            queryset = queryset.values('periodo_prodes').annotate(total=Sum('area_km2'))
        
        elif tipo == 'DETER':
            if self.context['request'].user.is_authenticated() and permited:
                queryset = DailyAlertaDeter.objects.all()

            elif not permited:
                queryset = PublicAlertaDeter.objects.all()

            queryset = filter_comparativo_prodes(
                queryset, self.context['request'].GET, obj
            )
            queryset = queryset.values('periodo_prodes').annotate(total=Sum('area_km2'))


        elif tipo == 'DETER_QUALIF':        
            if self.context['request'].user.is_authenticated() and permited:
                queryset = DailyAlertaDeterQualif.objects.all()
        
            elif not permited:
                queryset = PublicAlertaDeterQualif.objects.all()

            queryset = filter_comparativo_prodes(
                queryset, self.context['request'].GET, obj, True
            )

            if estagio == 'Corte Raso':
                queryset = queryset.values('periodo_prodes').annotate(total=Sum('corte_raso_deter'))
            elif estagio == 'Cicatriz de Queimada':
                queryset = queryset.values('periodo_prodes').annotate(total=Sum('cicatriz_fogo'))
            elif estagio == 'Degradação':
                queryset = queryset.values('periodo_prodes').annotate(total=Sum('degradacao_deter'))


        if queryset:
            return queryset[0]
        else:
            return {'ano': obj, 'total': 0.0}


class PublicDeterSerializer(GeoFeatureModelSerializer):
    data = SerializerMethodField()

    class Meta:
        model = PublicAlertaDeter
        geo_field = 'shape'

    # def get_data(self, obj):
    #     queryset = self.model.objects
    #     queryset = filter_mapa(
    #         queryset, self.context['request'].GET
    #     )
    #     return queryset


class DailyDeterSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = DailyAlertaDeter
        geo_field = 'shape'

    # def get_data(self, obj):
    #     queryset = self.model.objects
    #     queryset = filter_mapa(
    #         queryset, self.context['request'].GET
    #     )
    #     return queryset


class PublicDeterQualifSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = PublicAlertaDeterQualif
        geo_field = 'shape'

    # def get_data(self, obj):
    #     queryset = self.model.objects
    #     queryset = filter_mapa(
    #         queryset, self.context['request'].GET, True
    #     )
    #     return queryset


class DailyDeterQualifSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = DailyAlertaDeterQualif
        geo_field = 'shape'

    # def get_data(self, obj):
    #     queryset = self.model.objects
    #     queryset = filter_mapa(
    #         queryset, self.context['request'].GET, True
    #     )
    #     return queryset


class DailyAwifsSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = DailyAlertaAwifs
        geo_field = 'shape'

    # def get_data(self, obj):
    #     queryset = self.model.objects
    #     queryset = filter_mapa(
    #         queryset, self.context['request'].GET
    #     )
    #     return queryset


class CruzamentoGrafico1Serializer(BaseSerializer):
    def to_representation(self,obj):

        tipo = self.context['request'].GET.get('tipo', None)
        permited = bool(UserPermited.objects.filter(username=self.context['request'].user.username))


        # if tipo == 'Alerta DETER' or tipo == 'Alerta AWiFS':
        #     queryset = filter_cruzamento_alerta(
        #         CruzamentoAlerta.objects.all(), self.context['request'].GET
        #     )
        # else:
        #     queryset = [];
        
        if self.context['request'].user.is_authenticated() and permited:

            if tipo == 'Alerta DETER':
                queryset = filter_cruzamento_alerta(
                    DailyAlertaDeter.objects.all(), self.context['request'].GET
                )
            else:
                queryset = filter_cruzamento_alerta(
                    DailyAlertaAwifs.objects.all(), self.context['request'].GET
                )
        else:
            queryset = filter_cruzamento_alerta(
                PublicAlertaDeter.objects.all(), self.context['request'].GET
            )


        return queryset


class CruzamentoGrafico2Serializer(BaseSerializer):
    def to_representation(self,obj):

        tipo = self.context['request'].GET.get('tipo', None)
        permited = bool(UserPermited.objects.filter(username=self.context['request'].user.username))


        if self.context['request'].user.is_authenticated() and permited:
            if tipo == 'Alerta DETER':
                mid_qs = filter_cruzamento_estadual_federal_padrao(
                    DailyAlertaDeter.objects.all(), self.context['request'].GET 
                )            
            # else if tipo == 'Alerta AWiFS':             
            else:
                mid_qs = filter_cruzamento_estadual_federal_padrao(
                    DailyAlertaAwifs.objects.all(), self.context['request'].GET 
                )

        else:
            mid_qs = filter_cruzamento_estadual_federal_padrao(
                PublicAlertaDeter.objects.all(), self.context['request'].GET 
            )


        qs_est_as = filter_cruzamento_estadual_federal_area(
            mid_qs, 'Estadual', 'dominio_as'
        )
        qs_est_pi = filter_cruzamento_estadual_federal_area(
            mid_qs, 'Estadual', 'dominio_pi'
        )
        qs_est_us = filter_cruzamento_estadual_federal_area(
            mid_qs, 'Estadual', 'dominio_us'
        )
        qs_est_ti = filter_cruzamento_estadual_federal_area(
            mid_qs, 'Estadual', 'dominio_ti'
        )
        qs_est_al = filter_cruzamento_estadual_federal_area(
            mid_qs, 'Estadual', 'areas_livre'
        )


        qs_fed_as = filter_cruzamento_estadual_federal_area(
            mid_qs, 'Federal', 'dominio_as'
        )
        qs_fed_pi = filter_cruzamento_estadual_federal_area(
            mid_qs, 'Federal', 'dominio_pi'
        )
        qs_fed_us = filter_cruzamento_estadual_federal_area(
            mid_qs, 'Federal', 'dominio_us'
        )
        qs_fed_al = filter_cruzamento_estadual_federal_area(
            mid_qs, 'Federal', 'areas_livre'
        )

        queryset = [{
            'estadual': 
            {
                'Assentamentos': qs_est_as['total'],
                'UC Proteção Integral': qs_est_pi['total'], 
                'UC Uso Sustentável': qs_est_us['total'], 
                'Terras Indígenas': qs_est_ti['total'], 
                'Áreas Livres': qs_est_al['total']
            },
            'federal':
            {
                'Assentamentos': qs_fed_as['total'],
                'UC Proteção Integral': qs_fed_pi['total'], 
                'UC Uso Sustentável': qs_fed_us['total'],
                'Áreas Livres': qs_fed_al['total']

            }
        }]
        # else:
        #     queryset = [[]]


        # estagio = self.context['request'].GET.get('estagio', None)
        # ano_inicio = self.context['request'].GET.get('ano_inicio', None)
        # ano_fim = self.context['request'].GET.get('ano_fim', None)
        # estado = self.context['request'].GET.get('estado', None)
        # dominio = self.context['request'].GET.get('dominio', None)
        # area = self.context['request'].GET.get('area', None)

        # if tipo == 'Alerta DETER' or tipo == 'Alerta AWiFS':
        #     mid_qs = filter_cruzamento_estadual_federal_padrao(
        #         CruzamentoAlerta.objects.all(), self.context['request'].GET 
        #     )

        #     qs_est_as = filter_cruzamento_estadual_federal_area(
        #         mid_qs, 'Estadual', 'dominio_as'
        #     )
        #     qs_est_pi = filter_cruzamento_estadual_federal_area(
        #         mid_qs, 'Estadual', 'dominio_pi'
        #     )
        #     qs_est_us = filter_cruzamento_estadual_federal_area(
        #         mid_qs, 'Estadual', 'dominio_us'
        #     )
        #     qs_est_ti = filter_cruzamento_estadual_federal_area(
        #         mid_qs, 'Estadual', 'dominio_ti'
        #     )
        #     qs_est_al = filter_cruzamento_estadual_federal_area(
        #         mid_qs, 'Estadual', 'areas_livre'
        #     )


        #     qs_fed_as = filter_cruzamento_estadual_federal_area(
        #         mid_qs, 'Federal', 'dominio_as'
        #     )
        #     qs_fed_pi = filter_cruzamento_estadual_federal_area(
        #         mid_qs, 'Federal', 'dominio_pi'
        #     )
        #     qs_fed_us = filter_cruzamento_estadual_federal_area(
        #         mid_qs, 'Federal', 'dominio_us'
        #     )
        #     qs_fed_al = filter_cruzamento_estadual_federal_area(
        #         mid_qs, 'Federal', 'areas_livre'
        #     )

        #     queryset = [{
        #         'estadual': 
        #         {
        #             'Assentamentos': qs_est_as['total'],
        #             'UC Proteção Integral': qs_est_pi['total'], 
        #             'UC Uso Sustentável': qs_est_us['total'], 
        #             'Terras Indígenas': qs_est_ti['total'], 
        #             'Áreas Livres': qs_est_al['total']
        #         },
        #         'federal':
        #         {
        #             'Assentamentos': qs_fed_as['total'],
        #             'UC Proteção Integral': qs_fed_pi['total'], 
        #             'UC Uso Sustentável': qs_fed_us['total'],
        #             'Áreas Livres': qs_fed_al['total']

        #         }
        #     }]
        # else:
        #     queryset = [[]]

        return queryset[0]