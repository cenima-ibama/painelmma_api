from __future__ import absolute_import

from .base import *

########## IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': 'painel.db'
			# "ENGINE": "django.db.backends.sqlite3",
			# "NAME": ":memory:",
			# "USER": "painel",
			# "PASSWORD": "painel",
			# "HOST": "localhost",
			# "PORT": "",
    },
   #  'siscom_db': {
			# 'ENGINE': 'django.db.backends.sqlite3',
			# 'NAME': 'siscom.db'
   #  }
}
SCHEMA = 'ibama'

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
