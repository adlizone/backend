from .base import *

DEBUG = True

ALLOWED_HOSTS = [ "*" ]

CORS_ALLOWED_ORIGINS = [
    "https://mountecox.com",
    "http://localhost:5173",
]

CORS_ALLOW_CREDENTIALS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
