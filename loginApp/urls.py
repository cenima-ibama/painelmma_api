# -*- coding: utf-8 -*-
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import patterns, url

from .views import ObtainPass


urlpatterns = patterns('',
    url(r'obtain-pass/', 
        ObtainPass.as_view(),
        name='obtain-pass'
    ),
)

urlpatterns = format_suffix_patterns(urlpatterns)