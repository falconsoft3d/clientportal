from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_clientportal2',
        'HOST': 'localhost',
        'USER' : 'odoo',
        'PASSWORD' : 'x1234567890',
        'PORT' : 5432
    }
}