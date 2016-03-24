# -*- coding: utf-8 -*-

def get_month(month):
    if month == 1:
        month = 'JANEIRO'
    elif month == 2:
        month = 'FEVEREIRO'
    elif month == 3:
        month = 'MARCO'
    elif month == 4:
        month = 'ABRIL'
    elif month == 5:
        month = 'MAIO'
    elif month == 6:
        month = 'JUNHO'
    elif month == 7:
        month = 'JULHO'
    elif month == 8:
        month = 'AGOSTO'
    elif month == 9:
        month = 'SETEMBRO'
    elif month == 10:
        month = 'OUTUBRO'
    elif month == 11:
        month = 'NOVEMBRO'
    elif month == 12:
        month = 'DEZEMBRO'
    return month

def get_reverse_month(month):
    if month == 'JANEIRO':
        month = 1
    elif month == 'FEVEREIRO':
        month = 2
    elif month == 'MARCO':
        month = 3
    elif month == 'ABRIL':
        month = 4
    elif month == 'MAIO':
        month = 5
    elif month == 'JUNHO':
        month = 6
    elif month == 'JULHO':
        month = 7
    elif month == 'AGOSTO':
        month = 8
    elif month == 'SETEMBRO':
        month = 9
    elif month == 'OUTUBRO':
        month = 10
    elif month == 'NOVEMBRO':
        month = 11
    elif month == 'DEZEMBRO':
        month = 12
    return int(month)


def belongs_prodes(qs,prodes):
    return ((get_reverse_month(qs['mes']) >= 8 and int(qs['ano']) == prodes[0]) or\
             (get_reverse_month(qs['mes']) <= 7 and int(qs['ano']) == prodes[1]))

def get_prodes(mes, ano, indice=0):
    if int(mes) > 7:
        return str(int(ano) + int(indice)) + '-' + str(int(ano) + int(indice) + 1)
    else:
        return str(int(ano) + int(indice) - 1) + '-' + str(int(ano) + int(indice))


def create_list(value):
    return [v for v in value]
