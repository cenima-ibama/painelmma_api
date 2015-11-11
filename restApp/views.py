from rest_framework.generics import ListAPIView

#from .models import DailyAlertaAwifs, DailyAlertaDeter
from .serializers import *


class grafico1(ListAPIView):
    queryset = [0]

    def get_serializer_class(self):
        tipo = self.request.GET.get('tipo', None)
        if tipo == 'AWIFS':
            serializer_class = DailyAlertaAwifsSerializer
        elif tipo == 'DETER':
            serializer_class = DailyAlertaDeterSerializer
        elif tipo == 'DETER_QUALIF':
            serializer_class = DailyAlertaDeterSerializer

        return serializer_class


class grafico2(ListAPIView):
    queryset = []

    def get_queryset(self):
        ano = self.request.GET.get('ano', None)
        mes = self.request.GET.get('mes', None)
        series = 2 + int(self.request.GET.get('frequencia',0)) if self.request.GET.get('frequencia',0) else 2
        
        if int(mes) > 7:
            queryset = [str(int(ano) - i) + '-' + str(int(ano) - i + 1) for i in range(0,series)]
            # queryset = [str(ano) + '-' + str((int(ano) + 1)), str((int(ano) - 1)) + '-' + str(ano)]
        else:
            queryset = [str(int(ano) - i - 1) + '-' + str(int(ano) - i) for i in range(0,series)]
            # queryset = [str((int(ano) - 1)) + '-' + str(ano), str((int(ano) - 2)) + '-' + str((int(ano) - 1))]

        return queryset

    def get_serializer_class(self):
        serializer_class = MontlySerializer

        return serializer_class


class grafico3(ListAPIView):
    queryset = ['Total','Parcial']

    def get_serializer_class(self):
        serializer_class = IndiceSerializer

        return serializer_class


class grafico4(ListAPIView):
    queryset = []

    def get_queryset(self):
        ano = self.request.GET.get('ano', None)
        mes = self.request.GET.get('mes', None)
        series = 2 + int(self.request.GET.get('frequencia',0)) if self.request.GET.get('frequencia',0) else 2
        
        if int(mes) > 7:
            queryset = [str(int(ano) - i) + '-' + str(int(ano) - i + 1) for i in range(0,series)]
            # queryset = [str(ano) + '-' + str((int(ano) + 1)), str((int(ano) - 1)) + '-' + str(ano)]
        else:
            queryset = [str(int(ano) - i - 1) + '-' + str(int(ano) - i) for i in range(0,series)]
            # queryset = [str((int(ano) - 1)) + '-' + str(ano), str((int(ano) - 2)) + '-' + str((int(ano) - 1))]

        return queryset

    def get_serializer_class(self):
        serializer_class = UFSerializer

        return serializer_class


class grafico5(ListAPIView):
    queryset = ['PRODES', 'DETER', 'AWIFS']

    def get_serializer_class(self):
        serializer_class = AcumuladoSerializer

        return serializer_class


class grafico6(ListAPIView):
    queryset = ['PRODES', 'DETER', 'AWIFS']

    def get_serializer_class(self):
        serializer_class = UFComparativoSerializer

        return serializer_class


class grafico7(ListAPIView):
    # queryset = ['2013-2014', '2014-2015']
    def get_queryset(self):
        ano = self.request.GET.get('ano', None)
        mes = self.request.GET.get('mes', None)
        series = 2 + int(self.request.GET.get('frequencia',0)) if self.request.GET.get('frequencia',0) else 2
        
        if int(mes) > 7:
            queryset = [str(int(ano) - i) + '-' + str(int(ano) - i + 1) for i in range(0,series)]
            # queryset = [str(ano) + '-' + str((int(ano) + 1)), str((int(ano) - 1)) + '-' + str(ano)]
        else:
            queryset = [str(int(ano) - i - 1) + '-' + str(int(ano) - i) for i in range(0,series)]
            # queryset = [str((int(ano) - 1)) + '-' + str(ano), str((int(ano) - 2)) + '-' + str((int(ano) - 1))]

        return queryset

    def get_serializer_class(self):
        serializer_class = NuvemSerializer

        return serializer_class


class grafico8(ListAPIView):
    # queryset = ['2015-2016']
    queryset = []

    def get_queryset(self):
        ano = self.request.GET.get('ano', None)
        mes = self.request.GET.get('mes', None)

        if int(mes) > 7:
            queryset = [str(ano) + '-' + str((int(ano) + 1))]
        else:
            queryset = [str((int(ano) - 1)) + '-' + str(ano)]
                    
        # if int(mes) > 7:
        #     queryset = [str(ano) + '-' + str((int(ano) + 1)), str((int(ano) - 1)) + '-' + str(ano)]
        # else:
        #     queryset = [str((int(ano) - 1)) + '-' + str(ano), str((int(ano) - 2)) + '-' + str((int(ano) - 1))]

        return queryset


    def get_serializer_class(self):
        serializer_class = UFPeriodoSerializer

        return serializer_class


class grafico9(ListAPIView):
    # queryset = ['2015-2016']
    queryset = [0]

    def get_serializer_class(self):
        serializer_class = UFMesPeriodoSerializer

        return serializer_class