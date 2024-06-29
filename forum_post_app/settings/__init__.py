import os

environment = os.getenv('DJANGO_ENV')

if environment == 'development':
    from .development import *
elif environment == 'production':
    from .production import *
else:
    raise Exception('Invalid environment.')
