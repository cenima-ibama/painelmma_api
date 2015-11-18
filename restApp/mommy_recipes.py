# -*- coding: utf-8 -*-

from .models import DailyAlertaAwifs, DailyAlertaDeter, DailyAlertaDeterQualif

#from model_mommy import mommy
from model_mommy.recipe import Recipe

AlertaAwifs_2015_10 = Recipe(DailyAlertaAwifs,
    ano=2015, area_km2=0.13, estado="MT", mes="OUTUBRO", mesid="03")
AlertaAwifs_2015_11 = Recipe(DailyAlertaAwifs,
    ano=2015, area_km2=0.82, estado="MT", mes="NOVEMBRO", mesid="04")

AlertaDeter_2015_08 = Recipe(DailyAlertaDeter,
    ano=2015, area_km2=0.23, estado="MA", mes="AGOSTO", mesid="03", estagio='Degradação')
AlertaDeter_2015_09 = Recipe(DailyAlertaDeter,
    ano=2013, area_km2=0.58, estado="MA", mes="SETEMBRO", mesid="04", estagio='Degradação')
