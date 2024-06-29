"""
Development Django settings for site project.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from .common import *


## debug configurations ##
DEBUG = True

ALLOWED_HOSTS = ['localhost']

LOGIN_URL = None # Django's built-in login view

LOGIN_REDIRECT_URL = '/home'

LOGOUT_REDIRECT_URL = '/login'

## application configurations ##
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main_site',
    'crispy_forms',
    'crispy_bootstrap5'
]
