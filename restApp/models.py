# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.conf import settings

from .utils import get_reverse_month


class DailyAlertaAwifs(models.Model):
    objectid = models.AutoField(primary_key=True)
    mes = models.CharField(max_length=10, blank=True, null=True)
    ano = models.SmallIntegerField(blank=True, null=True)
    area_km2 = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
    dominio = models.CharField(max_length=200, blank=True, null=True)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    uf = models.SmallIntegerField(blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    data_imagem = models.DateTimeField(blank=True, null=True)
    shape = models.GeometryField(blank=True, null=True)
    centroide = models.GeometryField(blank=True, null=True)
    mesid = models.TextField(blank=True, null=True)
    estagio = models.CharField(max_length=50, blank=True, null=True)
    periodo_prodes = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        try:
            db_table = '%s\".\"vw_alerta_awifs' % settings.SCHEMA
            managed = False
        except AttributeError:
            pass


class DailyAlertaDeter(models.Model):
    objectid = models.AutoField(primary_key=True)
    mes = models.CharField(max_length=10, blank=True, null=True)
    ano = models.SmallIntegerField(blank=True, null=True)
    area_km2 = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
    dominio = models.CharField(max_length=200, blank=True, null=True)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    uf = models.SmallIntegerField(blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    data_imagem = models.DateTimeField(blank=True, null=True)
    shape = models.GeometryField(blank=True, null=True)
    centroide = models.GeometryField(blank=True, null=True)
    mesid = models.TextField(blank=True, null=True)
    estagio = models.CharField(max_length=50, blank=True, null=True)
    periodo_prodes = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        try:
            db_table = '%s\".\"vw_alerta_deter' % settings.SCHEMA
            managed = False
        except AttributeError:
            pass

    def __str__(self):
        return "mes: %s, ano: %s, mesid: %s" % (self.mes, self.ano, self.mesid)


class DailyAlertaLandsat(models.Model):
    objectid = models.AutoField(primary_key=True)
    mes = models.CharField(max_length=10, blank=True, null=True)
    ano = models.SmallIntegerField(blank=True, null=True)
    area_km2 = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)
    dominio = models.CharField(max_length=200, blank=True, null=True)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    uf = models.SmallIntegerField(blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    data_imagem = models.DateTimeField(blank=True, null=True)
    shape = models.GeometryField(blank=True, null=True)
    centroide = models.GeometryField(blank=True, null=True)
    mesid = models.TextField(blank=True, null=True)
    estagio = models.CharField(max_length=50, blank=True, null=True)
    periodo_prodes = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        try:
            db_table = '%s\".\"vw_alerta_indicar' % settings.SCHEMA
            managed = False
        except AttributeError:
            pass


class DailyAlertaDeterQualif(models.Model):
    objectid = models.AutoField(primary_key=True)
    periodo_prodes = models.CharField(max_length=10, blank=True, null=True)
    mes = models.CharField(max_length=10, blank=True, null=True)
    ano = models.SmallIntegerField(blank=True, null=True)
    mes_ano = models.CharField(max_length=6, blank=True, null=True)
    cicatriz_fogo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    corte_raso_deter = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    degradacao_deter = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    alta = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    leve = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    moderada = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    falso_positivo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    nao_avaliado = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    deter_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    total_avaliado = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    porc_area_avaliada = models.SmallIntegerField(blank=True, null=True)
    mesid = models.TextField(blank=True, null=True)

    class Meta:
        try:
            db_table = '%s\".\"vw_deter_qualificado' % settings.SCHEMA
            managed = False
        except AttributeError:
            pass

    def __str__(self):
        return str(self.mes) + "/" + str(self.ano)


class PublicAlertaDeterQualif(models.Model):
    objectid = models.AutoField(primary_key=True)
    periodo_prodes = models.CharField(max_length=10, blank=True, null=True)
    mes = models.CharField(max_length=10, blank=True, null=True)
    ano = models.SmallIntegerField(blank=True, null=True)
    mes_ano = models.CharField(max_length=6, blank=True, null=True)
    cicatriz_fogo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    corte_raso_deter = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    degradacao_deter = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    alta = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    leve = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    moderada = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    falso_positivo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    nao_avaliado = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    deter_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    total_avaliado = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    porc_area_avaliada = models.SmallIntegerField(blank=True, null=True)
    mesid = models.TextField(blank=True, null=True)

    class Meta:
        try:
            db_table = '%s\".\"vw_publica_deter_qualificado' % settings.SCHEMA
            managed = False
        except AttributeError:
            pass

    def __str__(self):
        return str(self.mes) + '/' + str(self.ano)


class PublicAlertaDeter(models.Model):
    objectid = models.AutoField(primary_key=True)
    mes = models.CharField(max_length=10, blank=True, null=True)
    ano = models.SmallIntegerField(blank=True, null=True)
    area_km2 = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    area_ha = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    municipio = models.CharField(max_length=200, blank=True, null=True)
    dominio = models.CharField(max_length=200, blank=True, null=True)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    quinzena = models.CharField(max_length=5, blank=True, null=True)
    id_des = models.CharField(unique=True, max_length=16, blank=True, null=True)
    ai = models.IntegerField(blank=True, null=True)
    tei = models.IntegerField(blank=True, null=True)
    processo = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    vistoria = models.CharField(max_length=100, blank=True, null=True)
    resp_vistoria = models.CharField(max_length=150, blank=True, null=True)
    longitude = models.CharField(max_length=17, blank=True, null=True)
    latitude = models.CharField(max_length=17, blank=True, null=True)
    uf = models.SmallIntegerField(blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    obs = models.CharField(max_length=250, blank=True, null=True)
    id_tablet = models.CharField(max_length=10, blank=True, null=True)
    data_vist = models.CharField(max_length=50, blank=True, null=True)
    globalid = models.CharField(max_length=50, blank=True, null=True)
    dado_final = models.CharField(max_length=1, blank=True, null=True)
    estagio = models.CharField(max_length=50, blank=True, null=True)
    data_imagem = models.DateTimeField(blank=True, null=True)
    shape = models.GeometryField(blank=True, null=True)
    veg_sec = models.CharField(max_length=100, blank=True, null=True)
    periodo_prodes = models.CharField(max_length=10, blank=True, null=True)
    mesid = models.TextField(blank=True, null=True)

    class Meta:
        try:
            db_table = '%s\".\"vw_publica_alerta_deter_por_periodo' % settings.SCHEMA
            managed = False
        except AttributeError:
            pass


class TaxaProdes(models.Model):
    ano_prodes = models.CharField(max_length=9, blank=True, null=False, primary_key=True)
    ac = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=False)
    am = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=False)
    ap = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=False)
    ma = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=False)
    mt = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=False)
    pa = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=False)
    ro = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=False)
    rr = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=False)
    to = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'public\".\"taxa_prodes'

    def total(self):
        return self.ac + self.am + self.ap + self.ma + self.mt + self.pa + self.ro + self.rr + self.to

    def attributes(self):
        return [p for p in dir(self) if len(p) == 2 and not p == 'pk']

    def __str__(self):
        return self.ano_prodes


class TaxaNuvens(models.Model):
    objectid = models.AutoField(primary_key=True)
    mes = models.CharField(max_length=10, blank=True, null=True)
    ano = models.SmallIntegerField(blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    area_km2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    porc_area_km2 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    dat_cadastro = models.DateTimeField(blank=True, null=True)

    class Meta:
        try:
            db_table = '%s\".\"taxa_nuvem' % settings.SCHEMA
            managed = False
        except AttributeError:
            pass

    def periodo_prodes(self):
        if get_reverse_month(self.mes) > 7:
            return str(self.ano) + "-" + str(int(self.ano) + 1)
        else:
            return str(int(self.ano) - 1) + "-" + str(self.ano)

    def __str__(self):
        return str(self.mes) + "/" + str(self.ano) + "('" + str(self.porc_area_km2) + "')"
        

def prodes_filter(queryset, year, month):
    monthList = ['01','02','03','04','05','06','07','08','09','10','11','12']
    if month > 7:
        return queryset.filter(ano__gte=year - 1, ano__lte=year + 1)
