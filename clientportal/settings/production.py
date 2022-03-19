from .local import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'client-portal',
        'HOST': 'pgsql',
        'USER' : 'odoo',
        'PASSWORD' : 'x1234567890',
        'PORT' : 5432
    }
}