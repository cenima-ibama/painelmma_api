from rest_framework.generics import ListAPIView

#from .models import DailyAlertaAwifs, DailyAlertaDeter
from .serializers import *
from loginApp.models import UserPermited


class grafico1(ListAPIView):
    queryset = [0]

    def get_serializer_class(self):
        tipo = self.request.GET.get('tipo', None)
        permited = bool(UserPermited.objects.filter(username=self.request.user.username))

        if tipo == 'AWIFS' and self.request.user.is_authenticated() and permited:
            serializer_class = DailyAlertaAwifsSerializer
        elif tipo == 'DETER' and self.request.user.is_authenticated() and permited:
            serializer_class = DailyAlertaDeterSerializer
        elif tipo == 'DETER' and not permited:
            serializer_class = PublicAlertaDeterSerializer
        elif tipo == 'DETER_QUALIF' and self.request.user.is_authenticated() and permited:
            serializer_class = DailyAlertaDeterSerializer
        elif tipo == 'DETER_QUALIF' and not permited:
            serializer_class = PublicAlertaDeterSerializer

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
    queryset = ['Diferença','Parcial']

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
        indice = self.request.GET.get('indice', 0)

        if int(mes) > 7:
            queryset = [str(int(ano) + int(indice)) + '-' + str((int(ano) + int(indice) + 1))]
        else:
            queryset = [str((int(ano) + int(indice) - 1)) + '-' + str(int(ano) + int(indice))]
                    
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

     
class gauge1(ListAPIView):
    def get_queryset(self):
        ano = self.request.GET.get('ano', None)
        return [int(ano)-1, int(ano)]

    def get_serializer_class(self):
        serializer_class = ComparativoPeriodosSerializer

        return serializer_class

     