# -*- coding: utf-8 -*-
"""Development settings and globals."""

from __future__ import absolute_import

from os.path import join, normpath

from .base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'siscom',
        'USER': 'caio',
        'PASSWORD': 'caio',
        'HOST': 'localhost',
    },
    'siscom_db': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'siscom',
        'USER': 'painel',
        'PASSWORD': 'db!p41n3l',
        'HOST': '10.1.8.58',
    }
}

SCHEMA = 'ibama'
DATABASE_ROUTERS = ['restApp.dbrouters.SiscomRouter']

########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION

AUTH_USER_MODEL = 'loginApp.LDAPUser'
# ########## LDAP CONFIG
LDAP_AUTH_URL = 'ldap://10.1.25.17:389'
LDAP_AUTH_USE_TLS = False
LDAP_AUTH_SEARCH_BASE = 'ou=Users,ou=ibama,o=redegoverno,c=br'
LDAP_AUTH_USER_FIELDS = {
    "username": "uid",
    "name": "cn",
    #"last_name": "sn",
    "email": "mail",
}
LDAP_AUTH_USER_LOOKUP_FIELDS = ("username",)
# LDAP_AUTH_CLEAN_USER_DATA = clean_user_data
# END LDAP CONFIG

# AUTH BACKEND CONFIG
AUTHENTICATION_BACKENDS = (
    'django_python3_ldap.auth.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
########## END AUTH BACKEND CONFIG

########## TOOLBAR CONFIGURATION
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
# INTERNAL_IPS = ('127.0.0.1',)
INTERNAL_IPS = ('10.1.8.28',)
########## END TOOLBAR CONFIGURATION
