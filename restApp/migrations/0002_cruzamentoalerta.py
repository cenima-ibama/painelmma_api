# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CruzamentoAlerta',
            fields=[
                ('objectid', models.AutoField(primary_key=True, serialize=False)),
                ('mes', models.CharField(max_length=10, blank=True, null=True)),
                ('ano', models.SmallIntegerField(blank=True, null=True)),
                ('area_km2', models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)),
                ('area_ha', models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)),
                ('municipio', models.CharField(max_length=200, blank=True, null=True)),
                ('dominio', models.CharField(max_length=200, blank=True, null=True)),
                ('tipo', models.CharField(max_length=15, blank=True, null=True)),
                ('quinzena', models.CharField(max_length=5, blank=True, null=True)),
                ('id_des', models.CharField(unique=True, max_length=16, blank=True, null=True)),
                ('ai', models.IntegerField(blank=True, null=True)),
                ('tei', models.IntegerField(blank=True, null=True)),
                ('processo', models.CharField(max_length=20, blank=True, null=True)),
                ('url', models.CharField(max_length=200, blank=True, null=True)),
                ('vistoria', models.CharField(max_length=100, blank=True, null=True)),
                ('resp_vistoria', models.CharField(max_length=150, blank=True, null=True)),
                ('longitude', models.CharField(max_length=17, blank=True, null=True)),
                ('latitude', models.CharField(max_length=17, blank=True, null=True)),
                ('uf', models.SmallIntegerField(blank=True, null=True)),
                ('estado', models.CharField(max_length=2, blank=True, null=True)),
                ('obs', models.CharField(max_length=250, blank=True, null=True)),
                ('id_tablet', models.CharField(max_length=10, blank=True, null=True)),
                ('data_vist', models.CharField(max_length=50, blank=True, null=True)),
                ('globalid', models.CharField(max_length=50, blank=True, null=True)),
                ('dado_final', models.CharField(max_length=1, blank=True, null=True)),
                ('estagio', models.CharField(max_length=50, blank=True, null=True)),
                ('data_imagem', models.DateTimeField(blank=True, null=True)),
                ('shape', django.contrib.gis.db.models.fields.GeometryField(srid=4326, blank=True, null=True)),
                ('veg_sec', models.CharField(max_length=100, blank=True, null=True)),
                ('dominio_pi', models.CharField(max_length=255, blank=True, null=True)),
                ('dominio_us', models.CharField(max_length=255, blank=True, null=True)),
                ('dominio_ti', models.CharField(max_length=255, blank=True, null=True)),
                ('dominio_ap', models.CharField(max_length=255, blank=True, null=True)),
                ('dominio_as', models.CharField(max_length=255, blank=True, null=True)),
                ('dominio_fp', models.CharField(max_length=255, blank=True, null=True)),
            ],
            options={
                'db_table': 'ibama"."alerta',
                'managed': False,
            },
        ),
    ]
