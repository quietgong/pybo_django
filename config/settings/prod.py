from .base import *

ALLOWED_HOSTS = ['15.164.187.80', 'emsys.site']
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = []
DEBUG = False

MEDIA_ROOT = '/home/ubuntu/projects/mysite/media/'
MEDIA_URL = '/media/'
