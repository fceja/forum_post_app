"""
Development Django settings for site project.
"""
from .common import *

## debug configurations ##
DEBUG = True
ALLOWED_HOSTS = ['localhost']

# static files - https://docs.djangoproject.com/en/4.1/howto/static-files/ ##
# resolves static files from `~/forum_post_app/static`
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
