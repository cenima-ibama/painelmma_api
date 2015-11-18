# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restApp', '0002_auto_20151118_1001'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dailyalertaawifs',
            table='ibama"."vw_alerta_awifs',
        ),
        migrations.AlterModelTable(
            name='dailyalertadeter',
            table='ibama"."vw_alerta_deter',
        ),
        migrations.AlterModelTable(
            name='dailyalertadeterqualif',
            table='ibama"."vw_deter_qualificado',
        ),
        migrations.AlterModelTable(
            name='dailyalertalandsat',
            table='ibama"."vw_alerta_indicar',
        ),
        migrations.AlterModelTable(
            name='publicalertadeter',
            table='ibama"."vw_publica_alerta_deter_por_periodo',
        ),
        migrations.AlterModelTable(
            name='taxanuvens',
            table='ibama"."taxa_nuvem',
        ),
        migrations.AlterModelTable(
            name='taxaprodes',
            table='public"."taxa_prodes',
        ),
    ]
