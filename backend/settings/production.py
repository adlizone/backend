from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ALLOWED_ORIGINS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
