
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

from django.db import models
from django.contrib.gis.db import models


class AlertaHexgis(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    geom = models.MultiPolygonField(srid=4674, blank=True, null=True)
    img_n_ex = models.CharField(max_length=40, blank=True, null=True)
    img_n_data = models.DateField(blank=True, null=True)
    img_ex = models.CharField(max_length=40, blank=True, null=True)
    img_data = models.DateField(blank=True, null=True)
    area_ha = models.FloatField(blank=True, null=True)
    area_km2 = models.FloatField(blank=True, null=True)
    intervalo = models.IntegerField(blank=True, null=True)
    municipio = models.CharField(max_length=40, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    id_des = models.CharField(max_length=20, blank=True, null=True)
    id_assoc = models.CharField(max_length=20, blank=True, null=True)
    estagio = models.CharField(max_length=24, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    data_ana = models.DateField(blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'alerta_hexgis'

    def dia(self):
        return self.img_data.day

    def mes(self):
        return self.img_data.month

    def ano(self):
        return self.img_data.year

    def total(self):
        return self.area_ha

    def interval(self):
        return (self.img_data - self.img_n_data).days
