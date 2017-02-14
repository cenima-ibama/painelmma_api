# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer, SerializerMethodField, BaseSerializer
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from django.db.models import Sum, Count
from decimal import *

from .models import *
# from loginApp.models import UserPermited

# from .utils import get_reverse_month, belongs_prodes, get_prodes,get_month


class AlertaSerializer(ModelSerializer):
    # data = SerializerMethodField()

    class Meta:
        model = AlertaHexgis
        fields = ['img_data', 'img_n_data', 'area_ha', 'img_ex','img_n_ex', 'estagio', 'dia', 'total']

    # def get_data(self, obj):
    #     queryset = AlertaHexgis.objects.values('img_data', 'img_n_data', 'area_ha', 'img_ex','img_n_ex')
    # #     # queryset = filter_daily_total(
    # #     #     queryset, self.context['request'].GET
    # #     # )
    #     return queryset



class AlertaMapaSerializer(GeoFeatureModelSerializer):
    # data = SerializerMethodField()

    class Meta:
        model = AlertaHexgis
        geo_field = 'geom'
        fields = ['img_data', 'area_ha', 'estagio', 'id_des', 'interval', 'img_ex', 'img_n_ex']
