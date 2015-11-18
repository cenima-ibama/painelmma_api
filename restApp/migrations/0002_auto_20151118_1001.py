# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dailyalertaawifs',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='dailyalertadeter',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='dailyalertadeterqualif',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='dailyalertalandsat',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='publicalertadeter',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='taxanuvens',
            options={'managed': False},
        ),
    ]
