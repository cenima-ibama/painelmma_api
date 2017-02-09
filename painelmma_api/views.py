from rest_framework.generics import ListAPIView
from django.shortcuts import render

from .serializers import *
from .filter_functions import *

# Create your views here.
class GetData(ListAPIView):

	def get_queryset(self):
		queryset = AlertaHexgis.objects.all()

		queryset = filter_total(
			queryset, self.request.GET
		)
		return queryset

	def get_serializer_class(self):
		return AlertaSerializer


class GetMapData(ListAPIView):
	serializer_class = AlertaMapaSerializer

	def get_queryset(self):
		queryset = AlertaHexgis.objects.all()

		queryset = filter_total(
			queryset, self.request.GET
		)

		return queryset
