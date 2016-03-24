# -*- coding: utf-8 -*-

from .models import DailyAlertaAwifs, DailyAlertaDeter, DailyAlertaDeterQualif
from .models import PublicAlertaDeterQualif, PublicAlertaDeter

#from model_mommy import mommy
from model_mommy.recipe import Recipe

deter_awifs_1 = Recipe(DailyAlertaAwifs,
    ano=2015, area_km2=0.13, estado="MT", mes="OUTUBRO", mesid="03", estagio='Degradação')
deter_awifs_2 = Recipe(DailyAlertaAwifs,
    ano=2015, area_km2=0.82, estado="RR", mes="NOVEMBRO", mesid="04", estagio='Corte Raso')

daily_deter_1 = Recipe(DailyAlertaDeter,
    ano=2015, area_km2=0.23, estado="MA", mes="AGOSTO", mesid="01")
daily_deter_2 = Recipe(DailyAlertaDeter,
    ano=2013, area_km2=0.58, estado="SE", mes="SETEMBRO", mesid="02")

public_deter_1 = Recipe(PublicAlertaDeter,
    ano=2015, area_km2=0.23, uf="RO", mes="OUTUBRO", mesid="03")
public_deter_2 = Recipe(PublicAlertaDeter,
    ano=2013, area_km2=0.58, uf="CE", mes="NOVEMBRO", mesid="04")

daily_deter_qualif_1 = Recipe(DailyAlertaDeterQualif,
    ano=2015, mes=10, cicatriz_fogo=12.12, corte_raso_deter=14.56, degradacao_deter=18.18, mesid="03")
daily_deter_qualif_2 = Recipe(DailyAlertaDeterQualif,
    ano=2013, mes=11, cicatriz_fogo=50.01, corte_raso_deter=150.01, degradacao_deter=250.01, mesid="04")

public_deter_qualif_1 = Recipe(PublicAlertaDeterQualif,
    ano=2015, mes=8, cicatriz_fogo=01.01, corte_raso_deter=02.02, degradacao_deter=03.03, mesid="01")
public_deter_qualif_2 = Recipe(PublicAlertaDeterQualif,
    ano=2013, mes=9, cicatriz_fogo=1.00, corte_raso_deter=100.00, degradacao_deter=1000.00, mesid="02")
