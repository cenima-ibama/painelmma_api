# -*- coding: utf-8 -*-
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import patterns, url

from .views import GetData, GetMapData


urlpatterns = patterns('',
    url(r'get-data/$', 
        GetData.as_view(),
        name='get-data'
    ),
    url(r'get-map-data/', 
        GetMapData.as_view(),
        name='get-map-data'
    ),
)

urlpatterns = format_suffix_patterns(urlpatterns)