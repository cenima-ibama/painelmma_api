#from django.test import TestCase
from datetime import date
from decimal import *

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase

from .models import *


class TestDiarioCase(APITestCase):

    def setUp(self):
        self.url = reverse('api:estatisticas-diario')

        DailyAlertaAwifs.objects.create(
            mes="OUTUBRO",
            ano=2015,
            area_km2=0.13,
            estado="MT",
            data_imagem=date(2015, 10, 10),
            mesid="03"
        )

    def test_response(self):
        response = self.client.get(
            self.url,
            {'uf': 'DF', 'ano': 2015, 'tipo': 'DETER'},
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_response_day(self):

        response = self.client.get(
            self.url,
            {'uf': 'MT', 'ano': 2015, 'mes': 10, 'tipo': 'AWIFS'},
            format='json'
        )

        data_received = response.data[0]['data']
        day = data_received[0]['dia']
        area = data_received[0]['total']

        self.assertEqual(len(data_received), 1)
        self.assertEqual(day, 10)
        self.assertEqual(area, Decimal('0.13'))

        DailyAlertaAwifs.objects.create(
            mes="OUTUBRO",
            ano=2015,
            area_km2=0.29,
            estado="MT",
            data_imagem=date(2015, 10, 12),
            mesid="03"
        )

        response = self.client.get(
            self.url,
            {'uf': 'MT', 'ano': 2015, 'mes': 10, 'tipo': 'AWIFS'},
            format='json'
        )

        data_received = response.data[0]['data']
        day = data_received[1]['dia']
        area = data_received[1]['total']
        self.assertEqual(len(data_received), 2)
        self.assertEqual(day, 12)
        self.assertEqual(area, Decimal('0.29'))

        DailyAlertaAwifs.objects.create(
            mes="OUTUBRO",
            ano=2015,
            area_km2=0.31,
            estado="MT",
            data_imagem=date(2015, 10, 12),
            mesid="03"
        )

        response = self.client.get(
            self.url,
            {'uf': 'MT', 'ano': 2015, 'mes': 10, 'tipo': 'AWIFS'},
            format='json'
        )

        data_received = response.data[0]['data']
        day = data_received[1]['dia']
        area = data_received[1]['total']

        self.assertEqual(len(data_received), 2)
        self.assertEqual(day, 12)
        self.assertEqual(area, Decimal('0.60'))