"""
Production Django settings for site project.
"""
from .common import *

## debug configurations ##
DEBUG = False
ALLOWED_HOSTS = ['django-user-post-a42f5d79d28f.herokuapp.com']

## static files - https://docs.djangoproject.com/en/4.1/howto/static-files/ ##
# NOTE: must first run `python3 ./manage.py collectstatic`
# resolves static files from `~/forum_post_app/staticfiles`
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/staticfiles/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
