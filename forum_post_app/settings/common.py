"""
Common Django settings for site project (development and production).

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from dotenv import load_dotenv
from .i18n import *
import mimetypes
import os

## load env vars ##
load_dotenv()

## path configurations ##
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

## application configurations ##
mimetypes.add_type("text/css", ".css", True)

LOGIN_URL = None # Django's built-in login view
LOGIN_REDIRECT_URL = '/home'
LOGOUT_REDIRECT_URL = '/login'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

## security configurations ##
SECRET_KEY = os.getenv('SECRET_KEY')

## django running configurations ##
WSGI_APPLICATION = 'forum_post_app.wsgi.application'

ROOT_URLCONF = 'forum_post_app.urls'

## application configurations ##
# NOTE: make sure changes for MIDDLEWARE are ok for production - otherwise, separate into respective env file
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

# NOTE: make sure changes for MIDDLEWARE are ok for production - otherwise, separate into respective env file
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

## debug configurations ##
DEBUG = False # should always be false here
ALLOWED_HOSTS = []
