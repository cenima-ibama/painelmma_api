#from django.test import TestCase
from datetime import date
from decimal import *

from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from .models import *
from .mommy_recipes import *


def get_response(client, url, params):
    return client.get(
        url,
        params,
        format='json'
    )


class TestDiarioAwifs(APITestCase):

    def setUp(self):
        self.url = reverse('api:estatisticas-diario')
        self.params = {'uf': 'MT', 'ano': 2015, 'mes': 10, 'tipo': 'AWIFS'}
        AlertaAwifs_2015_10.make(data_imagem=date(2015, 10, 10))

    def test_response(self):
        response = get_response(self.client, self.url, self.params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_response_diario(self):
        response = get_response(self.client, self.url, self.params)
        data_received = response.data[0]['data']
        self.assertEqual(len(data_received), 1)
        self.assertEqual(data_received[0]['dia'], 10)
        self.assertEqual(data_received[0]['total'], Decimal('0.13'))

        AlertaAwifs_2015_10.make(data_imagem=date(2015, 10, 12), area_km2=0.29)
        response = get_response(self.client, self.url, self.params)
        data_received = response.data[0]['data']

        self.assertEqual(len(data_received), 2)
        self.assertEqual(data_received[1]['dia'], 12)
        self.assertEqual(data_received[1]['total'], Decimal('0.29'))

        AlertaAwifs_2015_10.make(data_imagem=date(2015, 10, 12), area_km2=0.31)
        response = get_response(self.client, self.url, self.params)
        data_received = response.data[0]['data']

        self.assertEqual(len(data_received), 2)
        self.assertEqual(data_received[1]['dia'], 12)
        self.assertEqual(data_received[1]['total'], Decimal('0.60'))

        AlertaAwifs_2015_10.make(data_imagem=date(2015, 10, 12), area_km2=1)
        response = get_response(self.client, self.url, self.params)
        data_received = response.data[0]['data']
        self.assertEqual(len(data_received), 2)
        self.assertEqual(data_received[1]['dia'], 12)
        self.assertEqual(data_received[1]['total'], Decimal('1.60'))

        AlertaAwifs_2015_11.make(data_imagem=date(2015, 11, 1))
        AlertaAwifs_2015_11.make(data_imagem=date(2015, 11, 1))
        AlertaAwifs_2015_11.make(data_imagem=date(2015, 11, 2))
        AlertaAwifs_2015_11.make(data_imagem=date(2015, 11, 3), area_km2=1.2)

        self.params = {'uf': 'MT', 'ano': 2015, 'mes': 11, 'tipo': 'AWIFS'}
        response = get_response(self.client, self.url, self.params)
        data_received = response.data[0]['data']

        self.assertEqual(len(data_received), 3)
        self.assertEqual(response.data[0]['data'][0]['dia'], 1)
        self.assertEqual(response.data[0]['data'][0]['total'], Decimal('1.64'))

        self.assertEqual(response.data[0]['data'][1]['dia'], 2)
        self.assertEqual(response.data[0]['data'][1]['total'], Decimal('0.82'))

        self.assertEqual(response.data[0]['data'][2]['dia'], 3)
        self.assertEqual(response.data[0]['data'][2]['total'], Decimal('1.2'))


class TestDiarioDeter(APITestCase):

    def setUp(self):
        self.url = reverse('api:estatisticas-diario')
        self.params = {'uf': 'MA', 'ano': 2015, 'mes': 8,
            'tipo': 'DETER', 'estagio': 'Corte Raso'}
        AlertaDeter_2015_08.make(data_imagem=date(2015, 8, 1))

    def test_response(self):
        response = get_response(self.client, self.url, self.params)
        self.assertEqual(response.status_code, 200)

    def test_response_diario(self):
        response = get_response(self.client, self.url, self.params)

        data_received = response.data[0]['data']
        day = data_received[0]['dia']
        area = data_received[0]['total']
        self.assertEqual(len(data_received), 1)
        self.assertEqual(day, 1)
        self.assertEqual(area, Decimal('0.23'))

        AlertaDeter_2015_08.make(data_imagem=date(2015, 8, 1), area_km2=1)
        response = get_response(self.client, self.url, self.params)

        data_received = response.data[0]['data']
        day = data_received[0]['dia']
        area = data_received[0]['total']
        self.assertEqual(len(data_received), 1)
        self.assertEqual(day, 1)
        self.assertEqual(area, Decimal('1.23'))

        AlertaDeter_2015_08.make(data_imagem=date(2015, 8, 9), area_km2=1.89)
        response = get_response(self.client, self.url, self.params)
        data_received = response.data[0]['data']
        day = data_received[1]['dia']
        area = data_received[1]['total']
        self.assertEqual(len(data_received), 2)
        self.assertEqual(day, 9)
        self.assertEqual(area, Decimal('1.89'))

        AlertaDeter_2015_08.make(data_imagem=date(2015, 8, 10), area_km2=1)
        AlertaDeter_2015_08.make(data_imagem=date(2015, 8, 11), area_km2=1)
        AlertaDeter_2015_08.make(data_imagem=date(2015, 8, 10), area_km2=2)
        AlertaDeter_2015_08.make(data_imagem=date(2015, 8, 30), area_km2=2)

        response = get_response(self.client, self.url, self.params)
        data_received = response.data[0]['data']
        self.assertEqual(len(data_received), 5)

        self.assertEqual(data_received[0]['dia'], 1)
        self.assertEqual(data_received[1]['dia'], 9)
        self.assertEqual(data_received[2]['dia'], 10)
        self.assertEqual(data_received[3]['dia'], 11)
        self.assertEqual(data_received[4]['dia'], 30)

        self.assertEqual(data_received[0]['total'], Decimal('1.23'))
        self.assertEqual(data_received[1]['total'], Decimal('1.89'))
        self.assertEqual(data_received[2]['total'], Decimal('3'))
        self.assertEqual(data_received[3]['total'], Decimal('1'))
        self.assertEqual(data_received[4]['total'], Decimal('2'))


class TestDiarioQualif(APITestCase):

    def setUp(self):
        self.url = reverse('api:estatisticas-diario')
        self.params = {'uf': 'BA', 'ano': 2013, 'mes': 9,
            'tipo': 'DETER', 'estagio': 'Corte Raso'}

    def test_response(self):
        response = get_response(self.client, self.url, self.params)
        self.assertEqual(response.status_code, 200)


# class TestMapa(APITestCase):

#     def setUp(self):
#         self.url = reverse('api:mapa')

#     def test_response(self):
#         response = get_response(self.client, self.url)
#         self.assertEqual(response.status_code, 200)